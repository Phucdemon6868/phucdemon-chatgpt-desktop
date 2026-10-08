import json

import httpx
import pytest

from core.aio import BackgroundLoop
from core.base import Provider, ProviderError, StreamEvent
from core.config import Settings
from core.registry import Registry


# ─────────────────────────── Registry ─────────────────────────────

class FakeProvider(Provider):
    def __init__(self, name, models, stateful=True, fail=False):
        self.name, self._models, self.stateful, self.fail = name, models, stateful, fail

    def list_models(self):
        if self.fail:
            raise ProviderError("down", 502)
        return self._models

    def stream(self, prompt, **kw):
        yield StreamEvent("done", prompt)


def test_registry_configured_providers_and_resolve():
    s = Settings(cookie="c", gemini_api_key="g", deepseek_user_token="t")
    reg = Registry(s)
    assert reg.names == ["chatgpt", "gemini", "deepseek-web"]
    reg._instances.update({"chatgpt": FakeProvider("chatgpt", []), "gemini": FakeProvider("gemini", [])})
    assert reg.resolve("gemini/gemini-x")[1] == "gemini-x"
    assert reg.resolve("gemini/gemini-x")[0].name == "gemini"
    # Không có tiền tố → nhà cung cấp mặc định (ChatGPT)
    provider, model = reg.resolve("gpt-4o")
    assert (provider.name, model) == ("chatgpt", "gpt-4o")
    assert reg.default_model == "chatgpt/auto"
    with pytest.raises(ProviderError) as ei:
        reg.resolve("openai/gpt-4o")
    assert ei.value.status == 400


def test_registry_default_without_chatgpt():
    reg = Registry(Settings(deepseek_api_key="k"))
    assert reg.default_model == "deepseek/deepseek-flash"
    reg = Registry(Settings(deepseek_api_key="k", default_model="deepseek/deepseek-pro"))
    assert reg.default_model == "deepseek/deepseek-pro"


def test_registry_list_models_falls_back_on_error():
    reg = Registry(Settings(), providers={
        "chatgpt": FakeProvider("chatgpt", ["auto"]),
        "deepseek-web": FakeProvider("deepseek-web", [], fail=True),
    })
    reg.settings.provider_models["deepseek-web"] = ["default"]
    assert reg.list_models() == ["chatgpt/auto", "deepseek-web/default"]


# ─────────────────────────── Async bridge ─────────────────────────

def test_background_loop_iterate_and_errors():
    loop = BackgroundLoop()

    async def gen(fail):
        yield 1
        yield 2
        if fail:
            raise ValueError("boom")

    assert list(loop.iterate(gen(False))) == [1, 2]
    with pytest.raises(ValueError):
        list(loop.iterate(gen(True)))


# ─────────────────────────── OpenAI-compatible API ────────────────

def sse_body(chunks):
    lines = [f"data: {json.dumps(c)}\n\n" for c in chunks] + ["data: [DONE]\n\n"]
    return "".join(lines).encode()


def make_openai(handler, **kw):
    from core.openai_api import OpenAICompatProvider
    return OpenAICompatProvider("deepseek", "key", base_url="https://api.test/v1", max_retries=0,
                                http_client=httpx.Client(transport=httpx.MockTransport(handler)), **kw)


def test_openai_compat_stream_and_history():
    seen = {}

    def handler(request):
        seen["body"] = json.loads(request.content)
        chunk = lambda d: {"id": "x", "object": "chat.completion.chunk", "created": 0, "model": "m",
                           "choices": [{"index": 0, "delta": d, "finish_reason": None}]}
        body = sse_body([chunk({"role": "assistant", "reasoning_content": "nghĩ"}),
                         chunk({"content": "Xin "}), chunk({"content": "chào"})])
        return httpx.Response(200, content=body, headers={"content-type": "text/event-stream"})

    p = make_openai(handler)
    history = [{"role": "system", "content": "Ngắn gọn"}, {"role": "user", "content": "A"},
               {"role": "assistant", "content": "B"}, {"role": "tool", "content": "T"}]
    events = list(p.stream("C", model="deepseek-flash", history=history))
    assert [e.text for e in events if e.type == "delta"] == ["Xin ", "chào"]
    assert events[-1].text == "Xin chào"
    assert seen["body"]["model"] == "deepseek-flash" and seen["body"]["stream"] is True
    assert [m["role"] for m in seen["body"]["messages"]] == ["system", "user", "assistant", "user", "user"]


