# Cấu hình chung và cấu trúc gói

Bản dịch tiếng Việt kèm giải thích cho **các file cấu hình chung** của gói bot **天堂经典版 Bd 9.16** (bot treo máy – auto farm – cho game *Lineage Classic* của NCSOFT, chạy qua launcher Purple, trong file gọi là `紫P`). Phần đầu giải thích **cấu trúc gói**: mỗi file, mỗi thư mục là gì và có cần sửa không.

| File gốc | Tên hiển thị trên ổ đĩa (tên có thể bị mã hóa) | Số dòng | Mã hóa ký tự |
|---|---|---|---|
| `config/config.ini` | `config/config.ini` | 32 | UTF-8 |
| `config/ZKT.ini` | `config/ZKT.ini` | 4 | UTF-8 |
| `config/ServerText.txt` | `config/ServerText.txt` | 35 | UTF-8 |
| `大中控/Data/ServerText.txt` | `#U5927#U4e2d#U63a7/Data/ServerText.txt` | 35 (giống hệt file ở trên) | UTF-8 |
| `大中控/Data/Config.ini` | `#U5927#U4e2d#U63a7/Data/Config.ini` | 2 | **GBK** |
| `组队服务器/config.ini` | `#U7ec4#U961f#U670d#U52a1#U5668/config.ini` | 2 | ASCII |
| `Account.txt` | `Account.txt` | 2 | UTF-8 |
| `ip.txt`, `key.txt` | `ip.txt`, `key.txt` | 0 (file rỗng) | — |

> **Ký hiệu trong tài liệu:** chữ trong ô `code` là **chữ gốc**, phải giữ nguyên khi chép vào file cấu hình. "(?)" nghĩa là bản dịch chưa chắc chắn 100%. "(suy đoán)" hoặc "(suy luận)" nghĩa là thông tin được suy ra từ tên file hoặc ngữ cảnh, tài liệu gốc không nói rõ.
>
> Các phần khác của bộ hướng dẫn: `01-huong-dan-su-dung.md` (dịch `使用说明.txt`), `02-nhat-ky-cap-nhat.md` (dịch `更新说明.txt`), các file 04–06 (dịch thư mục `Game_Config`).

**Mục lục**

- Quy tắc chung khi sửa cấu hình (đọc trước)
- 1. Cấu trúc gói
  - 1.1 Cây thư mục
  - 1.2 Bảng giải thích từng file và thư mục
  - 1.3 Thư mục `lua/`: 32 file logic đã mã hóa
  - 1.4 Các chương trình kết nối với nhau thế nào
- 2. `config/config.ini`: cấu hình chính của bảng điều khiển
- 3. `config/ZKT.ini`: kết nối tới trung tâm điều khiển `大中控`
- 4. `config/ServerText.txt`: danh sách server
- 5. `大中控/Data/Config.ini`: cấu hình trung tâm điều khiển
- 6. `组队服务器/config.ini`: cấu hình server tổ đội
- 7. `Account.txt`: danh sách tài khoản
- 8. `ip.txt` và `key.txt`
- 9. Checklist cài đặt lần đầu
- 10. Thuật ngữ dùng trong file này

---

## Quy tắc chung khi sửa cấu hình (đọc trước)

1. **Bot đọc chữ Trung theo đúng từng ký tự.** Giữ nguyên tên mục trong ngoặc vuông `[...]`, tên khóa (phần bên trái dấu `=`), tên server, tên bản đồ, vật phẩm và NPC. **Chỉ thay số hoặc giá trị** ở bên phải dấu `=`.
2. **Không đổi chữ phồn thể ↔ giản thể.** Gói dùng lẫn cả hai kiểu chữ: tên server như `太陽神阿波羅` là phồn thể, còn tên khóa như `登录器路径` là giản thể. Cũng **không "sửa lỗi chính tả"** trong tên khóa. Ví dụ khóa `每次登陆前先关闭紫p` viết `登陆` (không phải `登录`) và chữ `p` thường; phải giữ y nguyên.
3. **Dùng dấu ASCII:** dấu bằng `=` và dấu phẩy `,` thường. Không dùng dấu phẩy kiểu Trung `，` hoặc dấu bằng full-width `＝`.
4. **Giữ nguyên mã hóa ký tự khi lưu file.** Hầu hết các file là UTF-8; riêng `大中控/Data/Config.ini` là **GBK**. Nên dùng Notepad++, phần mềm này hiện mã hóa của file ở góc dưới bên phải.
5. 💡 Sao lưu (copy) file trước khi sửa. Nên đóng bảng điều khiển của bot trước khi sửa, rồi mở lại để bot đọc cấu hình mới (lời khuyên chung).

---

## 1. Cấu trúc gói

### 1.1 Cây thư mục

Một số công cụ giải nén trên máy không dùng tiếng Trung hiển thị tên file tiếng Trung thành dạng `#U` + mã Unicode. Tên gốc và tên bị mã hóa tương ứng như sau:

| Tên gốc | Tên bị mã hóa | Nghĩa |
|---|---|---|
| `使用说明.txt` | `#U4f7f#U7528#U8bf4#U660e.txt` | Hướng dẫn sử dụng |
| `更新说明.txt` | `#U66f4#U65b0#U8bf4#U660e.txt` | Ghi chú cập nhật |
| `大中控` | `#U5927#U4e2d#U63a7` | Trung tâm điều khiển lớn |
| `组队服务器` | `#U7ec4#U961f#U670d#U52a1#U5668` | Server tổ đội |

```text
天堂经典版 Bd 9.16/
├── Bd.exe                     chương trình bot chính (bảng điều khiển)
├── tmp68A9.tmp                bản sao tạm còn sót lại (không cần)
├── JSBProxy64.dll             thư viện native do bot nạp
├── Account.txt                danh sách tài khoản
├── ip.txt                     (rỗng)
├── key.txt                    (rỗng)
├── 使用说明.txt               hướng dẫn sử dụng      → xem 01-huong-dan-su-dung.md
├── 更新说明.txt               ghi chú cập nhật       → xem 02-nhat-ky-cap-nhat.md
├── config/                    cấu hình bảng điều khiển / launcher (file này)
│   ├── config.ini
│   ├── ZKT.ini
│   └── ServerText.txt
├── Game_Config/               cấu hình lối chơi (19 file .txt) → xem file 04–06
├── bmp/                       ảnh mẫu nhận dạng launcher (10 .bmp) + login.exe + libcurl-x64.dll
├── lua/                       logic của bot (32 file .lua, đã mã hóa)
├── 大中控/                    trung tâm điều khiển lớn
│   ├── 大中控.exe
│   └── Data/
│       ├── Config.ini
│       └── ServerText.txt
└── 组队服务器/                server tổ đội trong mạng LAN
    ├── 组队服务器.exe
    ├── config.ini
    └── 使用说明.txt
```

> Lưu ý: các file chương trình (`.exe`, `.dll`, `.tmp`) **không được mở hay chạy** khi làm tài liệu này. Thông tin về chúng lấy từ danh sách file của gói (tên, kích thước) và từ ghi chú cập nhật. Bản sao dùng để dịch chỉ có các file chữ, ảnh `.bmp` và file `.lua`.

### 1.2 Bảng giải thích từng file và thư mục

#### Thư mục gốc

