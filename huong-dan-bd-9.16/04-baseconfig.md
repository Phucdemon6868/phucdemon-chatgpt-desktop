# Game_Config/BaseConfig.txt — Cấu hình chơi chính của bot (dịch & giải thích tiếng Việt)

> **Tệp gốc:** `Game_Config/BaseConfig.txt`: 218 dòng, mã hóa UTF-8, xuống dòng kiểu Windows (CRLF).
> **Gói:** `天堂经典版 Bd` bản 9.16, bot treo máy (auto farm) cho Lineage Classic.

## Tệp này dùng để làm gì?

`BaseConfig.txt` là **file cấu hình gameplay quan trọng nhất** của bot. Nó quyết định gần như mọi hành vi trong game:
đăng nhập, bảo vệ nhân vật (về thành, nghỉ ngơi, nhà trọ), đi mua món đặc biệt ở NPC, nhặt đồ, tự dịch chuyển ngẫu nhiên khi bị kẹt,
né người chơi/quái, lịch nghỉ, đổi file treo máy theo giờ, chế độ bộ nhớ, cuộn biến hình, đổi đồ, tạo nhân vật, thuốc tăng tốc,
kỹ năng/buff, uống thuốc, phản công và tổ đội (trên cùng máy hoặc qua mạng LAN).

## ⚠️ Đọc trước khi sửa file

1. **Giữ nguyên mọi chữ Trung Quốc.** Bot đọc chữ đúng từng ký tự: tên mục `[...]`, tên khóa (bên trái dấu `=`), tên bản đồ, vật phẩm, NPC, kỹ năng. Khi sửa, **chỉ thay số/giá trị** bên phải dấu `=`. Phần tiếng Việt trong tài liệu này chỉ giúp bạn hiểu, **đừng** gõ tiếng Việt vào file.
2. Một dòng có dạng `khóa=giá trị        -- chú thích`. Phần sau `--` là chú thích viết cho người đọc. Các dòng chỉ có dấu `-----` là đường kẻ trang trí.
3. File trộn chữ **Phồn thể** và **Giản thể** (ví dụ `說話之島村` là phồn thể, `古鲁丁7楼` là giản thể). Hãy chép **y nguyên** ký tự như trong file/trong game, đừng tự chuyển đổi qua lại.
4. Khi nhập danh sách, dùng **dấu phẩy tiếng Anh** `,` (không dùng dấu phẩy Trung `，`) và không thêm khoảng trắng thừa. Dấu `|` dùng để ngăn cách các khung giờ hoặc các điều kiện của kỹ năng.
5. 💡 Lưu file ở mã hóa **UTF-8** như bản gốc. Nếu trình soạn thảo lưu sang ANSI/mã khác thì chữ Trung bị hỏng và bot không đọc được.
6. 💡 Theo ghi chú trong mục `[休息配置]`, bot có bộ nhớ đệm (cache): sửa xong, muốn có hiệu lực ngay thì **khởi động lại script**.

**Quy ước chung:** `=0` thường là **tắt**, `=1` là **bật** (trừ khi ghi khác). Đơn vị: `秒` = giây, `分钟` = phút, `%`/`百分比` = phần trăm.
Cột **#** trong các bảng là số dòng trong file gốc. Dấu `\|` trong bảng chính là ký tự `|` trong file (phải viết như vậy để bảng Markdown không bị vỡ).

## Tổng quan các mục (đúng thứ tự trong file)

| # | Mục gốc | Tên tiếng Việt | Tóm tắt |
|---|---|---|---|
| 1 | `[登录配置]` | Cấu hình đăng nhập | Thời gian chờ màn hình xác thực, bỏ qua "xác thực giả", và một mục xác minh thiết bị (không hướng dẫn). |
| 6 | `[角色保护]` | Bảo vệ nhân vật | Nghỉ khi phải về thành/rớt mạng quá nhiều, dùng cuộn khi máu/mana thấp, nghỉ nhà trọ. |
| 20 | `[NPC特殊购买]` | Mua đặc biệt ở NPC | Tự đi mua cuộn phù phép giáp `對盔甲施法的卷軸`, có giới hạn số lần, thời gian, thời gian chờ. |
| 29 | `[挂机全局配置]` | Cấu hình treo máy toàn cục | Đánh quái trên đường, phản công, nhặt tiền/đồ, cuộn ghi nhớ, máu/mana để xuất phát (thay cho `gj.txt` khi bật). |
| 42 | `[触发随机传送配置]` | Kích hoạt dịch chuyển ngẫu nhiên | Tự dịch chuyển ngẫu nhiên khi kẹt đường, lâu không có tiền, không có quái, bị quái/người/thú cưng đánh; nghỉ khi bị PK liên tục. |
| 68 | `[触发回城休息配置]` | Kích hoạt về thành nghỉ / né tránh | Thấy (hoặc bị đánh bởi) người/quái trong danh sách né thì về thành nghỉ hoặc dịch chuyển chạy và tạm "cấm" điểm treo máy. |
| 84 | `[休息配置]` | Lịch nghỉ | Chạy X phút nghỉ Y phút, hoặc nghỉ theo khung giờ. |
| 96 | `[按时间切换挂机配置]` | Đổi file treo máy theo giờ | Mỗi khung giờ dùng một file treo máy khác (`gj2.txt`, `gj3.txt`...). |
| 108 | `[键鼠模式附加内存功能]` | Chức năng bộ nhớ bổ sung cho chế độ bàn phím-chuột | Cho từng thao tác (đi, đánh, nhặt, kỹ năng...) chạy bằng chế độ bộ nhớ thay vì bàn phím-chuột. |
| 120 | `[基础配置]` | Cấu hình cơ bản | Cuộn biến hình, tự đổi đồ, tự học kỹ năng, tố cáo, chuyển hóa máu/mana, tự mua cung, cuộn dịch chuyển về Talking Island, mua thịt, đổi mũ... |
| 139 | `[创建角色配置]` | Cấu hình tạo nhân vật | Chọn nghề và kiểu tên ngẫu nhiên khi tạo nhân vật. |
| 144 | `[使用加速药水]` | Dùng thuốc tăng tốc | Bật/tắt từng loại thuốc tăng tốc, bánh quy Tiên, thuốc xanh... |
| 158 | `[解释技能配置说明 这里为无效字段]` | Giải thích cách cấu hình kỹ năng (mục không có hiệu lực) | Ví dụ và cách đọc điều kiện `hp`/`mp`/`time`. |
| 168 | `[技能配置_妖精]` | Cấu hình kỹ năng (Elf; theo ghi chú thì dùng chung cho mọi nghề) | Điều kiện dùng từng kỹ năng/buff. |
| 190 | `[吃药配置]` | Cấu hình uống thuốc | Ngưỡng máu/mana để uống thuốc. |
| 195 | `[反击配置]` | Cấu hình phản công | Phản công chó (thú cưng), người chơi, thú triệu hồi của pháp sư. |
| 201 | `[组队配置]` | Tổ đội trên cùng máy | Tự lập đội cho các tài khoản trên máy này, tập trung đánh, buff/hồi máu cho đồng đội. |
| 209 | `[局域网组队配置]` | Tổ đội qua mạng LAN | Lập đội giữa nhiều máy qua server tổ đội (`组队服务器`), mật khẩu đội, IP, cổng. |

---

### [登录配置] — Cấu hình đăng nhập

Các thiết lập cho bước đăng nhập vào game (qua launcher Purple, trong file gọi là `紫P`).

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 2 | `认证界面等待时间=50` | Thời gian chờ ở màn hình xác thực = 50 | Chú thích gốc: "Quá thời gian này mà vẫn chưa vào được màn hình đồng ý (điều khoản) thì buộc đóng game và đăng nhập lại." File không ghi đơn vị, nhiều khả năng là **giây** (?). 💡 Máy yếu/mạng chậm có thể tăng số này. |
| 3 | `自动跳过假验证=0` | Tự động bỏ qua xác thực giả | `=0` tắt, `=1` bật. Chú thích gốc: "bỏ qua bước xác thực giả khi đăng nhập". "Xác thực giả" (`假验证`/`假认证`) (?) có lẽ là một bảng/màn hình yêu cầu xác thực hiện ra lúc đăng nhập nhưng thực ra không bắt buộc, bot sẽ bấm bỏ qua. Mặc định: tắt. |
| 4 | `自动接码验证设备` | tự động nhận mã SMS để xác minh thiết bị | ⚠️ Tài liệu này không hướng dẫn phần này. |

