# Hai công cụ điều khiển, thành phần mạng và IOC

> Phân tích tĩnh phục vụ **phòng thủ** (nhận biết + phòng ngừa) gói bot "天堂经典版 Bd" 9.16.
> Tài liệu này chỉ mô tả *các file làm gì trên máy và cách phát hiện chúng*, không hướng dẫn tái tạo.

## 0. Phạm vi và quy ước

Phần này tập trung vào bốn mảnh "biết nói chuyện mạng" của gói: hai console quản trị
`大中控` (DaZhongKong.exe) và `组队服务器` (ZuDuiServer.exe), bộ đăng nhập `login.exe` +
`libcurl-x64.dll`, và DLL tăng tốc mạng `JSBProxy64.dll`. Cuối cùng là bảng tổng hợp
toàn bộ **IOC** (Indicator of Compromise — chỉ số dấu hiệu xâm nhập: IP, domain, cổng,
chuỗi nhận dạng... dùng để phát hiện).

Quy ước:

- **[Đã xác minh]** = đọc trực tiếp được từ file bằng công cụ (pefile đọc bảng import/version, `strings`, so khớp với `FACTS.md`).
- **(suy luận)** = diễn giải hành vi dựa trên dữ kiện, chưa có bằng chứng cứng vì bị đóng gói (packed) hoặc logic nằm trong code đã bị che.
- IP/domain chưa tra cứu whois được ghi rõ **(chưa xác minh whois)** — phân tích này không dùng mạng.
- Hai console `DaZhongKong.exe` và `ZuDuiServer.exe` **không bị đóng gói** (app MFC bình thường), nên import và chuỗi đọc được đầy đủ; `Bd.exe`/`login.exe`/`JSBProxy64.dll` bị protector che nên chỉ thấy bề mặt.

Một số thuật ngữ giữ nguyên tiếng Anh:
- **Import / IAT** (Import Address Table): bảng các hàm hệ thống mà file gọi tới — đọc nó biết file "định làm gì".
- **Client / Server (socket)**: client dùng `connect/send/recv` để gọi ra; server dùng `bind/listen/accept` để chờ kết nối vào.
- **version resource / VERSIONINFO**: khối metadata (tên công ty, mô tả, bản quyền, phiên bản) nhúng trong file PE.
- **PDB path**: đường dẫn file symbol gỡ lỗi mà trình biên dịch nhúng lại — lộ tên project gốc của lập trình viên.

---

## 1. DaZhongKong.exe (大中控) — bảng điều khiển đa máy, đóng vai CLIENT tới nhà bán

### 1.1 Danh tính file [Đã xác minh]

Đọc version resource bằng pefile:

| Trường | Giá trị |
|---|---|
| OriginalFilename / InternalName | `GameServerDrive.exe` |
| FileDescription | `GameServerDrive` |
| CompanyName | `TODO: <CC科技 客户机监视系统>` ("CC科技" = CC Technology; "客户机监视系统" = *hệ thống giám sát máy khách*) |
| ProductName | `TODO: <CC科技>` |
| ProductVersion / FileVersion | `1.0.0.3` / `1.0.0.4` |
| PDB path | `\GameServerDrive\Release\CCMainSer.pdb` ("CCMainSer" = CC Main Server) |

Nhận xét phòng thủ: metadata còn nguyên chuỗi mẫu `TODO: <...>` — tác giả chưa điền tên
công ty thật. Đây là dấu hiệu của phần mềm "xưởng" làm vội, không có pháp nhân rõ ràng,
đồng thời là một đặc trưng nhận dạng tốt (ít phần mềm hợp pháp để lại `TODO:` trong
`CompanyName`). Tên nội bộ **GameServerDrive** và PDB **CCMainSer** cho thấy đây là
"máy chủ điều khiển chính" của bộ công cụ.

### 1.2 Import mạng [Đã xác minh bằng pefile]

`WS2_32.dll` nhập cả hai nhóm hàm:

- Nhóm client: `connect`, `send`, `recv`, `socket`, `inet_pton`, `htons`, `setsockopt`, `closesocket`, `WSAStartup`/`WSACleanup`, `WSAAsyncSelect`.
- Nhóm server: `bind`, `listen`, `accept`.

