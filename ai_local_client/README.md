# ai-local-client

Dùng **ChatGPT, Gemini và DeepSeek** như một "backend" local. Mỗi AI có hai chế độ:

| Nhà cung cấp | Chế độ | Cấu hình trong `.env` | Tên model (ví dụ) |
|---|---|---|---|
| `chatgpt` | Web (cookie) | `CHATGPT_COOKIE` | `chatgpt/auto` |
| `openai` | API chính thức | `OPENAI_API_KEY` | `openai/gpt-4o-mini` |
| `gemini` | API chính thức | `GEMINI_API_KEY` | `gemini/gemini-2.5-flash`, `gemini/gemini-2.5-flash-image` (tạo ảnh) |
| `gemini-web` | Web (cookie) | `GEMINI_COOKIE` | `gemini-web/default` |
| `deepseek` | API chính thức | `DEEPSEEK_API_KEY` | `deepseek/deepseek-flash` |
| `deepseek-web` | Web (userToken) | `DEEPSEEK_USER_TOKEN` | `deepseek-web/default`, `deepseek-web/expert+think+search` |

Chỉ cần điền nhà cung cấp bạn muốn dùng. Tên model luôn có dạng `<nhà cung cấp>/<model>`. Danh sách model thật được lấy trực tiếp từ từng nhà cung cấp (`/models` trong CLI, nút 🔄 trong UI). Tên không có tiền tố (ví dụ `auto`, `gpt-4o`) thuộc nhà cung cấp của model mặc định, nên cấu hình cũ vẫn chạy.

Có ba cách dùng:

- **Proxy tương thích OpenAI API**: `http://localhost:8000/v1`. Cursor, Continue.dev, Aider, Open WebUI, LangChain, SDK `openai`… đều dùng được.
- **Web UI local** (Gradio): lịch sử lưu SQLite, đổi model, streaming.
- **CLI chat** trong terminal.

> ⚠️ Các chế độ **web** (`chatgpt`, `gemini-web`, `deepseek-web`) là API **không chính thức**: chúng vi phạm điều khoản của OpenAI/Google/DeepSeek, tài khoản có thể bị giới hạn hoặc khóa, và có thể hỏng khi trang web thay đổi. Chỉ dùng tài khoản của chính bạn, cho mục đích cá nhân. Cookie/token bằng với quyền đăng nhập: **không commit `.env`, không chia sẻ cookie**. Đừng mở proxy ra Internet; nếu cần thì đặt `PROXY_API_KEY`. Các chế độ **API key** là cách chính thức và ổn định.

## Cài đặt

```bash
pip install -r requirements.txt
python -m ui.app        # mở http://127.0.0.1:7860 → tab ⚙️ Cài đặt để nhập khóa/cookie
```

Cách dễ nhất là nhập API key / cookie ngay trên **Web UI, tab ⚙️ Cài đặt**: có nút **Kiểm tra** kết nối, bấm **Lưu** là áp dụng ngay (không cần khởi động lại) và được ghi vào file `.env` (quyền 600). Ô bí mật chỉ hiện dạng `••••abcd`, để trống nghĩa là giữ nguyên. Nếu thích, bạn vẫn có thể sửa `.env` bằng tay (`cp .env.example .env`).

Lấy thông tin đăng nhập:
- **ChatGPT web**: mở https://chatgpt.com và đăng nhập → F12 → Network → chọn request bất kỳ tới chatgpt.com → copy giá trị header `cookie`.
- **Gemini web**: mở https://gemini.google.com → F12 → Application → Cookies → copy `__Secure-1PSID` và `__Secure-1PSIDTS`, dán dạng `__Secure-1PSID=...; __Secure-1PSIDTS=...`.
- **DeepSeek web**: mở https://chat.deepseek.com → F12 → Application → Local Storage → copy giá trị `userToken` (dán nguyên cả `{"value":...}` cũng được).
- **API key**: platform.openai.com, aistudio.google.com, platform.deepseek.com.

Ghi chú theo nhà cung cấp:
- **Tạo ảnh**: Gemini API với model có chữ `image` (Nano Banana), hoặc Gemini web khi bạn yêu cầu "tạo ảnh ...". Ảnh được lưu vào `IMAGE_DIR` (mặc định `data/images`), hiển thị trong UI và được báo đường dẫn trong CLI/proxy.
- **DeepSeek web**: `default` (Nhanh) hoặc `expert` (Chuyên gia); thêm `+think` để bật DeepThink, `+search` để tìm kiếm web. Mỗi tin nhắn phải giải thử thách chống bot (proof-of-work) bằng tệp WebAssembly của DeepSeek (`core/assets/sha3_wasm_bg.wasm`, chạy trong `wasmtime`, không truy cập được tệp hay mạng).
- **DeepSeek API/web** và các model "thinking" khác: phần suy nghĩ không được hiển thị, giống ChatGPT web.

