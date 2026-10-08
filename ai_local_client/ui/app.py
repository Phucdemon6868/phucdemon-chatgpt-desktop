"""
Giao diện web local (Gradio) cho ChatGPT, Gemini, DeepSeek.

- Tab 💬 Chat: lịch sử hội thoại lưu SQLite, đổi model (kể cả đổi nhà cung cấp giữa
  chừng), streaming, hiển thị ảnh do AI tạo.
- Tab ⚙️ Cài đặt: nhập API key / cookie / token và các cài đặt chung, kiểm tra kết nối,
  lưu vào .env và áp dụng ngay không cần khởi động lại.

Chạy: python -m ui.app [--port 7860]
"""

from __future__ import annotations

import argparse
import html
import logging
from dataclasses import replace
from pathlib import Path

import gradio as gr

from core.base import ProviderError, flatten
from core.config import ENV_FIELDS, SECRET_KEYS, Settings, load_settings, save_env
from core.registry import PROVIDER_LABELS, Registry
from core.store import Store

log = logging.getLogger(__name__)

IMAGE_PREFIX = "[Ảnh] "   # tin nhắn ảnh được lưu trong SQLite dưới dạng "[Ảnh] <đường dẫn>"

# (AI, [(nhà cung cấp, tiêu đề, [(biến .env, nhãn, bắt buộc)], hướng dẫn)])
PROVIDER_SECTIONS = [
    ("ChatGPT", [
        ("openai", "🔑 API chính thức (OpenAI)", [("OPENAI_API_KEY", "API key", True)],
         "Lấy tại **platform.openai.com → API keys**. Trả phí theo token, ổn định."),
        ("chatgpt", "🌐 Web (tài khoản chatgpt.com)", [("CHATGPT_COOKIE", "Cookie", True)],
         "Đăng nhập **chatgpt.com** → F12 → Network → chọn request bất kỳ tới chatgpt.com → "
         "copy giá trị header `cookie`."),
    ]),
    ("Gemini", [
        ("gemini", "🔑 API chính thức (Google AI Studio)", [("GEMINI_API_KEY", "API key", True)],
         "Lấy miễn phí tại **aistudio.google.com → Get API key**. Model có chữ `image` tạo được ảnh."),
        ("gemini-web", "🌐 Web (tài khoản gemini.google.com)", [("GEMINI_COOKIE", "Cookie", True)],
         "Đăng nhập **gemini.google.com** → F12 → Application → Cookies → dán dạng "
         "`__Secure-1PSID=...; __Secure-1PSIDTS=...`."),
    ]),
    ("DeepSeek", [
        ("deepseek", "🔑 API chính thức (DeepSeek Platform)", [("DEEPSEEK_API_KEY", "API key", True)],
         "Lấy tại **platform.deepseek.com → API keys** (cần nạp tiền trước)."),
        ("deepseek-web", "🌐 Web (tài khoản chat.deepseek.com)",
         [("DEEPSEEK_USER_TOKEN", "userToken", True), ("DEEPSEEK_COOKIE", "Cookie (tùy chọn)", False)],
         "Đăng nhập **chat.deepseek.com** → F12 → Application → Local Storage → copy `userToken`. "
         "Chỉ cần cookie khi bị chặn (lỗi 403)."),
    ]),
]

THEME = gr.themes.Soft(primary_hue="indigo", neutral_hue="slate")
CSS = """
#app-header { padding: 4px 4px 0; }
#app-header h1 { margin: 0; font-size: 1.6rem; }
.chips { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 6px; }
.chip { padding: 2px 10px; border-radius: 999px; font-size: 0.8rem; border: 1px solid transparent; }
.chip.on { background: #dcfce7; color: #166534; border-color: #bbf7d0; }
.chip.off { background: #f1f5f9; color: #64748b; border-color: #e2e8f0; }
.dark .chip.on { background: #14532d; color: #dcfce7; border-color: #166534; }
.dark .chip.off { background: #1e293b; color: #94a3b8; border-color: #334155; }
.provider-card { border-radius: 12px; }
.hint p { font-size: 0.85rem; opacity: 0.85; }
"""


# ─────────────────────────── Tiện ích ─────────────────────────────

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


def env_value(settings: Settings, key: str) -> str:
    value = getattr(settings, ENV_FIELDS[key])
    if isinstance(value, bool):
        return "1" if value else "0"
    return str(value)


def secret_placeholder(settings: Settings, key: str) -> str:
    value = env_value(settings, key)
    if not value:
        return "Chưa cấu hình"
    tail = value[-4:] if len(value) > 12 else ""
    return f"Đã lưu (••••{tail}) — để trống để giữ nguyên, nhập mới để thay"


