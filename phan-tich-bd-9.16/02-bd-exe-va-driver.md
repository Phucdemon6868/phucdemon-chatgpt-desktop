# Bd.exe, JSBProxy64.dll, login.exe và driver kernel

> **Phạm vi & mục đích.** Đây là báo cáo **phân tích tĩnh** (static analysis — chỉ đọc byte/PE/chuỗi, không chạy file) phục vụ **phòng thủ an ninh**: hiểu các file này *làm gì trên máy*, và *nhận biết / phòng ngừa* chúng ra sao. Báo cáo **không** gỡ gói (unpack), **không** giải ảo hóa protector, **không** tái tạo logic driver/hypervisor, và **không** mô tả cách né anti-cheat hay cách ẩn file. Mọi suy đoán được đánh dấu **(suy luận)**; phần còn lại đã xác minh bằng công cụ (pefile/strings) trên chính các file trong gói.
>
> Nguồn chuẩn: `analysis/FACTS.md`. Các dữ kiện dưới đây đã được kiểm chứng lại trực tiếp bằng `pefile` và `strings` trong phiên phân tích này.

---

## 0. Giải thích nhanh một số thuật ngữ

Giữ nguyên tiếng Anh, giải thích ngắn ở lần dùng đầu:

- **PE (Portable Executable):** định dạng file thực thi của Windows (`.exe`, `.dll`, `.sys`). Gồm nhiều **section** (vùng) như `.text` (mã), `.rdata` (dữ liệu chỉ đọc), `.data`, `.rsrc` (tài nguyên)...
- **IAT (Import Address Table):** bảng các hàm mà file vay mượn từ DLL hệ thống. Đọc IAT thường cho biết nhanh file *định làm gì* (gọi mạng, ghi registry, mở file...).
- **Entropy:** độ "ngẫu nhiên" của byte, thang 0–8. Dữ liệu đã nén/mã hóa cho entropy ≈ 7.8–8.0; mã nguồn bình thường thấp hơn.
- **Protector / packer:** lớp vỏ bọc tự giải nén/giải mã phần thân thật khi chạy. Bản **VM-based** còn dịch mã gốc sang một "máy ảo" (virtual machine) riêng, khiến không đọc được logic nếu chỉ nhìn file tĩnh.
- **Authenticode:** chữ ký số của Microsoft dùng để xác thực nguồn gốc & tính toàn vẹn của file PE. Lưu trong **Security Directory** của PE.
- **Subsystem:** trường trong PE header cho biết file chạy ở đâu — `GUI` (2), `CUI/console` (3), hay `NATIVE` (1 = driver chạy trong nhân Windows).
- **Ring-0:** mức đặc quyền cao nhất của CPU, nơi nhân (kernel) và driver chạy; toàn quyền trên phần cứng & bộ nhớ. Ứng dụng thường chạy **Ring-3** (user-mode).
- **Hook:** chèn mã của mình vào giữa một luồng xử lý của hệ thống để quan sát/can thiệp.
- **EPT (Extended Page Tables) / VT-x:** công nghệ ảo hóa phần cứng của Intel. Một **hypervisor** mỏng có thể dùng EPT để chen xuống *bên dưới* hệ điều hành.
- **PDB (Program Database):** file gỡ lỗi do trình biên dịch sinh ra; đường dẫn PDB thường còn sót trong binary và tiết lộ tên dự án/đường dẫn máy build.

---

## 1. Tổng quan từng file

Gói Bd 9.16 có 3 thành phần "lõi" bị đóng gói nặng: `Bd.exe`, `JSBProxy64.dll`, `bmp/login.exe`. (Hai file `DaZhongKong.exe` / `ZuDuiServer.exe` *không* đóng gói và được phân tích ở báo cáo khác; `libcurl-x64.dll` là thư viện libcurl chuẩn của bên thứ ba, **có** chữ ký số.)

### 1.1 `Bd.exe` — tiến trình bot chính

