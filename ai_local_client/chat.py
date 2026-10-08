"""
CLI chat trong terminal cho ChatGPT, Gemini, DeepSeek.
Chạy: python chat.py
"""

from __future__ import annotations

import sys

from core.base import ProviderError, flatten
from core.config import load_settings
from core.registry import PROVIDER_LABELS, Registry

HELP_TEXT = """
Lệnh đặc biệt:
  /new                 - Bắt đầu cuộc trò chuyện mới
  /model <tên>         - Đổi model, dạng <nhà cung cấp>/<model>
                         (ví dụ: /model gemini/gemini-2.5-flash, /model deepseek-web/expert+think)
  /models              - Liệt kê model của mọi nhà cung cấp đã cấu hình
  /providers           - Liệt kê nhà cung cấp đã cấu hình
  /quit                - Thoát
  /help                - Hiển thị trợ giúp này
Ảnh do AI tạo (Gemini) được lưu vào thư mục IMAGE_DIR (mặc định data/images).
"""


def read_cookie() -> str:
    print("Chưa cấu hình nhà cung cấp nào trong .env.")
    print("Dán cookie ChatGPT vào đây (nhấn Enter 2 lần để kết thúc):")
    lines = []
    while True:
        line = input()
        if line == "" and lines:
            break
        lines.append(line)
    return " ".join(lines).strip()


def main() -> None:
    settings = load_settings()
    registry = Registry(settings)
    if not registry.names:
        settings.cookie = read_cookie()
        registry = Registry(settings)
    if not registry.names:
        print("Lỗi: Chưa cấu hình nhà cung cấp nào (xem .env.example).")
        sys.exit(1)

    model = registry.default_model
    history: list[dict[str, str]] = []          # lịch sử hiển thị, dùng cho API và khi đổi nhà cung cấp
    thread: dict[str, str | None] = {}          # thread của bản web: provider, conversation_id, message_id

    print("=" * 60)
    print("  AI Client  |  model:", model)
    print("  Nhà cung cấp:", ", ".join(registry.names))
    print("  Nhập /help để xem lệnh đặc biệt")
    print("=" * 60)

    while True:
        try:
            user_input = input("\nBạn: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nThoát.")
            break
        if not user_input:
            continue

        if user_input.startswith("/"):
            cmd, _, arg = user_input[1:].partition(" ")
            cmd = cmd.lower()
            if cmd == "quit":
                print("Thoát.")
                break
            elif cmd == "new":
                history, thread = [], {}
                print("✓ Đã bắt đầu cuộc trò chuyện mới.")
            elif cmd == "model":
                if arg.strip():
                    model = arg.strip()
                    print(f"✓ Đã đổi sang model: {model}")
                else:
                    print(f"Model hiện tại: {model}\nDùng: /model <nhà cung cấp>/<model>")
            elif cmd == "models":
                print("Đang lấy danh sách model...")
                for m in registry.list_models():
                    print(f"  {m}{' ← hiện tại' if m == model else ''}")
            elif cmd == "providers":
                for name in registry.names:
                    print(f"  {name:<14} {PROVIDER_LABELS.get(name, '')}")
            elif cmd == "help":
                print(HELP_TEXT)
            else:
                print(f"Lệnh không hợp lệ: /{cmd}  —  Nhập /help để xem danh sách.")
            continue

        try:
            provider, model_name = registry.resolve(model)
        except ProviderError as e:
            print(f"✗ Lỗi: {e}")
            continue

        kwargs: dict = {"model": model_name}
        prompt = user_input
        if not provider.stateful:
            kwargs["history"] = history
        elif thread.get("provider") == provider.name:
            kwargs.update(conversation_id=thread["conversation_id"], parent_message_id=thread["message_id"])
        elif history:
            # Đổi sang nhà cung cấp bản web khác giữa chừng: mở thread mới kèm toàn bộ lịch sử
            prompt = flatten(history + [{"role": "user", "content": user_input}])

        print(f"\n{model}: ", end="", flush=True)
        try:
            for ev in provider.stream(prompt, **kwargs):
                if ev.type == "delta":
                    print(ev.text, end="", flush=True)
                    continue
                print()
                for path in ev.images:
                    print(f"🖼  Ảnh đã lưu: {path}")
                history += [{"role": "user", "content": user_input}, {"role": "assistant", "content": ev.text}]
                if provider.stateful:
                    thread = {"provider": provider.name, "conversation_id": ev.conversation_id,
                              "message_id": ev.message_id or thread.get("message_id")}
                else:
                    thread = {}
        except ProviderError as e:
            print(f"\n✗ Lỗi: {e}")


if __name__ == "__main__":
    main()
