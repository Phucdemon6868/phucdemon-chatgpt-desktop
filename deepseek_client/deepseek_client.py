import asyncio
import base64
import hashlib
import json
import mimetypes
import pathlib
import struct
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

# Chế độ chính thức: API của DeepSeek tương thích OpenAI, dùng SDK `openai`
try:
    from openai import AsyncOpenAI
    openai_installed = True
except ImportError:
    openai_installed = False

# Chế độ không chính thức: giả lập trình duyệt (curl_cffi) + giải thử thách PoW (wasmtime)
try:
    from curl_cffi import CurlMime
    from curl_cffi.requests import AsyncSession
    import wasmtime
    web_libs_installed = True
except ImportError:
    web_libs_installed = False


class DeepSeekClient:
    """
    Client bất đồng bộ để tương tác với DeepSeek, hỗ trợ cả hai chế độ.
    - Chế độ chính thức (API Key): ổn định, trả phí theo token, hỗ trợ ảnh (deepseek-flash) và tệp văn bản.
    - Chế độ không chính thức (Token web): dùng tài khoản chat.deepseek.com miễn phí, có DeepThink và tìm kiếm web.

    DeepSeek không có tính năng tạo ảnh ở cả hai chế độ.
    """

    # --- Chế độ chính thức ---
    _OFFICIAL_BASE_URL = "https://api.deepseek.com"
    _OFFICIAL_IMAGE_TYPES = {"image/jpeg", "image/png", "image/gif", "image/webp"}
    _MAX_TEXT_FILE_CHARS = 200_000

    # --- Chế độ không chính thức (theo giao thức web chat.deepseek.com, 09/2026) ---
    _WEB_BASE_URL = "https://chat.deepseek.com"
    _WEB_CLIENT_VERSION = "2.5.0"
    _WEB_MODEL_TYPES = {"1": ("default", "Nhanh (Instant)"), "2": ("expert", "Chuyên gia (Expert)")}
    # Tệp WebAssembly giải PoW của chính DeepSeek (sha3_wasm_bg.wasm), ghim mã băm để phát hiện tệp lạ
    _POW_WASM_PATH = pathlib.Path(__file__).resolve().parent / "sha3_wasm_bg.wasm"
    _POW_WASM_SHA256 = "b3fca8cc072c1defbd60c02266a8e48bd307a1804aaff4314900aea720e72f7d"

    def __init__(self, api_key: Optional[str] = None, user_token: Optional[str] = None,
                 cookie_string: Optional[str] = None, proxy: Optional[str] = None):
        if api_key:
            if not openai_installed:
                raise ImportError("Thư viện `openai` chưa được cài đặt. Vui lòng chạy `pip install openai`.")
            self._mode = 'official'
            self._api_key = api_key
            self._history: List[Dict[str, Any]] = []
        elif user_token:
            if not web_libs_installed:
                raise ImportError("Thiếu thư viện. Vui lòng chạy `pip install curl_cffi wasmtime`.")
            self._mode = 'unofficial'
            self._token = self._parse_user_token(user_token)
            self._cookies = self._parse_cookie_string(cookie_string or "")
            self._proxy = self._format_proxy(proxy)
            self._chat_session_id: Optional[str] = None
            self._parent_message_id: Optional[int] = None
            self._pow = None
        else:
            raise ValueError("Phải cung cấp `api_key` (chính thức) hoặc `user_token` (không chính thức).")

        self._client: Any = None
        self._models: List[Dict[str, str]] = []
        self.thinking = True   # DeepThink / chế độ suy nghĩ
        self.search = False    # Tìm kiếm web (chỉ chế độ không chính thức)

    @property
    def mode(self) -> str:
        return self._mode

    @property
    def models(self) -> List[Dict[str, str]]:
        """Danh sách mô hình: [{"id": ..., "name": ...}, ...]. Chỉ có sau khi `connect()`."""
        return self._models

    async def connect(self):
        if self._mode == 'official':
            self._client = AsyncOpenAI(api_key=self._api_key, base_url=self._OFFICIAL_BASE_URL)
            page = await self._client.models.list()
            self._models = sorted(({"id": m.id, "name": m.id} for m in page.data), key=lambda m: m["id"])
        else:
            self._pow = _DeepSeekPow(self._POW_WASM_PATH, self._POW_WASM_SHA256)
            self._client = AsyncSession(impersonate="chrome", proxy=self._proxy, cookies=self._cookies, timeout=300)
            print("Đang xác thực bằng token (unofficial)...")
            profile = await self._web_request("GET", "/api/v0/users/current")
            print(f"Xác thực thành công: {profile.get('email') or profile.get('mobile_number') or profile.get('id') or 'OK'}")
            self._models = [{"id": mt, "name": name} for mt, name in self._WEB_MODEL_TYPES.values()]

    async def close(self):
        if self._client is not None:
            await self._client.close()

    def reset_chat(self):
        """Bắt đầu cuộc trò chuyện mới (xóa ngữ cảnh)."""
        if self._mode == 'official':
            self._history = []
        else:
            self._chat_session_id = None
            self._parent_message_id = None

    async def ask(self, prompt: str, model: str, file_paths: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Gửi tin nhắn, giữ ngữ cảnh hội thoại giữa các lần gọi.
        Trả về {"success": bool, "mess": str, "thinking": str}.
        """
        if self._client is None:
            raise RuntimeError("Client chưa được kết nối. Hãy gọi `connect()` hoặc dùng `async with`.")
        for path in file_paths or []:
            if not pathlib.Path(path).is_file():
                return {"success": False, "mess": f"Lỗi: Không tìm thấy tệp tại '{path}'", "thinking": ""}
        try:
            if self._mode == 'official':
                return await self._ask_official(prompt, model, file_paths or [])
            return await self._ask_unofficial(prompt, model, file_paths or [])
        except Exception as e:
            return {"success": False, "mess": f"{type(e).__name__}: {e}", "thinking": ""}

    # --- Chế độ chính thức ---
    async def _ask_official(self, prompt: str, model: str, file_paths: List[str]) -> Dict[str, Any]:
        content: List[Dict[str, Any]] = []
        text_prefix = ""
        for path_str in file_paths:
            path = pathlib.Path(path_str)
            mime_type, _ = mimetypes.guess_type(path)
            if mime_type in self._OFFICIAL_IMAGE_TYPES:
                data_url = f"data:{mime_type};base64,{base64.b64encode(path.read_bytes()).decode()}"
                content.append({"type": "image_url", "image_url": {"url": data_url}})
                continue
            try:
                text = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                return {"success": False, "thinking": "",
                        "mess": f"Lỗi: '{path.name}' không phải ảnh (jpg/png/gif/webp) hay tệp văn bản UTF-8."}
            text_prefix += f"--- Tệp: {path.name} ---\n{text[:self._MAX_TEXT_FILE_CHARS]}\n--- Hết tệp ---\n\n"

        user_text = text_prefix + prompt
        if content:
            content.append({"type": "text", "text": user_text})
            user_message = {"role": "user", "content": content}
        else:
            user_message = {"role": "user", "content": user_text}

        kwargs: Dict[str, Any] = {}
        if not self.thinking:
            kwargs["reasoning_effort"] = "none"  # "none" = tắt chế độ suy nghĩ
        response = await self._client.chat.completions.create(
            model=model, messages=self._history + [user_message], **kwargs
        )
        message = response.choices[0].message
        answer = message.content or ""
        # Không cần gửi lại reasoning_content trong lịch sử khi không dùng tools
        self._history += [user_message, {"role": "assistant", "content": answer}]
        return {"success": True, "mess": answer, "thinking": getattr(message, "reasoning_content", None) or ""}

    # --- Chế độ không chính thức ---
    def _web_headers(self, extra: Optional[Dict[str, str]] = None) -> Dict[str, str]:
        offset = datetime.now().astimezone().utcoffset() or timedelta(0)
        referer = f"{self._WEB_BASE_URL}/a/chat/s/{self._chat_session_id}" if self._chat_session_id else f"{self._WEB_BASE_URL}/"
        headers = {
            "accept": "*/*",
            "authorization": f"Bearer {self._token}",
            "origin": self._WEB_BASE_URL,
            "referer": referer,
            "x-app-version": self._WEB_CLIENT_VERSION,
            "x-client-version": self._WEB_CLIENT_VERSION,
            "x-client-platform": "web",
            "x-client-locale": "en_US",
            "x-client-bundle-id": "com.deepseek.chat",
            "x-client-timezone-offset": str(int(offset.total_seconds())),
        }
        headers.update(extra or {})
        return headers

    async def _web_request(self, method: str, path: str, json_body: Any = None,
                           extra_headers: Optional[Dict[str, str]] = None, **kwargs) -> Dict[str, Any]:
        response = await self._client.request(
            method, self._WEB_BASE_URL + path, json=json_body, headers=self._web_headers(extra_headers), **kwargs
        )
        if response.status_code in (401, 403):
            raise PermissionError(f"HTTP {response.status_code}: token hết hạn hoặc bị chặn. Hãy lấy lại userToken.")
        if response.status_code == 429:
            raise RuntimeError("HTTP 429: gửi quá nhanh, hãy đợi một lúc rồi thử lại.")
        response.raise_for_status()
        return self._unwrap_biz_data(response.json())

    @staticmethod
    def _unwrap_biz_data(data: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(data, dict):
            raise RuntimeError(f"Phản hồi không hợp lệ: {str(data)[:200]}")
        if data.get("code") not in (None, 0):
            raise RuntimeError(f"DeepSeek báo lỗi {data.get('code')}: {data.get('msg') or data}")
        inner = data.get("data")
        if isinstance(inner, dict):
            if inner.get("biz_code") not in (None, 0):
                raise RuntimeError(f"DeepSeek báo lỗi {inner.get('biz_code')}: {inner.get('biz_msg')}")
            return inner.get("biz_data") if isinstance(inner.get("biz_data"), dict) else inner
        return data

    async def _get_pow_header(self, target_path: str) -> str:
        biz = await self._web_request("POST", "/api/v0/chat/create_pow_challenge", {"target_path": target_path})
        challenge = biz.get("challenge")
        if not challenge:
            raise RuntimeError(f"Không nhận được thử thách PoW: {biz}")
        # Giải PoW tốn CPU nên chạy ở luồng riêng để không chặn event loop
        return await asyncio.to_thread(self._pow.make_header, challenge)

    async def _upload_web_file(self, path: pathlib.Path) -> str:
        print(f"Đang tải tệp lên: {path.name}")
        target = "/api/v0/file/upload_file"
        mime = CurlMime()
        mime.addpart("file", filename=path.name, local_path=str(path),
                     content_type=mimetypes.guess_type(path)[0] or "application/octet-stream")
        headers = self._web_headers({"x-ds-pow-response": await self._get_pow_header(target)})
        try:
            response = await self._client.post(self._WEB_BASE_URL + target, multipart=mime, headers=headers)
        finally:
            mime.close()
        response.raise_for_status()
        biz = self._unwrap_biz_data(response.json())
        file_id = biz.get("id") or biz.get("file_id")
        if not file_id:
            raise RuntimeError(f"Không nhận được ID tệp: {biz}")

        # Chờ DeepSeek xử lý tệp xong (tối đa ~30 giây)
        for _ in range(30):
            try:
                info = await self._web_request("GET", "/api/v0/file/fetch_files", params={"file_ids": file_id})
                files = info.get("files") or []
                status = str(files[0].get("status", "")).upper() if files else ""
                if status in ("SUCCESS", "COMPLETED", "DONE"):
                    break
                if status in ("FAILED", "ERROR", "PARSE_FAILED", "CONTENT_EMPTY"):
                    raise RuntimeError(f"DeepSeek không xử lý được tệp '{path.name}' (trạng thái {status}).")
            except RuntimeError:
                raise
            except Exception:
                pass
            await asyncio.sleep(1)
        print("Tải tệp thành công.")
        return str(file_id)

    async def _ask_unofficial(self, prompt: str, model: str, file_paths: List[str]) -> Dict[str, Any]:
        if self._chat_session_id is None:
            biz = await self._web_request("POST", "/api/v0/chat_session/create", {})
            session = biz.get("chat_session") or biz
            self._chat_session_id = session.get("id")
            if not self._chat_session_id:
                raise RuntimeError(f"Không tạo được phiên chat: {biz}")
            self._parent_message_id = None

        ref_file_ids = [await self._upload_web_file(pathlib.Path(p)) for p in file_paths]

        target = "/api/v0/chat/completion"
        body = {
            "chat_session_id": self._chat_session_id,
            "parent_message_id": self._parent_message_id,
            "model_type": model or "default",
            "prompt": prompt,
            "ref_file_ids": ref_file_ids,
            "thinking_enabled": self.thinking,
            "search_enabled": self.search,
            "action": None,
            "preempt": False,
        }
        headers = {"x-ds-pow-response": await self._get_pow_header(target)}

        parser = _WebStreamParser()
        response = await self._client.request(
            "POST", self._WEB_BASE_URL + target, json=body, headers=self._web_headers(headers), stream=True
        )
        try:
            if response.status_code != 200:
                raise RuntimeError(f"HTTP {response.status_code} khi gửi tin nhắn.")
            if "text/event-stream" not in response.headers.get("content-type", ""):
                # Lỗi ứng dụng được trả về dạng JSON với mã HTTP 200
                raw = b"".join([chunk async for chunk in response.aiter_content()])
                self._unwrap_biz_data(json.loads(raw.decode("utf-8", "replace")))
                raise RuntimeError(f"Phản hồi không phải luồng SSE: {raw[:200]!r}")
            async for line in response.aiter_lines():
                parser.feed(line.decode("utf-8", "replace") if isinstance(line, bytes) else line)
        finally:
            await response.aclose()

        if parser.message_id is not None:
            self._parent_message_id = parser.message_id
        if not parser.response and not parser.thinking:
            return {"success": False, "mess": "Không nhận được phản hồi hợp lệ.", "thinking": ""}
        return {"success": True, "mess": parser.response, "thinking": parser.thinking}

    # --- Tiện ích ---
    @staticmethod
    def _parse_user_token(raw: str) -> str:
        raw = raw.strip()
        if raw.startswith("{"):
            # Giá trị localStorage `userToken` có dạng {"value":"<TOKEN>","__version":"0"}
            raw = json.loads(raw).get("value", "")
        raw = raw.removeprefix("Bearer ").strip().strip('"')
        if not raw:
            raise ValueError("userToken trống.")
        return raw

    @staticmethod
    def _parse_cookie_string(cookie_string: str) -> Dict[str, str]:
        cookies = {}
        for part in cookie_string.split(';'):
            if '=' in part:
                key, value = part.split('=', 1)
                cookies[key.strip()] = value.strip()
        return cookies

    @staticmethod
    def _format_proxy(proxy_string: Optional[str]) -> Optional[str]:
        if not proxy_string or proxy_string.startswith(('http://', 'https://', 'socks5://')):
            return proxy_string
        parts = proxy_string.split(':')
        if len(parts) == 2:
            return f"http://{parts[0]}:{parts[1]}"
        if len(parts) == 4:
            return f"http://{parts[2]}:{parts[3]}@{parts[0]}:{parts[1]}"
        print(f"Cảnh báo: Định dạng proxy '{proxy_string}' không hợp lệ. Sẽ không sử dụng proxy.")
        return None

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


class _DeepSeekPow:
    """Giải thử thách PoW (thuật toán DeepSeekHashV1) bằng tệp WebAssembly của chính DeepSeek."""

    def __init__(self, wasm_path: pathlib.Path, expected_sha256: str):
        if not wasm_path.is_file():
            raise FileNotFoundError(f"Thiếu tệp PoW '{wasm_path.name}' cạnh script.")
        wasm_bytes = wasm_path.read_bytes()
        if hashlib.sha256(wasm_bytes).hexdigest() != expected_sha256:
            print(f"Cảnh báo: '{wasm_path.name}' khác bản đã kiểm tra (có thể DeepSeek đã cập nhật).")
        self._store = wasmtime.Store()
        module = wasmtime.Module(self._store.engine, wasm_bytes)
        # Module không có import nào: không truy cập được tệp hay mạng
        exports = wasmtime.Instance(self._store, module, []).exports(self._store)
        self._memory = exports["memory"]
        self._solve = exports["wasm_solve"]
        self._malloc = exports["__wbindgen_export_0"]
        self._add_to_stack = exports["__wbindgen_add_to_stack_pointer"]

    def _write_str(self, text: str):
        data = text.encode("utf-8")
        ptr = self._malloc(self._store, len(data), 1)
        self._memory.write(self._store, data, ptr)
        return ptr, len(data)

    def solve(self, challenge: str, prefix: str, difficulty: float) -> Optional[int]:
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

    def make_header(self, challenge: Dict[str, Any]) -> str:
        answer = self.solve(challenge["challenge"], f"{challenge['salt']}_{challenge['expire_at']}_", challenge["difficulty"])
        if answer is None:
            raise RuntimeError("Không giải được thử thách PoW (có thể đã hết hạn).")
        payload = {key: challenge[key] for key in ("algorithm", "challenge", "salt", "signature", "target_path")}
        payload["answer"] = answer
        return base64.b64encode(json.dumps(payload, separators=(",", ":")).encode()).decode()


class _WebStreamParser:
    """
    Đọc luồng SSE của chat.deepseek.com. Phản hồi là một đối tượng `response` chứa các
    `fragments` (THINK = suy nghĩ, RESPONSE = trả lời, SEARCH, TIP), được cập nhật bằng các bản vá:
        {"v":{"response":{..., "fragments":[{"type":"THINK","content":"..."}]}}}
        {"p":"response/fragments/-1/content","o":"APPEND","v":"..."}
        {"v":"..."}                                      <- nối tiếp vào fragment hiện tại
        {"p":"response/fragments","o":"APPEND","v":[{"type":"RESPONSE","content":"..."}]}
        {"p":"response","o":"BATCH","v":[...]}
    """

    def __init__(self):
        self.thinking = ""
        self.response = ""
        self.message_id: Optional[int] = None
        self._event: Optional[str] = None
        self._fragments: List[Dict[str, Any]] = []
        self._target: Optional[Dict[str, Any]] = None

    def feed(self, line: str):
        line = line.strip()
        if line.startswith("event:"):
            self._event = line[6:].strip()
            return
        if not line.startswith("data:"):
            return
        raw = line[5:].strip()
        if not raw or raw == "[DONE]":
            return
        try:
            data = json.loads(raw)
        except ValueError:
            return
        if self._event == "ready" and isinstance(data, dict):
            if data.get("response_message_id") is not None:
                self.message_id = data["response_message_id"]
        elif self._event in (None, "message", "update_session"):
            self._dispatch(data)

    def _append(self, text: Any):
        if not isinstance(text, str) or self._target is None:
            return
        self._target["content"] += text
        if self._target["type"] == "THINK":
            self.thinking += text
        elif self._target["type"] == "RESPONSE":
            self.response += text

    def _start_fragment(self, frag: Dict[str, Any]):
        fragment = {"type": str(frag.get("type") or "RESPONSE").upper(), "content": ""}
        self._fragments.append(fragment)
        self._target = fragment
        self._append(frag.get("content") or "")

    def _apply_response(self, resp: Dict[str, Any]):
        if resp.get("message_id") is not None:
            self.message_id = resp["message_id"]
        for frag in resp.get("fragments") or []:
            if isinstance(frag, dict):
                self._start_fragment(frag)

    def _dispatch(self, data: Any):
        if not isinstance(data, dict):
            return
        path, op, value = data.get("p"), data.get("o"), data.get("v")
        if not path:
            if isinstance(value, dict) and isinstance(value.get("response"), dict):
                self._apply_response(value["response"])
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
            field = parts[3] if len(parts) > 3 else "content"
            if field == "content":
                if op == "SET":
                    fragment["content"] = ""
                self._append(value)


async def main():
    print("Chào mừng đến với DeepSeek Client!")
    print("Bạn muốn sử dụng phương thức nào?")
    print("  1: Chính thức (dùng API Key từ platform.deepseek.com, trả phí theo token)")
    print("  2: Không chính thức (dùng userToken của chat.deepseek.com, miễn phí, có tìm kiếm web)")

    while True:
        auth_choice = input("Lựa chọn của bạn (1 hoặc 2): ").strip()
        try:
            if auth_choice == "1":
                api_key = input("Vui lòng nhập API Key của bạn: ").strip()
                client = DeepSeekClient(api_key=api_key)
                break
            elif auth_choice == "2":
                print("Lấy userToken: mở chat.deepseek.com > F12 > Application > Local Storage > 'userToken'.")
                user_token = input("Dán userToken: ").strip()
                cookie_string = input("Dán chuỗi cookie (bỏ trống nếu không cần): ").strip()
                proxy = input("Nhập proxy (bỏ trống nếu không dùng): ").strip()
                client = DeepSeekClient(user_token=user_token, cookie_string=cookie_string, proxy=proxy or None)
                break
            else:
                print("Lựa chọn không hợp lệ.")
        except (ImportError, ValueError) as e:
            print(f"Lỗi: {e}")
            return

    try:
        await client.connect()
    except Exception as e:
        print(f"\nKhông thể kết nối: {type(e).__name__}: {e}")
        await client.close()
        return

    try:
        await chat_loop(client)
    finally:
        await client.close()


async def chat_loop(client: DeepSeekClient):
    models = client.models
    print("\nVui lòng chọn mô hình:")
    for i, m in enumerate(models, 1):
        print(f"  {i}: {m['name']}" + (f" ({m['id']})" if m['name'] != m['id'] else ""))
    while True:
        choice = input("Lựa chọn của bạn: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(models):
            model = models[int(choice) - 1]["id"]
            break
        print("Lựa chọn không hợp lệ.")

    print("\nLệnh: 'exit' thoát | 'new' trò chuyện mới | 'think' bật/tắt suy nghĩ"
          + (" | 'search' bật/tắt tìm kiếm web" if client.mode == 'unofficial' else ""))
    while True:
        prompt = input(f"\n[suy nghĩ: {'bật' if client.thinking else 'tắt'}"
                       + (f", tìm kiếm: {'bật' if client.search else 'tắt'}" if client.mode == 'unofficial' else "")
                       + "] Bạn: ").strip()
        command = prompt.lower()
        if command in ["exit", "quit"]:
            print("Đang kết thúc cuộc trò chuyện...")
            break
        if command == "new":
            client.reset_chat()
            print("Đã bắt đầu cuộc trò chuyện mới.")
            continue
        if command == "think":
            client.thinking = not client.thinking
            continue
        if command == "search" and client.mode == 'unofficial':
            client.search = not client.search
            continue
        if not prompt:
            continue

        file_input = input("Nhập đường dẫn tệp đính kèm (cách nhau bằng dấu phẩy), hoặc bỏ trống: ").strip()
        file_paths = [p.strip().strip('"') for p in file_input.split(',') if p.strip()] if file_input else []

        print("DeepSeek đang trả lời...")
        response = await client.ask(prompt, model, file_paths=file_paths)
        if not response["success"]:
            print(f"DeepSeek (Lỗi): {response['mess']}")
            continue
        if response["thinking"]:
            print(f"\n[Suy nghĩ]\n{response['thinking'].strip()}\n[/Suy nghĩ]\n")
        print(f"DeepSeek: {response['mess']}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nChương trình đã dừng.")