| Thuộc tính | Giá trị (đã xác minh) |
|---|---|
| Kích thước | 56,904,704 bytes (~54 MB) |
| SHA-256 | `e8eeb19780543f76eec1375f0fd5e35b62b8270d9b96bfedb03883a968062786` |
| Kiến trúc | x64 (Machine `0x8664`) |
| Subsystem | 2 = **GUI** (có cửa sổ) |
| Chữ ký số | **KHÔNG** (Security Directory size = 0) |
| Phiên bản (version resource, đã xác minh bằng pefile) | `FileVersion = ProductVersion = 1.0.0.1`; `OriginalFilename = InternalName = YOLOGraphColor.exe`; `CompanyName / ProductName / LegalCopyright` còn chuỗi giữ chỗ `"TODO: <...>"` ⇒ **resource là stub mẫu còn sót, KHÔNG mang tên sản phẩm thật**. Chuỗi `1.0.0.3 / 1.0.0.4` **không** xuất hiện trong file (ASCII/UTF-16). Nhãn "9.16" khớp **tên gói** "天堂经典版 Bd 9.16"; banner `Ver 9.16(TT)` chỉ xác minh được trong `DaZhongKong.exe`, **không** đọc được tĩnh trong `Bd.exe` |

**Vai trò (suy luận):** đây là chương trình bot chính — GUI điều khiển auto-farm cho Lineage Classic. Bề mặt import cho thấy nó có khả năng: nối mạng (`WINHTTP!WinHttpConnect`, `WS2_32!inet_ntoa`), đọc thông tin card mạng/MAC để định danh máy (`IPHLPAPI!GetAdaptersInfo`) **(suy luận: dùng cho license/định danh thiết bị)**, chạy tiến trình khác (`SHELL32!ShellExecuteExW`), xóa cả cây khóa registry (`ADVAPI32!RegDeleteTreeW`), và thao tác chuỗi kiểu kernel-style (`ntdll!RtlInitUnicodeString`). Điểm quan trọng nhất: **Bd.exe mang theo nhiều driver kernel nhúng** trong phần đọc được của file (xem mục 3).

### 1.2 `JSBProxy64.dll` — thư viện "proxy" của nhà bán

| Thuộc tính | Giá trị (đã xác minh) |
|---|---|
| Kích thước | 23,254,528 bytes (~22 MB) |
| SHA-256 | `42ce658a1e7f6229a60e2bf914c2555cc342086170b03aeb2372bfda892e5c43` |
| Kiến trúc | x64 |
| Subsystem | 3 (DLL — nạp vào tiến trình khác) |
| Chữ ký số | **KHÔNG** |
| Version info | `OriginalFilename = JSBProxy.dll`; Copyright/website **`www.8u18.com`** (trang chủ nhà bán) |

**Vai trò (suy luận):** DLL được nạp để làm lớp "proxy"/trung gian cho bot. Bề mặt import gợi ý chức năng mạng + liệt kê kết nối (`WS2_32!WSAStartup`, `IPHLPAPI!GetExtendedTcpTable` — liệt kê bảng TCP), đọc chứng chỉ (`CRYPT32!CertGetCertificateContextProperty`), và dùng `dbghelp!UnDecorateSymbolName`. Tên `8u18.com` liên kết file này trực tiếp với nhà bán phần mềm bot. Logic thật bị đóng gói che (mục 2).

### 1.3 `bmp/login.exe` — module đăng nhập / xác thực

| Thuộc tính | Giá trị (đã xác minh) |
|---|---|
| Kích thước | 14,888,960 bytes (~14 MB) |
| SHA-256 | `8196fc82e4e084b93ba3e95331bd1ef708293ce435ccfd57cd4678b8adff9130` |
| Kiến trúc | x64 |
| Subsystem | 3 |
| Chữ ký số | **KHÔNG** |

