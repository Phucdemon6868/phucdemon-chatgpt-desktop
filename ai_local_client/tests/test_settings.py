import os

from core.base import Provider, StreamEvent
from core.config import Settings, load_settings, save_env
from core.registry import Registry
from core.store import Store
from ui.app import build_ui, secret_placeholder


def test_save_env_updates_in_place_and_keeps_comments(tmp_path, monkeypatch):
    env = tmp_path / ".env"
    env.write_text("# chú thích\nCHATGPT_COOKIE=old\n# GEMINI_API_KEY=commented\nCHATGPT_TIMEOUT=180\n")
    monkeypatch.setattr(os, "environ", {})   # cô lập: save_env/load_settings không đụng môi trường thật
    save_env({"CHATGPT_COOKIE": "a=b; c=d", "GEMINI_API_KEY": "g-key",
              "DEEPSEEK_USER_TOKEN": '{"value":"tok"}\n'}, env)
    lines = env.read_text().splitlines()
    assert lines[:4] == ["# chú thích", "CHATGPT_COOKIE=a=b; c=d", "# GEMINI_API_KEY=commented", "CHATGPT_TIMEOUT=180"]
    assert lines[4:] == ["GEMINI_API_KEY=g-key", 'DEEPSEEK_USER_TOKEN={"value":"tok"}']
    assert oct(env.stat().st_mode & 0o777) == "0o600"
    s = load_settings(env)
    assert (s.cookie, s.gemini_api_key, s.deepseek_user_token) == ("a=b; c=d", "g-key", '{"value":"tok"}')
    assert os.environ["GEMINI_API_KEY"] == "g-key"


class Closable(Provider):
    name = "chatgpt"
    closed = False

    def list_models(self):
        return ["auto"]

    def stream(self, prompt, **kw):
        yield StreamEvent("done", "x")

    def close(self):
        self.closed = True


def test_registry_reconfigure_closes_old_providers():
    reg = Registry(Settings(cookie="c"))
    old = reg._instances["chatgpt"] = Closable()
    reg.reconfigure(Settings(deepseek_api_key="k"))
    assert old.closed and reg.names == ["deepseek"]


def test_secret_placeholder_masks_value():
    s = Settings(openai_api_key="sk-abcdefghijkl1234")
    assert "1234" in secret_placeholder(s, "OPENAI_API_KEY")
    assert "abcdefgh" not in secret_placeholder(s, "OPENAI_API_KEY")
    assert secret_placeholder(s, "GEMINI_API_KEY") == "Chưa cấu hình"


def get_fns(demo, name):
    return [fn.fn for fn in demo.fns.values() if getattr(fn.fn, "__name__", "") == name]


def test_settings_tab_save_and_clear(tmp_path, monkeypatch):
    monkeypatch.setattr(os, "environ", {})
    env = tmp_path / ".env"
    settings = Settings(cookie="old-cookie")
    registry = Registry(settings)
    registry.list_models = lambda timeout=20: []   # không gọi mạng trong test
    demo = build_ui(settings, Store(tmp_path / "t.db"), registry, env_file=env)
    (save,) = get_fns(demo, "save")

    # Thứ tự: 7 ô bí mật nhà cung cấp + PROXY_API_KEY, rồi cài đặt chung
    secrets = ["", "", "", "", "ds-key", "", "", ""]   # chỉ nhập DeepSeek API key, còn lại để trống
    general = ["deepseek/deepseek-flash", "", 120, 2, False, "data/img"]
    out = save(*secrets, *general)
    assert out[-1].startswith("✅")
    text = env.read_text()
    assert "CHATGPT_COOKIE=old-cookie" in text          # ô trống = giữ nguyên
    assert "DEEPSEEK_API_KEY=ds-key" in text
    assert "CHATGPT_TIMEOUT=120" in text and "CHATGPT_TEMPORARY_CHAT=0" in text
    assert registry.names == ["chatgpt", "deepseek"]
    assert registry.default_model == "deepseek/deepseek-flash"

    # Nút Xóa của DeepSeek API (thứ tự nhà cung cấp: openai, chatgpt, gemini, gemini-web, deepseek, deepseek-web)
    clear = get_fns(demo, "clear")[4]
    clear()
    assert "DEEPSEEK_API_KEY=\n" in env.read_text() and registry.names == ["chatgpt"]


def test_settings_tab_check_uses_form_values(tmp_path):
    registry = Registry(Settings())
    registry.list_models = lambda timeout=20: []
    demo = build_ui(Settings(), Store(tmp_path / "t.db"), registry, env_file=tmp_path / ".env")
    test_openai = get_fns(demo, "test")[0]
    assert test_openai("").startswith("❌") and "chưa được cấu hình" in test_openai("")
    assert not (tmp_path / ".env").exists()   # kiểm tra không ghi file