## 1. Proxy OpenAI-compatible

```bash
python -m server --port 8000
```

```python
from openai import OpenAI
client = OpenAI(base_url="http://localhost:8000/v1", api_key="PROXY_API_KEY-hoặc-gì-cũng-được")
r = client.chat.completions.create(model="gemini/gemini-2.5-flash", messages=[{"role": "user", "content": "Xin chào"}])
print(r.choices[0].message.content)
```

```bash
curl http://localhost:8000/v1/chat/completions -H 'content-type: application/json' \
  -d '{"model":"auto","stream":true,"messages":[{"role":"user","content":"hi"}]}'
```

| Công cụ | Cấu hình |
|---|---|
| Continue.dev / Cursor | provider `openai`, `apiBase: http://localhost:8000/v1` |
| Aider | `aider --openai-api-base http://localhost:8000/v1 --model openai/deepseek/deepseek-flash` |
| Open WebUI | Settings → Connections → OpenAI API → `http://localhost:8000/v1` |

**Cách nối lịch sử.** Nhà cung cấp dùng API key nhận thẳng toàn bộ lịch sử. Bản web (ChatGPT, Gemini, DeepSeek) giữ trạng thái theo thread, còn API OpenAI là stateless (gửi lại toàn bộ lịch sử mỗi lượt). Với bản web, proxy hash phần lịch sử (theo từng nhà cung cấp) trước tin nhắn cuối:
- Nếu đã thấy hash đó: nối tiếp thread cũ và chỉ gửi tin nhắn mới.
- Nếu chưa thấy, lịch sử bị sửa, hoặc thread cũ không dùng được nữa: gộp cả lịch sử (kèm system prompt) thành một prompt và mở thread mới.

Mặc định proxy dùng **chat tạm** (`CHATGPT_TEMPORARY_CHAT=1`), nên không làm đầy lịch sử ChatGPT/Gemini của bạn. DeepSeek web không có chat tạm.

Giới hạn: không hỗ trợ function calling/`tools`, ảnh/tệp đầu vào, `temperature`… (các trường này bị bỏ qua); `usage` luôn trả về 0.

## 2. Web UI

```bash
python -m ui.app --port 7860   # mở http://127.0.0.1:7860
```

- **💬 Chat**: chọn model, lịch sử hội thoại, ảnh do AI tạo hiển thị ngay trong khung chat.
- **⚙️ Cài đặt**: API key / cookie / token của từng AI (mỗi AI một tab: 🔑 API chính thức và 🌐 Web), model mặc định, proxy cho bản web, thời gian chờ, số lần thử lại, chat tạm, thư mục ảnh, khóa bảo vệ proxy.
  Thay đổi áp dụng ngay cho UI; proxy `python -m server` và CLI đọc `.env` khi khởi động nên cần chạy lại.

> UI mặc định chỉ mở ở `127.0.0.1`. Đừng chạy với `--host 0.0.0.0` trên mạng lạ: ai mở được UI đều sửa được cookie/khóa trong tab Cài đặt.

Hội thoại được lưu ở `data/chats.db` và nối tiếp đúng thread kể cả sau khi khởi động lại. Có thể đổi model (kể cả đổi nhà cung cấp) giữa cuộc trò chuyện: lịch sử được chuyển sang nhà cung cấp mới.

## 3. CLI

```bash
python chat.py      # /new, /model <nhà cung cấp>/<model>, /models, /providers, /help, /quit
```

## Cấu trúc

```
core/
  config.py      # đọc .env
  base.py        # Provider (giao diện chung), StreamEvent, ProviderError, flatten
  registry.py    # cấu hình nhà cung cấp, định tuyến "<provider>/<model>"
  client.py      # ChatGPT web: stream()/list_models(), retry/backoff
  auth.py        # ChatGPT: cookie → accessToken, cache + tự refresh
  sentinel.py    # ChatGPT: chat-requirements + proof-of-work
  sse.py         # ChatGPT: parser SSE (định dạng cũ + delta v1)
  openai_api.py  # OpenAI API và DeepSeek API (định dạng OpenAI)
  gemini.py      # Gemini API (google-genai) và Gemini web (gemini-webapi)
  deepseek_web.py# DeepSeek web: PoW (wasmtime) + parser SSE
  aio.py         # chạy thư viện async (gemini-webapi) từ code đồng bộ
  store.py       # SQLite: hội thoại UI + cache thread của proxy
server/        # FastAPI /v1/chat/completions, /v1/models
ui/            # Gradio
chat.py        # CLI
tests/         # pytest, không cần mạng/cookie
```

Client ChatGPT tự xử lý:
- **401**: lấy accessToken mới rồi thử lại.
- **429/5xx**: backoff theo `Retry-After` hoặc lũy thừa, tối đa `CHATGPT_MAX_RETRIES` lần.

## Test

```bash
pip install -r requirements-dev.txt
pytest -q
```