Ngoài ra nhập `IPHLPAPI.DLL` (thư viện IP Helper — truy vấn cấu hình mạng/adapter).

Lưu ý: `FACTS.md` mô tả DaZhongKong là "CLIENT (connect/send/recv)". Kiểm chứng lại bằng
pefile cho thấy nó nhập **cả** `bind/listen/accept`. Nghĩa là:

- Chắc chắn đóng vai **client** khi gọi ra máy chủ nhà bán (xem 1.3). **[Đã xác minh: có `connect`]**
- Nhiều khả năng còn mở cổng **nghe** để các máy con/bot trong mạng kết nối về nó (đúng với tên "大中控" = *đại trung khống* = trung tâm điều khiển lớn, quản nhiều máy). **(suy luận — có `bind/listen/accept` nhưng chưa thấy cổng cố định trong chuỗi)**

### 1.3 IP cứng và luồng đồng bộ file [Đã xác minh]

Trong vùng `.rdata` đọc được, chuỗi IP **`101.43.73.242`** nằm **ngay cạnh** tên lớp
`CFileToClient` (và tên decorate `.?AVCFileToClient@@`). Cụm chuỗi lân cận gồm các dialog MFC
và tên file dữ liệu:

```
CFileToClient
101.43.73.242
...
%s\Data
%s\Clients.txt
%s\Config.ini
%s\CmdData.txt
%s\ServerText.txt
...
%s\UserBin\%s.bin
```

Các lớp dialog đọc được: `CClientMainDlg`, `CRunCmdCodeDlg` ("chạy mã lệnh"),
`CEditUserDlg`, `CEditBakUserDlg`, `CUserBakInsertDlg`, `CPopUserFishDlg`,
`ComputerNameDlg`, `CDebugPrintDlg`, `CTablePage1..4`.

Diễn giải:

- `CFileToClient` + `101.43.73.242`: lớp phụ trách **gửi/đồng bộ file tới "client"**. Kết hợp với
  việc có `connect`, console này **kết nối ra `101.43.73.242`** để nhận file/lệnh/cập nhật. **[Đã xác minh: IP cứng + có connect]**
- `Clients.txt`: danh sách máy/tài khoản được quản; `CmdData.txt`: dữ liệu lệnh; `ServerText.txt`:
  văn bản/thông báo từ server; `UserBin\*.bin`: dữ liệu nhị phân từng tài khoản.
- Vai trò tổng thể: **nhận lệnh điều khiển, đồng bộ file cấu hình/kịch bản, và kiểm tra giấy phép** từ máy chủ của người bán. **(suy luận về "giấy phép": hợp với mô hình kinh doanh bot thuê bao, nhưng không thấy chuỗi "license/授权/卡密" tường minh trong file)**
- `127.0.0.1` cũng xuất hiện (loopback — giao tiếp nội bộ giữa các tiến trình trên cùng máy). **[Đã xác minh]**

### 1.4 Khóa registry `Policies\...` được tham chiếu [Đã xác minh — cần đọc đúng bối cảnh]

Chuỗi đọc được:

```
Software\Microsoft\Windows\CurrentVersion\Policies\Explorer
Software\Microsoft\Windows\CurrentVersion\Policies\Network
Software\Microsoft\Windows\CurrentVersion\Policies\Comdlg32
```

và kèm theo các *tên giá trị chính sách* chuẩn của Windows: `NoNetConnectDisconnect`,
`NoRecentDocsHistory`, `NoClose`, `NoEntireNetwork`, `NoPlacesBar`, `NoBackButton`, `NoFileMru`.

Đọc đúng bối cảnh: đây là **ba khóa Policies chuẩn của Windows Shell** (hạn chế Explorer/
hộp thoại mở-lưu file/kết nối mạng). Chúng nằm sát chuỗi `...\ATLMFC\Src\MFC\appcore.cpp`,
tức **do khung MFC tham chiếu**, không phải khóa riêng do bot đặt ra. **[Đã xác minh: chuỗi có thật, là khóa Windows chuẩn]** Việc app *đọc* các khóa này để biết Shell đang bị hạn chế gì là
hành vi bình thường của MFC — **(suy luận)** nên không nên dùng riêng chúng làm bằng chứng
độc hại; giá trị phòng thủ của chúng thấp. (Không tìm thấy khóa `Run`/autostart riêng trong chuỗi đọc được.)