---

### [角色保护] — Bảo vệ nhân vật

Nhóm chức năng giữ an toàn cho nhân vật: nghỉ khi phải về thành hoặc rớt mạng quá nhiều, dùng cuộn khi máu/mana thấp, vào nhà trọ (`旅馆`) hồi máu.
Liên quan: "về thành" (`回城`), "cuộn về thành" (`回城卷`), "cuộn dịch chuyển về Talking Island (Đảo Nói Chuyện)" (`说话卷`), "cuộn dịch chuyển ngẫu nhiên" (`随机卷`).

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 7 | `开启=1` | Bật = 1 | Chú thích gốc: "`=1` là công tắc tổng, phải bật thì mọi chức năng bên dưới mới có hiệu lực." `=0` thì cả mục này bị tắt. |
| 8 | `几分钟内回城=60` | Trong vòng bao nhiêu phút (đếm số lần về thành) = 60 | `=0` tắt chức năng về thành nghỉ ngơi. Chú thích gốc: "Ý nghĩa ở đây là: trong 60 phút, nếu liên tục bị kích hoạt về thành 10 lần thì nghỉ 30 phút. Về thành bình thường để mua bán **không** tính; chết tính là 1 lần về thành; máu thấp dùng cuộn về thành tính là 1 lần về thành." 💡 Số "30 phút" trong chú thích chỉ là ví dụ; thời gian nghỉ thật lấy từ `休息几分钟` (dòng 11, hiện là 10) (?). |
| 9 | `连续回城几次=10` | Số lần về thành liên tiếp = 10 | Ngưỡng số lần về thành trong khoảng thời gian ở dòng 8. Đủ số lần thì nhân vật nghỉ. |
| 10 | `连续掉线几次=0` | Số lần rớt mạng liên tiếp | `=0` tắt. Chú thích gốc: "`=60` nghĩa là trong 60 phút rớt mạng 10 lần thì sau khi vào lại game sẽ nghỉ ở thị trấn 30 phút." 💡 Chú thích này hơi lộn xộn (ví dụ `=60` có vẻ chép từ dòng 8). Cách hiểu hợp lý (?): số điền ở đây là **số lần rớt mạng** (ví dụ `10`), khoảng thời gian đếm có lẽ dùng chung dòng 8, thời gian nghỉ lấy từ dòng 11. |
| 11 | `休息几分钟=10` | Nghỉ bao nhiêu phút = 10 | Thời gian nghỉ (phút) khi điều kiện ở dòng 8–10 bị kích hoạt. |
| 12 | `低血量使用回城卷=30` | Máu thấp thì dùng cuộn về thành = 30 | Đơn vị: % máu. Chú thích gốc: "Máu dưới 30% thì dùng cuộn dịch chuyển về Talking Island (`说话卷`) hoặc cuộn về thành (`回城卷`) hoặc phép `世界樹的呼喚` (Tiếng gọi Cây Thế giới, Teleport to Mother: phép của Elf đưa nhân vật về Cây Thế giới). `=0` là không dùng." |
| 13 | `低血量使用随机卷=0` | Máu thấp thì dùng cuộn dịch chuyển ngẫu nhiên | Đơn vị: % máu. Chú thích gốc: "Máu dưới 50% thì dùng cuộn ngẫu nhiên. `=0` là không dùng." (Ví dụ trong chú thích tương ứng với `=50`.) Hiện tại `=0` → tắt. |
| 14 | `低蓝量使用回城卷=0` | Mana thấp thì dùng cuộn về thành | Đơn vị: % mana. Chú thích gốc: "Mana dưới 30% thì dùng cuộn dịch chuyển về Talking Island, cuộn về thành hoặc phép `世界樹的呼喚`. `=0` là không dùng." (Ví dụ tương ứng với `=30`.) Hiện `=0` → tắt. 💡 Theo nhật ký cập nhật, mục này thêm vào cho Hoàng tộc khi hết mana lúc buff cho đồng đội. |
| 15 | `旅馆休息回血=1` | Nghỉ ở nhà trọ để hồi máu | `=0` tắt, `=1` bật. Chú thích gốc: "Khi máu thấp, bỏ 800 (tiền game) mua chìa khóa để vào nhà trọ hồi máu; chỉ dành cho Hoàng tộc (`王族`) và Hiệp sĩ (`骑士`)." 💡 Nhớ giữ đủ tiền (ít nhất 800). |
| 16 | `旅馆休息村庄=說話之島村` | Làng có nhà trọ để nghỉ = làng Talking Island (`說話之島村`) | Giá trị là **tên làng**. Muốn đổi làng thì gõ đúng tên làng như trong game (chữ phồn thể). |
| 17 | `旅馆为自己放加速次数=0` | Số lần tự niệm Tăng tốc khi ở nhà trọ | Chú thích gốc: "`=0` tắt; `=1` `=2` `=3` `=4` `=5`: khi nghỉ ở nhà trọ thì tự niệm phép Tăng tốc (`加速术`, Haste) cho bản thân bấy nhiêu lần (ví dụ `=5` là 5 lần). Tối đa điền 5." |

---

### [NPC特殊购买] — Mua đặc biệt ở NPC

Bot tự đi tới NPC để mua một món hàng đặc biệt: **cuộn phù phép giáp** `對盔甲施法的卷軸` (Scroll of Enchant Armor, dùng để cường hóa giáp). Theo nhật ký cập nhật, món này mua ở **tầng 7 (hầm ngục) Gludin** (`古鲁丁7楼`; `古鲁丁` = Gludin, trong file viết giản thể; `7楼` = tầng 7).
Có giới hạn số lần thử, thời gian tối đa, thời gian chờ sau khi thất bại, và có thể tắt riêng cho từng tài khoản.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 21 | `對盔甲施法的卷軸=0` | Mua cuộn phù phép giáp | Chú thích gốc: "đặt 0 là tắt, đặt 1 là bật: mua `對盔甲施法的卷軸`." Mặc định: tắt. |
| 22 | `最大执行次数=3` | Số lần thực hiện tối đa = 3 | Chú thích gốc: "Số lần thử tối đa trong một chu kỳ. `=0` **không giới hạn**; `=3` là mỗi chu kỳ tối đa 3 lần, đạt mức thì dừng, sang chu kỳ sau đếm lại từ 0. Nếu cả 3 lần đều không thành công thì sẽ không thực hiện mua nữa." |
| 23 | `最大执行时间=2400` | Thời gian thực hiện tối đa = 2400 giây | Chú thích gốc: "Thời gian tối đa (giây) cho một lần mua. `=0` thì **mặc định 2400 giây**; `=2400` nghĩa là mỗi lần tối đa 40 phút, tính tổng từ lúc kích hoạt → di chuyển đến điểm đích → mua xong." |
| 24 | `下次触发等待时间=3600` | Thời gian chờ trước lần kích hoạt sau = 3600 giây | Chú thích gốc: "Thời gian hồi (giây) sau khi thất bại hoặc quá giờ. `0` = không giới hạn; `=3600` nghĩa là thất bại thì chờ 1 tiếng rồi thử lại." |
| 25 | `寻路时反击怪物=1` | Phản công quái khi đang tìm đường | Chú thích gốc: "Khi đang tìm đường mà có quái tấn công: đặt 1 thì phản công mục tiêu; đặt 0 thì không phản công." |
| 26 | `关闭古鲁丁7楼怪物反击=0` | Tắt phản công quái ở tầng 7 Gludin | Chú thích gốc: "Khi tìm đường, nếu đặt 1 thì lúc ở tầng 7 Gludin sẽ không phản công quái; đặt 0 thì tùy theo `寻路时反击怪物` (dòng 25) có bật hay không." |
| 27 | `<email>=0` | Bật/tắt việc mua cho riêng một tài khoản | Chú thích gốc: "Nếu đặt một email chỉ định `=0` thì tài khoản này sẽ không mua. Định dạng là `tên email=0 hoặc 1` (0 tắt, 1 bật)." Trong file gốc, chỗ `<email>` là một **địa chỉ email mẫu** (đã ẩn trong tài liệu này). Thay bằng email đăng nhập của tài khoản bạn muốn chỉnh; nhiều tài khoản thì có lẽ viết mỗi tài khoản một dòng (?). |

---