| Đường dẫn | Là gì | Có cần sửa không |
|---|---|---|
| `Bd.exe` | **Chương trình bot chính**, tức bảng điều khiển (`控制台`) (khoảng 56,9 MB). File được đóng gói bằng phần mềm bảo vệ (packer/protector) và **cần chạy bằng quyền Administrator**. Bên trong có nhúng một driver kernel của Windows (nhìn thấy qua chuỗi ký tự trong file). | **Không sửa.** Khi cập nhật thì thay bằng EXE mới (ghi chú cập nhật hay ghi `需要替换EXE` = "cần thay EXE"). |
| `tmp68A9.tmp` | File có cùng kích thước với `Bd.exe` nhưng bị hỏng trong file nén. Có vẻ là bản sao tạm còn sót lại. | **Không cần.** Bỏ qua hoặc xóa được. |
| `JSBProxy64.dll` | Thư viện native (khoảng 23 MB) do bot nạp vào. Gói không ghi rõ công dụng. Ghi chú cập nhật bản 8.8 có câu `恢复单进程ip代理加速（控制台右键单击 导入ip 目录需要JSBProxy64.dll文件）`, nghĩa là "khôi phục tăng tốc bằng proxy IP cho từng tiến trình (nhấp chuột phải trên bảng điều khiển → `导入ip` = nhập IP; thư mục cần có file JSBProxy64.dll)". Vì vậy nhiều khả năng file này dùng cho tính năng proxy IP (suy đoán). | **Không sửa, không xóa.** |
| `Account.txt` | Danh sách tài khoản game để bot đăng nhập (xem mục 7). | **Có**: điền tài khoản của bạn. |
| `ip.txt` | File rỗng. Có lẽ là danh sách IP proxy cho chức năng `导入ip` (nhập IP) (suy đoán). | Chỉ cần khi dùng proxy (suy đoán). |
| `key.txt` | File rỗng. Có lẽ là nơi lưu mã kích hoạt hoặc bản quyền (key) của bot (suy đoán từ tên file). | Thường không sửa tay. Nếu file có nội dung thì đừng chia sẻ cho người khác. |
| `使用说明.txt` | Hướng dẫn sử dụng do tác giả viết. Bản dịch nằm ở `01-huong-dan-su-dung.md`. | Không: chỉ để đọc. |
| `更新说明.txt` | Nhật ký các bản cập nhật. Bản dịch nằm ở `02-nhat-ky-cap-nhat.md`. | Không: chỉ để đọc. |

#### Thư mục `config/` (cấu hình bảng điều khiển, được dịch trong file này)

| Đường dẫn | Là gì | Có cần sửa không |
|---|---|---|
| `config/` | Cấu hình của bảng điều khiển và launcher. | Xem từng file. |
| `config/config.ini` | Cấu hình chính: đường dẫn launcher Purple, cách đăng nhập, số cửa sổ game, bố cục cửa sổ, chế độ điều khiển game… (mục 2). | **Có**: ít nhất phải kiểm tra `登录器路径`. |
| `config/ZKT.ini` | Địa chỉ và cổng để kết nối tới trung tâm điều khiển `大中控`, cùng tên máy hiển thị (mục 3). | Chỉ khi dùng `大中控`. |
| `config/ServerText.txt` | Danh sách server (`大区`) để chọn trên bảng điều khiển (mục 4). | Thường không. Chỉ thay khi ghi chú cập nhật báo có server mới. |

#### Thư mục `Game_Config/` (cấu hình lối chơi, chi tiết ở file 04–06)

| Đường dẫn | Là gì | Có cần sửa không |
|---|---|---|
| `Game_Config/` | Toàn bộ cấu hình lối chơi. | **Có**: đây là nơi chỉnh cách bot chơi. |
| `Game_Config/BaseConfig.txt` | Cấu hình chính của lối chơi: đăng nhập, bảo vệ nhân vật, treo máy, dịch chuyển ngẫu nhiên, về thành nghỉ, kỹ năng, uống thuốc, phản công, tổ đội, tổ đội LAN… | **Có.** |
| `Game_Config/gj.txt` | Cấu hình điểm treo máy (`挂机`, viết tắt là gj): bản đồ, tọa độ, lọc quái, quái cần phản công, lọc nhặt đồ… | **Có.** |
| `Game_Config/G_Filtering_Monster_And_Item.txt` | Lọc quái, phản công quái và lọc nhặt đồ **dùng chung cho mọi điểm treo**. Khi bật thì thay thế các mục tương ứng trong `gj.txt`. | Tùy nhu cầu. |
| `Game_Config/ActivityConfig.txt` | Sự kiện trong game, ví dụ `[冰之女王活动]` (sự kiện Nữ hoàng Băng). | Tùy nhu cầu. |
| `Game_Config/Buff.txt` | Nhân vật chuyên buff (ví dụ Hoàng tộc hoặc Hiệp sĩ đội mũ nhanh nhẹn buff cho Elf) và danh sách tài khoản phụ nhận buff. | Tùy nhu cầu. |
| `Game_Config/CounterattackPeoples.txt` | Danh sách người chơi cần phản công hoặc chủ động tấn công (PvP), cùng danh sách trắng. | Tùy nhu cầu. |
| `Game_Config/BloodConfig.txt` | Huyết minh (`血盟`, tức clan): tự xin vào clan, gửi vàng và đồ vào kho clan. | Tùy nhu cầu. |
| `Game_Config/BloodStorage.txt` | Vật phẩm cần gửi vào kho huyết minh. | Tùy nhu cầu. |
| `Game_Config/BloodTakeOutTheItem.txt` | Tự lấy vật phẩm từ kho huyết minh khi thiếu. | Tùy nhu cầu. |
| `Game_Config/PersonageStorage.txt` | Vật phẩm gửi vào kho cá nhân khi về thành vì túi đầy trọng lượng. | Tùy nhu cầu. |
| `Game_Config/PersonageTakeOutTheItem.txt` | Tự lấy vật phẩm từ kho cá nhân khi thiếu. | Tùy nhu cầu. |
| `Game_Config/SellBuy.txt` | Mua và bán ở NPC theo từng làng (ví dụ mua tên, mua thuốc). | Tùy nhu cầu. |
| `Game_Config/SellList.txt` | Bán vật phẩm chỉ định cho thương nhân chỉ định. | Tùy nhu cầu. |
| `Game_Config/saveitem.txt` | Vật phẩm giữ lại, không bán. | Tùy nhu cầu. |
| `Game_Config/Deleteitem.txt` | Vật phẩm cần xóa (vứt bỏ). | Tùy nhu cầu. |
| `Game_Config/TradedConfig.txt` | Giao dịch chuyển hàng (`倒货`) sang nhân vật nhận hàng khi đạt mức vàng hoặc nguyên liệu. | Tùy nhu cầu. |
| `Game_Config/Tradeditems.txt` | Vật phẩm đem giao dịch và số lượng kích hoạt giao dịch. | Tùy nhu cầu. |
| `Game_Config/TreasureName.txt` | Tên bảo vật (`宝物`): có trong túi thì số lượng hiện lên bảng điều khiển (thêm ở bản 9.16). | Tùy nhu cầu. |
| `Game_Config/UseItems.txt` | Dùng vật phẩm định kỳ, ví dụ mở `神秘方塊` mỗi N phút. | Tùy nhu cầu. |

#### Thư mục `bmp/` (ảnh mẫu nhận dạng)

Các file `.bmp` là **ảnh mẫu nhỏ**. Bot dùng chúng để nhận ra nút bấm và màn hình của launcher Purple cũng như màn hình đăng nhập bằng mã QR. Ý nghĩa từng tên file chỉ là suy đoán.

