# Hướng dẫn phòng thủ & bảng IOC tổng hợp

> Tài liệu này phục vụ **phòng thủ**: nhận biết gói Bd 9.16 trên máy và giảm thiểu rủi ro. Mọi dữ kiện lấy từ phân tích tĩnh (xem [01](01-tom-tat.md), [02](02-bd-exe-va-driver.md), [03](03-console-mang-va-ioc.md)). Không chứa hướng dẫn gỡ gói, giải mã hay né phát hiện.

## 1. Bảng IOC tổng hợp

Cột "Trạng thái": **Đã xác minh** = trích/đọc trực tiếp từ file; **Suy luận**; **Chưa xác minh** = cần công cụ/mạng ngoài để chốt.

### 1.1 Hash file (SHA-256)

| Giá trị | File | Trạng thái |
|---|---|---|
| `e8eeb19780543f76eec1375f0fd5e35b62b8270d9b96bfedb03883a968062786` | `Bd.exe` | Đã xác minh |
| `42ce658a1e7f6229a60e2bf914c2555cc342086170b03aeb2372bfda892e5c43` | `JSBProxy64.dll` | Đã xác minh |
| `8196fc82e4e084b93ba3e95331bd1ef708293ce435ccfd57cd4678b8adff9130` | `login.exe` | Đã xác minh |
| `433a3f9eef9314c4508aec8d15c9572d5992528593293b1e03c7d57e0802ec68` | `大中控.exe` | Đã xác minh |
| `87007457db0917c52fc6b5ca4135451509eb6636200ed5d16411f6589d714bb0` | `组队服务器.exe` | Đã xác minh |
| `0972257268afddf123464b37e844293ffd424f71c3f7893dfb855b5642054238` | `libcurl-x64.dll` (bên thứ ba, có chữ ký) | Đã xác minh |

### 1.2 Mạng

| Loại | Giá trị | Nguồn | Trạng thái |
|---|---|---|---|
| IPv4 | `101.43.73.242` | `大中控.exe` (cạnh `CFileToClient`) | Đã xác minh (có trong file); whois: chưa xác minh |
| IPv4 | `49.235.147.185` | `Bd.exe` (chuỗi) | Đã xác minh (có trong file); whois: chưa xác minh |
| Website | `www.8u18.com` | `JSBProxy64.dll` (version info) | Đã xác minh |
| Cổng TCP | `9527` | `组队服务器\config.ini` (không nằm trong EXE) | Đã xác minh |

> Các URL `*.digicert.com`, `*.verisign.com`, `crl.microsoft.com`, `schemas.microsoft.com` chỉ thuộc **bộ chứng chỉ / manifest**, **không phải** máy chủ điều khiển (C2). Không đưa vào danh sách chặn.

### 1.3 Dấu vết host (chuỗi / artefact đặc trưng)