**Vai trò (suy luận):** tiến trình lo việc đăng nhập/kích hoạt. Nó dùng `libcurl-x64.dll` (`curl_easy_getinfo`) để gọi HTTP(S) và `WS2_32!ntohs` cho socket; có `CRYPT32!CertCloseStore` (xử lý chứng chỉ TLS). Trong chuỗi có token `sms` **(suy luận: liên quan tính năng nhận mã SMS / 自动接码 — tự động nhận mã; đây là dấu hiệu yếu, chưa đủ để kết luận luồng SMS)**. URL/endpoint thật bị lớp đóng gói che nên **không** đọc được từ phân tích tĩnh.

---

## 2. Lớp bảo vệ (protector) — vì sao không đọc được logic

Cả ba file lõi đều bị bọc bằng một **protector tùy biến, nhiều khả năng VM-based** (suy luận về "VM-based" dựa trên dấu hiệu dưới đây). Không thấy marker ASCII của VMProtect/Themida/Enigma, nên đây là protector tự chế hoặc ít gặp. **Trong báo cáo này KHÔNG gỡ gói.** Ba dấu hiệu dưới đây giải thích tại sao binary "nhìn thấy nhưng không đọc được":

### 2.1 Các PE section bất thường + section mã bị rỗng trên đĩa

Số liệu `pefile` (đã xác minh):

**`Bd.exe`**

| Section | VirtualSize | SizeOfRawData (trên đĩa) | Entropy | Ghi chú |
|---|---|---|---|---|
| `.text` | `0xC0E68C` | `0x0` | 0.00 | mã gốc **rỗng trên đĩa** — chỉ hình thành khi chạy |
| `.rdata` | `0x10EFCC` | `0x0` | 0.00 | rỗng trên đĩa |
| `.data` | `0x2CD74` | `0x0` | 0.00 | rỗng trên đĩa |
| `.pdata` | `0x4E4B0` | `0x0` | 0.00 | rỗng trên đĩa |
| `.msvcjmc` | `0x2A0D` | `0x0` | 0.00 | rỗng trên đĩa (section MSVC "just-my-code") |
| `.rsrc` | `0x1EF3A0` | `0x1EF400` | 7.30 | tài nguyên (nén) |
| `.sp0` | `0x1000` | `0x0` | 0.00 | tên lạ, rỗng |
| `.4rld` | `0x1000` | `0x0` | 0.00 | tên lạ, rỗng |
| `.1yz2q` | `0x944000` | `0x0` | 0.00 | tên lạ, vsize lớn, rỗng trên đĩa |
| `.8z2wl` | `0x3450000` | `0x344F200` (~55 MB) | **7.85** | khối dữ liệu đóng gói chính |
| `.reloc` | `0x6000` | `0x6000` | 6.48 | relocation |

**`JSBProxy64.dll`**

| Section | VirtualSize | SizeOfRawData | Entropy | Ghi chú |
|---|---|---|---|---|
| `.text`/`.rdata`/`.data`/`.pdata` | lớn | `0x0` | 0.00 | mã/dữ liệu gốc rỗng trên đĩa |
| `.Number0` | `0xEE24A3` | `0x0` | 0.00 | tên lạ, rỗng |
| `.Number1` | `0x120` | `0x200` | 1.10 | nhỏ |
| `.Number2` | `0x162A078` | `0x162A200` (~22 MB) | **7.88** | khối đóng gói chính |

**`login.exe`**

