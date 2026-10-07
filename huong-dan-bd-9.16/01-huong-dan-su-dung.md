# Hướng dẫn sử dụng

Bản dịch tiếng Việt kèm giải thích cho **2 file hướng dẫn** trong gói bot **天堂经典版 Bd 9.16** (bot treo máy – auto farm – cho game *Lineage Classic* của NCSOFT).

| File gốc | Tên hiển thị trên ổ đĩa (đã bị mã hóa tên) | Số dòng |
|---|---|---|
| `使用说明.txt` (thư mục gốc của bot) | `#U4f7f#U7528#U8bf4#U660e.txt` | 221 (lệnh `wc -l` báo 220 vì dòng cuối không có ký tự xuống dòng) |
| `组队服务器/使用说明.txt` (thư mục server tổ đội) | `#U7ec4#U961f#U670d#U52a1#U5668/#U4f7f#U7528#U8bf4#U660e.txt` | 3 |

> Ký hiệu trong tài liệu: chữ trong ô `code` là **chữ gốc**, phải giữ nguyên khi chép vào file cấu hình. "(?)" = bản dịch chưa chắc chắn 100%.

**Mục lục**

- Phần A — `使用说明.txt` (hướng dẫn sử dụng chính)
  - A0. Mục đích của file
  - Quy tắc khi sửa cấu hình (đọc trước)
  - A1. Dòng 1–4: khối `[登录配置]`
  - A2. Dòng 6–9: Thêm bản đồ mới
  - A3. Dòng 12–17: Đánh Ent và Pan ở Rừng Tiên
  - A4. Dòng 19–69: Bản đồ hỗ trợ Sách ghi nhớ hầm ngục
  - A5. Dòng 71–100: Bản đồ sự kiện ở làng Gludin
  - A6. Dòng 104–141: Bản đồ quán net
  - A7 → A15. Dòng 146–221: Danh sách hầm ngục được bổ sung theo từng bản cập nhật
  - A16. Tổng hợp những điểm dễ nhầm
- Phần B — `组队服务器/使用说明.txt` (hướng dẫn server tổ đội)

---

## Phần A — `使用说明.txt` (Hướng dẫn sử dụng chính)

### A0. Mục đích của file

`使用说明.txt` (*Hướng dẫn sử dụng*) là file ghi chú do tác giả bot viết, **không phải file cấu hình**. Nội dung gồm:

- cách cài đặt cho một số trường hợp đặc biệt: đánh Ent/Pan ở Rừng Tiên, dùng sách ghi nhớ hầm ngục, bản đồ sự kiện, bản đồ quán net, Hang Kiến…;
- **danh sách tên bản đồ** mà bot hỗ trợ, để bạn chép vào dòng `打怪地图=` (bản đồ đánh quái).

File chia thành nhiều khối. Mỗi khối bắt đầu bằng một hàng 20 dấu gạch `--------------------` rồi tới tiêu đề khối. Nhiều tiêu đề có dạng `增加支持…` (= "Bổ sung hỗ trợ …"): đó là ghi chú cập nhật, nghĩa là một phiên bản bot nào đó đã thêm hỗ trợ cho các bản đồ này.

### ⚠️ Quy tắc khi sửa cấu hình (đọc trước)

1. **Giữ nguyên chữ Trung Quốc.** Bot đọc chữ đúng theo từng ký tự. Tên khóa (`打怪地图`, `记忆卷轴传送`, `打怪坐标`…), tên mục `[...]`, tên bản đồ, tên quái, tên vật phẩm, tên NPC phải giữ **y nguyên** như bản gốc. Bạn **chỉ thay số / giá trị** sau dấu `=`.
2. **Chữ Phồn thể và Giản thể là khác nhau.** Tên khóa viết bằng chữ Giản thể (ví dụ `打怪地图`), còn tên bản đồ trong game viết bằng chữ Phồn thể (ví dụ `龍之谷地監6樓`, **không phải** 龙之谷地监6楼). Sai một nét là bot không nhận ra. Một số tiêu đề khối trong file gốc dùng chữ Giản thể (`蚂蚁洞窟`, `古鲁丁村`, `海音地监`), nhưng tên để điền vào cấu hình luôn là tên Phồn thể trong các danh sách bên dưới.
3. **Chép cả dấu cách và ký hiệu.** Ví dụ: `被遺棄者之地 : 深淵` có một dấu cách trước và sau dấu hai chấm `:`; `污染的祝福之地 - 精靈之地` có dấu cách hai bên dấu gạch `-`; `(網咖)` dùng ngoặc tròn thường `( )`, **không phải** ngoặc toàn khổ `（ ）`.
4. **Cách an toàn nhất:** sao chép (copy) tên trong ô `code` của tài liệu này rồi dán vào file cấu hình, đừng gõ lại bằng bộ gõ.
5. **Giữ mã hóa UTF-8** khi lưu file (các file cấu hình trong gói này là UTF-8). Nên sửa bằng Notepad++ hoặc VS Code.
6. **Các khóa được nhắc tới nằm ở đâu?** (tra trong các file khác của gói)
   - `打怪地图=` (bản đồ đánh quái), `打怪坐标=` (tọa độ đánh quái), `记忆卷轴传送=` (dịch chuyển bằng cuộn ghi nhớ), `怪物过滤=` (lọc quái): nằm trong `Game_Config/gj.txt`. Trong gói đi kèm, file này có 5 mục `[1]`, `[5]`, `[7]`, `[10]`, `[15]`; có vẻ mỗi mục ứng với một mốc cấp độ nhân vật (?). Bạn sửa trong mục ứng với cấp độ muốn treo máy.
   - `记忆卷轴传送=` cũng có trong `Game_Config/BaseConfig.txt`, mục `[挂机全局配置]` (cấu hình treo máy toàn cục). Mục này chỉ có hiệu lực khi `启用全局配置=1`; nếu `=0` thì bot dùng giá trị trong `gj.txt`. Trong gói đi kèm đang để `启用全局配置=0`, tức là mặc định bot dùng `gj.txt`.
   - `自动购买装备=` (tự động mua trang bị): `Game_Config/BaseConfig.txt`, mục `[基础配置]` (cấu hình cơ bản).
   - `内存打怪=` (đánh quái bằng bộ nhớ): `Game_Config/BaseConfig.txt`, mục `[键鼠模式附加内存功能]` (chức năng bộ nhớ bổ sung cho chế độ bàn phím-chuột).
   - `键鼠模式=` (chế độ bàn phím-chuột): `config/config.ini`.

---

### A1. Dòng 1–4 — Khối `[登录配置]`