### [挂机全局配置] — Cấu hình treo máy (`挂机`) toàn cục

Các thiết lập chung khi treo máy đánh quái (`打怪`). Chỉ có hiệu lực khi `启用全局配置=1`; nếu `=0` bot dùng các thiết lập tương ứng trong file `gj.txt`.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 30 | `启用全局配置=0` | Bật cấu hình toàn cục | Chú thích gốc: "Nếu đặt `=0` thì dùng cấu hình trong `gj.txt`; `=1` thì dùng cấu hình ở đây (áp dụng cho mọi cấp độ). Đưa về đây cho tiện khi mọi người thay file `gj.txt`." 💡 Bật `=1` thì khi thay `gj.txt` khác bạn không phải chỉnh lại các mục bên dưới. |
| 31 | `攻击寻路到挂机点路上怪物=0` | Đánh quái trên đường tìm tới điểm treo máy | `=0` tắt; `=1` đánh mọi quái trên đường; `=2` chỉ đánh quái trên đường trong hầm ngục (`地监`); `=3` chỉ đánh quái trên đường trong **cùng một tầng** hầm ngục. |
| 32 | `反击全部怪物=0` | Phản công mọi quái | `=0` tắt, `=1` bật: hễ quái nào đang đánh bạn là phản công. |
| 33 | `拾取别人金币=1` | Nhặt tiền vàng của người khác | `=0` tắt, `=1` bật: khi không còn quái để đánh và không còn đồ do chính mình giết quái rơi ra để nhặt, thì nhặt tiền vàng của người khác. Tắt thì không nhặt. |
| 34 | `不拾取物品=0` | Không nhặt đồ | `=0` tắt (vẫn nhặt), `=1` bật: không nhặt bất kỳ vật phẩm hay tiền vàng nào. |
| 35 | `低于多少金币不拾取=0` | Không nhặt đống tiền nhỏ hơn bao nhiêu | `=0` tắt. Lớn hơn 0, ví dụ `=5`, thì không nhặt các đống tiền từ 5 trở xuống. |
| 36 | `记忆卷轴传送=0` | Dịch chuyển bằng cuộn ghi nhớ vị trí | `=0` tắt. `=1` bật, dịch chuyển tới điểm ghi nhớ thứ 1; `=2` tới điểm thứ 2; `=3` tới điểm thứ 3; cứ thế tiếp tục. **Phải tự ghi nhớ vị trí bằng tay trong game.** |
| 37 | `优先攻击在拾取=0` | Ưu tiên đánh quái trước rồi mới nhặt | `=0` tắt, `=1` bật. Dành cho hầm ngục khi quá nhiều quái thì có thể bật. 💡 Chữ `在` trong tên khóa là lỗi chính tả của `再` ("rồi mới"), nhưng **phải giữ nguyên `在`** vì bot đọc đúng chữ này. |
| 38 | `出门血量=100` | Máu để ra khỏi làng | Đơn vị %. Chú thích gốc: "Nếu `=100` nghĩa là máu đạt 100% mới xuất phát từ làng." |
| 39 | `出门蓝量=95` | Mana để ra khỏi làng | Đơn vị %. Chú thích gốc: "Nếu `=100` nghĩa là mana đạt 100% mới xuất phát từ làng." Hiện đặt 95 → mana đạt 95% là đi. |

---

### [触发随机传送配置] — Kích hoạt dịch chuyển ngẫu nhiên

Khi gặp các tình huống như kẹt đường, lâu không có thêm tiền, không có quái, bị quái chỉ định hoặc người chơi/thú cưng tấn công..., bot dùng **phép dịch chuyển** (`传送术`, Teleport) hoặc **cuộn dịch chuyển** để nhảy sang chỗ khác. Phần cuối mục là thiết lập **nghỉ khi bị người chơi PK liên tục**.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 43 | `开启=0` | Bật | Chú thích gốc: "Đặt 0 là tắt, đặt 1 là bật chức năng này." |
| 44 | `地监途中路径被堵时=30` | Khi đường bị chặn trên đường vào hầm ngục = 30 giây | Chú thích gốc: "Thiết lập riêng cho bản đồ hầm ngục: thời gian (giây) để xác định là đường bị chặn khi đang đi tới hầm ngục (có hiệu lực trên đường tới điểm treo máy, **không** có hiệu lực khi đã ở trong phạm vi treo máy)." |
| 45 | `无金币变化秒数=900` | Số giây không thay đổi tiền vàng = 900 | Chú thích gốc: "Nghĩa là sau 900 giây tiền không thay đổi thì sẽ dùng (dịch chuyển). Đừng đặt thời gian quá ngắn; quá ngắn thì khi không giành được quái sẽ dễ dùng liên tục." |
| 46 | `被指定怪攻击时=怪物名21,怪物名12111` | Khi bị quái chỉ định tấn công | Chú thích gốc: "Gặp các quái này tấn công và chúng ở trong vòng 10 mét thì kích hoạt ngay; nhiều quái thì cách nhau bằng dấu phẩy." 💡 `怪物名21` và `怪物名12111` chỉ là **tên mẫu** ("tên quái 21", "tên quái 12111"); thay bằng tên quái thật trong game. "10 mét" là khoảng cách trong game (có lẽ ~10 ô) (?). |
| 47 | `使用冷却=10` | Thời gian hồi khi dùng = 10 | Chú thích gốc: "Thời gian chờ của kỹ năng, tức là thời gian chờ từ lúc dùng dịch chuyển xong đến lần thực hiện tiếp theo; mọi điều kiện kích hoạt đều dựa vào thời gian này để quyết định có kích hoạt hay không." Không ghi đơn vị, có lẽ là **giây** (?). |
| 48 | `检测位置停滞秒数=30` | Số giây kiểm tra vị trí đứng yên = 30 | Chú thích gốc: "Không kích hoạt khi đang ở trong phạm vi treo máy. Sau 30 giây mà vị trí không thay đổi thì dùng (ở bất kỳ bản đồ nào). Không muốn chức năng này thì **đặt 0 để tắt; khi tắt sẽ không kiểm tra việc bị chặn đường**." |
| 49 | `位置变动判定半径=5` | Bán kính để xác định vị trí có thay đổi = 5 | Chú thích gốc: "Phạm vi tọa độ (`坐标`) coi như chưa di chuyển. Vô hiệu khi `检测位置停滞秒数` bị tắt. (Có hiệu lực trên đường tới điểm treo máy, không có hiệu lực trong phạm vi treo máy.)" Đơn vị có lẽ là ô tọa độ (?). |
| 50 | `无怪物触发秒数=600` | Số giây không có quái thì kích hoạt = 600 | Chú thích gốc: "Nghĩa là 600 giây đều không có quái thì kích hoạt." |
| 51 | `被玩家攻击随机传送=0` | Bị người chơi tấn công thì dịch chuyển ngẫu nhiên | `=0` tắt, `=1` bật. |
| 52 | `被宠物攻击随机传送=0` | Bị thú cưng tấn công thì dịch chuyển ngẫu nhiên | `=0` tắt, `=1` bật. Khi đã bật thiết lập **phản công chó** (`反击狗`, mục `[反击配置]`) thì dòng này không có hiệu lực. 💡 Trong file mặc định `反击狗=1`, nên muốn dùng dòng này thì phải đặt `反击狗=0`. |

**Các dòng chú thích 54–59** (giải thích cho dòng 60 và 61):

- Dòng 54 — `-- 首次进入地监随机传送【0关，1开启】，当设置1时，会触发：...`
  → "**Dịch chuyển ngẫu nhiên khi vào hầm ngục lần đầu** [0 tắt, 1 bật]. Khi đặt 1 sẽ kích hoạt: lần đầu tìm đường vào bản đồ hầm ngục, **hoặc** vào bản đồ bạn đặt ở 'chỉ định bản đồ xuất phát dịch chuyển ngẫu nhiên', sẽ dùng phép dịch chuyển hoặc cuộn **một lần**; đổi bản đồ thì đếm lại."
- Dòng 55 — `-- 指定地图出发随机传送：当寻路挂机首次进入设置的地图时会触发一次使用随机。`
  → "Chỉ định bản đồ xuất phát dịch chuyển ngẫu nhiên: khi tìm đường đi treo máy mà vào bản đồ đã đặt lần đầu tiên thì kích hoạt dùng dịch chuyển ngẫu nhiên một lần."