def test_openai_compat_errors_and_models():
    def handler(request):
        if request.url.path.endswith("/models"):
            data = [{"id": i, "object": "model", "created": 0, "owned_by": "x"}
                    for i in ["gpt-4o", "tts-1", "text-embedding-3-small", "o4-mini"]]
            return httpx.Response(200, json={"object": "list", "data": data})
        return httpx.Response(401, json={"error": {"message": "bad key"}})

    from core.openai_api import is_openai_chat_model
    p = make_openai(handler, model_filter=is_openai_chat_model)
    assert p.list_models() == ["gpt-4o", "o4-mini"]
    with pytest.raises(ProviderError) as ei:
        list(p.stream("hi", model="gpt-4o"))
    assert ei.value.status == 401


# ─────────────────────────── DeepSeek web ─────────────────────────

DS_STREAM = [
    'event: ready', 'data: {"request_message_id":1,"response_message_id":2}',
    'event: update_session', 'data: {"updated_at":1}',
    'data: {"v":{"response":{"message_id":2,"fragments":[{"id":1,"type":"THINK","content":"Ngư"}]}}}',
    'data: {"p":"response/fragments/-1/content","o":"APPEND","v":"ời dùng"}', 'data: {"v":" chào"}',
    'data: {"p":"response/fragments","o":"APPEND","v":[{"id":2,"type":"RESPONSE","content":"Xin"}]}',
    'data: {"p":"response/fragments/-1/content","v":" chào"}', 'data: {"v":"!"}',
    'data: {"p":"response","o":"BATCH","v":[{"p":"accumulated_token_usage","v":9},{"p":"status","v":"FINISHED"}]}',
    'event: close', 'data: {}',
]


def test_deepseek_stream_parser():
    from core.deepseek_web import DeepSeekStreamParser
    p = DeepSeekStreamParser()
    deltas = [d for line in DS_STREAM if (d := p.feed_line(line))]
    assert deltas == ["Xin", " chào", "!"]
    assert (p.thinking, p.response, p.message_id) == ("Người dùng chào", "Xin chào!", 2)


def test_deepseek_helpers():
    from core.deepseek_web import parse_model, parse_user_token, unwrap_biz_data
    assert parse_user_token('{"value":"tok","__version":"0"}') == "tok"
    assert parse_user_token("Bearer tok2") == "tok2"
    assert parse_model("expert+think+search") == ("expert", True, True)
    assert parse_model(None) == ("default", False, False)
    with pytest.raises(ProviderError):
        unwrap_biz_data({"code": 0, "data": {"biz_code": 3, "biz_msg": "bad"}})


class FakeResp:
    def __init__(self, status=200, data=None, lines=None, content_type="application/json"):
        self.status_code = status
        self._data, self._lines = data, lines or []
        self.headers = {"content-type": content_type}

    def json(self):
        return self._data

    def iter_lines(self):
        for line in self._lines:
            yield line.encode()

    def iter_content(self):
        yield json.dumps(self._data).encode()

    def close(self):
        pass


class FakeSession:
    def __init__(self, completion):
        self.calls = []
        self.completion = completion

    def post(self, url, json=None, headers=None, stream=False):
        self.calls.append((url.rsplit("/api/v0/", 1)[1], json, headers))
        if url.endswith("chat_session/create"):
            return FakeResp(data={"code": 0, "data": {"biz_code": 0, "biz_data": {"chat_session": {"id": "s1"}}}})
        if url.endswith("create_pow_challenge"):
            return FakeResp(data={"code": 0, "data": {"biz_data": {"challenge": {"c": 1}}}})
        return self.completion


class FakePow:
    def make_header(self, challenge):
        return "pow-ok"


def make_deepseek(completion):
    from core.deepseek_web import DeepSeekWebProvider
    p = DeepSeekWebProvider('{"value":"tok"}', pow_solver=FakePow())
    session = FakeSession(completion)
    p._local.session = session
    return p, session