### 1.5 Cách nhận biết DaZhongKong.exe

- Tiến trình tên gốc `GameServerDrive.exe` (hoặc đổi tên thành `大中控.exe` / `DaZhongKong.exe`), version `1.0.0.3/1.0.0.4`, `CompanyName` chứa `TODO:`.
- Có **kết nối TCP ra `101.43.73.242`** (xem bảng IOC §6) và/hoặc **mở cổng nghe nội mạng**.
- Sinh các file cạnh nó: `Clients.txt`, `CmdData.txt`, `ServerText.txt`, `Config.ini`, thư mục `Data\`, `UserBin\*.bin`.
- Phòng ngừa: chặn IP ở tường lửa, chặn tiến trình, theo dõi tạo các file dữ liệu trên.

---

## 2. ZuDuiServer.exe (组队服务器) — máy chủ tổ đội LAN, đóng vai SERVER

### 2.1 Danh tính file [Đã xác minh]

| Trường | Giá trị |
|---|---|
| OriginalFilename / InternalName | `NewGameServerMember.exe` |
| FileDescription | `NewGameServerMember` |
| CompanyName / ProductName | `TODO: <公司名>` / `TODO: <产品名>` (placeholder — "tên công ty/sản phẩm") |
| ProductVersion / FileVersion | `1.0.0.1` |
| PDB path | `\NewGameServerMember\Release\NewGameServerMember.pdb` |
| App class | `CNewGameServerMemberApp`, `CNewGameServerMemberDlg`, `CClientMainDlg` |

"组队服务器" = *máy chủ tổ đội*. Metadata cũng còn nguyên `TODO: <公司名>` — cùng dấu hiệu "làm vội" như DaZhongKong.

### 2.2 Import mạng [Đã xác minh bằng pefile]

`WS2_32.dll` nhập: `bind`, `listen`, `accept`, `recv`, `send`, `socket`, `htons`,
`closesocket`, `WSAStartup`, `WSAAsyncSelect`.

Khác biệt then chốt so với DaZhongKong: **KHÔNG nhập `connect`**. Tức file này **chỉ đóng vai
SERVER** — mở cổng, chờ và nhận kết nối vào, không tự gọi ra ngoài. **[Đã xác minh]** Đây là
máy chủ cục bộ cho tính năng "tổ đội" (nhiều nhân vật đi theo nhóm) chạy trong mạng LAN.

### 2.3 Cấu hình và cổng [Đã xác minh một phần]

- Trong file có chuỗi `%s\config.ini` — server **đọc cấu hình từ `config.ini`** đặt cạnh nó. **[Đã xác minh]**
- Cổng lắng nghe **không** nằm cứng trong binary (không thấy chuỗi số cổng); nó được nạp từ `config.ini` lúc chạy.
- Ở bản mẫu đi kèm gói, `config.ini` đặt `port=9527`. **[Đã xác minh — giá trị nằm trong file cấu hình mẫu `组队服务器\config.ini` (`port=9527`, cũng trùng `Game_Config\BaseConfig.txt`), KHÔNG nằm trong EXE và KHÔNG có trong `FACTS.md`]** 9527 là cổng "số đẹp" quen thuộc trong phần mềm tiếng Trung, dễ đổi.

### 2.4 Cách nhận biết ZuDuiServer.exe

- Tiến trình `NewGameServerMember.exe` (hay `组队服务器.exe` / `ZuDuiServer.exe`) ở trạng thái **LISTENING** trên cổng lấy từ `config.ini` (mẫu: **TCP 9527**).
- Có file `config.ini` cạnh nó chứa khóa `port=`.
- Vì chỉ nghe nội mạng, dấu hiệu nằm ở **cổng mở trên máy** chứ không phải lưu lượng ra Internet. Kiểm tra bằng liệt kê cổng đang nghe và đối chiếu tên tiến trình.
- Phòng ngừa: chặn cổng ở tường lửa cục bộ, chặn tiến trình.

---

## 3. login.exe + libcurl-x64.dll — đăng nhập qua HTTP và tính năng nhận mã SMS

### 3.1 login.exe [Đã xác minh bề mặt — file bị đóng gói]

- Loại: **console app** (subsystem CUI), x64, **bị đóng gói** (section entropy cao ~7.86, xem `FACTS.md`). Vì vậy phần lớn chuỗi và URL thật bị che.
- Import bề mặt (mỗi DLL lộ 1 hàm do IAT dựng lúc chạy) [Đã xác minh bằng pefile]:
  - `libcurl-x64.dll` → `curl_easy_getinfo` (dùng thư viện curl để làm HTTP/HTTPS).
  - `WS2_32.dll` → `ntohs` (xử lý byte-order mạng).
  - `CRYPT32.dll` → `CertCloseStore` (thao tác kho chứng chỉ — hợp với TLS).
  - Phần còn lại là CRT/ucrt chuẩn (`MSVCP140`, `VCRUNTIME140`, `api-ms-win-crt-*`).
- Chuỗi đọc được (ít do packing): mảnh `sms`, `curl_easy_getinfo`, `libcurl-x64.dll`, và `59yZm`
  ("yZm"/"yzm" thường là viết tắt *验证码 = mã xác minh*). **[Đã xác minh các mảnh chuỗi này]**

Diễn giải:

- login.exe **dùng libcurl để nói chuyện HTTP/HTTPS** với một dịch vụ bên ngoài. **[Đã xác minh: có import libcurl + CRYPT32]**
- Có liên quan tính năng **nhận mã xác minh qua SMS** (自动接码 — "tự động nhận mã", dịch vụ cho thuê số điện thoại để lấy mã OTP đăng ký/đăng nhập game). **(suy luận — dựa trên mảnh chuỗi `sms`/`yzm`; URL/endpoint thật bị đóng gói che)**
- **Rủi ro an ninh (suy luận):** quy trình này **gửi tên tài khoản/mật khẩu và/hoặc mã OTP ra máy chủ bên thứ ba** (dịch vụ nhận mã). Người dùng không kiểm soát được dữ liệu gửi đi; nguy cơ lộ/đánh cắp thông tin đăng nhập game là có thật. Không trích được endpoint cụ thể nên **không khẳng định đích đến**.

### 3.2 libcurl-x64.dll [Đã xác minh — là thư viện curl hợp pháp]

- Version resource: `ProductName = The curl library`, `CompanyName = The curl library, https://curl.se/`,
  `LegalCopyright = Copyright (C) Daniel Stenberg, <daniel@haxx.se>.`, `OriginalFilename = libcurl.dll`,
  **phiên bản `8.17.0`**. **[Đã xác minh]**