| Đường dẫn | Là gì | Có cần sửa không |
|---|---|---|
| `bmp/` | Thư mục ảnh mẫu và công cụ đăng nhập. | **Không sửa ảnh.** Chỉ chép đè ảnh mới khi ghi chú cập nhật yêu cầu. |
| `bmp/IDLogin_qr.bmp` | Mẫu nhận dạng màn hình đăng nhập bằng mã QR (`IDLogin_qr`). | Không. |
| `bmp/launcher_CL.bmp` | Mẫu một nút hoặc màn hình của launcher. Chữ "CL" chưa rõ nghĩa (?). | Không. |
| `bmp/launcher_min_main.bmp` | Mẫu màn hình chính của launcher khi thu nhỏ ("min main") (suy đoán). | Không. |
| `bmp/launcher_TTGame.bmp` | Mẫu mục game trong launcher. "TT" có lẽ là 天堂 (Tiāntáng = Lineage) (?). | Không. |
| `bmp/launcher_TTGame2.bmp` | Biến thể thứ 2 của mẫu trên. | Không. |
| `bmp/launcher_TTGame_max.bmp` | Mẫu mục game khi launcher phóng to ("max") (suy đoán). | Không. |
| `bmp/launcher_TTGame_max_new.bmp` | Mẫu mới của ảnh trên. Các bản cập nhật 8.31.1 → 9.2 yêu cầu thay file này để sửa lỗi đăng nhập launcher Purple. | Chỉ thay khi có bản mới. |
| `bmp/launcher_TTGame_max_new2.bmp` | Như trên (bản 2). Được yêu cầu thay ở các bản 8.31.2 → 9.2. | Chỉ thay khi có bản mới. |
| `bmp/launcher_TTGame_max_new3.bmp` | Như trên (bản 3). Được yêu cầu thay ở các bản 9.1.1 và 9.2. | Chỉ thay khi có bản mới. |
| `bmp/launcher_TY.bmp` | Mẫu một nút của launcher. "TY" có lẽ là 同意 (tóngyì = "đồng ý"), tức nút đồng ý điều khoản (?). Bản 9.10.1 có thêm tính năng `紫P会自动点同意，勾选用户协议` ("launcher Purple sẽ tự bấm Đồng ý, tích chọn thỏa thuận người dùng"), khớp với suy đoán này. | Không. |
| `bmp/login.exe` | Chương trình phụ trợ đăng nhập (khoảng 14,9 MB). | Không. |
| `bmp/libcurl-x64.dll` | Thư viện HTTP tiêu chuẩn (libcurl). | Không. |

#### Thư mục `lua/`

| Đường dẫn | Là gì | Có cần sửa không |
|---|---|---|
| `lua/` | 32 file `.lua` chứa **logic của bot**. Các file này đã bị **mã hóa hoặc làm rối**, không đọc được (danh sách ở mục 1.3). | **Không sửa.** Khi cập nhật thì chép đè toàn bộ thư mục (ghi chú cập nhật hay ghi `需要替换lua` = "cần thay lua"). |

#### Thư mục `大中控/` (trung tâm điều khiển lớn)

| Đường dẫn | Là gì | Có cần sửa không |
|---|---|---|
| `大中控/` | Trung tâm điều khiển lớn, dùng để **quản lý nhiều máy và nhiều tài khoản** cùng lúc. | — |
| `大中控/大中控.exe` | Chương trình trung tâm điều khiển. Bảng điều khiển `Bd.exe` trên các máy kết nối vào chương trình này. Theo ghi chú cập nhật, nó dùng để: hiện bảo vật, sửa tài khoản, đổi tên máy hiển thị, phân phối tài khoản phụ đến nhận buff… | **Không sửa.** `大中控` có số phiên bản riêng (hiện là 9.16); thay khi ghi chú cập nhật yêu cầu. |
| `大中控/Data/` | Dữ liệu và cấu hình của `大中控`. | Xem từng file. |
| `大中控/Data/Config.ini` | Cổng (port) mà `大中控` mở để nhận kết nối (mục 5). | Chỉ khi muốn đổi cổng. |
| `大中控/Data/ServerText.txt` | Danh sách server, **giống hệt** `config/ServerText.txt` (mục 4). | Nếu có server mới thì nên thay cùng lúc với `config/ServerText.txt` (suy luận). |

#### Thư mục `组队服务器/` (server tổ đội)

| Đường dẫn | Là gì | Có cần sửa không |
|---|---|---|
| `组队服务器/` | Server tổ đội: giúp nhiều máy chạy bot tự lập tổ đội với nhau qua mạng LAN. | — |
| `组队服务器/组队服务器.exe` | Chương trình server tổ đội trong mạng LAN. | Không sửa. |
| `组队服务器/config.ini` | Cổng của server tổ đội (mục 6). | Chỉ khi muốn đổi cổng. |
| `组队服务器/使用说明.txt` | Hướng dẫn 3 dòng cho server tổ đội. Bản dịch ở `01-huong-dan-su-dung.md`, Phần B; tóm tắt ở mục 6 của file này. | Không: chỉ để đọc. |

### 1.3 Thư mục `lua/`: 32 file logic đã mã hóa

> ⚠️ Các file này đã bị mã hóa nên **không đọc được nội dung**. Vai trò dưới đây chỉ là **(suy đoán từ tên file)**, có tham khảo thêm từ khóa trong ghi chú cập nhật `更新说明.txt`. Bạn không cần và không nên sửa các file này.
>
> Ghi chú: thư mục thực tế có **32** file `.lua` (đã đếm lại).