def status_html(registry: Registry) -> str:
    configured = set(registry.names)
    chips = "".join(
        f'<span class="chip {"on" if name in configured else "off"}">'
        f'{"✅" if name in configured else "⚪"} {html.escape(label)}</span>'
        for name, label in PROVIDER_LABELS.items()
    )
    hint = "" if configured else " — mở tab <b>⚙️ Cài đặt</b> để nhập API key hoặc cookie"
    return (f'<div id="app-header"><h1>🤖 AI Local</h1>'
            f'<div>ChatGPT · Gemini · DeepSeek trên máy của bạn{hint}</div>'
            f'<div class="chips">{chips}</div></div>')


# ─────────────────────────── Giao diện ────────────────────────────

def build_ui(settings: Settings, store: Store, registry: Registry | None = None,
             env_file: str | Path = ".env") -> gr.Blocks:
    registry = registry or Registry(settings)

    def provider_name(model: str | None) -> str | None:
        try:
            return registry.resolve(model)[0].name
        except ProviderError:
            return None

    def model_choices() -> list[str]:
        return registry.list_models() if registry.names else []

    def chat_model_value() -> str | None:
        return registry.default_model if registry.names else None

    AUTO = ("Tự chọn (ChatGPT nếu có, không thì nhà cung cấp đầu tiên)", "")

    def conv_choices() -> list[tuple[str, str]]:
        return [(c.title, c.id) for c in store.list_conversations()]

    # ── Chat ────────────────────────────────────────────────────

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
        models = model_choices()
        return gr.update(choices=models, value=current if current in models else chat_model_value())

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

    # ── Cài đặt ─────────────────────────────────────────────────

    def form_settings(keys: list[str], values: list) -> Settings:
        """Cấu hình hiện tại + giá trị trên form (ô bí mật để trống = giữ nguyên)."""
        changes = {}
        for key, value in zip(keys, values):
            value = "" if value is None else str(value).strip()
            if key in SECRET_KEYS and not value:
                continue
            field = ENV_FIELDS[key]
            current = getattr(registry.settings, field)
            if isinstance(current, bool):
                changes[field] = value.lower() in ("1", "true", "yes")
            elif isinstance(current, int):
                changes[field] = int(float(value or current))
            else:
                changes[field] = value
        return replace(registry.settings, **changes)

    def apply(updates: dict[str, str]) -> None:
        save_env(updates, env_file)
        registry.reconfigure(load_settings(env_file))

    with gr.Blocks(title="AI Local") as demo:
        header = gr.HTML(status_html(registry))
        conv_state = gr.State(None)

        with gr.Tabs():
            # ───────────── Tab Chat ─────────────
            with gr.Tab("💬 Chat"):
                with gr.Row(equal_height=False):
                    with gr.Column(scale=1, min_width=270):
                        model = gr.Dropdown(model_choices(), value=chat_model_value(),
                                            label="Model (nhà cung cấp/model)", allow_custom_value=True)
                        refresh_btn = gr.Button("🔄 Tải lại danh sách model", size="sm")
                        new_btn = gr.Button("＋ Hội thoại mới", variant="primary")
                        conv_list = gr.Radio(conv_choices(), label="Lịch sử", value=None)
                        del_btn = gr.Button("🗑 Xóa hội thoại đang chọn", variant="stop", size="sm")
                    with gr.Column(scale=4):
                        chatbot = gr.Chatbot(
                            height=600, label="AI", show_label=False,
                            placeholder="### Xin chào 👋\nChọn model bên trái và bắt đầu trò chuyện. "
                                        "Chưa có model? Mở tab **⚙️ Cài đặt** để nhập API key hoặc cookie.")
                        with gr.Row():
                            box = gr.Textbox(placeholder="Nhập tin nhắn… (Enter để gửi, Shift+Enter xuống dòng)",
                                             show_label=False, scale=8, lines=1, max_lines=8, autofocus=True)
                            send_btn = gr.Button("Gửi ➤", variant="primary", scale=1, min_width=90)

            # ───────────── Tab Cài đặt ─────────────
            with gr.Tab("⚙️ Cài đặt"):
                gr.Markdown(
                    "Thông tin được lưu vào file `.env` trên máy bạn và **áp dụng ngay**. "
                    "Ô API key / cookie để trống nghĩa là **giữ nguyên** giá trị đã lưu. "
                    "Bấm **Kiểm tra** để thử kết nối trước khi lưu.\n\n"
                    "⚠️ Chế độ 🌐 Web là không chính thức: có thể vi phạm điều khoản và tài khoản có thể bị khóa. "
                    "Cookie/token bằng quyền đăng nhập, đừng chia sẻ.")

                secret_boxes: dict[str, gr.Textbox] = {}
                with gr.Tabs():
                    for ai, forms in PROVIDER_SECTIONS:
                        with gr.Tab(ai):
                            with gr.Row(equal_height=True):
                                for name, title, fields, help_text in forms:
                                    with gr.Column(elem_classes="provider-card", variant="panel"):
                                        gr.Markdown(f"#### {title}")
                                        gr.Markdown(help_text, elem_classes="hint")
                                        boxes = []
                                        for key, label, _required in fields:
                                            tb = gr.Textbox(label=label, type="password",
                                                            placeholder=secret_placeholder(registry.settings, key))
                                            secret_boxes[key] = tb
                                            boxes.append(tb)
                                        with gr.Row():
                                            test_btn = gr.Button("🔌 Kiểm tra", size="sm")
                                            clear_btn = gr.Button("🗑 Xóa", size="sm", variant="stop")
                                        result = gr.Markdown()
                                        keys = [k for k, _, _ in fields]

                                        def test(*values, name=name, keys=keys):
                                            temp = Registry(form_settings(keys, list(values)))
                                            try:
                                                provider = temp.get(name)
                                                try:
                                                    return f"✅ {provider.check()}"
                                                finally:
                                                    provider.close()
                                            except ProviderError as e:
                                                return f"❌ {e}"
                                            except Exception as e:   # noqa: BLE001
                                                return f"❌ {type(e).__name__}: {e}"

                                        def clear(keys=keys):
                                            apply({k: "" for k in keys})
                                            return ([gr.update(value="", placeholder=secret_placeholder(registry.settings, k))
                                                     for k in keys] + [status_html(registry), "🗑 Đã xóa."])

                                        test_btn.click(test, boxes, result)
                                        clear_btn.click(clear, None, boxes + [header, result])

                with gr.Accordion("🛠 Cài đặt chung", open=True):
                    s = registry.settings
                    with gr.Row():
                        default_model = gr.Dropdown(
                            [AUTO] + model_choices(), value="" if s.default_model == "auto" else s.default_model,
                            label="Model mặc định", allow_custom_value=True,
                            info="Dạng <nhà cung cấp>/<model>, ví dụ gemini/gemini-2.5-flash")
                        web_proxy = gr.Textbox(s.web_proxy, label="Proxy cho bản web",
                                               placeholder="http://user:pass@host:port",
                                               info="Dùng cho Gemini web và DeepSeek web")
                    with gr.Row():
                        timeout = gr.Number(s.request_timeout, label="Thời gian chờ (giây)", precision=0, minimum=10)
                        retries = gr.Number(s.max_retries, label="Số lần thử lại (ChatGPT web)", precision=0, minimum=0)
                        temporary = gr.Checkbox(s.temporary_chat, label="Proxy dùng chat tạm (không lưu lịch sử web)")
                    with gr.Row():
                        image_dir = gr.Textbox(s.image_dir, label="Thư mục lưu ảnh",
                                               info="Đổi thư mục cần khởi động lại UI để hiển thị ảnh")
                        proxy_key = gr.Textbox(label="Khóa bảo vệ proxy /v1 (PROXY_API_KEY)", type="password",
                                               placeholder=secret_placeholder(s, "PROXY_API_KEY"),
                                               info="Proxy (python -m server) cần khởi động lại để nhận thay đổi")
                    secret_boxes["PROXY_API_KEY"] = proxy_key

                save_btn = gr.Button("💾 Lưu cài đặt", variant="primary", size="lg")
                save_result = gr.Markdown()

                general = {"DEFAULT_MODEL": default_model, "WEB_PROXY": web_proxy, "CHATGPT_TIMEOUT": timeout,
                           "CHATGPT_MAX_RETRIES": retries, "CHATGPT_TEMPORARY_CHAT": temporary,
                           "IMAGE_DIR": image_dir}
                save_keys = list(secret_boxes) + list(general)

                def save(*values):
                    try:
                        new = form_settings(save_keys, list(values))
                    except ValueError as e:
                        return [gr.update()] * (len(secret_boxes) + 3) + [f"❌ Giá trị không hợp lệ: {e}"]
                    apply({k: env_value(new, k) for k in save_keys})
                    models = model_choices()
                    return ([gr.update(value="", placeholder=secret_placeholder(registry.settings, k))
                             for k in secret_boxes]
                            + [status_html(registry),
                               gr.update(choices=models, value=chat_model_value()),
                               gr.update(choices=[AUTO] + models),
                               f"✅ Đã lưu và áp dụng. Nhà cung cấp đang bật: "
                               f"{', '.join(registry.names) or 'chưa có'}."])

                save_btn.click(save, list(secret_boxes.values()) + list(general.values()),
                               list(secret_boxes.values()) + [header, model, default_model, save_result])

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
    ap.add_argument("--env-file", default=".env", help="file lưu cấu hình (mặc định .env)")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO)
    settings = load_settings(args.env_file)
    Path(settings.image_dir).mkdir(parents=True, exist_ok=True)
    if args.host not in ("127.0.0.1", "localhost"):
        log.warning("UI mở ra ngoài localhost: ai truy cập được UI đều sửa được cookie/khóa trong tab Cài đặt.")
    build_ui(settings, Store(settings.db_path), env_file=args.env_file).queue().launch(
        server_name=args.host, server_port=args.port, theme=THEME, css=CSS,
        allowed_paths=[str(Path(settings.image_dir).resolve())])


if __name__ == "__main__":
    main()
