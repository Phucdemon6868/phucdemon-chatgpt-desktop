# Hướng dẫn tiếng Việt cho gói bot "天堂经典版 Bd" bản 9.16

Bộ tài liệu này dịch và giải thích sang tiếng Việt toàn bộ phần chữ trong gói `Bd9.16` (bot treo máy cho **Lineage Classic** của NCSOFT, server Đài Loan/Hàn Quốc, chạy qua launcher **Purple** – trong file gọi là `紫P`).

Tài liệu **không** chứa file gốc của gói (không có `.exe`, `.dll`, `.lua` hay file cấu hình gốc), chỉ có bản dịch và phần giải thích.

## Đọc theo thứ tự nào?

| Thứ tự | File | Nội dung |
|---|---|---|
| 1 | [03-cau-hinh-chung-va-cau-truc-goi.md](03-cau-hinh-chung-va-cau-truc-goi.md) | Cấu trúc gói (từng file/thư mục là gì), `config/config.ini`, `ZKT.ini`, danh sách server, `Account.txt`, các module Lua |
| 2 | [01-huong-dan-su-dung.md](01-huong-dan-su-dung.md) | Bản dịch `使用说明.txt`: cách đặt bản đồ đánh quái, danh sách bản đồ được hỗ trợ, tọa độ Hang Kiến, bản đồ quán net; hướng dẫn server tổ đội |
| 3 | [04-baseconfig.md](04-baseconfig.md) | `Game_Config/BaseConfig.txt` – file cấu hình gameplay quan trọng nhất, giải thích từng mục `[...]` và từng khóa |
| 4 | [05-game-config-chien-dau-va-vat-pham.md](05-game-config-chien-dau-va-vat-pham.md) | Sự kiện, clan (huyết minh `血盟`), buff, phản công người chơi, xóa đồ, lọc quái/vật phẩm, dùng vật phẩm |
| 5 | [06-game-config-treo-may-kho-va-giao-dich.md](06-game-config-treo-may-kho-va-giao-dich.md) | `gj.txt` (treo máy theo cấp), kho cá nhân, cất/lấy đồ, mua bán NPC, giao dịch giữa nhân vật, bảo vật |
| 6 | [02-nhat-ky-cap-nhat.md](02-nhat-ky-cap-nhat.md) | Bản dịch `更新说明.txt`: lịch sử các bản cập nhật, mới nhất ở trên |
| — | [07-tu-dien-thuat-ngu.md](07-tu-dien-thuat-ngu.md) | Từ điển 622 thuật ngữ: bản đồ, server, nghề, vật phẩm, quái/NPC, kỹ năng, thuật ngữ của bot |

## Quy tắc quan trọng nhất khi sửa cấu hình

- **Giữ nguyên chữ Trung.** Bot đọc chữ đúng từng ký tự: tên mục `[...]`, tên khóa bên trái dấu `=`, tên bản đồ, vật phẩm, quái, NPC, server. Chỉ đổi số hoặc giá trị sau dấu `=`. Đừng gõ tiếng Việt vào file cấu hình.
- **Phồn thể và Giản thể là hai chữ khác nhau** (ví dụ `說話之島` khác `说话之岛`). Hãy chép y nguyên từ ô `code` trong tài liệu hoặc từ file gốc.
- Lưu file bằng **UTF-8** như bản gốc (riêng `大中控/Data/Config.ini` dùng mã **GBK**). Dùng dấu `=`, `,`, `|` kiểu tiếng Anh (nửa độ rộng).
- **Sao lưu thư mục `Game_Config`** trước khi sửa và trước khi cập nhật bot lên bản mới.

## Ký hiệu trong tài liệu

- **(?)** – bản dịch hoặc suy luận chưa chắc chắn (tên chính thức của bản đồ/vật phẩm, đơn vị không được ghi trong file gốc...).
- **(suy đoán từ tên file)** – các file Lua đã bị **mã hóa**, không đọc được, nên vai trò của chúng chỉ được đoán qua tên file và nhật ký cập nhật.
- **⚠️ Tài liệu này không hướng dẫn phần này.** – ba mục `驱动模式` (chế độ driver kernel), `目录保护` (ẩn thư mục của bot) và `自动接码验证设备` (tự động nhận mã SMS để xác minh thiết bị) chỉ được ghi nhãn, không giải thích cách dùng.
- `\|` trong bảng chính là ký tự `|` trong file gốc (viết vậy để bảng Markdown không bị vỡ).

## Cảnh báo

- **Rủi ro cho máy tính:** `Bd.exe` đòi quyền quản trị (admin), đã bị đóng gói bảo vệ và có nhúng một driver kernel của Windows. Chạy nó nghĩa là cho phần mềm không rõ nguồn gốc toàn quyền trên máy.
- **Rủi ro tài khoản:** dùng bot vi phạm điều khoản của NCSOFT, tài khoản có thể bị khóa. Những câu kiểu "đã xử lý cơ chế phát hiện" trong nhật ký cập nhật chỉ là lời của tác giả bot.
- **Thông tin cá nhân:** file `使用说明.txt` gốc có một dòng tài khoản mẫu trông như thật (email, mật khẩu, số điện thoại, đường link có token). Tài liệu này đã thay chúng bằng chỗ giữ chỗ (`<email>`, `<mật khẩu>`, `<số điện thoại>`, `<đường link>`). `Account.txt` lưu mật khẩu dạng chữ thường: đừng gửi gói bot cho người khác khi đã điền tài khoản thật.
- File `tmp68A9.tmp` trong archive bị hỏng; có vẻ là bản sao tạm của `Bd.exe`, không cần dùng.