| File | Vai trò (suy đoán từ tên file) | Gợi ý liên quan trong ghi chú cập nhật |
|---|---|---|
| `A_Strat.lua` | Có lẽ là "A_Start" bị viết sai: file khởi động (điểm vào) của script. Tiền tố `A_` làm nó đứng đầu danh sách (?). | — |
| `ActivityExchange.lua` | Đổi thưởng sự kiện (Activity = sự kiện, Exchange = đổi). | Có thể liên quan `ActivityConfig.txt` (?). |
| `ActivityIceQueen.lua` | Sự kiện Nữ hoàng Băng (Ice Queen). | Bản 8.31.1 thêm `冰之女王活动` (sự kiện Nữ hoàng Băng) vào `ActivityConfig.txt`. |
| `AddBuff.lua` | Buff: tự buff, buff cho đồng đội, buff từ nhân vật chuyên buff. | Bản 8.20 (`为队员放技能`, buff kỹ năng chỉ định cho đồng đội) và 8.20.1 (sửa lỗi `为队员放加速术`, buff Haste cho đồng đội), 8.4 (buff cho tài khoản phụ), 8.2 (buff ở nhà trọ); file `Buff.txt`. |
| `AttackFunction.lua` | Các hàm tấn công dùng chung. | Bản 8.6 và 7.29.1 (sửa lỗi phản công `反击`) (?). |
| `AttackMonster.lua` | Logic đánh quái chính. Đây là file lớn (khoảng 114 KB). | Bản 9.16 (`定点打怪`, đánh quái tại điểm cố định), 7.3 (`定点挂机`, treo máy tại điểm cố định), 9.13 (đứng im, bắn tên xuyên cây), 7.1.1. |
| `BaseFuction.lua` | Các hàm cơ bản. Tên gốc viết sai "Fuction" (đúng là Function); giữ nguyên tên file. | — |
| `check_code.lua` | "Kiểm tra mã": không rõ là mã gì (?). | — |
| `GPS.lua` | Định vị: biết nhân vật đang ở bản đồ nào, tọa độ nào (?). | — |
| `G_Config_Core.lua` | Phần lõi đọc các file cấu hình (`Game_Config/*.txt`) (?). | — |
| `G_Config_Schemas.lua` | "Lược đồ" cấu hình: danh sách khóa hợp lệ và giá trị mặc định (?). | — |
| `G_Define.lua` | Định nghĩa toàn cục: hằng số, danh sách bản đồ, vật phẩm, NPC (?). Đây là file lớn nhất (khoảng 136 KB). | — |
| `ItemUseManager.lua` | Quản lý việc dùng vật phẩm: thuốc, cuộn biến hình, cuộn về thành… | Bản 9.9 và 9.9.1 (lỗi không dùng cuộn biến hình `变身卷轴`); file `UseItems.txt`. |
| `LocalTeam.lua` | Tổ đội trong mạng LAN, kết nối tới `组队服务器`. | Bản 9.13 (hồi máu cho đồng đội theo %), 7.29.1, 7.22, 7.15.1. |
| `Login.lua` | Đăng nhập: launcher Purple, chọn server, vào nhân vật. | Bản 9.9 (đổi logic đăng nhập, bắt buộc thay lua), 9.10.1 (tự đồng ý điều khoản, cộng điểm khi tạo nhân vật). |
| `Move.lua` | Di chuyển nhân vật. | — |
| `MultiGJ.lua` | Treo máy nhiều điểm hoặc nhiều bản đồ (GJ = `挂机`, treo máy) (?). | Có thể liên quan `gj.txt` và mục `[按时间切换挂机配置]` (đổi điểm treo theo thời gian) (?). |
| `NewGps.lua` | Phiên bản mới của chức năng định vị (?). | — |
| `NPCTradeManager.lua` | Mua và bán với NPC. | Bản 8.12 (không mua bán khi tên đỏ), 8.2 (tự mua thịt), 7.30.1; các file `SellBuy.txt`, `SellList.txt`, `saveitem.txt`. |
| `OtherFunction.lua` | Các chức năng khác (linh tinh). File lớn (khoảng 89 KB). | — |
| `PathFinding.lua` | Tìm đường. | Bản 7.29.1 (sửa lỗi đi tới `火龍窟` hay bị kẹt và đi vòng xa). |
| `RestControl.lua` | Điều khiển nghỉ ngơi: về thành nghỉ, nghỉ ở nhà trọ, hồi máu và mana. | Bản 8.12 (`[触发回城休息配置]`), 8.6 (buff chính rời nhà trọ khi mana chưa đầy), 7.31 (nhà trọ `欧瑞`), 7.30. |
| `res_GPS.lua` | Dữ liệu tài nguyên cho định vị: tọa độ, bản đồ, cổng hầm ngục (?). | — |
| `res_UIDefine.lua` | Dữ liệu định nghĩa giao diện: vị trí nút, cửa sổ (?). | — |
| `Teleportation.lua` | Dịch chuyển: dùng cuộn, NPC, sách ghi nhớ. | Bản 9.10 (`说话卷`, cuộn dịch chuyển về Talking Island), 8.5.2, 8.2 và 7.29.1 (dịch chuyển tới cửa hầm ngục), 7.31 (dịch chuyển ngẫu nhiên). |
| `ThreadControl.lua` | Điều khiển các luồng (thread) chạy song song của bot. | — |
| `TownFunction.lua` | Chức năng trong thành hoặc làng: mua, bán, kho, nhà trọ… | Bản 8.4 (lỗi đứng im trong thành, không ra đánh quái). |
| `Transfer.lua` | "Chuyển": có thể là chuyển đồ hoặc giao dịch giữa nhân vật (`TradedConfig.txt`), cũng có thể là chuyển bản đồ (?). | — |
| `UIControl.lua` | Điều khiển giao diện game: bấm nút, mở cửa sổ. | — |
| `UI_Search_Function.lua` | Tìm kiếm phần tử giao diện (nút, cửa sổ) (?). | — |
| `vision.lua` | "Thị giác": nhận dạng hình ảnh trên màn hình, ví dụ so khớp với ảnh mẫu trong `bmp/` (?). | — |
| `WarehouseManager.lua` | Quản lý kho đồ: kho cá nhân và kho huyết minh. | Bản 8.15 (kho cá nhân), 8.14 và 7.30 (lấy đồ kho huyết minh), 8.8 (lấy mũi tên từ kho). |

### 1.4 Các chương trình kết nối với nhau thế nào

```text
[Bd.exe – bảng điều khiển, chạy trên mỗi máy]
   │  đọc: config/config.ini, Account.txt, Game_Config/*.txt, lua/*.lua, bmp/*.bmp
   │
   ├──► mở launcher Purple (紫P) ở thư mục ghi trong 登录器路径
   │        └──► các cửa sổ game Lineage Classic (số lượng = 多开数量)
   │
   ├──► 大中控.exe  (trung tâm điều khiển lớn, không bắt buộc)
   │        địa chỉ = ip / port trong config/ZKT.ini
   │        cổng phải trùng 端口 trong 大中控/Data/Config.ini (mặc định 9011)
   │
   └──► 组队服务器.exe  (server tổ đội LAN, không bắt buộc)
            địa chỉ = ip / port trong Game_Config/BaseConfig.txt → mục [局域网组队配置]
            cổng phải trùng port trong 组队服务器/config.ini (mặc định 9527)
```

---

## 2. `config/config.ini`: cấu hình chính của bảng điều khiển

**Mục đích:** đây là file cấu hình của **bảng điều khiển** (`控制台`), tức chương trình `Bd.exe`. File quy định: launcher Purple nằm ở đâu, đăng nhập bằng cách nào, mở bao nhiêu cửa sổ game, xếp cửa sổ ra sao và bot điều khiển game theo cách nào (đọc bộ nhớ hay bấm phím-chuột). File có 32 dòng: 1 dòng tên mục, 14 dòng cài đặt (dòng 2–15), 13 dòng chú thích đặt trong `《》` (dòng 18–23, 25–26, 28–32) và 4 dòng trống (16, 17, 24, 27).

> 🔒 **Khi sửa file này:** giữ nguyên toàn bộ chữ Trung (tên mục `[config]` và tên khóa bên trái dấu `=`). Chỉ thay số hoặc giá trị bên phải dấu `=`. File lưu bằng **UTF-8**.

