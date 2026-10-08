"""
Google Gemini:
  - GeminiAPIProvider: API chính thức (google-genai, API key). Model có chữ "image"
    (Nano Banana, ví dụ gemini-2.5-flash-image) trả về ảnh, được lưu vào image_dir.
  - GeminiWebProvider: gemini.google.com qua cookie (gemini-webapi). Tạo ảnh bằng cách
    yêu cầu "tạo ảnh ..." với model bất kỳ.
"""

from __future__ import annotations

import json
import logging
from typing import Iterator

from .aio import BackgroundLoop
from .base import Provider, ProviderError, StreamEvent, save_image

log = logging.getLogger(__name__)

# Model không dùng để chat (embedding, TTS, live audio...) bị lọc khỏi danh sách
_GEMINI_EXCLUDED = ("embedding", "tts", "live", "native-audio", "aqa", "robotics", "computer-use")


class GeminiAPIProvider(Provider):
    name = "gemini"
    stateful = False

    def __init__(self, api_key: str, *, image_dir: str, fallback_models: list[str] | None = None):
        try:
            from google import genai
            from google.genai import errors, types
        except ImportError as e:
            raise ProviderError("Thiếu thư viện `google-genai`. Chạy: pip install google-genai") from e
        self._types, self._errors = types, errors
        self._client = genai.Client(api_key=api_key)
        self._image_dir = image_dir
        self._fallback = list(fallback_models or [])

    def check(self) -> str:
        try:
            return f"{sum(1 for _ in self._client.models.list())} model"
        except self._errors.APIError as e:
            raise ProviderError(f"gemini HTTP {e.code}: {e.message}", e.code) from e
        except Exception as e:   # noqa: BLE001
            raise ProviderError(f"gemini: {e}", 502) from e

    def list_models(self) -> list[str]:
        try:
            ids = []
            for m in self._client.models.list():
                model_id = (m.name or "").removeprefix("models/")
                if "generateContent" not in (m.supported_actions or []):
                    continue
                if model_id.startswith("gemini") and not any(k in model_id for k in _GEMINI_EXCLUDED):
                    ids.append(model_id)
            if ids:
                return sorted(ids)
        except Exception as e:   # noqa: BLE001 - lỗi mạng/khóa sai → dùng danh sách dự phòng
            log.debug("gemini: không lấy được danh sách model: %s", e)
        return list(self._fallback)

    def stream(self, prompt, *, model=None, conversation_id=None, parent_message_id=None,
               temporary=False, history=None) -> Iterator[StreamEvent]:
        model = model or (self._fallback[0] if self._fallback else None)
        if not model:
            raise ProviderError("gemini: chưa chọn model.", 400)
        types = self._types
        system = "\n\n".join(m["content"] for m in history or [] if m.get("role") == "system" and m.get("content"))
        contents = [
            types.Content(role="model" if m["role"] == "assistant" else "user",
                          parts=[types.Part(text=m["content"])])
            for m in history or [] if m.get("role") != "system" and m.get("content")
        ]
        contents.append(types.Content(role="user", parts=[types.Part(text=prompt)]))
        config = types.GenerateContentConfig(
            system_instruction=system or None,
            response_modalities=["TEXT", "IMAGE"] if "image" in model else None,
        )

        parts: list[str] = []
        images: list[str] = []
        try:
            for chunk in self._client.models.generate_content_stream(model=model, contents=contents, config=config):
                candidate = chunk.candidates[0] if chunk.candidates else None
                for part in (candidate.content.parts if candidate and candidate.content else None) or []:
                    if getattr(part, "thought", False):
                        continue
                    if part.text:
                        parts.append(part.text)
                        yield StreamEvent("delta", part.text)
                    elif part.inline_data and part.inline_data.data:
                        images.append(save_image(part.inline_data.data,
                                                 part.inline_data.mime_type or "image/png", self._image_dir))
        except self._errors.APIError as e:
            raise ProviderError(f"gemini HTTP {e.code}: {e.message}", e.code) from e
        except Exception as e:   # noqa: BLE001
            raise ProviderError(f"gemini: {e}", 502) from e
        yield StreamEvent("done", "".join(parts), model=model, images=images)


