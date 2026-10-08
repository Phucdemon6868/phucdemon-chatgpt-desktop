"""
DeepSeek web (chat.deepseek.com) qua userToken, theo giao thức web 09/2026.

Mỗi tin nhắn cần một lời giải proof-of-work (thuật toán DeepSeekHashV1). Lời giải được
tính bằng chính tệp WebAssembly của DeepSeek (assets/sha3_wasm_bg.wasm) chạy trong
wasmtime: module không có import nào nên không truy cập được tệp hay mạng.

Model: "default" (Nhanh) hoặc "expert" (Chuyên gia), thêm hậu tố "+think" để bật
DeepThink và "+search" để bật tìm kiếm web, ví dụ "expert+think+search".
Thread: conversation_id = chat_session_id, message_id = id tin nhắn trả lời cuối.
"""

from __future__ import annotations

import base64
import hashlib
import json
import logging
import struct
import threading
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Iterator

from .base import Provider, ProviderError, StreamEvent

log = logging.getLogger(__name__)

BASE_URL = "https://chat.deepseek.com"
CLIENT_VERSION = "2.5.0"
COMPLETION_PATH = "/api/v0/chat/completion"
POW_WASM_PATH = Path(__file__).resolve().parent / "assets" / "sha3_wasm_bg.wasm"
POW_WASM_SHA256 = "b3fca8cc072c1defbd60c02266a8e48bd307a1804aaff4314900aea720e72f7d"


def parse_user_token(raw: str) -> str:
    """Nhận token thô, "Bearer ..." hoặc giá trị localStorage {"value": "...", "__version": "0"}."""
    raw = raw.strip()
    if raw.startswith("{"):
        try:
            raw = json.loads(raw).get("value", "")
        except ValueError as e:
            raise ProviderError("DEEPSEEK_USER_TOKEN không phải JSON hợp lệ.", 401) from e
    raw = raw.removeprefix("Bearer ").strip().strip('"')
    if not raw:
        raise ProviderError("DEEPSEEK_USER_TOKEN trống.", 401)
    return raw


def parse_model(model: str | None) -> tuple[str, bool, bool]:
    """'expert+think+search' → (model_type, thinking_enabled, search_enabled)."""
    base, *flags = (model or "default").split("+")
    return (base or "default"), "think" in flags, "search" in flags


def unwrap_biz_data(data: Any, status_on_error: int = 502) -> dict:
    if not isinstance(data, dict):
        raise ProviderError(f"deepseek-web: phản hồi không hợp lệ: {str(data)[:200]}", 502)
    if data.get("code") not in (None, 0):
        raise ProviderError(f"deepseek-web lỗi {data.get('code')}: {data.get('msg') or data}", status_on_error)
    inner = data.get("data")
    if isinstance(inner, dict):
        if inner.get("biz_code") not in (None, 0):
            raise ProviderError(f"deepseek-web lỗi {inner.get('biz_code')}: {inner.get('biz_msg')}", status_on_error)
        return inner["biz_data"] if isinstance(inner.get("biz_data"), dict) else inner
    return data


