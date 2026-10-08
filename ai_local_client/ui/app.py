"""
Giao diện web local (Gradio) cho ChatGPT, Gemini, DeepSeek: lịch sử hội thoại lưu SQLite,
đổi model (kể cả đổi nhà cung cấp giữa chừng), streaming, hiển thị ảnh do AI tạo.
Chạy: python -m ui.app [--port 7860]
"""

from __future__ import annotations

import argparse
import logging
from pathlib import Path

import gradio as gr

from core.base import ProviderError, flatten
from core.config import Settings, load_settings
from core.registry import Registry
from core.store import Store

log = logging.getLogger(__name__)

IMAGE_PREFIX = "[Ảnh] "   # tin nhắn ảnh được lưu trong SQLite dưới dạng "[Ảnh] <đường dẫn>"


def to_display(messages: list[dict]) -> list[dict]:
    """Tin nhắn trong SQLite → tin nhắn Chatbot (ảnh còn tồn tại thì hiển thị ảnh)."""
    out = []
    for m in messages:
        content = m["content"]
        if content.startswith(IMAGE_PREFIX) and Path(content[len(IMAGE_PREFIX):]).is_file():
            content = gr.Image(content[len(IMAGE_PREFIX):])
        out.append({"role": m["role"], "content": content})
    return out


def text_history(messages: list[dict]) -> list[dict]:
    """Lịch sử gửi cho AI: bỏ tin nhắn ảnh."""
    return [m for m in messages if not m["content"].startswith(IMAGE_PREFIX)]


def build_ui(settings: Settings, store: Store, registry: Registry | None = None) -> gr.Blocks:
    registry = registry or Registry(settings)

    def provider_name(model: str | None) -> str | None:
        try:
            return registry.resolve(model)[0].name
        except ProviderError:
            return None

    def conv_choices() -> list[tuple[str, str]]:
        return [(c.title, c.id) for c in store.list_conversations()]

    def load_conversation(conv_id: str | None):
        if not conv_id:
            return [], gr.update()
        conv = store.get_conversation(conv_id)
        return to_display(store.get_messages(conv_id)), (conv.model if conv else gr.update())

    def new_chat():
        return [], None, gr.update(choices=conv_choices(), value=None)

    def delete_chat(conv_id: str | None):
        if conv_id:
            store.delete_conversation(conv_id)
        return [], None, gr.update(choices=conv_choices(), value=None)

    def refresh_models(current: str | None):
        models = registry.list_models()
        return gr.update(choices=models, value=current if current in models else registry.default_model)

    def send(text: str, history: list, conv_id: str | None, model: str):
        text = (text or "").strip()
        model = model or registry.default_model
        if not text:
            yield history, "", conv_id, gr.update()
            return

        try:
            provider, model_name = registry.resolve(model)
        except ProviderError as e:
            yield history, text, conv_id, gr.update()
            gr.Warning(str(e))
            return

        if not conv_id:
            conv_id = store.create_conversation(text.splitlines()[0][:60], model).id
        conv = store.get_conversation(conv_id)
        previous = text_history(store.get_messages(conv_id))
        store.add_message(conv_id, "user", text)

        kwargs: dict = {"model": model_name}
        prompt = text
        if not provider.stateful:
            kwargs["history"] = previous
        elif conv and conv.remote_id and provider_name(conv.model) == provider.name:
            kwargs.update(conversation_id=conv.remote_id, parent_message_id=conv.parent_message_id)
        elif previous:
            # Đổi sang nhà cung cấp bản web khác giữa chừng: mở thread mới kèm toàn bộ lịch sử
            prompt = flatten(previous + [{"role": "user", "content": text}])

        history = list(history or []) + [
            {"role": "user", "content": text},
            {"role": "assistant", "content": ""},
        ]
        yield history, "", conv_id, gr.update(choices=conv_choices(), value=conv_id)

        reply, images = "", []
        try:
            for ev in provider.stream(prompt, **kwargs):
                if ev.type == "delta":
                    reply += ev.text
                    history[-1]["content"] = reply
                    yield history, "", conv_id, gr.update()
                else:
                    reply, images = ev.text or reply, ev.images
                    if provider.stateful:
                        store.update_thread(conv_id, remote_id=ev.conversation_id,
                                            parent_message_id=ev.message_id, model=model)
                    else:
                        # Bản API không có thread: xóa thread cũ để lần sau không nối nhầm
                        store.update_thread(conv_id, remote_id="", parent_message_id="", model=model)
        except ProviderError as e:
            history[-1]["content"] = (reply + f"\n\n⚠️ Lỗi: {e}").strip()
            yield history, text, conv_id, gr.update()   # trả lại text để gửi lại
            return

        history[-1]["content"] = reply or ("(Ảnh)" if images else "")
        store.add_message(conv_id, "assistant", history[-1]["content"])
        for path in images:
            store.add_message(conv_id, "assistant", IMAGE_PREFIX + path)
            history.append({"role": "assistant", "content": gr.Image(path)})
        yield history, "", conv_id, gr.update(choices=conv_choices(), value=conv_id)

    with gr.Blocks(title="AI Local") as demo:
        conv_state = gr.State(None)
        with gr.Row():
            with gr.Column(scale=1, min_width=260):
                models = registry.list_models()
                model = gr.Dropdown(models, value=registry.default_model, label="Model (nhà cung cấp/model)",
                                    allow_custom_value=True)
                refresh_btn = gr.Button("🔄 Tải lại danh sách model", size="sm")
                new_btn = gr.Button("＋ Hội thoại mới", variant="primary")
                conv_list = gr.Radio(conv_choices(), label="Lịch sử", value=None)
                del_btn = gr.Button("🗑 Xóa hội thoại đang chọn", variant="stop")
            with gr.Column(scale=4):
                chatbot = gr.Chatbot(height=620, label="AI")
                with gr.Row():
                    box = gr.Textbox(placeholder="Nhập tin nhắn… (Enter để gửi, Shift+Enter xuống dòng)",
                                     show_label=False, scale=8, lines=1, max_lines=8)
                    send_btn = gr.Button("Gửi", variant="primary", scale=1)

        outputs = [chatbot, box, conv_state, conv_list]
        box.submit(send, [box, chatbot, conv_state, model], outputs)
        send_btn.click(send, [box, chatbot, conv_state, model], outputs)
        refresh_btn.click(refresh_models, model, model)
        new_btn.click(new_chat, None, [chatbot, conv_state, conv_list])
        del_btn.click(delete_chat, conv_state, [chatbot, conv_state, conv_list])
        conv_list.input(lambda cid: (*load_conversation(cid), cid), conv_list, [chatbot, model, conv_state])

    return demo


def main() -> None:
    ap = argparse.ArgumentParser(description="Web UI local cho ChatGPT, Gemini, DeepSeek")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=7860)
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO)
    settings = load_settings()
    Path(settings.image_dir).mkdir(parents=True, exist_ok=True)
    build_ui(settings, Store(settings.db_path)).queue().launch(
        server_name=args.host, server_port=args.port, allowed_paths=[str(Path(settings.image_dir).resolve())])


if __name__ == "__main__":
    main()
