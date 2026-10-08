"""API chính thức dạng OpenAI: dùng cho OpenAI và DeepSeek (DeepSeek tương thích định dạng OpenAI)."""

from __future__ import annotations

import logging
from typing import Callable, Iterator

from .base import Provider, ProviderError, StreamEvent, to_api_messages

log = logging.getLogger(__name__)

DEEPSEEK_BASE_URL = "https://api.deepseek.com"
# Model OpenAI không dùng để chat (âm thanh, ảnh, embedding...) bị lọc khỏi danh sách
_OPENAI_EXCLUDED = ("audio", "realtime", "tts", "transcribe", "embedding", "image", "dall-e",
                    "whisper", "moderation", "search", "davinci", "babbage")


def is_openai_chat_model(model_id: str) -> bool:
    return model_id.startswith(("gpt-", "o1", "o3", "o4", "chatgpt-")) and \
        not any(k in model_id for k in _OPENAI_EXCLUDED)


class OpenAICompatProvider(Provider):
    stateful = False

    def __init__(self, name: str, api_key: str, *, base_url: str | None = None,
                 fallback_models: list[str] | None = None,
                 model_filter: Callable[[str], bool] | None = None,
                 timeout: float = 180, max_retries: int = 3, http_client=None):
        try:
            import openai
        except ImportError as e:
            raise ProviderError("Thiếu thư viện `openai`. Chạy: pip install openai") from e
        self._openai = openai
        self.name = name
        self._fallback = list(fallback_models or [])
        self._filter = model_filter or (lambda _: True)
        self._client = openai.OpenAI(api_key=api_key, base_url=base_url, timeout=timeout,
                                     max_retries=max_retries, http_client=http_client)

    def _error(self, e: Exception) -> ProviderError:
        if isinstance(e, self._openai.APIStatusError):
            return ProviderError(f"{self.name} HTTP {e.status_code}: {e.message}", e.status_code)
        return ProviderError(f"{self.name}: {e}", 502)

    def list_models(self) -> list[str]:
        try:
            ids = sorted(m.id for m in self._client.models.list() if self._filter(m.id))
            if ids:
                return ids
        except self._openai.OpenAIError as e:
            log.debug("%s: không lấy được danh sách model: %s", self.name, e)
        return list(self._fallback)

    def stream(self, prompt, *, model=None, conversation_id=None, parent_message_id=None,
               temporary=False, history=None) -> Iterator[StreamEvent]:
        model = model or (self._fallback[0] if self._fallback else None)
        if not model:
            raise ProviderError(f"{self.name}: chưa chọn model.", 400)
        parts: list[str] = []
        try:
            response = self._client.chat.completions.create(
                model=model, messages=to_api_messages(history, prompt), stream=True)
            for chunk in response:
                if not chunk.choices:
                    continue
                # DeepSeek trả phần suy nghĩ ở delta.reasoning_content: không hiển thị, giống ChatGPT web
                delta = chunk.choices[0].delta.content
                if delta:
                    parts.append(delta)
                    yield StreamEvent("delta", delta)
        except self._openai.OpenAIError as e:
            raise self._error(e) from e
        yield StreamEvent("done", "".join(parts), model=model)