class DeepSeekPow:
    """Giải thử thách PoW bằng tệp WebAssembly của DeepSeek. Dùng chung giữa các luồng nên có khóa."""

    def __init__(self, wasm_path: Path = POW_WASM_PATH, expected_sha256: str = POW_WASM_SHA256):
        try:
            import wasmtime
        except ImportError as e:
            raise ProviderError("Thiếu thư viện `wasmtime`. Chạy: pip install wasmtime") from e
        wasm_bytes = wasm_path.read_bytes()
        if hashlib.sha256(wasm_bytes).hexdigest() != expected_sha256:
            log.warning("%s khác bản đã kiểm tra (có thể DeepSeek đã cập nhật).", wasm_path.name)
        self._store = wasmtime.Store()
        exports = wasmtime.Instance(self._store, wasmtime.Module(self._store.engine, wasm_bytes), []).exports(self._store)
        self._memory = exports["memory"]
        self._solve = exports["wasm_solve"]
        self._malloc = exports["__wbindgen_export_0"]
        self._add_to_stack = exports["__wbindgen_add_to_stack_pointer"]
        self._lock = threading.Lock()

    def _write_str(self, text: str) -> tuple[int, int]:
        data = text.encode("utf-8")
        ptr = self._malloc(self._store, len(data), 1)
        self._memory.write(self._store, data, ptr)
        return ptr, len(data)

    def solve(self, challenge: str, prefix: str, difficulty: float) -> int | None:
        with self._lock:
            retptr = self._add_to_stack(self._store, -16)
            try:
                c_ptr, c_len = self._write_str(challenge)
                p_ptr, p_len = self._write_str(prefix)
                self._solve(self._store, retptr, c_ptr, c_len, p_ptr, p_len, float(difficulty))
                status = struct.unpack("<i", self._memory.read(self._store, retptr, retptr + 4))[0]
                value = struct.unpack("<d", self._memory.read(self._store, retptr + 8, retptr + 16))[0]
            finally:
                self._add_to_stack(self._store, 16)
        return int(value) if status else None

    def make_header(self, challenge: dict) -> str:
        """Tạo giá trị header x-ds-pow-response từ biz_data.challenge."""
        answer = self.solve(challenge["challenge"], f"{challenge['salt']}_{challenge['expire_at']}_",
                            challenge["difficulty"])
        if answer is None:
            raise ProviderError("deepseek-web: không giải được thử thách PoW (có thể đã hết hạn).", 502)
        payload = {key: challenge[key] for key in ("algorithm", "challenge", "salt", "signature", "target_path")}
        payload["answer"] = answer
        return base64.b64encode(json.dumps(payload, separators=(",", ":")).encode()).decode()


class DeepSeekStreamParser:
    """
    Đọc luồng SSE. Phản hồi là đối tượng `response` chứa các `fragments`
    (THINK = suy nghĩ, RESPONSE = trả lời, SEARCH, TIP), cập nhật bằng các bản vá:
        {"v":{"response":{..., "fragments":[{"type":"THINK","content":"..."}]}}}
        {"p":"response/fragments/-1/content","o":"APPEND","v":"..."}
        {"v":"..."}                                      <- nối tiếp fragment hiện tại
        {"p":"response/fragments","o":"APPEND","v":[{"type":"RESPONSE","content":"..."}]}
        {"p":"response","o":"BATCH","v":[...]}
    """

    def __init__(self) -> None:
        self.thinking = ""
        self.response = ""
        self.message_id: int | None = None
        self._event: str | None = None
        self._fragments: list[dict] = []
        self._target: dict | None = None
        self._new = ""

    def feed_line(self, line: str) -> str:
        """Nhận một dòng SSE, trả về phần trả lời (RESPONSE) mới."""
        self._new = ""
        line = line.strip()
        if line.startswith("event:"):
            self._event = line[6:].strip()
            return ""
        if not line.startswith("data:"):
            return ""
        raw = line[5:].strip()
        if not raw or raw == "[DONE]":
            return ""
        try:
            data = json.loads(raw)
        except ValueError:
            return ""
        if self._event == "ready" and isinstance(data, dict):
            if data.get("response_message_id") is not None:
                self.message_id = data["response_message_id"]
        elif self._event in (None, "message", "update_session"):
            self._dispatch(data)
        return self._new

    def _append(self, text: Any) -> None:
        if not isinstance(text, str) or self._target is None:
            return
        self._target["content"] += text
        if self._target["type"] == "THINK":
            self.thinking += text
        elif self._target["type"] == "RESPONSE":
            self.response += text
            self._new += text

    def _start_fragment(self, frag: dict) -> None:
        fragment = {"type": str(frag.get("type") or "RESPONSE").upper(), "content": ""}
        self._fragments.append(fragment)
        self._target = fragment
        self._append(frag.get("content") or "")

    def _dispatch(self, data: Any) -> None:
        if not isinstance(data, dict):
            return
        path, op, value = data.get("p"), data.get("o"), data.get("v")
        if not path:
            if isinstance(value, dict) and isinstance(value.get("response"), dict):
                resp = value["response"]
                if resp.get("message_id") is not None:
                    self.message_id = resp["message_id"]
                for frag in resp.get("fragments") or []:
                    if isinstance(frag, dict):
                        self._start_fragment(frag)
            else:
                self._append(value)
            return

        parts = str(path).strip("/").split("/")
        if parts[0] != "response":
            return
        if len(parts) == 1:
            if op == "BATCH" and isinstance(value, list):
                for sub in value:
                    self._dispatch(sub)
            return
        if parts[1] == "message_id" and isinstance(value, int):
            self.message_id = value
        elif parts[1] == "fragments":
            if len(parts) == 2:
                for frag in value if isinstance(value, list) else [value]:
                    if isinstance(frag, dict):
                        self._start_fragment(frag)
                return
            try:
                fragment = self._fragments[int(parts[2])]
            except (ValueError, IndexError):
                fragment = self._target
            if fragment is None:
                return
            self._target = fragment
            if (parts[3] if len(parts) > 3 else "content") == "content":
                if op == "SET":
                    fragment["content"] = ""
                self._append(value)


