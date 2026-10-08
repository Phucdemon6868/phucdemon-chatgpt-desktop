# Báo cáo phân tích tĩnh gói Bd 9.16 — Tóm tắt điều hành

> **Phạm vi & phương pháp.** Phân tích **tĩnh** (static analysis) các file nhị phân của gói bot "天堂经典版 Bd" 9.16: chỉ đọc byte, cấu trúc PE, bảng import và chuỗi (dùng `pefile`, `strings`, `objdump`). **Không chạy** bất kỳ file nào, **không gỡ gói** (unpack), **không giải ảo hóa** protector, **không tái tạo** logic driver/hypervisor. Mục đích là **phòng thủ**: hiểu các file *làm gì trên máy* và *nhận biết / phòng ngừa* ra sao.
>
> **Ngày phân tích:** 2026-10-08. **Môi trường:** Linux (sandbox), phân tích offline, không truy cập mạng.
>
> Mọi suy đoán được đánh dấu **(suy luận)**. IP/domain chưa tra whois được ghi **(chưa xác minh whois)** vì phân tích không dùng mạng.

## Các file được phân tích (SHA-256)

| File | Vai trò | Kích thước | SHA-256 |
|---|---|---|---|
| `Bd.exe` | Bot chính (x64, GUI) | 56,904,704 | `e8eeb19780543f76eec1375f0fd5e35b62b8270d9b96bfedb03883a968062786` |
| `JSBProxy64.dll` | Thư viện phụ (x64) | 23,254,528 | `42ce658a1e7f6229a60e2bf914c2555cc342086170b03aeb2372bfda892e5c43` |
| `bmp/login.exe` | Trình đăng nhập (x64) | 14,888,960 | `8196fc82e4e084b93ba3e95331bd1ef708293ce435ccfd57cd4678b8adff9130` |
| `bmp/libcurl-x64.dll` | Thư viện HTTP libcurl (bên thứ ba) | 3,435,624 | `0972257268afddf123464b37e844293ffd424f71c3f7893dfb855b5642054238` |
| `大中控.exe` (DaZhongKong) | Console điều khiển nhiều máy (x86, MFC) | 3,685,888 | `433a3f9eef9314c4508aec8d15c9572d5992528593293b1e03c7d57e0802ec68` |
| `组队服务器.exe` (ZuDuiServer) | Server tổ đội LAN (x86, MFC) | 3,531,264 | `87007457db0917c52fc6b5ca4135451509eb6636200ed5d16411f6589d714bb0` |

## Phát hiện chính

1. **Lõi bot bị ảo hóa/đóng gói.** `Bd.exe`, `JSBProxy64.dll`, `login.exe` có các PE section tên ngẫu nhiên, entropy ~7.8–7.9, `.text` không có dữ liệu trên đĩa (dựng lại khi chạy), và bảng import gần như rỗng (IAT dựng lại lúc chạy). Vì vậy **không thể đọc logic tĩnh** — đây là giới hạn then chốt của báo cáo. Protector thuộc loại **VM-based tùy biến (suy luận)**; không thấy marker của VMProtect/Themida/Enigma.

2. **`Bd.exe` nhúng driver kernel chưa ký.** Trong vùng đọc được có **4 biến thể** driver chế độ NATIVE (3 bản ~0x71000, 1 bản ~0x6b000; timestamp từ 2026-04-30 đến 2026-07-16). Đường dẫn PDB: `F:\qudong\MyDriver1 - 副本 - 副本\x64\Release\MyDriver1.pdb` (*qudong* = 驱动 = driver; *副本* = bản sao).

3. **Driver có ba nhóm hành vi.** (a) Hook ngăn xếp driver bàn phím `kbdclass`; (b) hook `NtCreateFile` để **ẩn/bảo vệ thư mục** (khớp tùy chọn `目录保护` trong `config.ini`); (c) một **hypervisor EPT/VT-x** (chuỗi `hv.sys`, `VMCALL`, `EPT USED PAGES`) — khớp tùy chọn `驱动模式`. Đây là mã chạy ở **Ring-0**, về nguyên tắc có toàn quyền trên máy. Báo cáo chỉ mô tả hành vi + rủi ro + cách nhận biết, **không** nêu cách dựng lại.

4. **Không file nào của gói có chữ ký số hợp lệ.** `Bd.exe`, `JSBProxy64.dll`, `login.exe`, `大中控.exe`, `组队服务器.exe` đều **không ký** (không có Authenticode). Chỉ `libcurl-x64.dll` (bên thứ ba) có bảng chữ ký nhúng (không kiểm được chuỗi chứng chỉ bằng phân tích tĩnh). Các chuỗi VeriSign/DigiCert trong file chỉ là dữ liệu đi kèm, **không** phải chữ ký của gói.

5. **Metadata của `Bd.exe` là stub Visual Studio chưa điền.** Version resource ghi `1.0.0.1`, `OriginalFilename`/`InternalName` = `YOLOGraphColor.exe`, các trường công ty/sản phẩm còn nguyên `TODO: <...>`. Banner `Ver 9.16(TT)` **chỉ** có trong `大中控.exe`, không có trong `Bd.exe`; nhãn "9.16" khớp **tên gói bên ngoài**, không phải version resource của `Bd.exe`.

6. **Hai công cụ điều khiển đọc được (không đóng gói).** `大中控.exe` là **client** (WS2_32 `connect/send/recv`), có **IP cứng `101.43.73.242`** nằm cạnh chuỗi `CFileToClient`. `组队服务器.exe` là **server** (`listen/accept/bind`) cho tổ đội LAN, cổng lấy từ `组队服务器\config.ini` (`port=9527`).

7. **Chỉ số mạng.** Ngoài `101.43.73.242`, trong `Bd.exe` còn chuỗi IP `49.235.147.185`. Cả hai nghi thuộc dải Tencent Cloud (Trung Quốc) **(chưa xác minh whois)**. `JSBProxy64.dll` ghi tên gốc `JSBProxy.dll` và website nhà bán `www.8u18.com`. `login.exe` dùng `libcurl` để gọi HTTP (liên quan tính năng nhận mã SMS); URL cụ thể bị protector che.

## Đánh giá rủi ro

- **Máy tính:** cao. Một **driver Ring-0 chưa ký, không rõ nguồn gốc** được nạp vào kernel; phần người dùng bị đóng gói nên **không thể kiểm toán**. Không thể khẳng định (cũng không loại trừ) các hành vi ngoài ý muốn.
- **Tài khoản game:** cao. Dùng bot vi phạm điều khoản dịch vụ của NCSOFT; tài khoản có thể bị khóa.
- **Dữ liệu:** `login.exe` có khả năng gửi tài khoản/mã xác minh tới máy chủ bên thứ ba **(suy luận — chưa xác nhận do đóng gói)**. Nên coi mọi tài khoản đưa vào gói là có thể bị lộ.

## Mục lục

- [02 — Bd.exe, JSBProxy64.dll, login.exe và driver kernel](02-bd-exe-va-driver.md)
- [03 — Hai công cụ điều khiển, thành phần mạng và IOC](03-console-mang-va-ioc.md)
- [04 — Hướng dẫn phòng thủ & bảng IOC tổng hợp](04-phong-thu-va-ioc.md)
