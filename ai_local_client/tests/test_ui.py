from core.base import ProviderError, StreamEvent
from core.config import Settings
from core.registry import Registry
from core.store import Store
from ui.app import IMAGE_PREFIX, build_ui


class Web:
    stateful = True

    def __init__(self, name):
        self.name, self.calls = name, []

    def list_models(self):
        return ["m"]

    def stream(self, prompt, **kw):
        self.calls.append({"prompt": prompt, **kw})
        yield StreamEvent("delta", "ok")
        yield StreamEvent("done", "ok", conversation_id=f"{self.name}-c", message_id=f"m{len(self.calls)}")


class Api(Web):
    stateful = False

    def stream(self, prompt, **kw):
        self.calls.append({"prompt": prompt, **kw})
        yield StreamEvent("done", "img", images=[__file__])


def get_send(demo):
    for fn in demo.fns.values():
        if getattr(fn.fn, "__name__", "") == "send":
            return fn.fn
    raise AssertionError("send not found")


def run(send, text, conv_id, model):
    *_, last = send(text, [], conv_id, model)
    return last


def test_send_routes_threads_history_and_images(tmp_path):
    chatgpt, ds_web, gemini = Web("chatgpt"), Web("deepseek-web"), Api("gemini")
    reg = Registry(Settings(), providers={"chatgpt": chatgpt, "deepseek-web": ds_web, "gemini": gemini})
    store = Store(tmp_path / "t.db")
    send = get_send(build_ui(Settings(), store, reg))

    _, _, conv_id, _ = run(send, "Hi", None, "chatgpt/auto")
    run(send, "Again", conv_id, "chatgpt/auto")
    assert chatgpt.calls[1]["conversation_id"] == "chatgpt-c" and chatgpt.calls[1]["parent_message_id"] == "m1"

    # Đổi sang bản web khác: mở thread mới kèm toàn bộ lịch sử
    run(send, "Third", conv_id, "deepseek-web/default")
    assert "conversation_id" not in ds_web.calls[0] and "[User]\nThird" in ds_web.calls[0]["prompt"]

    # API chính thức: nhận lịch sử, ảnh trả về được lưu và hiển thị
    history, *_ = run(send, "Vẽ", conv_id, "gemini/x")
    assert [m["content"] for m in gemini.calls[0]["history"]][:2] == ["Hi", "ok"]
    assert store.get_messages(conv_id)[-1]["content"] == IMAGE_PREFIX + __file__
    assert history[-1]["role"] == "assistant" and not isinstance(history[-1]["content"], str)
    # Sau lượt API, thread cũ bị xóa → quay lại deepseek-web sẽ mở thread mới
    assert store.get_conversation(conv_id).remote_id == ""


def test_send_unconfigured_provider_returns_text(tmp_path):
    reg = Registry(Settings(), providers={"chatgpt": Web("chatgpt")})
    send = get_send(build_ui(Settings(), Store(tmp_path / "t.db"), reg))
    try:
        history, box, conv_id, _ = run(send, "Hi", None, "openai/gpt-4o")
    except ProviderError:
        raise AssertionError("lỗi phải được báo trên UI, không ném ra ngoài")
    assert box == "Hi" and conv_id is None