### Mục `[config]` (dòng 1–15)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `[config]` | Mục "cấu hình" | Tên mục (section). Giữ nguyên. |
| 2 | `登录器路径=D:\Program Files (x86)\NCSOFT\Purple` | Đường dẫn launcher (`登录器` = trình đăng nhập, tức launcher) | Thư mục cài launcher Purple (`紫P`) trên máy bạn. Giá trị mẫu nằm ở ổ `D:`. Nếu bạn cài Purple ở chỗ khác (ví dụ ổ `C:`), sửa phần sau dấu `=` cho đúng. Sai đường dẫn thì bot không mở được launcher. Theo giá trị mẫu, chỉ cần ghi **đường dẫn thư mục**, không ghi tên file .exe (suy luận). |
| 3 | `协议登录等待最大时间=120` | Thời gian chờ tối đa khi **đăng nhập bằng giao thức** | Dùng khi `协议登录` = `1`, `2` hoặc `3`. File không ghi đơn vị; nhiều khả năng là **giây**, tức 120 ≈ 2 phút (?). Hết thời gian này mà chưa vào được game thì bot coi là đăng nhập thất bại (suy luận). Mục này được thêm ở bản 7.12. |
| 4 | `模拟登录等待最大时间=200` | Thời gian chờ tối đa khi **đăng nhập mô phỏng** | Dùng khi `协议登录=0`, tức bot tự bấm trên giao diện launcher Purple. Đơn vị có lẽ là giây, tức 200 ≈ 3 phút 20 giây (?). 💡 Máy chậm hoặc mạng chậm thì có thể tăng số này. |
| 5 | `每次登陆前先关闭紫p=0` | Đóng launcher Purple (`紫p`) trước mỗi lần đăng nhập | `=0` (giá trị hiện tại): không đóng. `=1`: đóng launcher trước, rồi khởi động lại launcher để đăng nhập (chú thích dòng 21). 💡 Nếu launcher hay bị treo giữa các lần đăng nhập thì thử `=1`. |
| 6 | `登录失败停止上号=30` | Đăng nhập thất bại thì ngừng đưa tài khoản vào game (`上号`) | Đơn vị: **số lần**. `=30` nghĩa là một tài khoản đăng nhập 30 lần mà vẫn không vào được game thì bot **không đăng nhập tài khoản đó nữa** (chú thích dòng 22). |
| 7 | `出现验证停止上号=0` | Gặp xác minh thì ngừng đưa tài khoản vào game | `验证` = xác minh (khi tài khoản bị game yêu cầu xác minh). `=1`: tài khoản bị xác minh thì bot không đăng nhập tài khoản đó nữa; muốn dùng lại thì phải vào bảng điều khiển **xóa trạng thái** để tài khoản về trạng thái **chờ** (`等待`) (chú thích dòng 26). `=0` (giá trị hiện tại): không bật chức năng này. File chỉ giải thích giá trị `=1`. |
| 8 | `控制台韩文显示=0` | Bảng điều khiển hiển thị tiếng Hàn | `=0`: giao diện bảng điều khiển bằng **tiếng Trung**. `=1`: giao diện bằng **tiếng Hàn** (chú thích dòng 23). Không có lựa chọn tiếng Việt hay tiếng Anh. |
| 9 | `自动运行=0` | Tự động chạy | `=0` (giá trị hiện tại): bạn tự bấm chạy. `=1`: bảng điều khiển tải xong sẽ **tự khởi động tất cả game và chạy** (chú thích dòng 18). |
| 10 | `多开数量=1` | Số cửa sổ game mở cùng lúc (`多开`) | `=1`: chỉ 1 cửa sổ game. Tăng lên để chạy nhiều tài khoản trên một máy. 💡 Nên để số này không lớn hơn số ô của bố cục `窗口布局`, nhất là khi dùng `键鼠模式=1` (suy luận). |
| 11 | `窗口布局=2` | Bố cục cửa sổ | Cách xếp các cửa sổ game trên màn hình. `=1`: lưới 2×2, xếp 4 cửa sổ. `=2`: "3×3", xếp 6 cửa sổ. Các số lớn hơn cứ thế suy ra (chú thích dòng 20). 💡 Gốc ghi "3×3" nhưng chỉ có 6 cửa sổ, nên có lẽ là 3 cột × 2 hàng (?). |
| 12 | `协议登录=0` | Đăng nhập bằng giao thức | `=0`: **đăng nhập mô phỏng** (bot bấm trên giao diện launcher). `=1`: đăng nhập giao thức cho **server Đài Loan** (`台服`). `=2`: đăng nhập giao thức cho **server Hàn** (`韩服`). `=3`: dùng khi máy **hay bị màn hình xanh** (`蓝屏`, lỗi BSOD) (chú thích dòng 19). 💡 Khi `键鼠模式=1` thì nên dùng đăng nhập giao thức (chú thích dòng 30). |
| 13 | `驱动模式` | chế độ driver (dùng driver kernel của Windows) | ⚠️ Tài liệu này không hướng dẫn phần này. |
| 14 | `键鼠模式=0` | Chế độ bàn phím-chuột | Cách bot điều khiển game. `=0` (giá trị hiện tại): **chế độ bộ nhớ** (`内存模式`), cách làm cũ, bot đọc và ghi bộ nhớ game. `=1`: **chế độ bàn phím-chuột tiền cảnh** (`前台键鼠模式`; tiền cảnh = foreground), bot điều khiển trực tiếp trên màn hình. Xem các điều kiện ở chú thích dòng 28–31. |
| 15 | `目录保护` | bảo vệ/ẩn thư mục của bot | ⚠️ Tài liệu này không hướng dẫn phần này. |

Dòng 16 và 17 là dòng trống.

### Dịch các dòng chú thích `《》` (dòng 18–32)

Các dòng trong ngoặc `《》` là **chú thích để người dùng đọc**, giải thích ý nghĩa các giá trị ở trên.

| # | Dòng gốc | Dịch | Ghi chú |
|---|---|---|---|
| 18 | `《自动运行=0   =1表示控制台加载完毕自动全部启动游戏运行》` | 《`自动运行=0`; `=1` nghĩa là khi bảng điều khiển tải xong thì tự động khởi động toàn bộ game và chạy.》 | Xem dòng 9. |
| 19 | `《注意 协议登录=0为模拟登录  =1 协议登录台服  =2协议登录韩服 =3如果经常蓝屏可用》` | 《Chú ý: `协议登录=0` là đăng nhập mô phỏng; `=1` là đăng nhập giao thức server Đài Loan; `=2` là đăng nhập giao thức server Hàn; `=3` dùng được nếu máy hay bị màn hình xanh.》 | Xem dòng 12. |
| 20 | `《注意 窗口布局=1表示 2*2 桌面平铺4个      =2表示  3*3平铺6个   以此类推》` | 《Chú ý: `窗口布局=1` nghĩa là lưới 2×2, xếp lát 4 cửa sổ trên màn hình (`桌面` = desktop); `=2` nghĩa là 3×3, xếp lát 6 cửa sổ; cứ thế suy ra.》 | Xem dòng 11. |
| 21 | `《每次登陆前先关闭紫p=1 表示先关闭然后重新启动紫p登录器》` | 《`每次登陆前先关闭紫p=1` nghĩa là đóng trước, sau đó khởi động lại launcher Purple (`紫p登录器`).》 | Xem dòng 5. |
| 22 | `《登录失败停止上号=30表示这个账号登录30次没进入游戏则不在登录》` | 《`登录失败停止上号=30` nghĩa là tài khoản này đăng nhập 30 lần mà không vào được game thì không đăng nhập nữa.》 | Gốc viết `不在` (đúng ra là `不再` = "không… nữa"). Đây là lỗi chính tả trong chú thích, không ảnh hưởng gì. |
| 23 | `《控制台韩文显示=0  =0为中文控制台显示 =1韩文语言控制台显示》` | 《`控制台韩文显示=0`; `=0` là bảng điều khiển hiển thị tiếng Trung; `=1` là bảng điều khiển hiển thị bằng tiếng Hàn.》 | Xem dòng 8. |
| 25 | (chú thích về `驱动模式`) | chế độ driver (dùng driver kernel của Windows) | ⚠️ Tài liệu này không hướng dẫn phần này. |
| 26 | `《出现验证停止上号=1  账号被验证时当前账号不在上号，再次使用时需要控制台清空状态为等待状态》` | 《`出现验证停止上号=1`: khi tài khoản bị yêu cầu xác minh thì tài khoản đó không được đưa vào game nữa; muốn dùng lại thì cần vào bảng điều khiển xóa trạng thái, đưa về trạng thái "chờ".》 | Xem dòng 7. `账号被验证` = tài khoản bị game yêu cầu xác minh. Gốc lại viết `不在` thay cho `不再` ("không… nữa"), cùng lỗi chính tả như dòng 22. |
| 28 | `《键鼠模式=0 =1（操作游戏的方式） 有2种模式  =0原有的内存模式  =1前台键鼠模式》` | 《`键鼠模式` nhận `=0` hoặc `=1` (cách điều khiển game), tức có 2 chế độ: `=0` là chế độ bộ nhớ vốn có; `=1` là chế độ bàn phím-chuột tiền cảnh.》 | "Tiền cảnh" (`前台`) nghĩa là cửa sổ game phải hiện trên màn hình và bot di chuột, bấm phím thật. |
| 29 | `《前台键鼠模式下 多开情况下也支持前台模式同时操作多个游戏窗口   此模式需要游戏窗口能平铺 不能有遮挡》` | 《Ở chế độ bàn phím-chuột tiền cảnh, khi mở nhiều cửa sổ game, bot vẫn điều khiển được nhiều cửa sổ cùng lúc. Chế độ này cần các cửa sổ game xếp lát được trên màn hình và không bị che khuất.》 | 💡 Đừng để cửa sổ khác (trình duyệt, bảng điều khiển…) đè lên cửa sổ game. |
| 30 | `《前台键鼠模式下 建议用协议登录，因为在登录时所有游戏会暂停，等待登录完成，才会正常工作》` | 《Ở chế độ bàn phím-chuột tiền cảnh, nên dùng đăng nhập giao thức, vì trong lúc đăng nhập tất cả game sẽ tạm dừng và phải đợi đăng nhập xong mới làm việc bình thường.》 | Có lẽ vì đăng nhập mô phỏng phải dùng màn hình và chuột, lại lâu hơn, nên các cửa sổ khác phải đứng chờ lâu hơn (suy luận). |
| 31 | `《前台键鼠模式下 建议系统分辨率设置1920*1080或更大的分辨率，这样能平铺6个游戏正常前台操作》` | 《Ở chế độ bàn phím-chuột tiền cảnh, nên đặt độ phân giải hệ thống 1920×1080 hoặc lớn hơn; như vậy mới xếp lát được 6 game và điều khiển tiền cảnh bình thường.》 | Liên quan dòng 10 và 11. |
| 32 | (chú thích về `目录保护`) | bảo vệ/ẩn thư mục của bot | ⚠️ Tài liệu này không hướng dẫn phần này. |