| Loại | Giá trị | Nguồn | Trạng thái |
|---|---|---|---|
| Đường dẫn PDB | `F:\qudong\MyDriver1 - 副本 - 副本\x64\Release\MyDriver1.pdb` | `Bd.exe` | Đã xác minh |
| Version resource | `OriginalFilename=InternalName=YOLOGraphColor.exe`, `1.0.0.1`, trường công ty/sản phẩm `TODO: <...>` | `Bd.exe` | Đã xác minh |
| Tên PE section lạ | `.1yz2q`, `.8z2wl`, `.4rld`, `.sp0` (Bd.exe); `.Number0/1/2` (JSBProxy); `.?@\`, `.+W,`, `.y6\` (login.exe) | các EXE/DLL | Đã xác minh |
| Chuỗi driver | `kbdclass.sys`, `hv.sys`, `FakeNtCreateFile`, `KbdDevice %p: lowest driver = %wZ`, `EPT USED PAGES` | `Bd.exe` (vùng driver nhúng) | Đã xác minh |
| Banner phiên bản | `Ver 9.16(TT)` | `大中控.exe` (không có trong Bd.exe) | Đã xác minh |

## 2. Cách phát hiện phía phòng thủ (mức khái niệm)

Đây là nguyên tắc nhận biết, không phải mã khai thác.

1. **Kiểm tra chữ ký số.** Toàn bộ EXE/DLL của gói (trừ `libcurl`) đều **không ký**. Trên máy có chính sách chỉ chạy nhị phân đã ký, các file này sẽ nổi bật. Lệnh kiểm tra thủ công trên Windows: `Get-AuthenticodeSignature <file>` (PowerShell).
2. **Giám sát việc nạp driver chưa ký / service lạ.** Driver nhúng chạy ở kernel. Trên hệ thống phòng thủ, theo dõi sự kiện tạo service kernel mới và việc nạp driver không có chữ ký WHQL là chỉ dấu mạnh. Kích hoạt bắt buộc ký driver (DSE, HVCI/Memory Integrity) sẽ chặn nạp driver chưa ký.
3. **So khớp hash/chuỗi.** Dùng bảng IOC mục 1 để quét theo hash, và quét theo các chuỗi đặc trưng ở mục 1.3 (đặc biệt đường dẫn PDB và các tên section).
4. **Giám sát mạng.** Theo dõi/kết hợp cảnh báo khi có kết nối tới các IP ở mục 1.2 (sau khi tự xác minh whois/độ tin cậy).

### Rule YARA mẫu (chỉ để PHÁT HIỆN)

Rule dưới đây so khớp các chuỗi định danh công khai của chính gói, phục vụ phân loại file; không can thiệp hành vi.

```yara
rule Bot_Bd_9_16_Package
{
    meta:
        description = "Nhan dien goi bot 'Bd 9.16' qua chuoi/artefact dac trung (phong thu)"
        reference   = "Phan tich tinh noi bo, 2026-10-08"
        author      = "static-analysis"
    strings:
        $pdb   = "qudong\\MyDriver1" ascii
        $drv1  = "FakeNtCreateFile" ascii
        $drv2  = "KbdDevice" ascii
        $hv    = "hv.sys+" ascii
        $sec1  = ".1yz2q" ascii
        $sec2  = ".8z2wl" ascii
        $stub  = "YOLOGraphColor.exe" ascii wide
        $site  = "www.8u18.com" ascii wide
    condition:
        uint16(0) == 0x5A4D and          // "MZ"
        filesize > 5MB and
        3 of them
}
```

> Rule chỉ dùng chuỗi/hằng số công khai để nhận diện, phù hợp chia sẻ giữa người phòng thủ. Nên bổ sung các hash ở mục 1.1 vào danh sách so khớp riêng của công cụ.

## 3. Khuyến nghị cho người dùng cuối

- Nếu phải chạy gói, chỉ chạy trong **máy ảo riêng/máy dùng một lần**, tách hoàn toàn khỏi dữ liệu cá nhân, ví điện tử, trình duyệt có lưu mật khẩu và tài khoản game khác.
- Hiểu rằng khi driver kernel đã được nạp, **không có cách gỡ bỏ sạch chắc chắn** từ bên trong hệ điều hành đang chạy; cách an toàn là dựng lại máy/VM từ ảnh sạch.
- Coi mọi tài khoản đã đưa vào gói là **có thể bị lộ**; đổi mật khẩu từ một máy sạch khác.
- Rủi ro pháp lý và khóa tài khoản: dùng bot vi phạm điều khoản của NCSOFT.

## 4. Giới hạn của phân tích

- Lõi `Bd.exe` / `JSBProxy64.dll` / `login.exe` **bị đóng gói**, nên hành vi động thật — địa chỉ C2 cuối cùng, dữ liệu thực sự gửi đi, cách driver được nạp — **chưa được xác nhận**. Những mục này trong báo cáo là **(suy luận)**.
- Việc quy thuộc IP cho nhà cung cấp đám mây, và tính hợp lệ của chữ ký `libcurl`, **chưa xác minh** vì phân tích offline.
- Kết luận đầy đủ cần chạy trong **sandbox động** có giám sát kernel và mạng — ngoài phạm vi báo cáo tĩnh này.