| Dòng gốc | Nghĩa | Giải thích |
|---|---|---|
| `[登录配置]` | Mục "Cấu hình đăng nhập" | Tên một mục trong `Game_Config/BaseConfig.txt`. Dòng 1 trong file gốc mở đầu bằng `--------------------` rồi tới tên mục này. |
| `自动接码验证设备` | tự động nhận mã SMS để xác minh thiết bị | ⚠️ Tài liệu này không hướng dẫn phần này. |
| Dòng 2–4 (không dịch) | định dạng tài khoản đi kèm tính năng tự động nhận mã SMS để xác minh thiết bị | ⚠️ Tài liệu này không hướng dẫn phần này. |

> 🔒 **Cảnh báo bảo mật:** dòng 4 của file gốc là một dòng tài khoản mẫu, trông giống thông tin thật (gồm `<email>`, `<mật khẩu>`, `<số điện thoại>` và một `<đường link>` có chứa mã token). Tài liệu này đã ẩn toàn bộ nội dung đó. Nếu đó là thông tin của bạn hoặc của người khác, đừng gửi file `使用说明.txt` gốc cho ai; nên xóa dòng đó và đổi mật khẩu nếu cần.

---

### A2. Dòng 6–9 — `增加新地图` (Thêm bản đồ mới)

**Mục đích:** báo rằng bản cập nhật có thêm một bản đồ mới và chỉ cách điền tên bản đồ đó.

| Dòng gốc | Nghĩa | Giải thích |
|---|---|---|
| `增加新地图` | Thêm bản đồ mới | Tiêu đề khối (dòng 6). |
| `被遺棄者之地 : 深淵` | Vùng đất bị ruồng bỏ (`被遺棄者之地`) : Vực thẳm (`深淵`) | Tên bản đồ mới: khu **Vực thẳm** thuộc vùng **Vùng đất bị ruồng bỏ**. |
| `如下设置` | Cài đặt như sau | |
| `打怪地图=被遺棄者之地 : 深淵` | Bản đồ đánh quái = Vùng đất bị ruồng bỏ : Vực thẳm | Dòng mẫu để dán vào cấu hình (`gj.txt`). |

```ini
打怪地图=被遺棄者之地 : 深淵
```

> 💡 **Lưu ý:** dấu hai chấm là `:` kiểu thường (không phải `：` toàn khổ), có **một dấu cách trước và một dấu cách sau**. Thiếu dấu cách thì bot có thể không nhận bản đồ.

---

### A3. Dòng 12–17 — `妖精森林踢 安特  潘 的设置` (Cài đặt "đá" Ent và Pan ở Rừng Tiên)

**Mục đích:** hướng dẫn cho bot đi đánh hai loại quái **Ent** (`安特`, người cây) và **Pan** (`潘`) ở **Rừng Tiên** (`妖精森林`, Elven Forest) bằng tay không.

> Bối cảnh (kiến thức về game, không có trong file gốc) (?): trong Lineage, đánh Ent/Pan bằng tay không (không cầm vũ khí) có thể nhận được nguyên liệu (ví dụ quả của Ent, bờm của Pan), thường dùng cho tộc Elf (`妖精`). Vì vậy hướng dẫn bắt bạn cất vũ khí đi.