- Dòng 56 — `-- 比如：指定地图出发随机传送=枫木村 ...`
  → "Ví dụ: `指定地图出发随机传送=枫木村` thì ngoài bản đồ hầm ngục ra, khi vào `枫木村` (làng Phong Mộc, có lẽ là làng Windawood (?)) sẽ dùng dịch chuyển ngẫu nhiên một lần, theo thiết lập `使用冷却` (dòng 47)."
- Dòng 57 — `-- 比如：指定地图出发随机传送=枫木村,说话岛村 ...`
  → "Ví dụ: `指定地图出发随机传送=枫木村,说话岛村` thì ngoài bản đồ hầm ngục ra, khi vào `枫木村` hoặc `说话岛村` (làng Talking Island) sẽ dùng dịch chuyển ngẫu nhiên một lần, theo thiết lập `使用冷却`."
- Dòng 58 — `-- 多个地图时用英文逗号隔开，注意不要带多余的空字符`
  → "Nhiều bản đồ thì cách nhau bằng **dấu phẩy tiếng Anh**, chú ý không để ký tự trống thừa."
- Dòng 59 — `-- 注意：使用优先级 传送术技能 > 瞬移卷轴，使用一次传送术后将根据 使用冷却=30 的设置 等待下一次的使用时间`
  → "Lưu ý: thứ tự ưu tiên: **kỹ năng dịch chuyển** (`传送术`) > **cuộn dịch chuyển tức thời** (`瞬移卷轴`). Sau khi dùng dịch chuyển một lần sẽ chờ theo thiết lập `使用冷却` (ví dụ `=30`) mới dùng lần tiếp." 💡 Số `30` chỉ là ví dụ; giá trị thật trong file hiện là `使用冷却=10` (dòng 47).

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 60 | `首次进入地监随机传送=0` | Dịch chuyển ngẫu nhiên khi vào hầm ngục lần đầu | `=0` tắt, `=1` bật (xem chú thích dòng 54). |
| 61 | `指定地图触发随机传送=` | Chỉ định bản đồ kích hoạt dịch chuyển ngẫu nhiên | Để trống = không dùng. Điền tên bản đồ, nhiều bản đồ cách nhau bằng dấu phẩy tiếng Anh, ví dụ `指定地图触发随机传送=枫木村,说话岛村`. 💡 Chú thích (dòng 55–57) gọi khóa này là `指定地图出发随机传送` (chữ `出发`), nhưng **dòng thật trong file là `指定地图触发随机传送` (chữ `触发`)**. Hãy điền giá trị vào dòng 61 và giữ nguyên tên khóa của dòng này. |
| 63 | `被玩家PK连续次数=0` | Số lần bị người chơi PK liên tiếp | Chú thích gốc: "Đặt 0 là tắt. Đặt lớn hơn 0 nghĩa là: trong khoảng thời gian đặt ở `被玩家PK持续时间`, nếu số lần bị người chơi PK liên tiếp lớn hơn hoặc bằng số này thì sẽ kích hoạt nghỉ." |
| 64 | `被玩家PK持续时间=3600` | Khoảng thời gian đếm số lần bị PK = 3600 giây | Chú thích gốc: "Đặt 3600 nghĩa là trong 3600 giây sẽ liên tục ghi lại số lần bị người chơi PK." |
| 65 | `被玩家PK触发休息=600` | Bị PK thì kích hoạt nghỉ = 600 giây | Chú thích gốc: "Khi bị người chơi tấn công liên tục vượt quá số lần chỉ định thì nghỉ 600 giây. Các thời gian nghỉ khác tự thiết lập." |

---

### [触发回城休息配置] — Kích hoạt về thành nghỉ / né người, né quái

Khi **thấy** (hoặc **bị tấn công** bởi) người chơi hay quái có trong danh sách né, bot sẽ:
- **Chế độ 1** (`开启=1`): về thành (`回城`) nghỉ một lúc rồi quay lại.
- **Chế độ 2** (`开启=2`): dùng dịch chuyển chạy trốn và tạm "cấm" (đưa vào danh sách đen) điểm treo máy đang đứng.

- Dòng 69 — `-- 注意:触发都是在到达挂机范围内才会触发,开启分模式1和模式2`
  → "Lưu ý: mọi kích hoạt chỉ xảy ra khi **đã tới phạm vi treo máy**. Khi bật thì chia thành chế độ 1 và chế độ 2."

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 70 | `开启=0` | Bật / chọn chế độ | Chú thích gốc: "`=0` [tắt]; `=1` [về thành]; `=2` [phép dịch chuyển]. Phép dịch chuyển của chế độ 2 chỉ do mục cấu hình này điều khiển, dùng kỹ năng dịch chuyển hoặc cuộn." |
| 71 | `被玩家攻击才触发=0` | Chỉ kích hoạt khi bị người chơi tấn công | `=0` cứ **thấy** là kích hoạt; `=1` **bị tấn công** mới kích hoạt (người đó đang khóa mục tiêu vào bạn). |
| 72 | `被怪物攻击才触发=0` | Chỉ kích hoạt khi bị quái tấn công | `=0` cứ **thấy** là kích hoạt; `=1` **bị tấn công** mới kích hoạt (quái đang khóa mục tiêu vào bạn). |
| 73 | `躲避玩家名单=` | Danh sách người chơi cần né | Chú thích gốc: "Tên người chơi cách nhau bằng dấu phẩy; để trống = tắt; nhiều tên thì dùng **dấu phẩy tiếng Anh**, không để khoảng trắng ở đầu/cuối. Ví dụ: `躲避玩家名单=玩家A,玩家B,玩家C`." (`玩家A` = "người chơi A", chỉ là ví dụ.) |
| 74 | `躲避怪物名单=` | Danh sách quái cần né | Chú thích gốc: "Tên quái cách nhau bằng dấu phẩy; để trống = tắt; nhiều tên thì dùng dấu phẩy tiếng Anh, không để khoảng trắng ở đầu/cuối. Ví dụ: `躲避怪物名单=怪物A,怪物B,怪物C`." (`怪物A` = "quái A".) |
| 75 | `躲避检测距离=15` | Khoảng cách phát hiện để né = 15 | Chú thích gốc: "Khoảng cách phát hiện dùng chung cho cả người chơi và quái." Đơn vị có lẽ là ô (?). |
| 76 | `回城休息时间_分钟=15` | Thời gian nghỉ sau khi về thành (phút) = 15 | Chú thích gốc: "Chỉ dùng cho chế độ 1 (`开启=1`): về thành rồi chờ N phút mới xuất phát; chỉ chế độ 1 có hiệu lực." |

**Các dòng chú thích 78–79:**

- Dòng 78 — `-- 只有模式2【开启=2】才会拉黑挂机点，瞬移后的坐标即为临时点。`
  → "Chỉ chế độ 2 (`开启=2`) mới đưa điểm treo máy vào danh sách đen. Tọa độ sau khi dịch chuyển chính là **điểm tạm**."
- Dòng 79 — `-- 多个挂机点时:当前点被拉黑 -> 先去临时点 -> 临时点无怪后步进跳过被拉黑的点 -> 去没被拉黑的点。所有点都被拉黑时清空黑名单,留在临时点避难`
  → "Khi có nhiều điểm treo máy: điểm hiện tại bị đưa vào danh sách đen → đến điểm tạm trước → khi điểm tạm hết quái thì lần lượt bỏ qua các điểm bị chặn → đến điểm chưa bị chặn. Khi **tất cả** các điểm đều bị chặn thì xóa danh sách đen và ở lại điểm tạm để lánh nạn."

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 80 | `挂机点过滤_分钟=30` | Thời gian lọc (cấm) điểm treo máy (phút) = 30 | Chú thích gốc: "Chỉ dùng cho chế độ 2 (`开启=2`): thời gian (phút) một điểm treo máy bị lọc, hết hạn thì tự khôi phục. Ví dụ: đặt 30 phút, sau khi phát hiện mục tiêu trong danh sách và dịch chuyển bỏ chạy, điểm treo máy hiện tại bị chặn 30 phút, trong thời gian đó điểm này bị bỏ qua. Các điểm treo máy khác nằm trong 'bán kính lọc điểm treo máy' tính từ điểm bị chặn cũng bị lọc. Điểm đáp sau khi dịch chuyển sẽ tạm thời làm điểm treo máy để lánh nạn." |
| 81 | `挂机点过滤半径=10` | Bán kính lọc điểm treo máy = 10 | Chú thích gốc: "Chỉ dùng cho chế độ 2: sau khi chặn một điểm, các điểm treo máy khác bạn đã cấu hình có khoảng cách tới điểm bị chặn **≤ giá trị này** thì cũng bị lọc." |