- **Có chữ ký số hợp lệ** (theo `FACTS.md`) — là build curl chính chủ, không phải mã độc.
- Import đặc trưng curl: `WS2_32` (39 hàm), `Secur32` (SChannel/TLS của Windows), `CRYPT32`
  (kho chứng chỉ hệ thống), `WLDAP32` (hỗ trợ giao thức LDAP của curl), `Normaliz` (IDN),
  `bcrypt` (`BCryptGenRandom`). Đây là bề mặt import **bình thường của libcurl**. **[Đã xác minh]**
- Kết luận: libcurl chỉ là *phương tiện* truyền tải. Bản thân nó **không phải IOC độc hại**;
  điều đáng theo dõi là **ai gọi nó và gọi tới đâu** (ở đây là login.exe, đích bị che).

### 3.3 Cách nhận biết

- Tiến trình console `login.exe` nằm trong thư mục `bmp\` cùng `libcurl-x64.dll`.
- Có lưu lượng HTTPS do libcurl phát ra quanh thời điểm đăng nhập/đăng ký tài khoản game.
- Phòng ngừa: không nhập thông tin tài khoản thật vào công cụ này; theo dõi/chặn kết nối ra của `login.exe`; coi mọi tài khoản từng dùng qua nó là **đã lộ** và đổi mật khẩu.

---

## 4. JSBProxy64.dll — "加速宝" trình tăng tốc mạng cấp driver

### 4.1 Danh tính file [Đã xác minh bằng version resource]

| Trường | Giá trị |
|---|---|
| OriginalFilename / InternalName | `JSBProxy.dll` |
| ProductName | `加速宝` (JiaSuBao = *"Gia Tốc Bảo" / Acceleration Treasure*) |
| FileDescription | `加速宝-驱动级网络加速程序!` (*"加速宝 — chương trình tăng tốc mạng cấp driver!"*) |
| CompanyName | `老三工作室` (*"Lão Tam Studio"*) |
| LegalCopyright | `Copyright © www.8u18.com` (website nhà bán) |
| ProductVersion / FileVersion | `5.2.6.6` / `5.3.2.2` |

Suy ra: **JSB = 加速宝 (JiaSuBao)** — tên viết tắt pinyin. "JSBProxy" = *proxy của 加速宝*.

### 4.2 Vai trò thực tế [Đã xác minh — đính chính suy luận cũ]

> **Đính chính so với phỏng đoán ban đầu:** `FACTS.md` ghi "(suy luận: cầu nối đọc/ghi bộ nhớ
> game — 'JSB proxy')". Version resource đọc được **mâu thuẫn** với phỏng đoán đó: file tự
> khai là **"驱动级网络加速程序" — trình tăng tốc *mạng* cấp driver** (dạng VPN/proxy tăng tốc
> kết nối game, không phải cầu đọc/ghi RAM). Ưu tiên dữ kiện đã xác minh này.

Bằng chứng import củng cố vai trò mạng [Đã xác minh bằng pefile]:

- `WS2_32.dll` → `WSAStartup` (khởi tạo socket).
- `IPHLPAPI.DLL` → **`GetExtendedTcpTable`** (liệt kê toàn bộ bảng kết nối TCP của hệ thống kèm PID) — đặc trưng của phần mềm chặn/định tuyến lại lưu lượng để "tăng tốc". **[Đã xác minh]**
- `CRYPT32` → `CertGetCertificateContextProperty`; `VERSION`, `dbghelp`, `SHELL32`/`SHLWAPI` (đọc đường dẫn/kiểm tra file).

Diễn giải vai trò:

- Là một **proxy/accelerator mạng cho game** của hãng thứ ba (老三工作室 / www.8u18.com), được gói kèm để **giảm độ trễ hoặc định tuyến lại kết nối tới máy chủ game**. **(suy luận về mục đích cụ thể "giảm trễ/định tuyến", dựa trên tên + `GetExtendedTcpTable`)**
- "cấp driver" nghĩa là có thành phần chạy ở tầng thấp để can thiệp luồng mạng. **[Đã xác minh: self-description nêu "驱动级"]** Chi tiết cài đặt tầng driver **không** được mô tả ở đây.
- `Bd.exe` có tham chiếu tên `JSBProxy64.dll` trong vùng dữ liệu → Bd nạp/sử dụng DLL này lúc chạy. **(suy luận — thấy tên DLL trong Bd, nhưng vùng quanh nó bị đóng gói)**

### 4.3 Cách nhận biết

- File `JSBProxy64.dll` (tên gốc `JSBProxy.dll`), version `5.2.6.6/5.3.2.2`, `ProductName = 加速宝`, copyright trỏ `www.8u18.com`.
- Dấu hiệu mạng: tra cứu DNS/kết nối tới domain nhà bán `www.8u18.com` (xem §6); có thể có thành phần driver nạp kèm.
- Phòng ngừa: chặn DNS `8u18.com`, theo dõi DLL lạ được `Bd.exe` nạp, và cảnh giác với driver chưa ký (xem tài liệu phân tích driver riêng của gói).

---

## 5. Bề mặt mạng của Bd.exe (bổ sung — file bị đóng gói)

`Bd.exe` bị ảo hóa/đóng gói nên đích thật bị che, nhưng phần đọc được vẫn lộ vài chỉ số mạng:

- **User-Agent giả mạo** [Đã xác minh]: chuỗi HTTP qua WinINet gồm
  `InternetOpenA` / `InternetOpenUrlA` / `InternetReadFile` và header:

  ```
  Accept: */*
  Accept-Language: zh-cn
  Accept-Encoding: no-gzip, deflate
  User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/5.1.1.1000 Chrome/55.0.2883.75 Safari/537.36
  ```

  `Accept-Language: zh-cn` xác nhận đối tượng là thị trường Trung Quốc; User-Agent cố định
  (trình duyệt Maxthon) là **một dấu hiệu nhận dạng lưu lượng** rất hữu ích để phát hiện.
- Import mạng bề mặt (theo `FACTS.md`) [Đã xác minh]: `WINHTTP` (`WinHttpConnect`),
  `WS2_32` (`inet_ntoa`), `IPHLPAPI` (`GetAdaptersInfo` → đọc MAC/adapter để **định danh máy**).
- Chuỗi IP **`49.235.147.185`** nằm trong vùng đọc được của `Bd.exe` nhưng bị bao quanh bởi
  dữ liệu entropy cao (đã đóng gói), nên **không xác định chắc được đây có phải đích kết nối
  đang hoạt động hay không**. **[Đã xác minh: chuỗi IP có thật trong file]** **(suy luận: khả năng là máy chủ nhà bán)**

> **Cảnh báo kết quả dương tính giả:** chuỗi `5.1.1.100` mà tìm kiếm thô bắt được **KHÔNG phải
> địa chỉ IP** — nó là một phần của `Maxthon/5.1.1.1000` trong User-Agent. **Không** đưa vào IOC.

---

## 6. Bảng IOC mạng tổng hợp

### 6.1 IOC cần cảnh giác (đã xác minh có trong file)

| IOC | Loại | Nguồn (file) | Vai trò/diễn giải | Trạng thái |
|---|---|---|---|---|
| `101.43.73.242` | IPv4 | DaZhongKong.exe (cạnh `CFileToClient`) | Máy chủ nhà bán mà console đa máy **connect** ra để nhận lệnh/đồng bộ file | Chuỗi **đã xác minh**; nghi thuộc dải Tencent Cloud (TQ) — **(chưa xác minh whois)** |
| `49.235.147.185` | IPv4 | Bd.exe (vùng đã đóng gói) | Khả năng máy chủ nhà bán của bot chính | Chuỗi **đã xác minh**; vai trò **(suy luận)**; nghi Tencent Cloud — **(chưa xác minh whois)** |
| `www.8u18.com` | Domain | JSBProxy64.dll (LegalCopyright) | Website nhà bán trình tăng tốc `加速宝` | Chuỗi **đã xác minh**; **(chưa xác minh whois/DNS)** |
| `127.0.0.1` | IPv4 (loopback) | DaZhongKong.exe, Bd.exe | Giao tiếp nội bộ giữa các tiến trình trên cùng máy | **Đã xác minh**; bản thân không độc hại (lành tính) |
| TCP `9527` | Cổng nghe | ZuDuiServer.exe → `config.ini` (bản mẫu) | Cổng máy chủ tổ đội LAN; lấy từ `config.ini`, dễ đổi | **Đã xác minh theo file cấu hình mẫu** (không nằm cứng trong EXE) |
| `Mozilla/5.0 ... Maxthon/5.1.1.1000 Chrome/55.0.2883.75 Safari/537.36` | Chuỗi User-Agent | Bd.exe (WinINet) | UA cố định dùng cho HTTP của bot → dấu hiệu nhận dạng lưu lượng | **Đã xác minh** |
| `Accept-Language: zh-cn` | Header HTTP | Bd.exe | Xác nhận đối tượng thị trường TQ | **Đã xác minh** |

### 6.2 IOC phụ trợ ở tầng file/tiến trình (để đối chiếu)

| Chỉ số | Nguồn | Ý nghĩa |
|---|---|---|
| `GameServerDrive.exe` / PDB `CCMainSer.pdb` | DaZhongKong.exe | Tên gốc + project của console đa máy |
| `NewGameServerMember.exe` / PDB `NewGameServerMember.pdb` | ZuDuiServer.exe | Tên gốc + project của server tổ đội |
| `JSBProxy.dll`, ProductName `加速宝`, ver `5.2.6.6/5.3.2.2` | JSBProxy64.dll | Nhận dạng DLL tăng tốc mạng |
| `CompanyName = TODO: <...>` | cả hai console | Metadata placeholder — đặc trưng "xưởng" làm vội |
| `Clients.txt`, `CmdData.txt`, `ServerText.txt`, `Config.ini`, `Data\`, `UserBin\*.bin` | DaZhongKong.exe | Các file dữ liệu sinh ra cạnh console |
| Mảnh chuỗi `sms`, `yzm`/`59yZm` | login.exe | Dấu hiệu tính năng nhận mã SMS |

### 6.3 KHÔNG phải C2 — các URL chứng chỉ/khung chuẩn (loại trừ)

Các URL `http(s)` còn lại trong file **chỉ là của hạ tầng chứng chỉ và khung chuẩn**, xuất hiện
do thư viện/chứng chỉ đi kèm, **không phải địa chỉ điều khiển (C2)**:

| URL/host | Xuất hiện ở | Bản chất |
|---|---|---|
| `*.digicert.com` (`cacerts`, `crl3`, `ocsp`) | Bd.exe | CRL/OCSP của CA DigiCert (kiểm tra chứng chỉ) |
| `*.verisign.com` (`crl`, `ocsp`, `csc3-2010-*`, `logo`, `www`) | Bd.exe | Hạ tầng chứng chỉ VeriSign |
| `crl.microsoft.com` | **chỉ** Bd.exe | CRL của Microsoft (kiểm tra thu hồi chứng chỉ) |
| `schemas.microsoft.com` | Bd.exe + DaZhongKong.exe + ZuDuiServer.exe + JSBProxy64.dll | Namespace XML trong manifest PE (không thấy ở `login.exe` do bị đóng gói) |
| `www.winimage.com` | Bd.exe | Chuỗi bản quyền của thư viện nén zlib/minizip (WinImage) |
| `https://curl.se/`, `daniel@haxx.se` | libcurl-x64.dll | Thông tin dự án curl hợp pháp |

> Lưu ý quan trọng: `FACTS.md` nêu các chuỗi chứng chỉ VeriSign/DigiCert thấy trong file
> **chỉ là dữ liệu đi kèm**, và các file chính (Bd/JSBProxy/login/hai console) **đều KHÔNG được
> ký số hợp lệ** (chỉ `libcurl-x64.dll` có chữ ký của bên thứ ba). Sự hiện diện của tên CA
> **không** đồng nghĩa file được ký.

---

## 7. Tóm tắt phòng thủ (tầng mạng)

Nhận biết nhanh một máy nhiễm/chạy gói này ở tầng mạng:

1. **Kết nối ra** tới `101.43.73.242` (từ console `GameServerDrive/大中控`) và/hoặc `49.235.147.185` (từ `Bd.exe`). → Chặn ở tường lửa biên; cảnh báo khi thấy.
2. **Tra cứu DNS** tới `8u18.com` (trình tăng tốc `加速宝`). → Chặn DNS.
3. **HTTP với User-Agent `Maxthon/5.1.1.1000 ...` và `Accept-Language: zh-cn`** không khớp trình duyệt thực của máy. → Luật IDS/proxy theo User-Agent.
4. **Cổng nội mạng đang LISTENING** khớp `config.ini` của `ZuDuiServer` (mẫu TCP `9527`), tiến trình `NewGameServerMember.exe`. → Chặn cổng, chặn tiến trình.
5. **Lưu lượng HTTPS từ `login.exe`** quanh lúc đăng nhập → coi tài khoản liên quan là đã lộ.

Lưu ý giới hạn: `Bd.exe`, `login.exe`, `JSBProxy64.dll` bị đóng gói nên **đích kết nối thật có
thể còn bị che và sinh thêm lúc chạy**; hai IP trên là những gì đọc tĩnh được, chưa phải danh
sách đầy đủ. Mọi phán đoán về whois/chủ sở hữu IP cần tự xác minh (phân tích này không dùng mạng).