def test_deepseek_web_new_thread_and_continue():
    p, session = make_deepseek(FakeResp(lines=DS_STREAM, content_type="text/event-stream"))
    events = list(p.stream("hi", model="expert+think"))
    assert [e.text for e in events if e.type == "delta"] == ["Xin", " chào", "!"]
    done = events[-1]
    assert (done.text, done.conversation_id, done.message_id) == ("Xin chào!", "s1", "2")
    path, body, headers = session.calls[-1]
    assert path == "chat/completion" and headers["x-ds-pow-response"] == "pow-ok"
    assert headers["authorization"] == "Bearer tok"
    assert (body["model_type"], body["thinking_enabled"], body["search_enabled"]) == ("expert", True, False)
    assert body["chat_session_id"] == "s1" and body["parent_message_id"] is None

    session.calls.clear()
    list(p.stream("again", conversation_id="s1", parent_message_id="2"))
    assert [c[0] for c in session.calls] == ["chat/create_pow_challenge", "chat/completion"]
    assert session.calls[-1][1]["parent_message_id"] == 2


def test_deepseek_web_app_error_on_continue_is_400():
    p, _ = make_deepseek(FakeResp(data={"code": 0, "data": {"biz_code": 7, "biz_msg": "session not found"}}))
    with pytest.raises(ProviderError) as ei:
        list(p.stream("x", conversation_id="gone", parent_message_id="5"))
    assert ei.value.status == 400


# ─────────────────────────── Gemini ───────────────────────────────

def test_gemini_api_stream_text_and_image(tmp_path):
    from google.genai import types
    from core.gemini import GeminiAPIProvider

    p = GeminiAPIProvider("key", image_dir=str(tmp_path))
    seen = {}

    def fake_stream(model, contents, config):
        seen.update(model=model, contents=contents, config=config)
        part = lambda **kw: types.GenerateContentResponse(candidates=[types.Candidate(
            content=types.Content(role="model", parts=[types.Part(**kw)]))])
        yield part(text="nghĩ", thought=True)
        yield part(text="Con mèo")
        yield part(inline_data=types.Blob(data=b"\x89PNG", mime_type="image/png"))

    p._client.models.generate_content_stream = fake_stream
    history = [{"role": "system", "content": "Vẽ đẹp"}, {"role": "user", "content": "chào"},
               {"role": "assistant", "content": "chào bạn"}]
    events = list(p.stream("vẽ mèo", model="gemini-image-test", history=history))
    done = events[-1]
    assert done.text == "Con mèo" and len(done.images) == 1
    assert open(done.images[0], "rb").read() == b"\x89PNG"
    assert seen["config"].system_instruction == "Vẽ đẹp"
    assert seen["config"].response_modalities == ["TEXT", "IMAGE"]
    assert [c.role for c in seen["contents"]] == ["user", "model", "user"]


def test_gemini_web_stream_and_resume(tmp_path):
    from core.gemini import GeminiWebProvider

    class Out:
        def __init__(self, delta, text):
            self.text_delta, self.text, self.images = delta, text, []

    class FakeChat:
        def __init__(self, model=None, metadata=None):
            self.model = model
            self.metadata = metadata or ["c1", "r1", "rc1"]
            self.cid = self.metadata[0]

        async def send_message_stream(self, prompt, temporary=False):
            yield Out("Xin ", "Xin ")
            yield Out("chào", "Xin chào")

    chats = []

    class FakeClient:
        def start_chat(self, **kw):
            chats.append(kw)
            return FakeChat(**kw)

    p = GeminiWebProvider.__new__(GeminiWebProvider)
    p._client, p._loop, p._ready, p._image_dir = FakeClient(), BackgroundLoop(), True, str(tmp_path)
    p._generated_image_cls = type("GeneratedImage", (), {})
    events = list(p.stream("hi"))
    assert [e.text for e in events if e.type == "delta"] == ["Xin ", "chào"]
    done = events[-1]
    assert done.conversation_id == "c1" and json.loads(done.message_id) == ["c1", "r1", "rc1"]
    list(p.stream("again", model="gemini-pro", conversation_id="c1", parent_message_id=done.message_id))
    assert chats[-1] == {"model": "gemini-pro", "metadata": ["c1", "r1", "rc1"]}