| Dòng gốc | Nghĩa | Giải thích |
|---|---|---|
| `妖精森林踢 安特  潘 的设置` | Cài đặt "đá" Ent (`安特`) và Pan (`潘`) ở Rừng Tiên (`妖精森林`) | `踢` nghĩa đen là "đá", ở đây hiểu là đánh tay không (?). Tiêu đề khối (dòng 12). |
| `手动把武器存入仓库，BaseConfig.txt 中 自动购买装备=0` | Tự tay cất vũ khí vào kho đồ (`仓库`); trong `BaseConfig.txt` đặt `自动购买装备=0` | `自动购买装备` = tự động mua trang bị: `=0` tắt, `=1` bật. Trong file đi kèm giá trị đang là `=1`; theo chú thích trong `BaseConfig.txt`, khi đạt 11000 (có lẽ là 11000 adena (?)) bot sẽ tự mua `獵人之弓` (Cung Thợ săn, Hunter's Bow). Nếu không tắt, bot có thể tự mua và cầm vũ khí, như vậy sẽ không còn đánh tay không. |
| `如果是键鼠模式 需要设置内存打怪=1模式，因为键鼠打怪无法靠近这种怪物` | Nếu đang dùng chế độ bàn phím-chuột (`键鼠模式`) thì phải đặt `内存打怪=1` (đánh quái bằng chế độ bộ nhớ), vì kiểu đánh bằng bàn phím-chuột không lại gần được loại quái này. | `内存打怪`: `=0` đánh bằng bàn phím-chuột, `=1` đánh bằng chế độ bộ nhớ (đánh thường). Chỉ cần đặt khi `config/config.ini` có `键鼠模式=1` (chế độ bàn phím-chuột). Nếu `键鼠模式=0` (chế độ bộ nhớ, kiểu cũ) thì bot vốn đã thao tác bằng bộ nhớ. |
| `需要把周围所有怪物名字都过滤掉，只保留  安特  潘` | Phải lọc bỏ (`过滤`) tên tất cả các loại quái xung quanh, chỉ giữ lại Ent (`安特`) và Pan (`潘`). | Nghĩa là thêm tên mọi loại quái khác ở khu đó vào danh sách lọc quái `怪物过滤=` (danh sách quái bot **bỏ qua, không đánh**); tên cách nhau bằng dấu phẩy `,`. |
| `打怪地图=妖精森林` | Bản đồ đánh quái = Rừng Tiên | Giữ nguyên `妖精森林`. |
| `打怪坐标=x,y\|x,y\|x,y` | Tọa độ đánh quái = nhiều điểm `x,y` nối nhau bằng dấu `\|` | `x,y` chỉ là chỗ trống mẫu: thay bằng tọa độ thật (xem tọa độ nhân vật trong bảng điều khiển `控制台`). Mỗi cặp `x,y` là một điểm; nhiều điểm thì ngăn cách bằng dấu `\|`, không có dấu cách. |

Mẫu cấu hình (nguyên văn dòng 16–17):

```ini
打怪地图=妖精森林
打怪坐标=x,y|x,y|x,y
```

Ví dụ định dạng tọa độ thật (lấy từ mục `[7]` của `gj.txt` đi kèm, nơi `打怪地图=說話之島`; chỉ để minh họa cách viết, **không phải** tọa độ ở Rừng Tiên):

```ini
打怪坐标=32694,32872|32668,32848
```

> 💡 **Lưu ý 1 — rất dễ quên:** trong `gj.txt` đi kèm, danh sách `怪物过滤=` mặc định **đã có sẵn `安特`** (ở cả 5 mục `[1]`, `[5]`, `[7]`, `[10]`, `[15]`). Nếu không **xóa `安特` khỏi danh sách lọc** thì bot sẽ bỏ qua Ent và không đánh. (`潘` hiện không có trong danh sách mặc định.)
>
> 💡 **Lưu ý 2:** nếu file `Game_Config/G_Filtering_Monster_And_Item.txt` có `开启=1` thì bot dùng danh sách lọc toàn cục trong file đó, còn danh sách trong `gj.txt` không có tác dụng (trong gói đi kèm đang để `开启=0`, tức là `gj.txt` có hiệu lực). Khi bật `开启=1` thì phải sửa danh sách ở mục `[怪物过滤]` của file `G_Filtering_Monster_And_Item.txt` (mỗi tên quái một dòng). Danh sách này **cũng có sẵn `安特`**, nên phải xóa dòng `安特` ở đó nữa.
>
> 💡 **Lưu ý 3:** trong `BaseConfig.txt`, dòng chú thích ngay phía trên mục `[键鼠模式附加内存功能]` ghi rằng các tùy chọn `内存…` của mục này chỉ có hiệu lực khi `config\键鼠模式=1`, và tác giả dặn **dùng thận trọng vì có thể tăng nguy cơ bị khóa tài khoản**.

---

### A4. Dòng 19–69 — `地監記憶書  支持的地图` (Các bản đồ hỗ trợ Sách ghi nhớ hầm ngục)

**Mục đích:** liệt kê các bản đồ mà bot có thể dịch chuyển tới bằng **Sách ghi nhớ hầm ngục** (`地監記憶書`), một vật phẩm trong game dùng để dịch chuyển thẳng tới tầng hầm ngục (?). Khi bật `记忆卷轴传送=1`, bot dùng sách này để tới thẳng tầng hầm ngục thay vì đi bộ từng tầng.

Tiêu đề khối (dòng 19): `地監記憶書  支持的地图` = "Các bản đồ mà Sách ghi nhớ hầm ngục hỗ trợ".

| Dòng | Tên gốc (giữ nguyên) | Tên tiếng Việt / tiếng Anh |
|---|---|---|
| 20 | `象牙塔4樓` | Tháp Ngà (Ivory Tower, `象牙塔`) tầng 4 |
| 22 | `古魯丁地監1樓` | Hầm ngục Gludin (`古魯丁`) tầng 1 |
| 23 | `古魯丁地監2樓` | Hầm ngục Gludin tầng 2 |
| 24 | `古魯丁地監3樓` | Hầm ngục Gludin tầng 3 |
| 25 | `古魯丁地監4樓` | Hầm ngục Gludin tầng 4 |
| 26 | `古魯丁地監5樓` | Hầm ngục Gludin tầng 5 |
| 27 | `古魯丁地監6樓` | Hầm ngục Gludin tầng 6 |
| 29 | `龍之谷地監1樓` | Hầm ngục Thung lũng Rồng (Dragon Valley, `龍之谷`) tầng 1 |
| 30 | `龍之谷地監2樓` | Hầm ngục Thung lũng Rồng tầng 2 |
| 31 | `龍之谷地監3樓` | Hầm ngục Thung lũng Rồng tầng 3 |
| 32 | `龍之谷地監4樓` | Hầm ngục Thung lũng Rồng tầng 4 |
| 33 | `龍之谷地監5樓` | Hầm ngục Thung lũng Rồng tầng 5 |
| 34 | `龍之谷地監6樓` | Hầm ngục Thung lũng Rồng tầng 6 |
| 36 | `螞蟻洞窟地監1樓1` | Hầm ngục Hang Kiến (Ant Cave, `螞蟻洞窟`) tầng 1 – cửa 1 |
| 37 | `螞蟻洞窟地監1樓2` | Hầm ngục Hang Kiến tầng 1 – cửa 2 |
| 38 | `螞蟻洞窟地監1樓3` | Hầm ngục Hang Kiến tầng 1 – cửa 3 |
| 39 | `螞蟻洞窟地監1樓4` | Hầm ngục Hang Kiến tầng 1 – cửa 4 |
| 40 | `螞蟻洞窟地監1樓5` | Hầm ngục Hang Kiến tầng 1 – cửa 5 |
| 41 | `螞蟻洞窟地監1樓6` | Hầm ngục Hang Kiến tầng 1 – cửa 6 |
| 42 | `螞蟻洞窟地監1樓7` | Hầm ngục Hang Kiến tầng 1 – cửa 7 |
| 43 | `螞蟻洞窟地監1樓8` | Hầm ngục Hang Kiến tầng 1 – cửa 8 |
| 45 | `螞蟻洞窟地監2樓` | Hầm ngục Hang Kiến tầng 2 |
| 47 | `地下通道1樓` | Đường hầm ngầm (`地下通道`) tầng 1 |
| 48 | `地下通道2樓` | Đường hầm ngầm tầng 2 |
| 49 | `地下通道3樓` | Đường hầm ngầm tầng 3 |
| 51 | `伊娃王國` | Vương quốc Eva (Eva Kingdom) |
| 53 | `沙漠地監1樓` | Hầm ngục Sa mạc (Desert, `沙漠`) tầng 1 |
| 54 | `沙漠地監2樓` | Hầm ngục Sa mạc tầng 2 |
| 55 | `沙漠地監3樓` | Hầm ngục Sa mạc tầng 3 |
| 56 | `沙漠地監4樓` | Hầm ngục Sa mạc tầng 4 |
| 58 | `奇岩地監1樓` | Hầm ngục Giran (`奇岩`) tầng 1 |
| 59 | `奇岩地監2樓` | Hầm ngục Giran tầng 2 |
| 60 | `奇岩地監3樓` | Hầm ngục Giran tầng 3 |
| 61 | `奇岩地監4樓` | Hầm ngục Giran tầng 4 |
| 63 | `眠龍洞穴1樓` | Hang Rồng Ngủ (?) (`眠龍洞穴`) tầng 1 |
| 64 | `眠龍洞穴2樓` | Hang Rồng Ngủ (?) tầng 2 |
| 65 | `眠龍洞穴3樓` | Hang Rồng Ngủ (?) tầng 3 |

**Cách cài đặt (dòng 67–69):**

| Dòng gốc | Nghĩa | Giải thích |
|---|---|---|
| `设置方法如下` | Cách cài đặt như sau | |
| `打怪地图=龍之谷地監6樓` | Bản đồ đánh quái = Hầm ngục Thung lũng Rồng tầng 6 | Thay bằng tên bất kỳ trong bảng trên (chép đúng từng chữ). |
| `记忆卷轴传送=1` | Dịch chuyển bằng cuộn/sách ghi nhớ = bật | Theo chú thích trong `gj.txt`: `=0` tắt; `=1` bật, dịch chuyển tới điểm đã ghi nhớ thứ 1; `=2` tới điểm thứ 2; `=3` tới điểm thứ 3; cứ thế tiếp. Với cuộn ghi nhớ thường, bạn phải tự ghi nhớ vị trí trong game trước. **Nếu dùng `地監記憶書` (Sách ghi nhớ hầm ngục) thì chỉ cần điền `1`** (chú thích gốc: `如果是 地監記憶書 填1即可`). Trong `gj.txt` đi kèm, giá trị mặc định là `记忆卷轴传送=0` (tắt). |

```ini
打怪地图=龍之谷地監6樓
记忆卷轴传送=1
```

> 💡 **Lưu ý:** tên `螞蟻洞窟地監1樓1` (có số `1` ở cuối) ở danh sách này **khác** với tên `螞蟻洞窟地監1樓` (không có số `1`) ở khối Hang Kiến (A10). Nên dùng đúng tên của danh sách này khi bật `记忆卷轴传送=1`; nếu bot không nhận, thử tên còn lại (?).

---

### A5. Dòng 71–100 — `增加支持古鲁丁村的活动地图` (Bổ sung hỗ trợ các bản đồ sự kiện ở làng Gludin)

**Mục đích:** liệt kê các **bản đồ sự kiện** (`活动地图`) của **làng Gludin** (`古鲁丁村`, chữ Giản thể trong tiêu đề; có lẽ là các bản đồ đi vào từ làng Gludin (?)) mà bot đã hỗ trợ: hai nhóm **Vùng đất Ban phước bị ô nhiễm** (`污染的祝福之地`) và **Vùng đất Ban phước sa đọa** (`墮落的祝福之地`).

Từ vựng dùng trong tên bản đồ:

| Chữ gốc | Nghĩa |
|---|---|
| `污染的祝福之地` | Vùng đất Ban phước bị ô nhiễm (Polluted Blessed Land) |
| `墮落的祝福之地` | Vùng đất Ban phước sa đọa (Fallen/Corrupted Blessed Land) |
| `精靈之地` | Vùng đất Tinh linh (Spirit) (?) |
| `妖魔之地` | Vùng đất Yêu ma (quái vật / Orc) (?) |
| `人類之地` | Vùng đất Loài người (Human) |
| `妖精之地` | Vùng đất Tiên tộc (Elf) |
| `冬` / `秋` / `夏` / `春` | Mùa Đông / Thu / Hạ / Xuân |

**Nhóm "bị ô nhiễm" (dòng 73–76):**

| Dòng | Tên gốc (giữ nguyên) | Tên tiếng Việt |
|---|---|---|
| 73 | `污染的祝福之地 - 精靈之地` | Vùng đất Ban phước bị ô nhiễm – Vùng đất Tinh linh |
| 74 | `污染的祝福之地 - 妖魔之地` | Vùng đất Ban phước bị ô nhiễm – Vùng đất Yêu ma |
| 75 | `污染的祝福之地 - 人類之地` | Vùng đất Ban phước bị ô nhiễm – Vùng đất Loài người |
| 76 | `污染的祝福之地 - 妖精之地` | Vùng đất Ban phước bị ô nhiễm – Vùng đất Tiên tộc |

**Nhóm "sa đọa" theo mùa (dòng 78–96):**

| Dòng | Tên gốc (giữ nguyên) | Tên tiếng Việt |
|---|---|---|
| 78 | `墮落的祝福之地 - 冬 - 精靈之地` | Vùng đất Ban phước sa đọa – Đông – Vùng đất Tinh linh |
| 79 | `墮落的祝福之地 - 秋 - 精靈之地` | Vùng đất Ban phước sa đọa – Thu – Vùng đất Tinh linh |
| 80 | `墮落的祝福之地 - 夏 - 精靈之地` | Vùng đất Ban phước sa đọa – Hạ – Vùng đất Tinh linh |
| 81 | `墮落的祝福之地 - 春 - 精靈之地` | Vùng đất Ban phước sa đọa – Xuân – Vùng đất Tinh linh |
| 83 | `墮落的祝福之地 - 冬 - 妖魔之地` | Vùng đất Ban phước sa đọa – Đông – Vùng đất Yêu ma |
| 84 | `墮落的祝福之地 - 秋 - 妖魔之地` | Vùng đất Ban phước sa đọa – Thu – Vùng đất Yêu ma |
| 85 | `墮落的祝福之地 - 夏 - 妖魔之地` | Vùng đất Ban phước sa đọa – Hạ – Vùng đất Yêu ma |
| 86 | `墮落的祝福之地 - 春 - 妖魔之地` | Vùng đất Ban phước sa đọa – Xuân – Vùng đất Yêu ma |
| 88 | `墮落的祝福之地 - 冬 - 人類之地` | Vùng đất Ban phước sa đọa – Đông – Vùng đất Loài người |
| 89 | `墮落的祝福之地 - 秋 - 人類之地` | Vùng đất Ban phước sa đọa – Thu – Vùng đất Loài người |
| 90 | `墮落的祝福之地 - 夏 - 人類之地` | Vùng đất Ban phước sa đọa – Hạ – Vùng đất Loài người |
| 91 | `墮落的祝福之地 - 春 - 人類之地` | Vùng đất Ban phước sa đọa – Xuân – Vùng đất Loài người |
| 93 | `墮落的祝福之地 - 冬 - 妖精之地` | Vùng đất Ban phước sa đọa – Đông – Vùng đất Tiên tộc |
| 94 | `墮落的祝福之地 - 秋 - 妖精之地` | Vùng đất Ban phước sa đọa – Thu – Vùng đất Tiên tộc |
| 95 | `墮落的祝福之地 - 夏 - 妖精之地` | Vùng đất Ban phước sa đọa – Hạ – Vùng đất Tiên tộc |
| 96 | `墮落的祝福之地 - 春 - 妖精之地` | Vùng đất Ban phước sa đọa – Xuân – Vùng đất Tiên tộc |

**Cách cài đặt (dòng 98–100):**

| Dòng gốc | Nghĩa | Giải thích |
|---|---|---|
| `设置方法如下` | Cách cài đặt như sau | |
| `打怪地图=墮落的祝福之地 - 春 - 妖精之地` | Bản đồ đánh quái = Vùng đất Ban phước sa đọa – Xuân – Vùng đất Tiên tộc | Ví dụ 1. |
| `打怪地图=墮落的祝福之地 - 春 - 人類之地` | Bản đồ đánh quái = Vùng đất Ban phước sa đọa – Xuân – Vùng đất Loài người | Ví dụ 2. |

```ini
打怪地图=墮落的祝福之地 - 春 - 妖精之地
打怪地图=墮落的祝福之地 - 春 - 人類之地
```

> 💡 **Lưu ý:** đây là **hai ví dụ riêng**, không phải hai dòng ghi cùng lúc. Trong mỗi mục cấu hình chỉ để **một** dòng `打怪地图=`. Mỗi dấu `-` đều có một dấu cách trước và một dấu cách sau (ví dụ `之地 - 春 - 妖精`).

---

### A6. Dòng 104–141 — `增加支持网咖地图` (Bổ sung hỗ trợ bản đồ quán net)

**Mục đích:** liệt kê các bản đồ **dành cho quán net** (`網咖`, PC bang). Đây là các khu riêng trong game, thường chỉ vào được khi chơi ở quán net đối tác (?); tên bản đồ có hậu tố `(網咖)`.

**Danh sách (dòng 106–130):**

| Dòng | Tên gốc (giữ nguyên) | Tên tiếng Việt |
|---|---|---|
| 106 | `說話之島地監1樓(網咖)` | Hầm ngục Talking Island (Đảo Nói Chuyện, `說話之島`) tầng 1 (quán net) |
| 107 | `說話之島地監2樓(網咖)` | Hầm ngục Talking Island tầng 2 (quán net) |
| 109 | `古魯丁地監1樓(網咖)` | Hầm ngục Gludin tầng 1 (quán net) |
| 110 | `古魯丁地監2樓(網咖)` | Hầm ngục Gludin tầng 2 (quán net) |
| 111 | `古魯丁地監3樓(網咖)` | Hầm ngục Gludin tầng 3 (quán net) |
| 112 | `古魯丁地監4樓(網咖)` | Hầm ngục Gludin tầng 4 (quán net) |
| 113 | `古魯丁地監5樓(網咖)` | Hầm ngục Gludin tầng 5 (quán net) |
| 114 | `古魯丁地監6樓(網咖)` | Hầm ngục Gludin tầng 6 (quán net) |
| 115 | `古魯丁地監7樓(網咖)` | Hầm ngục Gludin tầng 7 (quán net) |
| 117 | `沙漠地監1樓(網咖)` | Hầm ngục Sa mạc tầng 1 (quán net) |
| 118 | `沙漠地監2樓(網咖)` | Hầm ngục Sa mạc tầng 2 (quán net) |
| 119 | `沙漠地監3樓(網咖)` | Hầm ngục Sa mạc tầng 3 (quán net) |
| 120 | `沙漠地監4樓(網咖)` | Hầm ngục Sa mạc tầng 4 (quán net) |
| 122 | `污染的祝福之地 - 精靈之地(網咖)` | Vùng đất Ban phước bị ô nhiễm – Vùng đất Tinh linh (quán net) |
| 123 | `污染的祝福之地 - 妖魔之地(網咖)` | Vùng đất Ban phước bị ô nhiễm – Vùng đất Yêu ma (quán net) |
| 124 | `污染的祝福之地 - 人類之地(網咖)` | Vùng đất Ban phước bị ô nhiễm – Vùng đất Loài người (quán net) |
| 125 | `污染的祝福之地 - 妖精之地(網咖)` | Vùng đất Ban phước bị ô nhiễm – Vùng đất Tiên tộc (quán net) |
| 127 | `墮落的祝福之地 - 精靈之地(網咖)` | Vùng đất Ban phước sa đọa – Vùng đất Tinh linh (quán net) |
| 128 | `墮落的祝福之地 - 妖魔之地(網咖)` | Vùng đất Ban phước sa đọa – Vùng đất Yêu ma (quán net) |
| 129 | `墮落的祝福之地 - 人類之地(網咖)` | Vùng đất Ban phước sa đọa – Vùng đất Loài người (quán net) |
| 130 | `墮落的祝福之地 - 妖精之地(網咖)` | Vùng đất Ban phước sa đọa – Vùng đất Tiên tộc (quán net) |

> 💡 **Lưu ý:** bản quán net của `墮落的祝福之地` **không có mùa** (`冬/秋/夏/春`) trong tên, khác với bản thường ở A5.

**Ghi chú và cách cài đặt (dòng 132–141):**

| Dòng gốc | Nghĩa | Giải thích |
|---|---|---|
| `台服需要自己购买沙漏放到背包中（脚本会自动使用沙漏）` | Server Đài Loan (`台服`) phải tự mua **đồng hồ cát** (`沙漏`) bỏ vào túi đồ (script sẽ tự động dùng đồng hồ cát) | Bot không tự mua đồng hồ cát; bạn phải mua sẵn và để trong túi đồ, bot chỉ tự **dùng** nó. Có lẽ đồng hồ cát là vật phẩm cho thời gian vào các bản đồ quán net trên server Đài Loan (?). Câu này chỉ nói về server Đài Loan; file không nhắc gì tới server Hàn. |
| `设置方法如下` | Cách cài đặt như sau | |
| `打怪地图=古魯丁地監1樓(網咖)` | Bản đồ đánh quái = Hầm ngục Gludin tầng 1 (quán net) | Ví dụ cho hầm ngục có tầng. |
| `这样设置为进入第1个地图` | Đặt như dòng dưới thì bot sẽ vào **bản đồ thứ 1** (của nhóm) | Câu này giải thích cho dòng ngay sau nó. |
| `打怪地图=污染的祝福之地(網咖)` | Bản đồ đánh quái = Vùng đất Ban phước bị ô nhiễm (quán net) | Chỉ ghi tên nhóm, không ghi khu con → bot vào khu đầu tiên. Theo thứ tự danh sách, khu đầu tiên có lẽ là `精靈之地` (?). |
| `这样设置为进入指定的地图` | Đặt như các dòng dưới thì bot sẽ vào **đúng bản đồ được chỉ định** | Câu này giải thích cho 2 dòng ngay sau nó. |
| `打怪地图=污染的祝福之地 - 精靈之地(網咖)` | Bản đồ đánh quái = Vùng đất Ban phước bị ô nhiễm – Vùng đất Tinh linh (quán net) | Ví dụ chỉ định khu. |
| `打怪地图=污染的祝福之地 - 妖魔之地(網咖)` | Bản đồ đánh quái = Vùng đất Ban phước bị ô nhiễm – Vùng đất Yêu ma (quán net) | Ví dụ chỉ định khu. |

Nguyên văn các dòng mẫu:

```ini
打怪地图=古魯丁地監1樓(網咖)

打怪地图=污染的祝福之地(網咖)

打怪地图=污染的祝福之地 - 精靈之地(網咖)
打怪地图=污染的祝福之地 - 妖魔之地(網咖)
```

> 💡 **Lưu ý:** mỗi dòng trên là một ví dụ riêng; trong một mục cấu hình chỉ để một dòng `打怪地图=`. Ngoặc trong `(網咖)` là ngoặc tròn thường `( )`.

---

### A7. Dòng 146–149 — `增加支持說話之島地監` (Bổ sung hỗ trợ hầm ngục Talking Island)

| Dòng | Tên gốc (giữ nguyên) | Tên tiếng Việt |
|---|---|---|
| 147 | `說話之島地監1樓` | Hầm ngục Talking Island (Đảo Nói Chuyện, `說話之島`) tầng 1 |
| 148 | `說話之島地監2樓` | Hầm ngục Talking Island tầng 2 |
| 149 | `地下通道` | Đường hầm ngầm (không có số tầng) |

> 💡 **Lưu ý:** `地下通道` ở đây **không có số tầng**, khác với `地下通道1樓` / `2樓` / `3樓` ở khối Heine (A11). Nằm trong khối Talking Island nên có lẽ đây là đường hầm ngầm ở khu Talking Island (?). Chép đúng tên tương ứng với nơi bạn muốn tới.

### A8. Dòng 150–157 — `增加支持古魯丁地監` (Bổ sung hỗ trợ hầm ngục Gludin)

| Dòng | Tên gốc (giữ nguyên) | Tên tiếng Việt |
|---|---|---|
| 151 | `古魯丁地監1樓` | Hầm ngục Gludin (`古魯丁`) tầng 1 |
| 152 | `古魯丁地監2樓` | Hầm ngục Gludin tầng 2 |
| 153 | `古魯丁地監3樓` | Hầm ngục Gludin tầng 3 |
| 154 | `古魯丁地監4樓` | Hầm ngục Gludin tầng 4 |
| 155 | `古魯丁地監5樓` | Hầm ngục Gludin tầng 5 |
| 156 | `古魯丁地監6樓` | Hầm ngục Gludin tầng 6 |
| 157 | `古魯丁地監7樓` | Hầm ngục Gludin tầng 7 |

> 💡 **Lưu ý:** `古魯丁地監7樓` có ở đây nhưng **không có** trong danh sách Sách ghi nhớ hầm ngục (A4 chỉ có tầng 1–6). Bot vẫn đi tới được tầng 7, nhưng có lẽ không dùng sách để dịch chuyển thẳng tới tầng 7 (?).

### A9. Dòng 158–162 — `增加支持奇岩地監` (Bổ sung hỗ trợ hầm ngục Giran)

| Dòng | Tên gốc (giữ nguyên) | Tên tiếng Việt |
|---|---|---|
| 159 | `奇岩地監1樓` | Hầm ngục Giran (`奇岩`) tầng 1 |
| 160 | `奇岩地監2樓` | Hầm ngục Giran tầng 2 |
| 161 | `奇岩地監3樓` | Hầm ngục Giran tầng 3 |
| 162 | `奇岩地監4樓` | Hầm ngục Giran tầng 4 |

### A10. Dòng 163–185 — `蚂蚁洞窟地图    有8个1楼的地图，分别为以下名字` (Bản đồ Hang Kiến)

**Tiêu đề khối:** "Bản đồ Hang Kiến (`蚂蚁洞窟`, chữ Giản thể trong tiêu đề) — có 8 bản đồ tầng 1, tên lần lượt như sau". Hang Kiến có **8 cửa hang**, mỗi cửa dẫn vào một bản đồ tầng 1 riêng.

| Dòng | Tên gốc (giữ nguyên) | Tên tiếng Việt |
|---|---|---|
| 164 | `螞蟻洞窟地監1樓` | Hầm ngục Hang Kiến (`螞蟻洞窟`) tầng 1 – cửa 1 |
| 165 | `螞蟻洞窟地監1樓2` | Hầm ngục Hang Kiến tầng 1 – cửa 2 |
| 166 | `螞蟻洞窟地監1樓3` | Hầm ngục Hang Kiến tầng 1 – cửa 3 |
| 167 | `螞蟻洞窟地監1樓4` | Hầm ngục Hang Kiến tầng 1 – cửa 4 |
| 168 | `螞蟻洞窟地監1樓5` | Hầm ngục Hang Kiến tầng 1 – cửa 5 |
| 169 | `螞蟻洞窟地監1樓6` | Hầm ngục Hang Kiến tầng 1 – cửa 6 |
| 170 | `螞蟻洞窟地監1樓7` | Hầm ngục Hang Kiến tầng 1 – cửa 7 |
| 171 | `螞蟻洞窟地監1樓8` | Hầm ngục Hang Kiến tầng 1 – cửa 8 |

**Tọa độ cửa hang (dòng 173–181):**

Dòng 173: `可以在控制台取角色坐标，然后对比下面就知道站在那个洞门口了` = "Bạn có thể lấy tọa độ nhân vật trong bảng điều khiển (`控制台`) của bot, rồi so với danh sách dưới đây là biết mình đang đứng ở cửa hang nào."

`进洞坐标` = tọa độ vào hang. `x` và `y` là tọa độ trong game.

| Dòng gốc | Nghĩa | Tên bản đồ tương ứng để điền |
|---|---|---|
| `1樓   进洞坐标 x = 32911,y = 33223` | Tầng 1 (cửa 1): tọa độ vào hang x = 32911, y = 33223 | `螞蟻洞窟地監1樓` |
| `1樓2 进洞坐标 x = 32836,y = 33171` | Tầng 1 – cửa 2: x = 32836, y = 33171 | `螞蟻洞窟地監1樓2` |
| `1樓3 进洞坐标 x = 32796,y = 33189` | Tầng 1 – cửa 3: x = 32796, y = 33189 | `螞蟻洞窟地監1樓3` |
| `1樓4 进洞坐标 x = 32789,y = 33256` | Tầng 1 – cửa 4: x = 32789, y = 33256 | `螞蟻洞窟地監1樓4` |
| `1樓5 进洞坐标 x = 32926,y = 33249` | Tầng 1 – cửa 5: x = 32926, y = 33249 | `螞蟻洞窟地監1樓5` |
| `1樓6 进洞坐标 x = 32845,y = 33292` | Tầng 1 – cửa 6: x = 32845, y = 33292 | `螞蟻洞窟地監1樓6` |
| `1樓7 进洞坐标 x = 32790,y = 33146` | Tầng 1 – cửa 7: x = 32790, y = 33146 | `螞蟻洞窟地監1樓7` |
| `1樓8 进洞坐标 x = 32756,y = 33205` | Tầng 1 – cửa 8: x = 32756, y = 33205 | `螞蟻洞窟地監1樓8` |

Nguyên văn (giữ nguyên mọi con số):

```text
1樓   进洞坐标 x = 32911,y = 33223
1樓2 进洞坐标 x = 32836,y = 33171
1樓3 进洞坐标 x = 32796,y = 33189
1樓4 进洞坐标 x = 32789,y = 33256
1樓5 进洞坐标 x = 32926,y = 33249
1樓6 进洞坐标 x = 32845,y = 33292
1樓7 进洞坐标 x = 32790,y = 33146
1樓8 进洞坐标 x = 32756,y = 33205
```

> 💡 **Lưu ý:** các dòng tọa độ trên **chỉ để tra cứu** (biết mình đang đứng ở cửa nào), không phải dòng cấu hình. Đừng chép chúng vào `gj.txt`.

**Cách cài đặt (dòng 183–185):**

| Dòng gốc | Nghĩa | Giải thích |
|---|---|---|
| `设置方法如下` | Cách cài đặt như sau | |
| `打怪地图=螞蟻洞窟地監1樓` | Bản đồ đánh quái = Hang Kiến tầng 1 (cửa 1) | Ví dụ 1. |
| `打怪地图=螞蟻洞窟地監1樓5` | Bản đồ đánh quái = Hang Kiến tầng 1 – cửa 5 | Ví dụ 2. |

```ini
打怪地图=螞蟻洞窟地監1樓
打怪地图=螞蟻洞窟地監1樓5
```

> 💡 **Lưu ý:** hai dòng trên là hai ví dụ riêng, chỉ để một dòng trong mỗi mục cấu hình. Cửa 1 ở khối này tên là `螞蟻洞窟地監1樓` (không có số `1` cuối), nhưng trong danh sách Sách ghi nhớ hầm ngục (A4) lại là `螞蟻洞窟地監1樓1`. Xem thêm A16.

### A11. Dòng 187–192 — `增加支持海音地监` (Bổ sung hỗ trợ hầm ngục Heine)

Tiêu đề viết bằng chữ Giản thể: `海音` = Heine, `地监` = hầm ngục.

| Dòng | Tên gốc (giữ nguyên) | Tên tiếng Việt |
|---|---|---|
| 188 | `地下通道1樓` | Đường hầm ngầm (`地下通道`) tầng 1 |
| 189 | `地下通道2樓` | Đường hầm ngầm tầng 2 |
| 190 | `地下通道3樓` | Đường hầm ngầm tầng 3 |
| 192 | `伊娃王國` | Vương quốc Eva (Eva Kingdom) |

### A12. Dòng 194–198 — `增加支持沙漠地監` (Bổ sung hỗ trợ hầm ngục Sa mạc)

| Dòng | Tên gốc (giữ nguyên) | Tên tiếng Việt |
|---|---|---|
| 195 | `沙漠地監1樓` | Hầm ngục Sa mạc (Desert, `沙漠`) tầng 1 |
| 196 | `沙漠地監2樓` | Hầm ngục Sa mạc tầng 2 |
| 197 | `沙漠地監3樓` | Hầm ngục Sa mạc tầng 3 |
| 198 | `沙漠地監4樓` | Hầm ngục Sa mạc tầng 4 |

### A13. Dòng 199–202 — `增加支持眠龍洞穴` (Bổ sung hỗ trợ Hang Rồng Ngủ (?))

| Dòng | Tên gốc (giữ nguyên) | Tên tiếng Việt |
|---|---|---|
| 200 | `眠龍洞穴1樓` | Hang Rồng Ngủ (?) (`眠龍洞穴`) tầng 1 |
| 201 | `眠龍洞穴2樓` | Hang Rồng Ngủ (?) tầng 2 |
| 202 | `眠龍洞穴3樓` | Hang Rồng Ngủ (?) tầng 3 |

### A14. Dòng 203–212 — `增加支持龍之谷地監` (Bổ sung hỗ trợ hầm ngục Thung lũng Rồng)

| Dòng | Tên gốc (giữ nguyên) | Tên tiếng Việt |
|---|---|---|
| 204 | `龍之谷地監1樓` | Hầm ngục Thung lũng Rồng (Dragon Valley, `龍之谷`) tầng 1 (khu 1) |
| 205 | `龍之谷地監1樓2` | Hầm ngục Thung lũng Rồng tầng 1 – khu 2 |
| 206 | `龍之谷地監1樓3` | Hầm ngục Thung lũng Rồng tầng 1 – khu 3 |
| 207 | `龍之谷地監1樓4` | Hầm ngục Thung lũng Rồng tầng 1 – khu 4 |
| 209 | `龍之谷地監2樓` | Hầm ngục Thung lũng Rồng tầng 2 |
| 210 | `龍之谷地監3樓` | Hầm ngục Thung lũng Rồng tầng 3 |
| 211 | `龍之谷地監4樓` | Hầm ngục Thung lũng Rồng tầng 4 |
| 212 | `龍之谷地監5樓` | Hầm ngục Thung lũng Rồng tầng 5 |

> 💡 **Lưu ý:** giống Hang Kiến, tầng 1 của Thung lũng Rồng có **nhiều bản đồ** (`1樓`, `1樓2`, `1樓3`, `1樓4`), có lẽ ứng với các lối vào khác nhau (?). Khối này không liệt kê `龍之谷地監6樓`, nhưng danh sách Sách ghi nhớ hầm ngục (A4) lại có tầng 6 và chính ví dụ cài đặt dùng `龍之谷地監6樓`.

### A15. Dòng 213–221 — `增加支持象牙塔` (Bổ sung hỗ trợ Tháp Ngà)

| Dòng | Tên gốc (giữ nguyên) | Tên tiếng Việt |
|---|---|---|
| 214 | `象牙塔1樓` | Tháp Ngà (Ivory Tower, `象牙塔`) tầng 1 |
| 215 | `象牙塔2樓` | Tháp Ngà tầng 2 |
| 216 | `象牙塔3樓` | Tháp Ngà tầng 3 |
| 217 | `象牙塔4樓` | Tháp Ngà tầng 4 |
| 218 | `象牙塔5樓` | Tháp Ngà tầng 5 |
| 219 | `象牙塔6樓` | Tháp Ngà tầng 6 |
| 220 | `象牙塔7樓` | Tháp Ngà tầng 7 |
| 221 | `象牙塔8樓` | Tháp Ngà tầng 8 |

> 💡 **Lưu ý:** bot đi được tầng 1–8 của Tháp Ngà, nhưng trong danh sách Sách ghi nhớ hầm ngục (A4) chỉ có `象牙塔4樓`.

### A16. Tổng hợp những điểm dễ nhầm

| Vấn đề | Chi tiết | Nên làm |
|---|---|---|
| Hang Kiến cửa 1 có 2 cách viết | A4 (Sách ghi nhớ hầm ngục) ghi `螞蟻洞窟地監1樓1`; A10 (khối Hang Kiến và ví dụ cài đặt) ghi `螞蟻洞窟地監1樓` | Đi bộ thường: dùng `螞蟻洞窟地監1樓`. Dùng sách ghi nhớ (`记忆卷轴传送=1`): thử `螞蟻洞窟地監1樓1` trước; nếu bot không nhận thì thử tên kia (?). |
| Thung lũng Rồng: danh sách hai nơi khác nhau | A4 có tầng 1–6; A14 có `1樓`, `1樓2`, `1樓3`, `1樓4`, tầng 2–5 | Chọn tên trong danh sách khớp với cách đi (có hay không dùng sách ghi nhớ). |
| Gludin tầng 7 | Có trong A8 và bản quán net (A6), không có trong A4 | Không dùng sách ghi nhớ cho tầng 7 (?). |
| Tháp Ngà | A15 có tầng 1–8, A4 chỉ có tầng 4 | Sách ghi nhớ chỉ dùng cho `象牙塔4樓`. |
| `地下通道` | A7 ghi `地下通道` (không số tầng); A4 và A11 ghi `地下通道1樓`–`3樓` | Hai tên khác nhau, chép đúng tên cần dùng. |
| Bản quán net của vùng "sa đọa" | `墮落的祝福之地 - …(網咖)` không có mùa | Đừng thêm `冬/秋/夏/春` vào tên bản quán net. |
| Giản thể và Phồn thể | Tiêu đề khối có lúc là Giản thể, tên bản đồ là Phồn thể | Luôn chép tên từ ô `code` trong các bảng danh sách. |
| Nhiều dòng `打怪地图=` trong ví dụ | Đó là các ví dụ thay thế cho nhau | Mỗi mục cấu hình chỉ để một dòng `打怪地图=`. |

---

## Phần B — `组队服务器/使用说明.txt` (Hướng dẫn server tổ đội)

### B0. Mục đích của file

Thư mục `组队服务器` (**server tổ đội**) dành cho chương trình phía server giúp nhiều máy chạy bot **tự lập tổ đội với nhau qua mạng LAN** (`局域网`). File hướng dẫn trong đó chỉ có 3 dòng, nói về vị trí đặt server và cách khớp cổng (port). Trong gói, thư mục này gồm chương trình server `组队服务器.exe`, file cấu hình `config.ini` và file hướng dẫn `使用说明.txt` (danh sách file đầy đủ ở `03-cau-hinh-chung-va-cau-truc-goi.md`).

> ⚠️ **Quy tắc khi sửa cấu hình:** giữ nguyên mọi chữ Trung Quốc và tên mục / tên khóa (ví dụ `[config]`, `[局域网组队配置]`, `port`, `ip`); **chỉ thay số / giá trị** sau dấu `=`.

### B1. Dịch từng dòng

| Dòng gốc | Nghĩa | Giải thích |
|---|---|---|
| `服务端需要与脚本控制台在同一个局域网中` | Server (`服务端`) phải nằm **cùng một mạng LAN** (`局域网`) với bảng điều khiển của bot (`脚本控制台`). | Máy chạy server và các máy chạy bot phải chung mạng nội bộ (ví dụ cùng một router). |
| `你可以把服务端放在远程同步专家的机器上` | Bạn có thể đặt server trên máy đang chạy **远程同步专家** | `远程同步专家` là tên một phần mềm (dịch sát: "Chuyên gia đồng bộ từ xa", Remote Sync Expert), có lẽ là phần mềm điều khiển/đồng bộ nhiều máy từ xa (?). Trong gói không có file nào khác nhắc tới tên này. Ý có lẽ là có thể đặt server lên máy "chủ" dùng để quản lý các máy khác (?). |
| `服务端只需要设置好端口就行，客户机的端口要一致` | Server **chỉ cần cài đúng cổng** (`端口`, port) là xong; cổng trên **các máy khách** (`客户机`) phải **giống hệt**. | Server không cần chỉnh gì khác ngoài cổng. Máy khách (máy chạy bot) phải ghi cùng số cổng đó. |

### B2. Khớp cổng ở đâu? (tham khảo từ các file cấu hình đi kèm)

| Phía | File | Dòng cần xem |
|---|---|---|
| Server | `组队服务器/config.ini`, mục `[config]` | `port=9527` |
| Máy khách (máy chạy bot) | `Game_Config/BaseConfig.txt`, mục `[局域网组队配置]` (cấu hình tổ đội LAN) | `port=9527` và `ip=127.0.0.1` |

```ini
; 组队服务器/config.ini (phía server)
[config]
port=9527
```

> 💡 **Lưu ý 1:** hai số `port` (mặc định đều là `9527`) **phải trùng nhau**. Nếu đổi ở server thì đổi ở mọi máy khách.
>
> 💡 **Lưu ý 2:** `ip=127.0.0.1` nghĩa là "chính máy này". Nếu server đặt ở máy khác, phải sửa `ip=` thành địa chỉ IP của máy chạy server (chú thích gốc trong `BaseConfig.txt`: `局域网的ip 或者外网ip` = "IP mạng LAN hoặc IP mạng ngoài").
>
> 💡 **Lưu ý 3:** cũng trong mục `[局域网组队配置]`, khóa `队伍最大人数` (số người tối đa mỗi đội) đang để `=0`, nghĩa là **tắt** tổ đội LAN (theo chú thích gốc; game cho tối đa 8 người một đội, có thể đặt `=8`). Các máy có cùng `组队密码` (mật khẩu tổ đội; trong gói đặt sẵn `组队密码=666`) sẽ được server gom vào cùng đội, ưu tiên những máy có cùng `打怪地图` và `打怪坐标` gần nhau. Chi tiết các khóa này nằm ở phần dịch `BaseConfig.txt`.