---

### [休息配置] — Lịch nghỉ

Cho bot nghỉ định kỳ (không treo máy liên tục). Dòng 85 và 89 là đường kẻ trang trí `-----...`.

- Dòng 86 — `-- 开关默认值 (=0关 ，=1【运行几分钟,休息几分钟模式】 =2【根据休息时间段，在你设置的时间段内只休息不挂机 】)，`
  → "Giá trị của công tắc: `=0` tắt; `=1` [chế độ chạy X phút, nghỉ Y phút]; `=2` [theo khung giờ nghỉ: trong các khung giờ bạn đặt thì chỉ nghỉ, không treo máy]."
- Dòng 87 — `-- 注意1：设置 休息几分钟 会随机追加1分钟左右，注意2：时间段的设置注意间隔符号`
  → "Lưu ý 1: thời gian `休息几分钟` sẽ được cộng thêm ngẫu nhiên khoảng 1 phút. Lưu ý 2: khi đặt khung giờ, chú ý ký hiệu ngăn cách."
- Dòng 88 — `-- 因为有缓存，所以每次设置完如果想要立刻生效则需要重新启动脚本运行`
  → "Vì có bộ nhớ đệm, mỗi lần chỉnh xong nếu muốn có hiệu lực ngay thì phải **khởi động lại script**."

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 90 | `休息模式=0` | Chế độ nghỉ | `=0` tắt; `=1` chạy X phút nghỉ Y phút (dùng dòng 91–92); `=2` nghỉ theo khung giờ (dùng dòng 93). |
| 91 | `运行几分钟=60` | Chạy bao nhiêu phút = 60 | Dùng cho `休息模式=1`: treo máy 60 phút thì nghỉ. |
| 92 | `休息几分钟=10` | Nghỉ bao nhiêu phút = 10 | Dùng cho `休息模式=1`: nghỉ 10 phút (cộng ngẫu nhiên khoảng 1 phút). 💡 Khóa này trùng tên với dòng 11 trong `[角色保护]` nhưng thuộc mục khác nên là hai thiết lập độc lập. |
| 93 | `休息时间段=12:00-13:10\|18:20-19:10\|21:00-21:10` | Các khung giờ nghỉ | Dùng cho `休息模式=2`. Mỗi khung có dạng `giờ bắt đầu-giờ kết thúc` (24 giờ, `HH:MM`), các khung cách nhau bằng `\|`. Mặc định: 12:00–13:10, 18:20–19:10, 21:00–21:10. |

Dòng 93 nguyên văn (để chép cho đúng):

```text
休息时间段=12:00-13:10|18:20-19:10|21:00-21:10
```

---

### [按时间切换挂机配置] — Đổi cấu hình treo máy theo khung giờ

Theo khung giờ, bot chuyển sang dùng file treo máy khác (`gj2.txt`, `gj3.txt`...) thay cho `gj.txt`. Dòng 97 và 101 là đường kẻ trang trí `-----...`.
Ba dòng 98–100 là lời giải thích viết thẳng trong file (không có `--` ở đầu); cứ để nguyên.

- Dòng 98 — `按照你设定的时间段，切换不同的挂机文件，格式为 开始时间(11:38)-结束时间(12:39),自定义挂机文件(gj2.txt)（其中符号别打错了，自定义文件必须存在）`
  → "Theo khung giờ bạn đặt, chuyển sang các file treo máy khác nhau. Định dạng: `giờ bắt đầu (11:38)-giờ kết thúc (12:39),file treo máy tự tạo (gj2.txt)` (đừng gõ sai các ký hiệu; **file tự tạo bắt buộc phải tồn tại**)."
- Dòng 99 — `比如11:38-12:39,gj2.txt表示在这个时间段，执行gj2.txt中的打怪配置，gj2.txt可以参考默认的gj.txt中的设置（复制gj.txt然后改名gj2.txt在进行设置）`
  → "Ví dụ `11:38-12:39,gj2.txt` nghĩa là trong khung giờ này sẽ chạy cấu hình đánh quái trong `gj2.txt`. `gj2.txt` có thể tham khảo thiết lập trong file mặc định `gj.txt` (sao chép `gj.txt`, đổi tên thành `gj2.txt`, rồi chỉnh)."
- Dòng 100 — "Có thể có nhiều khung giờ để treo máy với các điều kiện khác nhau, ví dụ:" (nguyên văn bên dưới)

```text
可以有多个时间段，进行不同条件的挂机配置，比如11:38-12:39,gj2.txt|16:10-16:40,gj3.txt|22:38-23:39,gj4.txt
```

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 102 | `开启切换=0` | Bật chuyển đổi | `=0` tắt, `=1` bật (theo quy ước chung). |
| 103 | `分段挂机配置=11:38-12:39,gj2.txt\|16:10-16:40,gj3.txt\|22:38-23:39,gj4.txt` | Cấu hình treo máy theo từng khung giờ | Mỗi đoạn có dạng `giờ bắt đầu-giờ kết thúc,tên file`; các đoạn cách nhau bằng `\|`. Ví dụ mặc định: 11:38–12:39 dùng `gj2.txt`, 16:10–16:40 dùng `gj3.txt`, 22:38–23:39 dùng `gj4.txt`. 💡 Các file này phải có thật; có lẽ đặt cùng thư mục với `gj.txt` (`Game_Config`) (?). |

Dòng 103 nguyên văn:

```text
分段挂机配置=11:38-12:39,gj2.txt|16:10-16:40,gj3.txt|22:38-23:39,gj4.txt
```

---

### [键鼠模式附加内存功能] — Chức năng bộ nhớ bổ sung cho chế độ bàn phím-chuột

Ngay trước tiêu đề mục này trong file có một đường kẻ (dòng 106) và một dòng lưu ý (dòng 107):

- Dòng 107 — `注意：此功能只有config\键鼠模式=1  才会生效   谨慎使用 可能会增加封号风险`
  → "Lưu ý: chức năng này **chỉ có hiệu lực khi `config\键鼠模式=1`** (tức là trong file `config/config.ini` đang bật chế độ bàn phím-chuột). Hãy dùng thận trọng, **có thể làm tăng nguy cơ bị khóa tài khoản** (`封号`)."

Giải thích: bot có hai cách điều khiển game. **Chế độ bàn phím-chuột** (`键鼠模式`) bấm trực tiếp trên màn hình game. **Chế độ bộ nhớ** (`内存模式`) đọc/ghi bộ nhớ game. Khi đang chạy chế độ bàn phím-chuột, mục này cho phép chọn **từng thao tác** chạy bằng bộ nhớ.
Mỗi dòng: `=0` dùng bàn phím-chuột, `=1` dùng chế độ bộ nhớ.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 109 | `内存寻路=0` | Tìm đường bằng bộ nhớ | `=0` bàn phím-chuột, `=1` chế độ bộ nhớ. |
| 110 | `内存打怪=0` | Đánh quái bằng bộ nhớ | `=0` bàn phím-chuột, `=1` chế độ bộ nhớ (đánh thường). |
| 111 | `内存拾取=0` | Nhặt đồ bằng bộ nhớ | `=0` bàn phím-chuột, `=1` chế độ bộ nhớ. |
| 112 | `内存放技能=0` | Dùng kỹ năng bằng bộ nhớ | `=0` bàn phím-chuột, `=1` chế độ bộ nhớ: áp dụng cho mọi kỹ năng buff và kỹ năng hồi máu. |
| 113 | `内存使用物品=0` | Dùng vật phẩm bằng bộ nhớ | `=0` bàn phím-chuột, `=1` chế độ bộ nhớ: ví dụ uống thuốc, dùng cuộn biến hình. |
| 114 | `内存删除物品=0` | Xóa vật phẩm bằng bộ nhớ | `=0` bàn phím-chuột, `=1` chế độ bộ nhớ: xóa đồ trong túi bằng chế độ bộ nhớ. |
| 115 | `内存交易=0` | Giao dịch bằng bộ nhớ | `=0` bàn phím-chuột, `=1` chế độ bộ nhớ: acc phụ giao dịch cho acc nhận hàng, acc nhận hàng chấp nhận giao dịch, tất cả đều dùng bộ nhớ. |
| 116 | `内存组队=0` | Tổ đội bằng bộ nhớ | `=0` bàn phím-chuột, `=1` chế độ bộ nhớ: đội trưởng mời đội viên bằng chế độ bộ nhớ. |