Dòng 24 và 27 là dòng trống.

### 💡 Lưu ý khi cấu hình `config.ini`

- **Chạy nhiều cửa sổ bằng chế độ bàn phím-chuột:** đặt `键鼠模式=1`, chọn đăng nhập giao thức (`协议登录=1` cho server Đài Loan hoặc `=2` cho server Hàn), đặt màn hình 1920×1080 trở lên, dùng `窗口布局=2` (6 cửa sổ) và để `多开数量` từ 6 trở xuống.
- **Chế độ bộ nhớ** (`键鼠模式=0`) là cách vốn có từ trước. Các điều kiện "xếp lát, không bị che" ở dòng 29–31 chỉ nói cho chế độ bàn phím-chuột, nên có lẽ chế độ bộ nhớ không đòi cửa sổ game phải hiện rõ trên màn hình (suy luận).
- Nếu một tài khoản bị bỏ qua không đăng nhập nữa, hãy xem nó có chạm giới hạn `登录失败停止上号` hoặc bị dừng do `出现验证停止上号=1` không. Với trường hợp xác minh, phải xóa trạng thái trên bảng điều khiển để tài khoản về trạng thái "chờ".

---

## 3. `config/ZKT.ini`: kết nối tới trung tâm điều khiển `大中控`

**Mục đích:** cho bảng điều khiển `Bd.exe` trên máy này biết **trung tâm điều khiển lớn** (`大中控`, gọi tắt là `中控`) nằm ở địa chỉ nào và cổng nào. "ZKT" có lẽ là viết tắt phiên âm của `中控台` (Zhōng Kòng Tái = bàn trung tâm điều khiển) (?). File có 4 dòng.

> 🔒 **Khi sửa file này:** giữ nguyên tên mục và tên khóa (`[config]`, `ip`, `port`, `中控显示计算机名`). Chỉ thay giá trị sau dấu `=`.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `[config]` | Mục "cấu hình" | Tên mục. Giữ nguyên. |
| 2 | `ip=127.0.0.1` | Địa chỉ IP của máy chạy `大中控` | `127.0.0.1` nghĩa là **chính máy này** (localhost). Nếu `大中控.exe` chạy trên máy khác trong mạng LAN, đổi thành IP LAN của máy đó (thường có dạng `192.168.x.x`). |
| 3 | `port=9011` | Cổng kết nối | Phải **trùng** với `端口=9011` trong `大中控/Data/Config.ini` (mục 5). |
| 4 | `中控显示计算机名=` | Tên máy tính hiển thị trên trung tâm điều khiển | Hiện để trống. Bạn có thể điền một tên dễ nhớ (ví dụ `May01`) để phân biệt các máy trên `大中控`. Để trống thì có lẽ dùng tên mặc định của Windows (?). Từ bản 9.9 cũng sửa được tên này ngay trên `中控`. |

💡 **Lưu ý:**
- Nếu bạn **không dùng** `大中控` thì có thể để nguyên file này (suy luận).
- Một số tính năng **bắt buộc phải kết nối `中控`** (theo các file trong `Game_Config`, xem file 04–06): `Buff.txt` với `开启=2` (trung tâm tự phân phối tài khoản phụ đến nhận buff) và `CounterattackPeoples.txt` với `开启=4` hoặc `=5`. Ngoài ra còn hiển thị bảo vật (bản 9.16) và sửa tài khoản trên trung tâm.
- Nếu `大中控` ở máy khác, tường lửa Windows trên máy đó phải cho phép cổng 9011 (lời khuyên chung).

---

## 4. `config/ServerText.txt`: danh sách server

**Mục đích:** danh sách **server** (`大区`, nghĩa đen là "đại khu") của Lineage Classic để bạn chọn trên bảng điều khiển. Ghi chú cập nhật bản 7.23 có câu `然后在控制台设置 服务器为 獅子涅墨亞2`, nghĩa là "sau đó trên bảng điều khiển đặt server là `獅子涅墨亞2`". Tên server cũng được dùng trong các file `Game_Config`, ví dụ `BloodConfig.txt` viết `太陽神阿波羅=血盟名字1,血盟名字2` (tên server = tên huyết minh). Thư mục `大中控/Data/` có một bản sao **giống hệt** file này. File có 35 dòng: 1 dòng tiêu đề, 31 tên server và 3 dòng trống.

Phần lớn tên server là **tên nhân vật thần thoại Hy Lạp** (vài tên dùng dạng La Mã: Cupid, Venus, Mars), viết bằng chữ phồn thể.

> 🔒 **Khi sửa file này:** giữ nguyên từng ký tự của tên server, kể cả số `2` ở cuối, phần `(伺服器)` và phần ` non-pvp` (có một dấu cách đứng trước). Khi cần ghi tên server vào file cấu hình khác, hãy **chép nguyên văn** từ danh sách này.

