"""
Quản lý các nhà cung cấp AI và định tuyến model.

Tên model đầy đủ có dạng "<provider>/<model>", ví dụ:
    chatgpt/auto            gemini/gemini-2.5-flash      deepseek/deepseek-flash
    openai/gpt-4o-mini      gemini-web/default           deepseek-web/expert+think
Tên không có tiền tố (ví dụ "auto", "gpt-4o") thuộc nhà cung cấp của model mặc định
(ChatGPT nếu có cookie), để công cụ cũ vẫn dùng được.

Mỗi nhà cung cấp chỉ được tạo (và chỉ cần thư viện của nó) khi được dùng lần đầu.
"""

from __future__ import annotations

import logging
import threading
from concurrent.futures import ThreadPoolExecutor, wait
from typing import Callable

from .base import Provider, ProviderError
from .config import Settings

log = logging.getLogger(__name__)

PROVIDER_LABELS = {
    "chatgpt": "ChatGPT (web, cookie)",
    "openai": "OpenAI (API key)",
    "gemini": "Gemini (API key)",
    "gemini-web": "Gemini (web, cookie)",
    "deepseek": "DeepSeek (API key)",
    "deepseek-web": "DeepSeek (web, userToken)",
}


def _factories(settings: Settings) -> dict[str, Callable[[], Provider]]:
    """Các nhà cung cấp đã được cấu hình (có khóa/cookie), theo thứ tự ưu tiên."""
    s = settings
    proxy = s.web_proxy or None
    out: dict[str, Callable[[], Provider]] = {}
    if s.cookie:
        def chatgpt():
            from .client import ChatGPTClient
            return ChatGPTClient(s)
        out["chatgpt"] = chatgpt
    if s.openai_api_key:
        def openai():
            from .openai_api import OpenAICompatProvider, is_openai_chat_model
            return OpenAICompatProvider("openai", s.openai_api_key, model_filter=is_openai_chat_model,
                                        fallback_models=s.provider_models.get("openai"),
                                        timeout=s.request_timeout, max_retries=s.max_retries)
        out["openai"] = openai
    if s.gemini_api_key:
        def gemini():
            from .gemini import GeminiAPIProvider
            return GeminiAPIProvider(s.gemini_api_key, image_dir=s.image_dir,
                                     fallback_models=s.provider_models.get("gemini"))
        out["gemini"] = gemini
    if s.gemini_cookie:
        def gemini_web():
            from .gemini import GeminiWebProvider
            return GeminiWebProvider(s.gemini_cookie, image_dir=s.image_dir, proxy=proxy,
                                     timeout=s.request_timeout)
        out["gemini-web"] = gemini_web
    if s.deepseek_api_key:
        def deepseek():
            from .openai_api import DEEPSEEK_BASE_URL, OpenAICompatProvider
            return OpenAICompatProvider("deepseek", s.deepseek_api_key, base_url=DEEPSEEK_BASE_URL,
                                        fallback_models=s.provider_models.get("deepseek"),
                                        timeout=s.request_timeout, max_retries=s.max_retries)
        out["deepseek"] = deepseek
    if s.deepseek_user_token:
        def deepseek_web():
            from .deepseek_web import DeepSeekWebProvider
            return DeepSeekWebProvider(s.deepseek_user_token, cookie=s.deepseek_cookie, proxy=proxy,
                                       timeout=s.request_timeout,
                                       fallback_models=s.provider_models.get("deepseek-web"))
        out["deepseek-web"] = deepseek_web
    return out


class Registry:
    def __init__(self, settings: Settings, providers: dict[str, Provider] | None = None):
        """`providers`: nhà cung cấp tạo sẵn (dùng trong test); nếu có thì chỉ dùng các nhà cung cấp này."""
        self.settings = settings
        self._instances: dict[str, Provider] = dict(providers or {})
        self._factories = {} if providers else _factories(settings)
        self._lock = threading.Lock()

    def reconfigure(self, settings: Settings) -> None:
        """Áp dụng cấu hình mới (từ tab Cài đặt): đóng các nhà cung cấp cũ, lần dùng sau tạo lại."""
        with self._lock:
            old = list(self._instances.values())
            self.settings = settings
            self._factories = _factories(settings)
            self._instances = {}
        for provider in old:
            try:
                provider.close()
            except Exception as e:   # noqa: BLE001
                log.debug("Lỗi khi đóng %s: %s", getattr(provider, "name", provider), e)

    @property
    def names(self) -> list[str]:
        return list(self._instances) + [n for n in self._factories if n not in self._instances]

    def get(self, name: str) -> Provider:
        with self._lock:
            if name not in self._instances:
                factory = self._factories.get(name)
                if factory is None:
                    configured = ", ".join(self.names) or "chưa có"
                    raise ProviderError(f"Nhà cung cấp '{name}' chưa được cấu hình (đang có: {configured}).", 400)
                self._instances[name] = factory()
            return self._instances[name]

    def _fallback_models(self, name: str) -> list[str]:
        if name == "chatgpt":
            return list(self.settings.models)
        return list(self.settings.provider_models.get(name, []))

    @property
    def default_model(self) -> str:
        """Model mặc định ở dạng đầy đủ "<provider>/<model>"."""
        model = self.settings.default_model
        provider, sep, _ = model.partition("/")
        if sep and provider in self.names:
            return model
        if "chatgpt" in self.names:
            return f"chatgpt/{model}"
        for name in self.names:
            models = self._fallback_models(name)
            if models:
                return f"{name}/{models[0]}"
        return f"{self.names[0]}/" if self.names else model

    def resolve(self, model: str | None) -> tuple[Provider, str]:
        """'gemini/gemini-2.5-flash' → (GeminiAPIProvider, 'gemini-2.5-flash')."""
        model = (model or "").strip() or self.default_model
        provider, sep, name = model.partition("/")
        if not (sep and (provider in self.names or provider in PROVIDER_LABELS)):
            provider, _, _ = self.default_model.partition("/")
            name = model
        return self.get(provider), name

    def list_models(self, timeout: float = 20) -> list[str]:
        """Danh sách model đầy đủ của mọi nhà cung cấp, lấy song song; lỗi thì dùng danh sách dự phòng."""
        names = self.names
        if not names:
            return []

        def fetch(name: str) -> list[str]:
            try:
                return self.get(name).list_models()
            except Exception as e:   # noqa: BLE001 - một nhà cung cấp lỗi không ảnh hưởng nhà khác
                log.warning("%s: không lấy được danh sách model: %s", name, e)
                return self._fallback_models(name)

        pool = ThreadPoolExecutor(max_workers=len(names))
        futures = {name: pool.submit(fetch, name) for name in names}
        wait(futures.values(), timeout=timeout)
        pool.shutdown(wait=False)
        result = []
        for name, fut in futures.items():
            models = fut.result() if fut.done() else self._fallback_models(name)
            result += [f"{name}/{m}" for m in models]
        return result