class DeepSeekWebProvider(Provider):
    name = "deepseek-web"
    stateful = True

    def __init__(self, user_token: str, *, cookie: str = "", proxy: str | None = None,
                 timeout: float = 300, fallback_models: list[str] | None = None, pow_solver=None):
        try:
            from curl_cffi import requests as curl_requests
        except ImportError as e:
            raise ProviderError("Thiếu thư viện `curl_cffi`. Chạy: pip install curl_cffi") from e
        self._curl = curl_requests
        self._token = parse_user_token(user_token)
        self._cookies = {k.strip(): v.strip() for k, _, v in
                         (p.partition("=") for p in cookie.split(";") if "=" in p)}
        self._proxy = proxy or None
        self._timeout = timeout
        self._models = list(fallback_models or ["default", "default+think", "expert", "expert+think"])
        self._pow = pow_solver
        self._pow_lock = threading.Lock()
        self._local = threading.local()   # Session không thread-safe

    @property
    def session(self):
        s = getattr(self._local, "session", None)
        if s is None:
            # impersonate: giả lập TLS/HTTP2 của Chrome để không bị chặn
            s = self._curl.Session(impersonate="chrome", cookies=self._cookies, timeout=self._timeout,
                                   proxies={"https": self._proxy, "http": self._proxy} if self._proxy else None)
            self._local.session = s
        return s

    def _headers(self, chat_session_id: str | None = None, extra: dict | None = None) -> dict:
        offset = datetime.now().astimezone().utcoffset() or timedelta(0)
        headers = {
            "accept": "*/*",
            "authorization": f"Bearer {self._token}",
            "origin": BASE_URL,
            "referer": f"{BASE_URL}/a/chat/s/{chat_session_id}" if chat_session_id else f"{BASE_URL}/",
            "x-app-version": CLIENT_VERSION,
            "x-client-version": CLIENT_VERSION,
            "x-client-platform": "web",
            "x-client-locale": "en_US",
            "x-client-bundle-id": "com.deepseek.chat",
            "x-client-timezone-offset": str(int(offset.total_seconds())),
        }
        headers.update(extra or {})
        return headers

    @staticmethod
    def _check_status(resp) -> None:
        if resp.status_code in (401, 403):
            raise ProviderError(f"deepseek-web HTTP {resp.status_code}: userToken hết hạn hoặc bị chặn.",
                                resp.status_code)
        if resp.status_code == 429:
            raise ProviderError("deepseek-web HTTP 429: gửi quá nhanh, hãy đợi một lúc.", 429)
        if resp.status_code != 200:
            raise ProviderError(f"deepseek-web HTTP {resp.status_code}", resp.status_code)

    def _post(self, path: str, body: dict, chat_session_id: str | None = None) -> dict:
        try:
            resp = self.session.post(BASE_URL + path, json=body, headers=self._headers(chat_session_id))
        except Exception as e:   # noqa: BLE001 - lỗi mạng của curl_cffi
            raise ProviderError(f"deepseek-web: lỗi mạng: {e}", 502) from e
        self._check_status(resp)
        return unwrap_biz_data(resp.json())

    def _pow_header(self, chat_session_id: str | None) -> str:
        challenge = self._post("/api/v0/chat/create_pow_challenge", {"target_path": COMPLETION_PATH},
                               chat_session_id).get("challenge")
        if not challenge:
            raise ProviderError("deepseek-web: không nhận được thử thách PoW.", 502)
        with self._pow_lock:
            if self._pow is None:
                self._pow = DeepSeekPow()
        return self._pow.make_header(challenge)

    def check(self) -> str:
        try:
            resp = self.session.get(BASE_URL + "/api/v0/users/current", headers=self._headers())
        except Exception as e:   # noqa: BLE001
            raise ProviderError(f"deepseek-web: lỗi mạng: {e}", 502) from e
        self._check_status(resp)
        user = unwrap_biz_data(resp.json(), status_on_error=401)
        return f"Đăng nhập thành công: {user.get('email') or user.get('mobile_number') or user.get('id') or 'OK'}"

    def list_models(self) -> list[str]:
        return list(self._models)

    def stream(self, prompt, *, model=None, conversation_id=None, parent_message_id=None,
               temporary=False, history=None) -> Iterator[StreamEvent]:
        model_type, thinking, search = parse_model(model)
        continuing = bool(conversation_id)
        if not conversation_id:
            biz = self._post("/api/v0/chat_session/create", {})
            conversation_id = (biz.get("chat_session") or biz).get("id")
            if not conversation_id:
                raise ProviderError(f"deepseek-web: không tạo được phiên chat: {biz}", 502)
            parent_message_id = None

        body = {
            "chat_session_id": conversation_id,
            "parent_message_id": int(parent_message_id) if parent_message_id else None,
            "model_type": model_type,
            "prompt": prompt,
            "ref_file_ids": [],
            "thinking_enabled": thinking,
            "search_enabled": search,
            "action": None,
            "preempt": False,
        }
        headers = self._headers(conversation_id, {"x-ds-pow-response": self._pow_header(conversation_id)})
        try:
            resp = self.session.post(BASE_URL + COMPLETION_PATH, json=body, headers=headers, stream=True)
        except Exception as e:   # noqa: BLE001
            raise ProviderError(f"deepseek-web: lỗi mạng: {e}", 502) from e

        parser = DeepSeekStreamParser()
        try:
            self._check_status(resp)
            if "text/event-stream" not in resp.headers.get("content-type", ""):
                # Lỗi ứng dụng trả về dạng JSON với HTTP 200; 400 để proxy thử mở thread mới
                raw = b"".join(resp.iter_content()).decode("utf-8", "replace")
                unwrap_biz_data(json.loads(raw or "{}"),
                                status_on_error=400 if continuing else 502)
                raise ProviderError("deepseek-web: phản hồi không phải luồng SSE.", 502)
            for line in resp.iter_lines():
                new = parser.feed_line(line.decode("utf-8", "replace") if isinstance(line, bytes) else line)
                if new:
                    yield StreamEvent("delta", new)
        except ProviderError:
            raise
        except Exception as e:   # noqa: BLE001
            raise ProviderError(f"deepseek-web: mất kết nối khi đang stream: {e}", 502) from e
        finally:
            resp.close()

        if not parser.response and not parser.thinking:
            raise ProviderError("deepseek-web: không nhận được phản hồi.", 502)
        yield StreamEvent("done", parser.response, conversation_id=conversation_id,
                          message_id=str(parser.message_id) if parser.message_id is not None else parent_message_id,
                          model=model or "default")
