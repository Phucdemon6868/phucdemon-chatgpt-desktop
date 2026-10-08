import asyncio
import mimetypes
import pathlib
import time
from typing import Any, Dict, List, Optional

# Chế độ chính thức: SDK mới `google-genai` (thay cho `google-generativeai` đã ngừng hỗ trợ)
try:
    from google import genai
    from google.genai import types as genai_types
    google_genai_installed = True
except ImportError:
    google_genai_installed = False

# Chế độ không chính thức: thư viện `gemini-webapi` (được cập nhật theo giao diện web của Gemini)
try:
    from gemini_webapi import GeminiClient as WebGeminiClient
    gemini_webapi_installed = True
except ImportError:
    gemini_webapi_installed = False


class GeminiClient:
    """
    Client bất đồng bộ để tương tác với Google Gemini, hỗ trợ cả hai chế độ.
    - Chế độ chính thức (API Key): dùng `google-genai`, hỗ trợ tệp đa phương thức và tạo ảnh
      (Nano Banana = các mô hình có chữ "image" trong tên, ví dụ `gemini-2.5-flash-image`).
    - Chế độ không chính thức (Cookie): dùng `gemini-webapi`, chat, gửi ảnh và tạo ảnh như trên web.

    Danh sách mô hình được lấy trực tiếp từ Google khi kết nối, nên không cần sửa code
    mỗi khi Google ra mô hình mới hoặc khai tử mô hình cũ.
    """

    _COOKIE_KEYS = ("__Secure-1PSID", "__Secure-1PSIDTS")
    # Mô hình không dùng để chat (embedding, TTS, live audio...) bị lọc khỏi danh sách
    _OFFICIAL_EXCLUDED_KEYWORDS = ("embedding", "tts", "live", "native-audio", "aqa", "robotics", "computer-use")

    def __init__(self, api_key: Optional[str] = None, cookie_string: Optional[str] = None, proxy: Optional[str] = None):
        if api_key:
            if not google_genai_installed:
                raise ImportError("Thư viện `google-genai` chưa được cài đặt. Vui lòng chạy `pip install google-genai`.")
            self._mode = 'official'
            self._api_key = api_key
        elif cookie_string:
            if not gemini_webapi_installed:
                raise ImportError("Thư viện `gemini-webapi` chưa được cài đặt. Vui lòng chạy `pip install gemini-webapi`.")
            self._mode = 'unofficial'
            self._cookies = self._parse_cookie_string(cookie_string)
            if not self._cookies.get("__Secure-1PSID"):
                raise ValueError("Chuỗi cookie thiếu `__Secure-1PSID`.")
            self._proxy = self._format_proxy(proxy)
        else:
            raise ValueError("Phải cung cấp `api_key` (chính thức) hoặc `cookie_string` (không chính thức).")

        self._client: Any = None
        self._chat: Any = None
        self._chat_model: Optional[str] = None
        self._models: List[Dict[str, str]] = []

    @property
    def mode(self) -> str:
        return self._mode

    @property
    def models(self) -> List[Dict[str, str]]:
        """Danh sách mô hình khả dụng: [{"id": ..., "name": ...}, ...]. Chỉ có sau khi `connect()`."""
        return self._models

    async def connect(self):
        if self._mode == 'official':
            self._client = genai.Client(api_key=self._api_key)
            self._models = await self._list_official_models()
        else:
            print("Đang xác thực bằng cookie (unofficial)...")
            self._client = WebGeminiClient(
                self._cookies["__Secure-1PSID"], self._cookies.get("__Secure-1PSIDTS"), proxy=self._proxy
            )
            # auto_refresh=True: thư viện tự làm mới cookie định kỳ (thay cho _rotate_cookies cũ)
            await self._client.init(timeout=300, auto_close=False, auto_refresh=True)
            print("Xác thực thành công.")
            self._models = [
                {"id": m.model_name or m.model_id, "name": m.display_name or m.model_name}
                for m in (self._client.list_models() or []) if m.is_available
            ]

    async def close(self):
        if not self._client:
            return
        if self._mode == 'official':
            await self._client.aio.aclose()
        else:
            await self._client.close()

    def reset_chat(self):
        """Bắt đầu cuộc trò chuyện mới (xóa ngữ cảnh)."""
        self._chat = None
        self._chat_model = None

    async def ask(self, prompt: str, model: Optional[str], file_paths: Optional[List[str]] = None) -> Dict[str, Any]:
        """
        Gửi tin nhắn, giữ ngữ cảnh hội thoại giữa các lần gọi.
        Trả về {"success": bool, "mess": str, "images": [ảnh]} — `images` dùng cho `save_images()`.
        """
        if not self._client:
            raise RuntimeError("Client chưa được kết nối. Hãy gọi `connect()` hoặc dùng `async with`.")

        for path in file_paths or []:
            if not pathlib.Path(path).is_file():
                return {"success": False, "mess": f"Lỗi: Không tìm thấy tệp tại '{path}'", "images": []}

        try:
            if self._mode == 'official':
                return await self._ask_official(prompt, model, file_paths)
            return await self._ask_unofficial(prompt, model, file_paths)
        except Exception as e:
            return {"success": False, "mess": f"{type(e).__name__}: {e}", "images": []}

    async def save_images(self, images: List[Any], save_path: str = ".") -> List[str]:
        """Lưu các ảnh trả về từ `ask()` vào thư mục, trả về danh sách đường dẫn đã lưu."""
        folder = pathlib.Path(save_path)
        folder.mkdir(parents=True, exist_ok=True)
        saved = []
        for i, image in enumerate(images):
            try:
                if self._mode == 'official':
                    ext = mimetypes.guess_extension(image["mime_type"]) or ".png"
                    full_path = folder / f"gemini_{int(time.time())}_{i}{ext}"
                    full_path.write_bytes(image["data"])
                    saved.append(str(full_path))
                else:
                    # full_size=True: tải ảnh độ phân giải gốc (chỉ áp dụng cho ảnh do Gemini tạo)
                    kwargs = {"full_size": True} if type(image).__name__ == "GeneratedImage" else {}
                    path = await image.save(path=str(folder), **kwargs)
                    if path:
                        saved.append(path)
            except Exception as e:
                print(f"Lỗi khi lưu ảnh #{i + 1}: {e}")
        return saved

    # --- Chế độ chính thức ---
    async def _list_official_models(self) -> List[Dict[str, str]]:
        models = []
        async for m in await self._client.aio.models.list():
            model_id = (m.name or "").removeprefix("models/")
            if "generateContent" not in (m.supported_actions or []):
                continue
            if not model_id.startswith("gemini") or any(k in model_id for k in self._OFFICIAL_EXCLUDED_KEYWORDS):
                continue
            models.append({"id": model_id, "name": m.display_name or model_id})
        return sorted(models, key=lambda m: m["id"])

    async def _ask_official(self, prompt: str, model: str, file_paths: Optional[List[str]]) -> Dict[str, Any]:
        if not model:
            raise ValueError("Chế độ chính thức cần chọn mô hình.")

        # Đổi mô hình thì bắt đầu cuộc trò chuyện mới
        if self._chat is None or self._chat_model != model:
            config = None
            if "image" in model:
                # Mô hình tạo ảnh (Nano Banana) cần bật đầu ra dạng ảnh
                config = genai_types.GenerateContentConfig(response_modalities=["TEXT", "IMAGE"])
            self._chat = self._client.aio.chats.create(model=model, config=config)
            self._chat_model = model

        contents: List[Any] = []
        for path_str in file_paths or []:
            path = pathlib.Path(path_str)
            mime_type, _ = mimetypes.guess_type(path)
            if mime_type is None:
                return {"success": False, "mess": f"Lỗi: Không thể xác định loại tệp cho '{path_str}'", "images": []}
            if path.stat().st_size > 15 * 1024 * 1024:
                # Tệp lớn phải tải lên File API thay vì gửi kèm trực tiếp
                contents.append(await self._client.aio.files.upload(file=path))
            else:
                contents.append(genai_types.Part.from_bytes(data=path.read_bytes(), mime_type=mime_type))
        contents.append(prompt)

        response = await self._chat.send_message(contents)

        texts, images = [], []
        candidate = response.candidates[0] if response.candidates else None
        for part in (candidate.content.parts if candidate and candidate.content else None) or []:
            if getattr(part, "thought", False):
                continue
            if part.text:
                texts.append(part.text)
            elif part.inline_data and part.inline_data.data:
                images.append({"data": part.inline_data.data, "mime_type": part.inline_data.mime_type or "image/png"})

        if not texts and not images:
            reason = candidate.finish_reason if candidate else getattr(response.prompt_feedback, "block_reason", None)
            return {"success": False, "mess": f"Không nhận được phản hồi (lý do: {reason}).", "images": []}
        return {"success": True, "mess": "\n".join(texts), "images": images}

    # --- Chế độ không chính thức ---
    async def _ask_unofficial(self, prompt: str, model: Optional[str], file_paths: Optional[List[str]]) -> Dict[str, Any]:
        if self._chat is None or self._chat_model != model:
            kwargs = {"model": model} if model else {}
            self._chat = self._client.start_chat(**kwargs)
            self._chat_model = model

        response = await self._chat.send_message(prompt, files=file_paths or None)
        return {"success": True, "mess": response.text, "images": list(response.images)}

    def _parse_cookie_string(self, cookie_string: str) -> Dict[str, str]:
        cookies = {}
        for part in cookie_string.split(';'):
            if '=' in part:
                key, value = part.split('=', 1)
                cookies[key.strip()] = value.strip()
        return {k: v for k, v in cookies.items() if k in self._COOKIE_KEYS}

    def _format_proxy(self, proxy_string: Optional[str]) -> Optional[str]:
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