| Section | VirtualSize | SizeOfRawData | Entropy | Ghi chú |
|---|---|---|---|---|
| `.text`/`.rdata`/`.data`/`.pdata` | lớn | `0x0` | 0.00 | mã/dữ liệu gốc rỗng trên đĩa |
| `.?@\` | `0x7B2C3F` | `0x0` | 0.00 | tên phi chuẩn (ký tự lạ), rỗng |
| `.+W,` | `0x1000` | `0x1000` | 0.27 | nhỏ |
| `.y6\` | `0xE317F4` | `0xE31800` (~14 MB) | **7.86** | khối đóng gói chính |

**Ý nghĩa:** section `.text` (nơi chứa mã thật) có `SizeOfRawData = 0` — tức **mã không tồn tại trên đĩa**, chỉ được protector giải nén/dựng vào bộ nhớ lúc chạy. Toàn bộ nội dung thật nằm trong một section entropy ~7.85–7.88 với tên vô nghĩa (`.8z2wl`, `.Number2`, `.y6\`). Entropy sát 8.0 = dữ liệu đã nén/mã hóa, không phải mã đọc trực tiếp được.

### 2.2 IAT bị dựng lại lúc chạy — mỗi DLL chỉ còn 1 import

`pefile` cho thấy bảng import bị **tối giản mạnh** (mức độ khác nhau theo từng file):

- `Bd.exe`: **mỗi DLL đúng 1 hàm** (21/21 DLL — ví dụ `KERNEL32!GetUserDefaultLCID`, `USER32!GetWindowRgn`, `GDI32!SetPolyFillMode`, `WS2_32!inet_ntoa`).
- `JSBProxy64.dll`: 1 hàm/DLL, **trừ** `KERNEL32` có 2 (`GetVersionExA`/`GetVersionExW`).
- `login.exe`: **tối giản ít hơn** — phần lớn DLL vẫn 1 hàm, nhưng còn **một mục `KERNEL32` với 6 hàm** (`HeapAlloc`, `HeapFree`, `ExitProcess`, `LoadLibraryA`, `GetModuleHandleA`, `GetProcAddress` — stub nạp/CRT) cùng bộ UCRT `api-ms-win-crt-*` tương đối đầy đủ (tổng ~28 hàm / 23 mục import). Tức IAT của `login.exe` nhìn "bình thường" hơn hai file kia.

Đây là "import tối giản": với `Bd.exe`/`JSBProxy64.dll`, protector chỉ để lại một hàm mồi để OS nạp đúng DLL, còn **địa chỉ các hàm thật được dựng lại (resolve) động lúc chạy**.

**Hệ quả:** bề mặt import tĩnh **đánh giá thấp** năng lực thật của file. Những hàm nhạy cảm (mạng, registry, tạo tiến trình, nạp driver) có thể được gọi runtime mà không xuất hiện trong IAT. Vì vậy các IOC mạng đọc được (mục dưới) chỉ là phần *lộ ra*; đích kết nối thật có thể bị che thêm.

### 2.3 Hệ quả cho việc phân tích

- Không thể đọc luồng điều khiển/logic từ `.text` (rỗng trên đĩa, dựng runtime, có thể bị VM hóa).
- Không thể liệt kê đầy đủ API/đích mạng từ IAT (đã bị tối giản).
- Chuỗi đọc được chủ yếu đến từ phần tài nguyên và **các PE nhúng chưa bị đóng gói** (đáng chú ý: cụm driver ở mục 3 — đây là nguồn thông tin hành vi giàu nhất còn sót lại).

> **Khẳng định:** báo cáo dừng ở mức *mô tả vỏ bọc*. Không thực hiện unpack, dump bộ nhớ, hay khôi phục IAT.

### 2.4 IOC mạng *lộ ra* (bề mặt, có thể chưa đầy đủ)

| File | Chỉ số | Trạng thái |
|---|---|---|
| `Bd.exe` | IP `49.235.147.185` (dải Tencent Cloud, TQ) | đọc được trong vùng tĩnh; **(chưa xác minh whois)** |
| `Bd.exe` | `127.0.0.1` (loopback) | đọc được |
| `JSBProxy64.dll` | `www.8u18.com` (trang nhà bán) | từ version info |

Các URL `http://...` khác còn sót trong file thuộc **bộ chứng chỉ** (digicert/verisign/microsoft) — **không phải** C2. Không suy ra domain/IP nào ngoài những gì đọc được.

---

## 3. Driver kernel nhúng trong `Bd.exe`

Đây là phần quan trọng nhất về mặt rủi ro. Trong **vùng đọc được** của `Bd.exe` có nhiều file PE nhúng, trong đó có các **driver NATIVE (Ring-0)**. Một blob driver đã được tách ra để xem xét (`analysis/_drv.bin`, 462,848 bytes). **Không tái tạo, không mô tả cách dựng lại — chỉ nêu hành vi, rủi ro và cách nhận biết.**

