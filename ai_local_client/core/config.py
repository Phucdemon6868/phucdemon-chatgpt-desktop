"""Đọc cấu hình từ biến môi trường / file .env (không cần python-dotenv)."""

from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/142.0.0.0 Safari/537.36"
)
DEFAULT_MODELS = ["auto", "gpt-4o", "gpt-4o-mini", "o3-mini", "o4-mini"]
# Danh sách dự phòng khi không lấy được model từ API (ghi đè bằng <TÊN>_MODELS trong .env)
DEFAULT_PROVIDER_MODELS = {
    "openai": [],
    "gemini": [],
    "gemini-web": ["default"],
    "deepseek": ["deepseek-flash"],
    "deepseek-web": ["default", "default+think", "expert", "expert+think"],
}


def load_dotenv(path: str | Path = ".env") -> None:
    """Nạp KEY=VALUE từ file .env vào os.environ (không ghi đè biến đã có)."""
    p = Path(path)
    if not p.is_file():
        return
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        os.environ.setdefault(key, value)


def _split(value: str) -> list[str]:
    return [v.strip() for v in value.split(",") if v.strip()]


@dataclass
class Settings:
    cookie: str = ""                 # ChatGPT web (cookie chatgpt.com)
    default_model: str = "auto"      # "auto" (ChatGPT) hoặc "<provider>/<model>", ví dụ "gemini/gemini-2.5-flash"
    models: list[str] = field(default_factory=lambda: list(DEFAULT_MODELS))
    # Các nhà cung cấp khác: để trống = không dùng
    openai_api_key: str = ""
    gemini_api_key: str = ""
    gemini_cookie: str = ""          # cookie gemini.google.com (cần __Secure-1PSID, nên có __Secure-1PSIDTS)
    deepseek_api_key: str = ""
    deepseek_user_token: str = ""    # localStorage "userToken" của chat.deepseek.com
    deepseek_cookie: str = ""        # tùy chọn, khi bị WAF chặn
    web_proxy: str = ""              # proxy cho gemini-web / deepseek-web, ví dụ http://user:pass@host:port
    provider_models: dict[str, list[str]] = field(
        default_factory=lambda: {k: list(v) for k, v in DEFAULT_PROVIDER_MODELS.items()})
    image_dir: str = "data/images"
    user_agent: str = DEFAULT_USER_AGENT
    proxy_api_key: str = ""          # khóa bảo vệ server proxy (để trống = không kiểm tra)
    db_path: str = "data/chats.db"
    temporary_chat: bool = True      # proxy dùng chat tạm, không làm rác lịch sử ChatGPT
    max_retries: int = 3
    request_timeout: int = 180


def load_settings(env_file: str | Path = ".env") -> Settings:
    load_dotenv(env_file)
    env = os.environ
    models = _split(env.get("CHATGPT_MODELS", ""))
    provider_models = {
        name: _split(env.get(f"{name.upper().replace('-', '_')}_MODELS", "")) or list(defaults)
        for name, defaults in DEFAULT_PROVIDER_MODELS.items()
    }
    default_model = env.get("DEFAULT_MODEL", "").strip() or env.get("CHATGPT_DEFAULT_MODEL", "").strip()
    return Settings(
        cookie=env.get("CHATGPT_COOKIE", "").strip(),
        default_model=default_model or "auto",
        models=models or list(DEFAULT_MODELS),
        openai_api_key=env.get("OPENAI_API_KEY", "").strip(),
        gemini_api_key=env.get("GEMINI_API_KEY", "").strip(),
        gemini_cookie=env.get("GEMINI_COOKIE", "").strip(),
        deepseek_api_key=env.get("DEEPSEEK_API_KEY", "").strip(),
        deepseek_user_token=env.get("DEEPSEEK_USER_TOKEN", "").strip(),
        deepseek_cookie=env.get("DEEPSEEK_COOKIE", "").strip(),
        web_proxy=env.get("WEB_PROXY", "").strip(),
        provider_models=provider_models,
        image_dir=env.get("IMAGE_DIR", "data/images"),
        user_agent=env.get("CHATGPT_USER_AGENT", DEFAULT_USER_AGENT),
        proxy_api_key=env.get("PROXY_API_KEY", "").strip(),
        db_path=env.get("CHATGPT_DB_PATH", "data/chats.db"),
        temporary_chat=env.get("CHATGPT_TEMPORARY_CHAT", "1").lower() not in ("0", "false", "no"),
        max_retries=int(env.get("CHATGPT_MAX_RETRIES", "3")),
        request_timeout=int(env.get("CHATGPT_TIMEOUT", "180")),
    )


# ─────────────────────────── Lưu cấu hình (dùng cho tab Cài đặt) ───────────

# Biến .env ↔ trường của Settings
ENV_FIELDS = {
    "CHATGPT_COOKIE": "cookie",
    "OPENAI_API_KEY": "openai_api_key",
    "GEMINI_API_KEY": "gemini_api_key",
    "GEMINI_COOKIE": "gemini_cookie",
    "DEEPSEEK_API_KEY": "deepseek_api_key",
    "DEEPSEEK_USER_TOKEN": "deepseek_user_token",
    "DEEPSEEK_COOKIE": "deepseek_cookie",
    "WEB_PROXY": "web_proxy",
    "DEFAULT_MODEL": "default_model",
    "PROXY_API_KEY": "proxy_api_key",
    "CHATGPT_TEMPORARY_CHAT": "temporary_chat",
    "IMAGE_DIR": "image_dir",
    "CHATGPT_MAX_RETRIES": "max_retries",
    "CHATGPT_TIMEOUT": "request_timeout",
}
# Không bao giờ hiển thị lại nguyên văn trên giao diện
SECRET_KEYS = {"CHATGPT_COOKIE", "OPENAI_API_KEY", "GEMINI_API_KEY", "GEMINI_COOKIE", "DEEPSEEK_API_KEY",
               "DEEPSEEK_USER_TOKEN", "DEEPSEEK_COOKIE", "PROXY_API_KEY"}


def save_env(updates: dict[str, str], path: str | Path = ".env") -> None:
    """
    Ghi KEY=VALUE vào file .env: sửa dòng đã có, thêm dòng mới ở cuối, giữ nguyên chú thích.
    Đồng thời cập nhật os.environ để load_settings() đọc được giá trị mới ngay.
    """
    p = Path(path)
    lines = p.read_text(encoding="utf-8").splitlines() if p.is_file() else []
    clean = {k: str(v).replace("\r", " ").replace("\n", " ").strip() for k, v in updates.items()}
    remaining = dict(clean)
    for i, line in enumerate(lines):
        key = line.partition("=")[0].strip()
        if "=" in line and not line.lstrip().startswith("#") and key in remaining:
            lines[i] = f"{key}={remaining.pop(key)}"
    lines += [f"{k}={v}" for k, v in remaining.items()]
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n".join(lines) + "\n", encoding="utf-8")
    try:
        p.chmod(0o600)   # file chứa cookie/khóa: chỉ chủ sở hữu được đọc
    except OSError:
        pass
    os.environ.update(clean)