def parse_gemini_cookie(cookie: str) -> tuple[str, str | None]:
    """Lấy __Secure-1PSID và __Secure-1PSIDTS từ chuỗi cookie."""
    values = {}
    for part in cookie.split(";"):
        if "=" in part:
            key, value = part.split("=", 1)
            values[key.strip()] = value.strip()
    psid = values.get("__Secure-1PSID")
    if not psid:
        raise ProviderError("GEMINI_COOKIE thiếu __Secure-1PSID.", 401)
    return psid, values.get("__Secure-1PSIDTS")


class GeminiWebProvider(Provider):
    """
    Thread được lưu như sau: conversation_id = cid, message_id = JSON metadata của
    ChatSession ([cid, rid, rcid, ...]) để nối tiếp đúng câu trả lời trước.
    """

    name = "gemini-web"
    stateful = True

    def __init__(self, cookie: str, *, image_dir: str, proxy: str | None = None, timeout: float = 300):
        try:
            from gemini_webapi import GeminiClient
            from gemini_webapi.types import GeneratedImage
        except ImportError as e:
            raise ProviderError("Thiếu thư viện `gemini-webapi`. Chạy: pip install gemini-webapi") from e
        psid, psidts = parse_gemini_cookie(cookie)
        self._generated_image_cls = GeneratedImage
        self._client = GeminiClient(psid, psidts, proxy=proxy or None)
        self._image_dir = image_dir
        self._timeout = timeout
        self._loop = BackgroundLoop()
        self._ready = False

    def _ensure_ready(self) -> None:
        if self._ready:
            return
        try:
            # auto_refresh: thư viện tự làm mới cookie định kỳ
            self._loop.run(self._client.init(timeout=self._timeout, auto_refresh=True), timeout=self._timeout)
        except Exception as e:   # noqa: BLE001
            raise ProviderError(f"gemini-web: xác thực thất bại ({e}). Cookie có thể đã hết hạn.", 401) from e
        self._ready = True

    def check(self) -> str:
        return f"Đăng nhập thành công, {len(self.list_models()) - 1} model"

    def close(self) -> None:
        if self._ready:
            try:
                self._loop.run(self._client.close(), timeout=10)
            except Exception as e:   # noqa: BLE001
                log.debug("gemini-web: lỗi khi đóng: %s", e)
            self._ready = False

    def list_models(self) -> list[str]:
        self._ensure_ready()
        names = [m.model_name for m in self._client.list_models() or [] if m.is_available and m.model_name]
        return ["default"] + names

    def stream(self, prompt, *, model=None, conversation_id=None, parent_message_id=None,
               temporary=False, history=None) -> Iterator[StreamEvent]:
        self._ensure_ready()
        model_arg = None if model in (None, "", "default") else model
        metadata = None
        if parent_message_id:
            try:
                metadata = json.loads(parent_message_id)
            except ValueError:
                raise ProviderError("gemini-web: parent_message_id không hợp lệ.", 400)

        async def run():
            chat = self._client.start_chat(model=model_arg, metadata=metadata)
            last = None
            async for output in chat.send_message_stream(prompt, temporary=temporary):
                last = output
                if output.text_delta:
                    yield StreamEvent("delta", output.text_delta)
            if last is None:
                raise ProviderError("gemini-web: không nhận được phản hồi.", 502)
            images = []
            for image in last.images:
                try:
                    kwargs = {"full_size": True} if isinstance(image, self._generated_image_cls) else {}
                    images.append(await image.save(path=self._image_dir, **kwargs))
                except Exception as e:   # noqa: BLE001
                    log.warning("gemini-web: không lưu được ảnh: %s", e)
            yield StreamEvent("done", last.text, conversation_id=chat.cid,
                              message_id=json.dumps(chat.metadata), model=model or "default",
                              images=[p for p in images if p])

        try:
            yield from self._loop.iterate(run())
        except ProviderError:
            raise
        except Exception as e:   # noqa: BLE001
            # 400: để proxy thử mở thread mới khi không nối tiếp được thread cũ
            status = 400 if metadata else 502
            raise ProviderError(f"gemini-web: {type(e).__name__}: {e}", status) from e