### 3.1 Kiểm kê các blob nhúng (đã xác minh)

| Loại blob | Số lượng | Subsystem | SizeOfImage | Ghi chú |
|---|---|---|---|---|
| Driver kernel | **4 biến thể** | 1 = **NATIVE** | 3× `0x71000` + 1× `0x6b000` (≈462 KB / ≈428 KB) | 4 lần xuất hiện `MyDriver1.pdb`; 4 timestamp khác nhau (khoảng 2026-04-30 → 2026-07-16) ⇒ nhiều biến thể/phiên bản driver |
| Helper GUI x64 | 1 | GUI | ~`0x19000` | nhỏ |
| Helper GUI x86 | 1 | GUI | ~`0x33000` | nhỏ |

Blob driver tách ra (`_drv.bin`) xác nhận bằng `pefile`:

- Machine `0x8664` (x64), **Subsystem = 1 (NATIVE)** ⇒ driver chạy trong nhân.
- `SizeOfImage = 0x71000` (462,848 bytes).
- Sections bình thường của một driver: `.text` (entropy 6.40 — **mã đọc được, KHÔNG bị đóng gói**), `.rdata`, `.data`, `.pdata`, `INIT`, `.reloc`.
- **Security Directory size = 0 ⇒ driver KHÔNG được ký (unsigned).**

> Ghi chú: ngoài driver, trong `Bd.exe` còn một PDB của lõi user-mode: `...\BdX64\x64\Release\BdX64.pdb` (xuất hiện 1 lần). **(suy luận: đây là PDB của phần lõi Bd trước khi bị bọc protector.)**

### 3.2 Dấu vết build & API kernel (đã xác minh)

- **PDB (đã xác minh từng byte trong file):** `F:\qudong\MyDriver1 - 副本 - 副本\x64\Release\MyDriver1.pdb`. "qudong" = 驱动 = *driver*; "副本" = *bản sao/copy* (thư mục build là bản sao nhân đôi của `MyDriver1`). **Lưu ý quan trọng cho luật phát hiện:** dạng rút gọn `F:\qudong\MyDriver1\x64\...` **KHÔNG tồn tại** trong file — phải dùng đúng chuỗi có "副本", hoặc các mảnh ASCII ổn định `F:\qudong\MyDriver1 - ` và `\x64\Release\MyDriver1.pdb`. Đường dẫn build tay nghiệp dư còn nguyên ⇒ dễ dùng làm luật phát hiện.
- **API kernel được driver dùng:** `IoCreateDevice`, `IoCreateSymbolicLink`, `IoDriverObjectType`, `IoCreateFileSpecifyDeviceObjectHint`, `IoQueryFileDosDeviceName`, `KeInsertQueueApc`, `KeInitializeApc`, `ExGetPreviousMode`, `DbgPrintEx`.

### 3.3 Ba nhóm hành vi (mức hành vi + rủi ro + cách nhận biết)

Dưới đây chỉ nêu *driver làm gì* và *làm sao nhận ra*, **không** nêu chi tiết cài đặt đủ để dựng lại.

#### (a) Hook lớp bàn phím `kbdclass`

- **Hành vi:** driver gắn/hook vào ngăn xếp driver của lớp bàn phím Windows (`kbdclass.sys`) ở tầng thấp. **(suy luận: nhằm bơm thao tác phím vào game và/hoặc đọc đầu vào — phù hợp với một bot auto-farm.)**
- **Chuỗi nhận biết (đã xác minh):** `kbdclass.sys`, `#mymsg no:kbdclass`, `#mymsg kbdclass no %x`, `#mymsg KbdDevice %p: lowest driver = %wZ`, `#mymsg pTargetDeviceObject: %p KbdDriverSize %X`, `#mymsg Failed to chushihuahook driver object: 0x%X` / `ok to chushihuahook driver object` ("chushihua" = 初始化 = *khởi tạo*).
- **Rủi ro:** can thiệp đầu vào ở Ring-0 tác động đến *mọi* ứng dụng, không chỉ game; một bug ở tầng này có thể gây BSOD toàn hệ thống.