async def main():
    print("Chào mừng đến với Gemini Client!")
    download_dir = "gemini_images"
    print(f"Tất cả ảnh được tạo sẽ được lưu trong thư mục '{download_dir}'.")

    print("Bạn muốn sử dụng phương thức nào?")
    print("  1: Chính thức (dùng API Key, hỗ trợ đính kèm nhiều loại tệp, tạo ảnh với mô hình *-image)")
    print("  2: Không chính thức (dùng Cookie, chat, gửi ảnh, tạo và tải ảnh như trên web)")

    while True:
        auth_choice = input("Lựa chọn của bạn (1 hoặc 2): ").strip()
        try:
            if auth_choice == "1":
                api_key = input("Vui lòng nhập API Key của bạn: ").strip()
                client = GeminiClient(api_key=api_key)
                break
            elif auth_choice == "2":
                print("Cần ít nhất cookie __Secure-1PSID (nên có thêm __Secure-1PSIDTS).")
                cookie_string = input("Vui lòng dán chuỗi cookie của bạn: ").strip()
                proxy = input("Nhập proxy (bỏ trống nếu không dùng): ").strip()
                client = GeminiClient(cookie_string=cookie_string, proxy=proxy or None)
                break
            else:
                print("Lựa chọn không hợp lệ.")
        except (ImportError, ValueError) as e:
            print(f"Lỗi: {e}")
            return

    try:
        await client.connect()
    except Exception as e:
        hint = " (Cookie có thể đã hết hạn — hãy lấy lại cookie mới từ trình duyệt.)" if client.mode == 'unofficial' else ""
        print(f"\nKhông thể kết nối: {type(e).__name__}: {e}{hint}")
        await client.close()
        return

    try:
        await chat_loop(client, download_dir)
    finally:
        await client.close()