| # | Dòng gốc | Nghĩa (tiếng Việt / tiếng Anh) | Ghi chú |
|---|---|---|---|
| 1 | `[大区]` | Mục "server" (đại khu) | Tiêu đề danh sách. Giữ nguyên. |
| 2 | `太陽神阿波羅` | Thần Mặt Trời Apollo | |
| 3 | `愛神邱比特` | Thần Tình yêu Cupid | |
| 4 | `勝利女神雅典娜` | Nữ thần Chiến thắng Athena | |
| 5 | `美神維納斯` | Nữ thần Sắc đẹp Venus | |
| 6 | `天神宙斯` | Thần Zeus (vua các vị thần) | |
| 7 | `天后海拉` | Thiên hậu Hera | |
| 8 | `戰神馬爾斯` | Thần Chiến tranh Mars | |
| 9 | `月亮女神阿緹蜜斯` | Nữ thần Mặt Trăng Artemis | |
| 10 | `海神波塞頓` | Thần Biển Poseidon | |
| 11 | `冥王黑帝斯` | Diêm vương Hades (thần Âm phủ) | |
| 12 | `火神赫發斯特斯` | Thần Lửa Hephaestus | |
| 13 | `收穫女神帝蜜特` | Nữ thần Mùa màng Demeter | |
| 14 | `蛇髮女墨杜沙` | Nữ yêu tóc rắn Medusa | |
| 15 | `半人馬涅索斯` | Nhân mã Nessus | |
| 16 | *(dòng trống)* | — | Chỉ để chia nhóm (?). |
| 17 | `牛人彌諾陶洛斯` | Người bò Minotaur (quái vật đầu bò) | |
| 18 | `牛人彌諾陶洛斯2` | Người bò Minotaur 2 | Server thứ hai cùng tên. |
| 19 | *(dòng trống)* | — | Chỉ để chia nhóm (?). |
| 20 | `俄雷恩(伺服器)` | Orion (?) | `(伺服器)` = "(máy chủ)" và là một phần của tên, phải giữ nguyên. `俄雷恩` là phiên âm; theo chủ đề thần thoại Hy Lạp của các server khác, có lẽ là chàng thợ săn Orion (?). Đây không phải Oren: làng Oren trong game viết là `歐瑞`. 💡 Trong các file `Game_Config`, server này được ghi là `俄雷恩` (không có `(伺服器)`); hãy chép đúng cách viết của từng file. |
| 21 | `凱斯特(伺服器)` | Castor (?) | Giống dòng trên: `(伺服器)` = "(máy chủ)". `凱斯特` là phiên âm, có lẽ là Castor trong thần thoại Hy Lạp (?). Server này không có trong các danh sách server của `Game_Config`. |
| 22 | `獅子涅墨亞` | Sư tử Nemea | Được thêm ở bản 7.22. |
| 23 | `獅子涅墨亞2` | Sư tử Nemea 2 | Được thêm ở bản 7.23. |
| 24 | *(dòng trống)* | — | Chỉ để chia nhóm (?). |
| 25 | `獨眼巨人庫克羅普斯` | Khổng lồ một mắt Cyclops | |
| 26 | `飛馬珀伽索斯` | Ngựa bay Pegasus (ngựa có cánh) | |
| 27 | `飛馬珀伽索斯2` | Ngựa bay Pegasus 2 | Được thêm ở bản 7.23.2. |
| 28 | `公牛克里特` | Bò mộng xứ Crete (Cretan Bull) | |
| 29 | `女妖塞壬` | Nữ yêu Siren | |
| 30 | `巨龍拉冬` | Rồng khổng lồ Ladon | |
| 31 | `百眼怪阿爾戈斯` | Quái vật trăm mắt Argus | |
| 32 | `大地之神蓋亞` | Thần Đất Gaia | |
| 33 | `泰坦女神瑞亞 non-pvp` | Nữ thần Titan Rhea (**non-PvP**) | Server **không PvP**. |
| 34 | `水蛇許德拉 non-pvp` | Rắn nước Hydra (**non-PvP**) | Server **không PvP**. |
| 35 | `地獄犬刻耳柏洛斯` | Chó địa ngục Cerberus | |

💡 **Lưu ý:**
- **Hai server non-PvP** là `泰坦女神瑞亞 non-pvp` và `水蛇許德拉 non-pvp`. Trên hai server này người chơi không đánh nhau được, nên các cài đặt PvP và phản công người chơi (`反击`, `CounterattackPeoples.txt`) gần như không có tác dụng (suy luận).
- **Server mới:** khi game mở server mới, tác giả phát hành `ServerText.txt` mới kèm lua mới (bản 7.22, 7.23, 7.23.2). Hãy chép đè file vào `config/`, và nên chép cả vào `大中控/Data/` (suy luận).
- **Tên gần giống nhau** (có và không có số `2`): ghi chú bản 7.23.2 có câu `如果是 飛馬珀伽索斯 会选最底下的区的需要替换lua`, nghĩa là "nếu bạn chơi `飛馬珀伽索斯` mà bot lại chọn server ở cuối danh sách thì cần thay lua".

---

## 5. `大中控/Data/Config.ini`: cấu hình trung tâm điều khiển

**Mục đích:** cổng mạng (port) mà chương trình `大中控.exe` mở ra để các bảng điều khiển `Bd.exe` (trên máy này hoặc các máy khác trong mạng LAN) kết nối vào. File có 2 dòng và được **lưu bằng mã hóa GBK** (khác với các file khác).

> 🔒 **Khi sửa file này:** giữ nguyên `[中控配置]` và `端口`. Chỉ đổi con số.
>
> ⚠️ **Mã hóa GBK:** nếu mở bằng Notepad trên Windows tiếng Việt, chữ Trung có thể hiện thành ký tự lạ. Đừng lưu đè khi đang thấy ký tự lạ, vì bot sẽ không đọc được tên mục nữa. Hãy mở bằng Notepad++ và chọn *Encoding → Character sets → Chinese → GB2312 (Simplified Chinese)* để thấy đúng chữ, rồi chỉ sửa con số và lưu lại.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `[中控配置]` | Mục "cấu hình trung tâm điều khiển" | Tên mục. Giữ nguyên. |
| 2 | `端口=9011` | Cổng = 9011 | Cổng mà `大中控.exe` lắng nghe. Phải **trùng** với `port=` trong `config/ZKT.ini` của **mọi máy** chạy bot. Nếu đổi số (ví dụ vì trùng cổng với phần mềm khác) thì phải đổi đồng loạt ở tất cả các máy. |

---

## 6. `组队服务器/config.ini`: cấu hình server tổ đội

**Mục đích:** đặt cổng (port) cho chương trình **server tổ đội** `组队服务器.exe`. Server này giúp các nhân vật trên nhiều máy, nhiều cửa sổ tự lập tổ đội qua mạng LAN. File có 2 dòng.

> 🔒 **Khi sửa file này:** giữ nguyên `[config]` và `port`. Chỉ đổi con số.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `[config]` | Mục "cấu hình" | Tên mục. Giữ nguyên. |
| 2 | `port=9527` | Cổng server tổ đội = 9527 | Phải **trùng** với `port=9527` trong `Game_Config/BaseConfig.txt`, mục `[局域网组队配置]` (cấu hình tổ đội LAN) của mọi máy chạy bot. Mục đó còn có `ip=` (địa chỉ của máy chạy server tổ đội: chú thích gốc ghi `局域网的ip 或者外网ip` = "IP mạng LAN hoặc IP mạng ngoài"; để `127.0.0.1` nếu cùng máy) và `组队密码=` (mật khẩu tổ đội: các máy dùng cùng mật khẩu sẽ được ghép đội với nhau). Chi tiết ở file 04–06. |