#### (b) Hook `NtCreateFile` để ẩn/bảo vệ thư mục

- **Hành vi:** driver chặn (hook) lời gọi mở file ở tầng nhân để **ẩn hoặc bảo vệ** một số đường dẫn/thư mục — khớp tính năng "目录保护" (*bảo vệ thư mục*) mà nhà bán nêu trong `config.ini` **(tên tính năng trích theo FACTS.md)**. Cũng hook `NtCreateSemaphore` / `NtOpenSemaphore`.
- **Chuỗi nhận biết (đã xác minh):** `#mymsg [FakeNtCreateFile] Trying to open: %wZ`, `#mymsg tianjiadaobaohu%lld` ("tianjia...baohu" = 添加...保护 = *thêm bảo vệ*), `NtCreateSemaphore`, `#mymsg OriginalNtCreateSemaphore:%p`, `#mymsg OriginalNtOpenSemaphore:%p`.
- **Rủi ro:** khi file/thư mục bị ẩn ở tầng nhân, công cụ bảo mật user-mode (Explorer, AV quét theo đường dẫn, liệt kê file thông thường) có thể **không thấy** các file đó — gây khó cho điều tra và dọn dẹp. (Không mô tả cơ chế ẩn.)

#### (c) Hypervisor mỏng dùng EPT / VT-x

- **Hành vi:** driver khởi tạo một **hypervisor** cấp-1 mỏng dùng ảo hóa phần cứng Intel (VT-x) với **EPT** và kênh **VMCALL**, tức chen xuống *bên dưới* hệ điều hành — khớp tùy chọn "驱动模式" (*chế độ driver*) `=1/=2/=3` trong `config.ini` **(tên tính năng trích theo FACTS.md)**.
- **Chuỗi nhận biết (đã xác minh):** `Unhandled exception. RIP=hv.sys+%p. Vector=%u.`, `Handling host exception. RIP=hv.sys+%p. Vector=%u`, `Invalid VMCALL key. RIP=%p.`, `Unhandled VMCALL. RIP=%p.`, `EPT USED PAGES: %u / %u.`, `Failed to find EPT hook. PhysAddr = %p.`, `Invalid EPT access combination. PhysAddr = %p.`, `Unhandled EPT Misconfiguration: %p`.
- **Rủi ro:** chạy ở mức đặc quyền cao nhất có thể trên máy; làm cho việc quan sát/kiểm toán từ bên trong HĐH trở nên khó hơn và có thể xung đột với các hypervisor hợp pháp (Hyper-V, VBS, anti-cheat EAC/Vanguard), gây mất ổn định hoặc BSOD.

> **Giới hạn tự áp đặt:** các mục (a)(b)(c) chỉ nêu *mục đích hành vi + cách nhận biết*. Báo cáo **không** trình bày cách móc nối driver, cách tránh phát hiện, hay cách ẩn file.

---

## 4. Rủi ro bảo mật (đánh giá phòng thủ)