async def chat_loop(client: GeminiClient, download_dir: str):
    models = client.models
    print("\nVui lòng chọn mô hình:")
    if client.mode == 'unofficial':
        print("  0: Mặc định của tài khoản (tạo ảnh: chỉ cần yêu cầu \"tạo ảnh ...\" với mô hình bất kỳ)")
    for i, m in enumerate(models, 1):
        print(f"  {i}: {m['name']} ({m['id']})")

    while True:
        choice = input("Lựa chọn của bạn: ").strip()
        if choice == "0" and client.mode == 'unofficial':
            model = None
            break
        if choice.isdigit() and 1 <= int(choice) <= len(models):
            model = models[int(choice) - 1]["id"]
            break
        print("Lựa chọn không hợp lệ.")

    print("\nGõ 'exit' để thoát, 'new' để bắt đầu cuộc trò chuyện mới.")
    while True:
        prompt = input("\nBạn: ").strip()
        if prompt.lower() in ["exit", "quit"]:
            print("Đang kết thúc cuộc trò chuyện...")
            break
        if prompt.lower() == "new":
            client.reset_chat()
            print("Đã bắt đầu cuộc trò chuyện mới.")
            continue
        if not prompt:
            continue

        file_input = input("Nhập đường dẫn tệp đính kèm (cách nhau bằng dấu phẩy), hoặc bỏ trống: ").strip()
        file_paths = [p.strip().strip('"') for p in file_input.split(',') if p.strip()] if file_input else []

        print("Gemini đang trả lời...")
        response = await client.ask(prompt, model, file_paths=file_paths)

        if not response["success"]:
            print(f"Gemini (Lỗi): {response['mess']}")
            continue

        if response["mess"]:
            print(f"Gemini: {response['mess']}")
        images = response["images"]
        if images:
            print(f"Gemini đã trả về {len(images)} ảnh.")
            if input(f"Bạn có muốn tải ảnh về thư mục '{download_dir}' không? (y/n): ").strip().lower() == 'y':
                for path in await client.save_images(images, save_path=download_dir):
                    print(f"  Đã lưu: {path}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nChương trình đã dừng.")
