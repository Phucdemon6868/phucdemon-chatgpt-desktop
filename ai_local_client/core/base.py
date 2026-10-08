"""Giao diện chung cho mọi nhà cung cấp AI (ChatGPT, Gemini, DeepSeek...)."""

from __future__ import annotations

import time
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterator


class ProviderError(RuntimeError):
    def __init__(self, message: str, status: int | None = None):
        super().__init__(message)
        self.status = status


@dataclass
class StreamEvent:
    type: str                         # "delta" | "done"
    text: str = ""                    # delta: phần mới; done: toàn bộ câu trả lời
    conversation_id: str | None = None
    message_id: str | None = None     # dùng làm parent_message_id cho lượt sau
    model: str | None = None
    images: list[str] = field(default_factory=list)   # done: đường dẫn ảnh đã lưu (nếu có)


class Provider(ABC):
    """
    Một nhà cung cấp AI.

    - stateful=True (bản web): server giữ lịch sử theo thread, chỉ cần gửi tin nhắn mới
      kèm conversation_id/parent_message_id của lượt trước.
    - stateful=False (API chính thức): không có thread, mỗi lượt phải gửi kèm `history`
      (list {"role", "content"}) các tin nhắn trước đó.
    """

    name: str = ""
    stateful: bool = True

    @abstractmethod
    def list_models(self) -> list[str]:
        ...

    @abstractmethod
    def stream(
        self,
        prompt: str,
        *,
        model: str | None = None,
        conversation_id: str | None = None,
        parent_message_id: str | None = None,
        temporary: bool = False,
        history: list[dict[str, str]] | None = None,
    ) -> Iterator[StreamEvent]:
        """Yield StreamEvent("delta") cho từng mẩu text và một StreamEvent("done") ở cuối."""

    def check(self) -> str:
        """Kiểm tra đăng nhập/khóa bằng một request thật; lỗi thì ném ProviderError."""
        return f"{len(self.list_models())} model"

    def close(self) -> None:
        """Giải phóng tài nguyên (kết nối, luồng nền) khi cấu hình thay đổi."""

    def ask(self, prompt: str, **kwargs) -> StreamEvent:
        """Phiên bản không stream: trả về StreamEvent("done")."""
        final = None
        for ev in self.stream(prompt, **kwargs):
            if ev.type == "done":
                final = ev
        assert final is not None
        return final


def save_image(data: bytes, mime_type: str, image_dir: str | Path) -> str:
    """Lưu ảnh do AI tạo ra, trả về đường dẫn tuyệt đối."""
    folder = Path(image_dir)
    folder.mkdir(parents=True, exist_ok=True)
    ext = {"image/jpeg": ".jpg", "image/webp": ".webp", "image/gif": ".gif"}.get(mime_type, ".png")
    path = folder / f"{time.strftime('%Y%m%d-%H%M%S')}-{uuid.uuid4().hex[:6]}{ext}"
    path.write_bytes(data)
    return str(path.resolve())


def to_api_messages(history: list[dict[str, str]] | None, prompt: str) -> list[dict[str, str]]:
    """Chuẩn hóa lịch sử cho API chính thức: chỉ giữ system/user/assistant, bỏ tin rỗng."""
    out = []
    for m in history or []:
        role = m.get("role", "user")
        role = role if role in ("system", "user", "assistant") else "user"
        if m.get("content"):
            out.append({"role": role, "content": m["content"]})
    out.append({"role": "user", "content": prompt})
    return out


_ROLE_LABELS = {"system": "System instructions", "user": "User", "assistant": "Assistant", "tool": "Tool result"}


def flatten(messages: list[dict[str, str]]) -> str:
    """Gộp lịch sử thành một prompt duy nhất."""
    if len(messages) == 1 and messages[0]["role"] == "user":
        return messages[0]["content"]
    blocks = [
        "Below is a conversation transcript. Follow the system instructions (if any) "
        "and reply as the assistant to the last User message. Reply with the answer only."
    ]
    for m in messages:
        label = _ROLE_LABELS.get(m["role"], m["role"].capitalize())
        blocks.append(f"[{label}]\n{m['content']}")
    return "\n\n".join(blocks)