1. **Driver chưa ký chạy Ring-0 = toàn quyền máy.** Driver NATIVE không có Authenticode (Security Directory size = 0). Để một driver chưa ký nạp được, máy phải ở chế độ cho phép (test-signing / tắt kiểm tra chữ ký) hoặc driver được nạp qua một con đường bất thường **(suy luận: con đường nạp cụ thể không xác định được từ phân tích tĩnh vì lõi user-mode bị đóng gói)**. Một khi vào nhân, driver có **toàn quyền** đọc/ghi bộ nhớ, file, thiết bị — ngang hoặc trên cả HĐH.
2. **Nguồn gốc không rõ, không ký, build tay.** PDB `F:\qudong\MyDriver1 - 副本 - 副本\...` cho thấy đây là driver tự biên dịch (thư mục build là "bản sao" nhân đôi), không qua quy trình ký của nhà cung cấp uy tín. Không có cách nào xác nhận ai viết, phiên bản nào an toàn.
3. **Không thể kiểm toán vì bị đóng gói.** Lõi `Bd.exe` / `JSBProxy64.dll` / `login.exe` bị protector VM-based che (mục 2). Không thể audit đầy đủ: không rõ nó còn gửi gì ra mạng, thu thập dữ liệu gì (MAC/adapter đã lộ qua `IPHLPAPI`), hay nạp thêm thành phần nào lúc chạy.
4. **Kết hợp ba năng lực = bề mặt rủi ro rất cao.** Hook bàn phím Ring-0 + ẩn file ở tầng nhân + hypervisor EPT nằm chung trong một driver chưa ký là tổ hợp *điển hình của phần mềm xâm nhập sâu*. Dù mục đích tuyên bố là "auto game", năng lực kỹ thuật đủ để làm hại cả hệ thống (mất ổn định, ẩn mã độc khác, lộ dữ liệu). **(suy luận: về năng lực, không phải cáo buộc hành vi cụ thể ngoài những gì chuỗi cho thấy.)**
5. **Rủi ro vận hành kèm theo.** Import `ADVAPI32!RegDeleteTreeW` (xóa cả cây registry) và `SHELL32!ShellExecuteExW` (chạy tiến trình) trên tiến trình chính là năng lực thay đổi hệ thống đáng chú ý **(suy luận về mục đích; chỉ là bề mặt import)**.

**Khuyến nghị phòng thủ ngắn gọn:** coi toàn bộ gói là *không đáng tin*; chỉ phân tích trong VM cách ly, không mạng; nếu đã cài, kiểm tra ở tầng nhân (danh sách driver đã nạp, driver chưa ký) thay vì chỉ quét file user-mode; dùng các dấu hiệu ở mục 5 để viết luật phát hiện.

---

## 5. Bảng "Dấu hiệu nhận biết" (để viết luật phát hiện)

Các chuỗi/giá trị dưới đây **đã xác minh** trong file và phù hợp làm chữ ký (YARA / EDR / hunting). Ưu tiên nhóm driver vì ít thay đổi và rất đặc trưng.

### 5.1 Chuỗi & PDB đặc trưng

| Dấu hiệu (chuỗi/PDB) | Xuất hiện ở | Vì sao đặc trưng |
|---|---|---|
| `F:\qudong\MyDriver1 - 副本 - 副本\x64\Release\MyDriver1.pdb` (có CJK "副本") | driver nhúng / `Bd.exe` | đường dẫn build tay, gần như độc nhất — **dùng đúng chuỗi có "副本", không dùng dạng rút gọn** |
| `\BdX64\x64\Release\BdX64.pdb` | `Bd.exe` | PDB lõi user-mode (suy luận) |
| `#mymsg [FakeNtCreateFile] Trying to open: %wZ` | driver | tiền tố log `#mymsg` + hook file |
| `#mymsg tianjiadaobaohu%lld` | driver | 添加...保护 — bảo vệ/ẩn thư mục |
| `kbdclass.sys` + `#mymsg KbdDevice %p: lowest driver = %wZ` | driver | hook lớp bàn phím |
| `#mymsg pTargetDeviceObject: %p KbdDriverSize %X` | driver | hook bàn phím |
| `chushihuahook driver object` (初始化) | driver | pinyin lẫn trong log — rất đặc trưng |
| `hv.sys+%p. Vector=%u` / `Handling host exception` | driver | hypervisor |
| `Invalid VMCALL key. RIP=%p.` / `Unhandled VMCALL. RIP=%p.` | driver | kênh VMCALL của hypervisor |
| `EPT USED PAGES: %u / %u.` / `Failed to find EPT hook. PhysAddr = %p.` | driver | EPT |
| `Invalid EPT access combination. PhysAddr = %p.` / `Unhandled EPT Misconfiguration: %p` | driver | EPT |
| `www.8u18.com` + `OriginalFilename = JSBProxy.dll` | `JSBProxy64.dll` | liên kết nhà bán |
| `YOLOGraphColor.exe` + `FileVersion 1.0.0.1` + `CompanyName/ProductName = "TODO: <...>"` | version resource của `Bd.exe` | resource là stub mẫu còn sót — bất thường, dễ làm chữ ký |
| `Ver 9.16(TT)` | `DaZhongKong.exe` (**không** thấy trong `Bd.exe`) | nhãn phiên bản (console điều khiển, báo cáo khác) |