💡 **Lưu ý:** trong cùng mục `[局域网组队配置]` của `BaseConfig.txt`, khóa `队伍最大人数=0` nghĩa là **tắt** tổ đội LAN. Muốn dùng server tổ đội thì phải đặt số người tối đa của đội lớn hơn 0 (game cho tối đa 8 người một đội, có thể đặt `=8`). Nếu để `=0` thì chạy `组队服务器.exe` cũng không có tác dụng.

**Tóm tắt file hướng dẫn đi kèm** `组队服务器/使用说明.txt` (bản dịch đầy đủ ở `01-huong-dan-su-dung.md`, Phần B):

- `服务端需要与脚本控制台在同一个局域网中`: server phải nằm **cùng mạng LAN** với bảng điều khiển của bot.
- `你可以把服务端放在远程同步专家的机器上`: bạn có thể đặt server trên máy đang chạy phần mềm `远程同步专家` (dịch sát: "Chuyên gia đồng bộ từ xa") (?).
- `服务端只需要设置好端口就行，客户机的端口要一致`: phía server chỉ cần đặt cổng là xong; cổng trên các máy khách phải giống cổng của server.

---

## 7. `Account.txt`: danh sách tài khoản

**Mục đích:** danh sách tài khoản game để bot lần lượt đăng nhập (`上号`). **Mỗi dòng là một tài khoản.** File mẫu có 2 dòng, minh họa **hai định dạng** được chấp nhận. Hai dòng này là chữ mẫu ("tài khoản 1, mật khẩu 1"), không phải tài khoản thật.

> 🔒 **Khi sửa file này:** dùng đúng ký tự phân cách: dấu phẩy ASCII `,` (không dùng `，`) hoặc **4 dấu gạch ngang** `----`. File lưu bằng UTF-8.

| # | Dòng gốc (mẫu) | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `账号1,密码1` | "tài khoản 1, mật khẩu 1" | **Định dạng 1:** `<tài khoản>,<mật khẩu>`, phân cách bằng dấu phẩy. |
| 2 | `账号2----密码2` | "tài khoản 2 ---- mật khẩu 2" | **Định dạng 2:** `<tài khoản>----<mật khẩu>`, phân cách bằng 4 dấu gạch ngang. |

Ví dụ khi điền (chỉ là chỗ giữ chỗ, hãy thay bằng thông tin của bạn):

```text
<tài khoản>,<mật khẩu>
<tài khoản>----<mật khẩu>
```

💡 **Lưu ý:**
- **Xóa hai dòng mẫu** `账号1,密码1` và `账号2----密码2` sau khi điền tài khoản thật. Nếu không, bot có thể cố đăng nhập bằng chữ mẫu (suy luận).
- Không thêm dấu cách thừa quanh dấu phân cách (lời khuyên chung).
- Có một **định dạng thứ ba** (kèm số điện thoại và đường link nhận mã) dành cho tính năng `自动接码验证设备`: tự động nhận mã SMS để xác minh thiết bị. ⚠️ Tài liệu này không hướng dẫn phần này.
- 🔐 **Bảo mật:** file này chứa **mật khẩu dạng chữ thường** (không mã hóa). Đừng gửi gói bot cho người khác khi `Account.txt` đã có tài khoản của bạn.

---

## 8. `ip.txt` và `key.txt`

Cả hai file đều **rỗng** (0 byte), nên không có dòng nào để dịch.

| File | Là gì (suy đoán từ tên file) | Có cần sửa không |
|---|---|---|
| `ip.txt` | Có lẽ là danh sách IP proxy cho chức năng `导入ip` (nhập IP, chuột phải trên bảng điều khiển), đi cùng `JSBProxy64.dll` theo ghi chú bản 8.8. | Chỉ khi bạn dùng proxy (?). |
| `key.txt` | Có lẽ là nơi lưu mã kích hoạt hoặc bản quyền (key) của bot. | Thường không sửa tay. Nếu sau này file có nội dung thì đừng chia sẻ. |

---

## 9. Checklist cài đặt lần đầu

1. **Đường dẫn launcher:** trong `config/config.ini`, sửa `登录器路径=` thành thư mục cài launcher Purple trên máy bạn.
2. **Tài khoản:** trong `Account.txt`, mỗi dòng ghi `<tài khoản>,<mật khẩu>` hoặc `<tài khoản>----<mật khẩu>`, rồi xóa hai dòng mẫu.
3. **Cách đăng nhập và điều khiển:** chọn `协议登录` (`0` mô phỏng, `1` Đài Loan, `2` Hàn) và `键鼠模式` (`0` bộ nhớ, `1` bàn phím-chuột tiền cảnh). Sau đó đặt `多开数量` và `窗口布局` cho khớp.
4. **Server:** chọn server trên bảng điều khiển, dùng tên đúng như trong `config/ServerText.txt`.
5. **(Không bắt buộc) Trung tâm điều khiển `大中控`:** chạy `大中控.exe` trên một máy. Trên mỗi máy chạy bot, đặt `ip=` trong `config/ZKT.ini` thành IP của máy chạy `大中控`. Kiểm tra `port=` trùng với `端口=` trong `大中控/Data/Config.ini` (mặc định 9011).
6. **(Không bắt buộc) Tổ đội LAN:** chạy `组队服务器.exe`. Trong `Game_Config/BaseConfig.txt`, mục `[局域网组队配置]`, đặt `队伍最大人数=` lớn hơn 0 (=0 là tắt tổ đội LAN), đặt `ip=` và `port=` trùng với server tổ đội (mặc định 9527), rồi đặt cùng một `组队密码=` cho các máy muốn ghép đội.
7. Phần lối chơi (bản đồ, đánh quái, thuốc, kho…) xem các file 04–06.

---

## 10. Thuật ngữ dùng trong file này

| Gốc | Nghĩa | Ghi chú |
|---|---|---|
| `控制台` | Bảng điều khiển (console) của bot | Chính là `Bd.exe`. |
| `大中控` / `中控` | Trung tâm điều khiển lớn | Quản lý nhiều máy và nhiều tài khoản. |
| `组队服务器` | Server tổ đội | Ghép đội qua mạng LAN (`局域网`). |
| `紫P` / `紫p` | Launcher Purple của NCSOFT | `登录器` = launcher (trình đăng nhập). |
| `上号` | Đưa tài khoản vào game (đăng nhập) | |
| `协议登录` | Đăng nhập bằng giao thức | Không bấm qua giao diện launcher. |
| `模拟登录` | Đăng nhập mô phỏng | Bot bấm trên giao diện launcher. |
| `多开` | Mở nhiều cửa sổ game | |
| `键鼠模式` / `前台键鼠模式` | Chế độ bàn phím-chuột (tiền cảnh) | Bot điều khiển trực tiếp trên màn hình. |
| `内存模式` | Chế độ bộ nhớ | Bot đọc và ghi bộ nhớ game. |
| `验证` | Xác minh | Khi tài khoản bị yêu cầu xác minh. |
| `台服` / `韩服` | Server Đài Loan / server Hàn | |
| `大区` / `伺服器` / `服务器` | Server (máy chủ) | |
| `端口` / `port` | Cổng mạng | |
| `账号` / `密码` | Tài khoản / mật khẩu | |
| `血盟` | Huyết minh (clan) | |
| `挂机` (gj) | Treo máy (auto farm) | |