---

### [基础配置] — Cấu hình cơ bản

Các thiết lập lặt vặt nhưng quan trọng: cuộn biến hình (`变身卷轴`), đổi đồ, học kỹ năng, tố cáo, chuyển hóa máu/mana, mua trang bị, cuộn dịch chuyển về Talking Island, mua thịt, tự đổi mũ, dịch chuyển tới cửa hầm ngục.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 121 | `使用变身卷轴=1` | Dùng cuộn biến hình (loại được tặng) | Chú thích gốc: "Loại được tặng [`輕量變形卷軸`]" (Cuộn biến hình hạng nhẹ). `=1` dùng, `=0` không dùng. |
| 122 | `使用购买变身卷轴=0` | Dùng cuộn biến hình (loại mua) | Chú thích gốc: "Loại mua hoặc rơi ra [`變形卷軸`]" (Cuộn biến hình thường). `=1` dùng, `=0` không dùng. |
| 123 | `自动换装到等级=16` | Tự động đổi trang bị đến cấp = 16 | `=0` tắt tự đổi đồ. Ví dụ điền `20` nghĩa là dưới cấp 20 thì tự đổi trang bị, quá cấp 20 thì dừng. Hiện tại: tự đổi đồ đến cấp 16. |
| 124 | `自动学习技能=1` | Tự động học kỹ năng | Không có chú thích gốc. Theo quy ước chung: `=1` bật, `=0` tắt (?). |
| 125 | `举报附近的人=0` | Tố cáo (report) người ở gần | Chú thích gốc: "Sẽ không tố cáo nhầm người phe mình; ai dùng cùng script đều là người phe mình. Cần mua `摺紙傳令鳥` (Chim đưa tin gấp giấy (?)) ở NPC `艾伊拉` (Aira (?)) tại `说话之岛` (Talking Island), và đặt tự mua khi về thành trong file `SellBuy.txt`." `=0` tắt, `=1` bật. |
| 126 | `打怪拾取使用血蓝转换=3` | Dùng chuyển hóa máu/mana khi đánh quái và nhặt đồ | Chú thích gốc: "`=0` không dùng khi đánh quái/nhặt đồ. `=1` khi tấn công thì 'chuyển máu' (`转血`). `=2` khi tấn công thì 'chuyển máu' và 'chuyển mana' (`转蓝`). `=3` khi đánh quái và khi nhặt đồ đều chuyển máu, chuyển mana. Khi không có quái thì các mức đều dùng." 💡 Có lẽ liên quan đến kỹ năng đổi máu lấy mana như `心靈轉換`; mục này quyết định lúc nào bot được phép dùng chúng (?). |
| 127 | `自动购买装备=1` | Tự động mua trang bị | `=0` tắt, `=1` bật: khi tiền đạt **11000** thì tự mua `獵人之弓` (Cung Thợ săn, Hunter's Bow). |
| 128 | `无说话卷轴时停止脚本=1` | Hết cuộn dịch chuyển về Talking Island thì dừng script | `=0` tắt, `=1` bật: khi trong túi không còn cuộn dịch chuyển về Talking Island (`说话卷轴`) thì ngừng làm việc. |
| 129 | `自动领取说话卷轴=1` | Tự động nhận cuộn dịch chuyển về Talking Island | `=0` tắt, `=1` bật: tự động nhận cuộn dịch chuyển về Talking Island. Theo nhật ký cập nhật, mặc định bật. |
| 131 | `死亡复活后自动购买肉=19` | Sau khi chết và hồi sinh thì tự mua thịt = 19 | `=0` tắt. `=19` nghĩa là sau khi chết mua 19 miếng thịt và tự ăn đến khi **độ no** (`饱食度`) đầy; điền bao nhiêu thì mua bấy nhiêu, thường 19 miếng là vừa đầy. |
| 133 | `自动切换敏捷力量头盔=1` | Tự động đổi mũ Nhanh nhẹn / Sức mạnh | `=0` tắt, `=1` bật. Khi trong túi có cả `敏捷魔法頭盔` (Mũ phép thuật Nhanh nhẹn) và `力量魔法頭盔` (Mũ phép thuật Sức mạnh) thì tự đổi mũ để lấy buff. Cần bật tự dùng các kỹ năng tương ứng ở **mục cấu hình kỹ năng** bên dưới (`[技能配置_妖精]`; ví dụ `加速術` và `通暢氣脈術` được ghi chú là kỹ năng của mũ Nhanh nhẹn). 💡 Trang bị cần đổi phải được **khóa trong túi** (tính năng khóa đồ của game). |
| 134 | `自动穿戴头盔=` | Tự động mặc lại mũ | Chú thích gốc: "Ví dụ điền tên mũ của bạn. Khi bật `自动切换敏捷力量头盔=1`, sau khi đổi mũ lấy buff sẽ tự đổi về chiếc mũ này, để bot biết bạn muốn đội mũ nào. Trang bị muốn mặc phải được khóa trong túi." Để trống = không chỉ định. |
| 136 | `村庄传送到地监门口间隔=0` | Khoảng cách giữa các lần dịch chuyển từ làng tới cửa hầm ngục | `=0` tắt. `=10` nghĩa là trong 10 phút dịch chuyển 1 lần. Đây là khoảng cách thời gian khi treo máy ở hầm ngục: từ làng dịch chuyển tới cửa hầm ngục rồi đi bộ vào; nếu chưa hết thời gian thì đi bộ tới. Đơn vị: phút. |

---

### [创建角色配置] — Cấu hình tạo nhân vật

Dùng khi bot tự tạo nhân vật mới.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 140 | `职业=3` | Nghề nhân vật = 3 | Chú thích gốc: "Nghề: `1` là Hoàng tộc (`王族`); `2` là Hiệp sĩ (`骑士`); `3` là Elf (`妖精`); `4` Pháp sư (`魔法师`)." Mặc định 3 = Elf. |
| 141 | `角色名类型=0` | Kiểu tên nhân vật | `=0` tên tiếng Anh ngẫu nhiên; `=1` tên tiếng Trung ngẫu nhiên; `=2` tên tiếng Hàn ngẫu nhiên. |

---

### [使用加速药水] — Dùng thuốc tăng tốc

Bật/tắt từng loại thuốc tăng tốc độ (di chuyển, đánh) và vài thuốc buff khác. Theo quy ước: `=1` dùng, `=0` không dùng.
💡 Tên vật phẩm phải giữ đúng như trong game (chữ phồn thể).

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 145 | `輕量自我加速藥水=1` | Thuốc tự tăng tốc hạng nhẹ | Chú thích gốc: "Đặt `=1` thì `活力自我加速藥水` (Thuốc tự tăng tốc Hoạt lực; các món `活力…` là bản đổi được từ sự kiện Trứng màu, xem `ActivityConfig.txt`) cũng được dùng." |
| 146 | `自我加速藥水=1` | Thuốc tự tăng tốc (Haste) | `=1` dùng. |
| 147 | `強化自我加速藥水=0` | Thuốc tự tăng tốc cường hóa | `=0` không dùng. |
| 148 | `輕量精靈餅乾=1` | Bánh quy Tiên hạng nhẹ | Chú thích gốc: "Đặt `=1` thì `活力精靈餅乾` (Bánh quy Tiên Hoạt lực) cũng được dùng." Bánh quy Tiên (Elven Wafer) là đồ tăng tốc đánh của Elf. |
| 149 | `精靈餅乾=0` | Bánh quy Tiên | `=0` không dùng. |
| 150 | `藍色藥水=0` | Thuốc xanh lam (Blue Potion, tăng hồi mana) | Chú thích gốc: "Đặt `=1` thì `魔力回復藥水` (Thuốc hồi phục ma lực) cũng được dùng." 💡 Mục `吃蓝药百分比` ở `[吃药配置]` chỉ có tác dụng khi dòng này `=1`. |
| 151 | `輕量惡魔之血=1` | Máu Ác quỷ hạng nhẹ (Devil's Blood) (?) | Chú thích gốc: "Đặt `=1` thì `活力惡魔之血` (Máu Ác quỷ Hoạt lực) cũng được dùng." |
| 152 | `惡魔之血=0` | Máu Ác quỷ (Devil's Blood) (?) | `=0` không dùng. |
| 153 | `輕量勇敢藥水=1` | Thuốc Dũng cảm hạng nhẹ | `=1` dùng. Thuốc Dũng cảm (Brave Potion) tăng tốc đánh. |
| 154 | `勇敢藥水=0` | Thuốc Dũng cảm | `=0` không dùng. |

---

### [解释技能配置说明 这里为无效字段] — Giải thích cách cấu hình kỹ năng (đây là mục **không có hiệu lực**)

Tên mục nghĩa là "Giải thích cách cấu hình kỹ năng, **đây là trường không có hiệu lực**": bot **không** dùng các dòng trong mục này, chúng chỉ là ví dụ. Dòng 157 và 167 là đường kẻ `------------`.

**Cú pháp một dòng kỹ năng:** `tên kỹ năng=hp<điều kiện>|mp<điều kiện>|time=<số giây>`
- `hp` = % máu, `mp` = % mana; dấu `>` là "lớn hơn", `<` là "nhỏ hơn". Hai điều kiện phải **cùng đúng** thì mới dùng kỹ năng.
- `time` = thời gian chờ giữa hai lần dùng (giây); `time=0` là không cần chờ, cứ đủ điều kiện `hp`/`mp` là dùng.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 159 | `心靈轉換=hp>60\|mp<50\|time=3` | Ví dụ 1: `心靈轉換` (Chuyển hóa tâm linh, Body to Mind: đổi máu lấy mana) | Dòng 160 giải thích: "Ý nghĩa ở trên: điều kiện dùng kỹ năng này là máu **lớn hơn 60** và mana **nhỏ hơn 50** mới dùng; cách 3 giây dùng một lần." |
| 161 | `保護罩=hp>0\|mp>25\|time=0` | Ví dụ 2: `保護罩` (Khiên bảo vệ, Shield) | Dòng 162 giải thích: "Ý nghĩa ở trên: chỉ xét mana để dùng, không xét khoảng cách thời gian; mana lớn hơn 25 là dùng." |
| 163 | `擬似魔法武器=hp>100\|mp>100\|time=0` | Ví dụ 3: `擬似魔法武器` (Vũ khí ma pháp giả, Enchant Weapon) | Dòng 164 giải thích: "Ý nghĩa ở trên: **không** dùng kỹ năng `擬似魔法武器`, vì máu nhân vật không thể lớn hơn 100%." 💡 Đây là **mẹo tắt một kỹ năng**: đặt `hp>100`. |

Hai dòng ghi chú cuối của mục:

- Dòng 165 — `注：hp,mp 后面的数字代表百分比  time：释放间隔时间秒数`
  → "Chú ý: số sau `hp`, `mp` là **phần trăm**; `time`: khoảng cách giữa hai lần dùng, tính bằng **giây**."
- Dòng 166 — `所有职业通用这个技能，注意：不需要在改成  _骑士  _王族  _法师`
  → "Mọi nghề đều dùng chung (mục kỹ năng) này. Lưu ý: **không cần** đổi lại thành `_骑士` (Hiệp sĩ), `_王族` (Hoàng tộc), `_法师` (Pháp sư)." Tức là giữ nguyên tên mục `[技能配置_妖精]` cho mọi nghề (?).

---

### [技能配置_妖精] — Cấu hình kỹ năng (Elf / `妖精`; dùng chung cho mọi nghề)

Mỗi dòng là điều kiện để bot tự dùng một kỹ năng/buff (cú pháp xem mục trên).
`hp>0|mp>0|time=0` nghĩa là **luôn được phép dùng** (máu và mana chỉ cần trên 0%, không cần chờ giữa hai lần dùng).
Muốn **tắt** một kỹ năng thì đổi `hp>0` thành `hp>100` (như ví dụ dòng 163). Tên kỹ năng phải giữ nguyên chữ Trung.
Tên tiếng Anh trong ngoặc theo bản Lineage quốc tế; tên nào chưa chắc chắn thì có dấu (?).

| # | Dòng gốc | Nghĩa (tên kỹ năng) | Giải thích (điều kiện dùng) |
|---|---|---|---|
| 169 | `保護罩=hp>0\|mp>0\|time=0` | Khiên bảo vệ (Shield) | Luôn dùng. |
| 170 | `負重強化=hp>0\|mp>0\|time=0` | Tăng sức mang vác (Decrease Weight) | Luôn dùng. |
| 171 | `擬似魔法武器=hp>0\|mp>0\|time=0` | Vũ khí ma pháp giả (Enchant Weapon) | Luôn dùng. |
| 172 | `神聖武器=hp>0\|mp>0\|time=0` | Vũ khí thần thánh (Holy Weapon) | Luôn dùng. |
| 173 | `初級治癒術=hp<80\|mp>30\|time=6` | Trị liệu sơ cấp (Lesser Heal) | Máu **dưới 80%** và mana **trên 30%**; mỗi lần dùng cách nhau 6 giây. |
| 174 | `中級治癒術=hp<65\|mp>300\|time=6` | Trị liệu trung cấp (Heal) | Máu dưới 65% và mana trên **300%**; 6 giây một lần. 💡 Mana không bao giờ vượt 100% nên với `mp>300` kỹ năng này **thực tế không bao giờ được dùng** (bị tắt). Muốn dùng thì đổi `300` thành số ≤ 100, ví dụ `mp>30`. |
| 175 | `心靈轉換=hp>60\|mp<95\|time=3` | Chuyển hóa tâm linh (Body to Mind, đổi máu lấy mana) | Máu **trên 60%** và mana **dưới 95%**; 3 giây một lần. |
| 176 | `魔法防禦=hp>0\|mp>0\|time=0` | Phòng ngự ma pháp (Resist Magic) | Luôn dùng. |
| 177 | `加速術=hp>0\|mp>0\|time=0` | Tăng tốc (Haste) | Luôn dùng. Chú thích gốc: "Kỹ năng của mũ Nhanh nhẹn" (có được khi đội `敏捷魔法頭盔`). |
| 178 | `通暢氣脈術=hp>0\|mp>0\|time=0` | Thông suốt khí mạch (Physical Enchant: DEX, tăng Nhanh nhẹn) | Chú thích gốc: "Kỹ năng của mũ Nhanh nhẹn; **mặc định tắt**, có thể tự đặt để tự động dùng, ví dụ: `hp>0\|mp>0`." 💡 Giá trị hiện tại trong file đã là `hp>0\|mp>0\|time=0` (luôn dùng), nên câu "mặc định tắt" có lẽ đã cũ (?). |
| 179 | `大地防護=hp>0\|mp>0\|time=0` | Bảo hộ Đất (Earth Skin, tăng giáp) | Luôn dùng. |
| 180 | `風之疾走=hp>0\|mp>0\|time=0` | Phong tật tẩu, chạy nhanh như gió (Wind Walk) | Luôn dùng. |
| 181 | `風之神射=hp>0\|mp>0\|time=0` | Thần xạ của gió (Wind Shot) | Luôn dùng. |
| 182 | `淨化精神=hp>0\|mp>0\|time=5` | Tịnh hóa tinh thần (Clear Mind) | Luôn được phép; mỗi lần dùng cách nhau 5 giây. |
| 183 | `體魄強健術=hp>0\|mp>0\|time=5` | Cường kiện thể phách (Physical Enchant: STR, tăng Sức mạnh) | Luôn được phép; mỗi lần dùng cách nhau 5 giây. |
| 184 | `屬性防禦=hp>0\|mp>0\|time=0` | Phòng ngự thuộc tính (Resist Elemental) | Luôn dùng. |
| 185 | `單屬性防禦=hp>0\|mp>0\|time=0` | Phòng ngự đơn thuộc tính (Protection from Elemental (?)) | Luôn dùng. |
| 186 | `火焰武器=hp>0\|mp>0\|time=0` | Vũ khí lửa (Fire Weapon) | Luôn dùng. |
| 187 | `暴風之眼=hp>0\|mp>0\|time=0` | Mắt bão (Storm Eye) | Luôn dùng. |

Nguyên văn mục này (để đối chiếu/chép cho đúng):

```text
[技能配置_妖精]
保護罩=hp>0|mp>0|time=0
負重強化=hp>0|mp>0|time=0
擬似魔法武器=hp>0|mp>0|time=0
神聖武器=hp>0|mp>0|time=0
初級治癒術=hp<80|mp>30|time=6
中級治癒術=hp<65|mp>300|time=6
心靈轉換=hp>60|mp<95|time=3
魔法防禦=hp>0|mp>0|time=0
加速術=hp>0|mp>0|time=0				--敏捷头盔技能
通暢氣脈術=hp>0|mp>0|time=0			--敏捷头盔技能  默认关闭 可自己设置自动使用 比如： hp>0|mp>0 
大地防護=hp>0|mp>0|time=0
風之疾走=hp>0|mp>0|time=0
風之神射=hp>0|mp>0|time=0
淨化精神=hp>0|mp>0|time=5
體魄強健術=hp>0|mp>0|time=5
屬性防禦=hp>0|mp>0|time=0
單屬性防禦=hp>0|mp>0|time=0
火焰武器=hp>0|mp>0|time=0
暴風之眼=hp>0|mp>0|time=0
```

---

### [吃药配置] — Cấu hình uống thuốc

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 191 | `吃药血量=60` | Ngưỡng máu để uống thuốc = 60 | Chú thích gốc: "Máu dưới 60% thì tự uống thuốc. Cố gắng để giá trị này cao hơn (ngưỡng của) `心灵转换` (= `心靈轉換`). Mặc định uống `輕量紅色藥水` (Thuốc đỏ hạng nhẹ), `治癒藥水` (Thuốc trị liệu, Healing Potion)." 💡 `心靈轉換` ở trên đặt `hp>60`, tức là kỹ năng này tiêu máu khi máu trên 60%. Để ngưỡng uống thuốc cao hơn mốc đó giúp máu không bị tụt quá thấp (?). |
| 192 | `吃蓝药百分比=70` | Ngưỡng mana để uống thuốc xanh = 70% | Chú thích gốc: "Mana dưới mức phần trăm này **và** trong cấu hình, mục `[使用加速药水]` có `藍色藥水=1` thì mới uống." Hiện `藍色藥水=0` nên dòng này chưa có tác dụng. |

---

### [反击配置] — Cấu hình phản công (`反击`)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 196 | `反击狗=1` | Phản công chó | `=0` không đánh; `=1` phản công (khi bị đánh); `=2` thấy là đánh. "Chó" ở đây là thú cưng của người chơi khác (xem dòng 52) (?). |
| 197 | `反击人=0` | Phản công người chơi | Chú thích gốc: "Phản công khi (người chơi khác) tấn công bản thân hoặc đồng đội." Theo quy ước: `=0` tắt, `=1` bật. |
| 198 | `反击法师宝宝=0` | Phản công "cưng" của Pháp sư | `=0` không đánh; `=1` phản công; `=2` thấy là đánh. "Cưng của pháp sư" (`法师宝宝`) là quái do Pháp sư triệu hồi/thuần phục (?). |

---

### [组队配置] — Tổ đội trên cùng máy

Tự lập đội cho các tài khoản đang chạy trên **máy này** (`本机`), tập trung đánh, buff và hồi máu cho đồng đội.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 202 | `本机自动组队=0` | Tự tổ đội trên máy này | Chú thích gốc: "`=0` tắt. `=1` nghĩa là đội tối đa 8 người. Nếu bạn có 9 tài khoản có thể đặt `=5`, nghĩa là 5 tài khoản đầu vào một đội, 4 tài khoản sau vào một đội. Số điền vào là số người của một đội (từ 1 đến 8)." 💡 Câu "`=1` là đội tối đa 8 người" có vẻ mâu thuẫn với câu sau ("số điền vào = số người mỗi đội"); có lẽ `=1` được hiểu là bật với mặc định 8 người/đội (?). |
| 203 | `集火打怪=0` | Tập trung đánh quái | `=0` tắt; `=1` bật tập trung đánh; `=2` mọi tài khoản cố gắng đứng tụ lại một chỗ (nhưng **không** tập trung đánh). Ở chế độ `=1`: đội viên đi theo đội trưởng, đánh đúng con quái đội trưởng đang đánh; khi đội trưởng đi xa hoặc về thành thì đội viên chuyển sang treo máy một mình, đến khi đội trưởng quay lại điểm treo máy thì tiếp tục đi theo. |
| 204 | `为队员放加速术=0` | Niệm Tăng tốc cho đội viên | `=0` tắt, `=1` bật: buff Tăng tốc (`加速术`) cho mọi đội viên; cùng một đội viên mặc định cách **15 phút** buff 1 lần. |
| 205 | `为队员加血=0` | Hồi máu cho đội viên | `=0` tắt, `=1` bật: tự hồi máu cho đội viên máu thấp. (`=1` mặc định máu dưới 65% mới hồi; `=70` là máu dưới 70%; `=80` là dưới 80%; cứ thế.) |
| 206 | `为队员放技能=` | Dùng kỹ năng (buff) cho đội viên | Chú thích gốc: "Ví dụ điền `通暢氣脈術` để buff chỉ định cho đội viên; nhiều kỹ năng cách nhau dấu phẩy, ví dụ `通暢氣脈術,加速術`. Cùng một đội viên mặc định cách **19 phút** buff 1 lần." Để trống = không dùng. |

---

### [局域网组队配置] — Tổ đội qua mạng LAN (server tổ đội)

Lập đội giữa **nhiều máy tính** thông qua chương trình **server tổ đội** (thư mục `组队服务器` trong gói). Các dòng 211–214 giống hệt dòng 203–206 ở mục trên nhưng áp dụng cho tổ đội qua LAN.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 210 | `队伍最大人数=0` | Số người tối đa mỗi đội | Chú thích gốc: "`=0` tắt tổ đội qua LAN. Trong game một đội tối đa 8 người, bạn có thể đặt `=8`." |
| 211 | `集火打怪=0` | Tập trung đánh quái | `=0` tắt; `=1` bật tập trung đánh; `=2` mọi tài khoản cố gắng tụ lại một chỗ (không tập trung đánh). Ở `=1`: đội viên theo đội trưởng, đánh mục tiêu của đội trưởng; đội trưởng đi xa/về thành thì đội viên treo máy một mình đến khi đội trưởng quay lại điểm treo máy. |
| 212 | `为队员放加速术=0` | Niệm Tăng tốc cho đội viên | `=0` tắt, `=1` bật: buff Tăng tốc cho mọi đội viên; cùng một đội viên mặc định cách 15 phút buff 1 lần. |
| 213 | `为队员加血=0` | Hồi máu cho đội viên | `=0` tắt, `=1` bật: tự hồi máu cho đội viên máu thấp. (`=1` mặc định máu dưới 65% mới hồi; `=70` là máu dưới 70%; `=80` là dưới 80%; cứ thế.) |
| 214 | `为队员放技能=` | Dùng kỹ năng (buff) cho đội viên | Chú thích gốc: "Ví dụ điền `通暢氣脈術` để buff chỉ định cho đội viên; nhiều kỹ năng cách nhau dấu phẩy, ví dụ `通暢氣脈術,加速術`. Cùng một đội viên mặc định cách 19 phút buff 1 lần." Để trống = không dùng. |
| 216 | `组队密码=666` | Mật khẩu tổ đội = 666 (giá trị mặc định có sẵn trong gói) | Chú thích gốc: "Các máy có **cùng mật khẩu** sẽ được ghép với nhau. Bạn có thể đặt tất cả cùng một mật khẩu, server sẽ tự phân chia (ghép những tài khoản có **cùng bản đồ đánh quái** và **tọa độ đánh quái gần nhau** vào một đội)." 💡 Nếu server tổ đội mở ra Internet, nên đổi sang mã riêng để máy lạ không ghép nhầm vào đội của bạn. |
| 217 | `ip=127.0.0.1` | Địa chỉ IP của server tổ đội | Chú thích gốc: "IP trong mạng LAN hoặc IP ngoài (Internet)." `127.0.0.1` nghĩa là server tổ đội chạy **ngay trên máy này**. Nếu server chạy ở máy khác thì điền IP LAN của máy đó. |
| 218 | `port=9527` | Cổng (port) của server tổ đội = 9527 | Không có chú thích gốc. Phải trùng với cổng của chương trình server tổ đội; file `config.ini` trong thư mục `组队服务器` cũng đặt mặc định `port=9527`. 💡 Nếu đổi cổng thì đổi cả hai nơi. |