### 5.2 Dấu hiệu cấu trúc PE (section tên lạ + section mã rỗng)

| Dấu hiệu cấu trúc | File | Ghi chú phát hiện |
|---|---|---|
| Section tên `.sp0`, `.4rld`, `.1yz2q`, `.8z2wl` | `Bd.exe` | tên phi chuẩn; `.8z2wl` entropy ~7.85 |
| Section tên `.Number0/.Number1/.Number2` | `JSBProxy64.dll` | `.Number2` ~22 MB, entropy ~7.88 |
| Section tên `.?@\`, `.+W,`, `.y6\` (ký tự lạ) | `login.exe` | `.y6\` ~14 MB, entropy ~7.86 |
| `.text` có `SizeOfRawData = 0` | cả 3 file lõi | mã rỗng trên đĩa (dựng runtime) |
| IAT chỉ 1 hàm/DLL (`Bd.exe`: 21/21 DLL; `JSBProxy64.dll`: trừ `KERNEL32` có 2) | `Bd.exe`, `JSBProxy64.dll` | IAT bị tối giản/dựng runtime (`login.exe` tối giản ít hơn: còn mục `KERNEL32` 6 hàm + bộ UCRT `api-ms-win-crt-*`) |
| Security Directory size = 0 (không ký) | cả 3 file lõi + driver nhúng | file không có Authenticode |
| Blob PE **Subsystem = NATIVE** nằm *bên trong* một `.exe` GUI | `Bd.exe` | driver nhúng trong EXE user-mode — rất bất thường |

### 5.3 Dấu hiệu runtime/hành vi (để săn trên endpoint)

| Dấu hiệu | Ý nghĩa phòng thủ |
|---|---|
| Có driver chưa ký với device/symbolic-link do `IoCreateDevice`/`IoCreateSymbolicLink` tạo **(suy luận: tên device cụ thể không trích được tĩnh)** | driver lạ đã nạp vào nhân |
| Máy bật test-signing / tắt kiểm tra chữ ký driver | điều kiện để driver chưa ký chạy (suy luận) |
| File/thư mục của bot không thấy qua liệt kê user-mode nhưng tồn tại khi kiểm ở tầng khác | phù hợp hook ẩn file `NtCreateFile` |
| Xuất hiện hypervisor lạ / xung đột VBS–Hyper–V / anti-cheat báo lỗi EPT | phù hợp hypervisor VT-x của driver |
| `Bd.exe` đọc MAC/adapter (`IPHLPAPI`) rồi kết nối ra ngoài | định danh máy + báo về máy chủ (suy luận) |
| Kết nối tới `49.235.147.185` (Tencent Cloud) **(chưa xác minh whois)** | đích mạng *lộ ra* từ `Bd.exe` |

---

## 6. Tóm tắt một dòng

`Bd.exe` là bot GUI bị bọc protector VM-based, **mang theo một driver kernel chưa ký (NATIVE, Ring-0)** có ba năng lực — hook bàn phím `kbdclass`, ẩn/bảo vệ thư mục qua hook `NtCreateFile`, và hypervisor EPT/VT-x; `JSBProxy64.dll` và `login.exe` cũng bị đóng gói nặng và chưa ký. Logic chi tiết không audit được, nhưng tổ hợp năng lực + việc không ký + nguồn gốc không rõ khiến cả gói là **rủi ro bảo mật cao**; mục 5 cung cấp bộ dấu hiệu để phát hiện.
