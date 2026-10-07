# Game_Config: treo máy, kho đồ, mua bán, giao dịch

> **Gói:** `天堂经典版 Bd` bản 9.16, bot treo máy (auto farm) cho Lineage Classic.
> **Phạm vi tài liệu:** 9 file trong thư mục `Game_Config`, theo đúng thứ tự dưới đây. Cả 9 file đều mã hóa **UTF-8**, xuống dòng kiểu Windows (CRLF).

## Mục lục

| File | Số dòng | Chức năng |
|---|---|---|
| [`gj.txt`](#gjtxt) | 114 | Cấu hình treo máy đánh quái **theo từng mốc cấp độ**: bản đồ, tọa độ, quái không đánh, đồ không nhặt, khi nào về thành, khi nào ra khỏi làng. |
| [`PersonageStorage.txt`](#personagestoragetxt) | 4 | Vật phẩm tự **cất vào kho cá nhân** khi về thành vì đầy tải trọng. |
| [`PersonageTakeOutTheItem.txt`](#personagetakeouttheitemtxt) | 22 | Vật phẩm tự **lấy ra từ kho cá nhân** khi trong túi còn ít. |
| [`saveitem.txt`](#saveitemtxt) | 36 | Vật phẩm **giữ lại, không bán**. |
| [`SellBuy.txt`](#sellbuytxt) | 17 | Vật phẩm **tự mua** khi về làng, theo mốc cấp độ. |
| [`SellList.txt`](#selllisttxt) | 111 | Vật phẩm nào **bán cho NPC thương nhân nào**. |
| [`TradedConfig.txt`](#tradedconfigtxt) | 69 | Cấu hình **giao dịch / chuyển hàng** (倒货) từ acc treo máy sang acc nhận hàng. |
| [`Tradeditems.txt`](#tradeditemstxt) | 19 | Vật phẩm sẽ được chuyển đi và **số lượng kích hoạt** chuyển hàng. |
| [`TreasureName.txt`](#treasurenametxt) | 3 | Tên **bảo vật** (宝物) cần hiện số lượng trên bảng điều khiển (console). |

## ⚠️ Quy tắc chung khi sửa các file này (áp dụng cho cả 9 file)

1. **Giữ nguyên mọi chữ Trung Quốc.** Bot đọc chữ đúng từng ký tự: tên mục `[...]`, tên khóa (bên trái dấu `=`), tên bản đồ, tên vật phẩm, tên NPC, tên quái, tên server. Khi sửa, **chỉ thay số/giá trị**, hoặc thêm/bớt **tên vật phẩm đúng y như tên trong game**. Phần tiếng Việt trong tài liệu này chỉ để bạn hiểu, **đừng** gõ tiếng Việt vào file.
2. Dòng bắt đầu bằng `--` là **chú thích**, bot bỏ qua. Trên một dòng `khóa=giá trị   -- ...`, phần sau `--` cũng là chú thích.
3. Tên trong game là chữ **Phồn thể** (vd. `說話之島`), còn chú thích của tác giả phần lớn là chữ **Giản thể** (vd. 说话之岛). Với máy tính, hai kiểu chữ này **khác nhau**. Tên vật phẩm/bản đồ phải viết đúng kiểu chữ trong game, đừng tự chuyển đổi.
4. Dùng ký tự nửa độ rộng (bàn phím tiếng Anh): `=` `,` `|`. Không dùng dấu toàn độ rộng của Trung Quốc như `，` `＝` `｜`.
5. 💡 Lưu file ở mã hóa **UTF-8** như bản gốc (Notepad++ / VS Code). Nếu lưu sang ANSI/GBK thì chữ Trung hỏng và bot không đọc được.
6. Trong các bảng, cột **#** là số dòng trong file gốc. Ký hiệu `\|` trong bảng chính là ký tự `|` trong file (phải viết vậy để bảng Markdown không bị vỡ). Ký hiệu **(?)** nghĩa là bản dịch/giải thích chưa chắc chắn 100%.

**Quy ước chung:** `=0` thường là **tắt**, `=1` là **bật** (trừ khi ghi khác). Đơn vị: `秒` = giây, `分钟` = phút, `%` = phần trăm.

### Bức tranh tổng thể: các file này phối hợp thế nào (suy luận)

1. Nhân vật ra bãi đánh quái theo `gj.txt` (bản đồ, tọa độ, quái không đánh, đồ không nhặt).
2. Khi tải trọng đạt `负重回城` (trong `gj.txt`), bot về làng:
   - **bán** đồ cho NPC theo `SellList.txt`, **trừ** các món trong `saveitem.txt` (không bao giờ bán);
   - **mua** đồ theo `SellBuy.txt` (tên, tên bạc...);
   - **cất kho cá nhân** các món trong `PersonageStorage.txt`;
   - **lấy kho cá nhân** các món trong `PersonageTakeOutTheItem.txt` nếu trong túi còn ít.
3. Nếu bật giao dịch trong `TradedConfig.txt`, khi vàng hoặc vật phẩm trong `Tradeditems.txt` đạt số lượng, bot mang hàng đến **acc nhận hàng** để giao dịch.
4. Bot chờ máu/mana đạt `出门血量` / `出门蓝量` (trong `gj.txt`) rồi mới ra khỏi làng đi treo tiếp. Theo nhật ký cập nhật (`02-nhat-ky-cap-nhat.md`), bot còn chờ **độ no** (`饱食度`) đầy mới ra khỏi làng; nếu chưa no, bot tự mua thịt rồi ăn (tính năng này bật mặc định).
5. `TreasureName.txt` chỉ để **hiển thị** số lượng bảo vật trên bảng điều khiển, không ảnh hưởng hành vi.

Thứ tự chính xác các bước trong làng không được ghi trong file (?).

---

## gj.txt

**File này điều khiển gì:** `gj` là viết tắt pinyin của `挂机` (guà jī = treo máy). Đây là file cấu hình **treo máy đánh quái theo mốc cấp độ nhân vật**: đánh ở bản đồ nào, tọa độ nào, quái nào bỏ qua, quái nào đánh trả, đồ nào không nhặt, khi nào về thành, máu/mana bao nhiêu thì ra khỏi làng.

**Khi nào bot dùng:** mỗi lần nhân vật đi treo máy (từ làng ra bãi quái), trong lúc đánh quái, nhặt đồ và khi quyết định về thành.

**Liên quan tới file khác trong gói** (xem thêm `04-baseconfig.md`):
- `BaseConfig.txt`, mục `[挂机全局配置]`, khóa `启用全局配置`: `=0` thì bot dùng `gj.txt`; `=1` thì bot dùng cấu hình chung trong `BaseConfig.txt` cho **mọi cấp** (các khóa trùng tên với gj.txt).
- `G_Filtering_Monster_And_Item.txt`: khi `开启=1`, ba dòng `怪物过滤`, `反击怪物`, `拾取过滤` trong `gj.txt` **mất hiệu lực** (dùng danh sách toàn cục); khi `开启=0` thì `gj.txt` có hiệu lực.
- `BaseConfig.txt`, mục `[按时间切换挂机配置]`, khóa `分段挂机配置`: đổi sang file treo máy khác (vd. `gj2.txt`) theo khung giờ (bật bằng khóa `开启切换=1` ngay phía trên). File đó là bản chép từ `gj.txt` rồi đổi tên, nên có cấu trúc giống hệt.

✏️ **Khi sửa:** giữ nguyên chữ Trung (tên mục, tên khóa, tên bản đồ, tên quái, tên vật phẩm); chỉ đổi số/giá trị, hoặc thêm/bớt tên trong danh sách (cách nhau bằng dấu phẩy `,`).

### Cách các mốc cấp độ `[1]`, `[5]`, `[7]`, `[10]`, `[15]` hoạt động

File chia thành 5 mục, mỗi mục bắt đầu bằng một số trong ngoặc vuông. Số đó là **cấp độ nhân vật bắt đầu áp dụng mục**. File không ghi rõ quy tắc, nhưng theo cách đặt tên (giống `SellBuy.txt`), có thể hiểu: nhân vật **cấp ≥ N** dùng mục `[N]` cho đến khi đạt mốc kế tiếp (?). Mỗi mục có đủ 21 khóa giống nhau, chỉ khác giá trị.

| Mục | Áp dụng cho cấp (suy luận) | Bản đồ đánh quái (`打怪地图`) | Tọa độ (`打怪坐标`) |
|---|---|---|---|
| `[1]` | 1 – 4 | `說話之島` = Talking Island (Đảo Nói Chuyện) | `32526,32830` |
| `[5]` | 5 – 6 | `說話之島` = Talking Island | `32574,33100` |
| `[7]` | 7 – 9 | `說話之島` = Talking Island | `32694,32872\|32668,32848` (2 điểm) |
| `[10]` | 10 – 14 | `古魯丁` = Gludin (vùng quanh làng Gludin) | `32923,32831` |
| `[15]` | từ 15 trở lên | `銀騎士地區` = Khu vực Hiệp sĩ Bạc (Silver Knight) | `32931,33375` |

Ngoài bản đồ/tọa độ, các mục chỉ khác nhau ở danh sách `怪物过滤` (quái không đánh) và `拾取过滤` (đồ không nhặt); xem chi tiết ở từng mục bên dưới.

💡 **Lưu ý:**
- Muốn thêm mốc mới (vd. `[20]`): chép nguyên một khối mục (từ dòng `[..]` tới dòng `出门蓝量=...`), đổi số trong ngoặc, sửa bản đồ/tọa độ (?). File gốc không nói rõ việc này; thêm xong nên chạy thử và quan sát.
- Tên bản đồ phải ghi đúng tên mà bot nhận biết. Hướng dẫn sử dụng có nhiều ví dụ `打怪地图=...` và các danh sách bản đồ mới được hỗ trợ (xem `01-huong-dan-su-dung.md`).
- Tọa độ lấy trong game (dạng `x,y`). Nhiều điểm thì nối bằng `|`.

### Giải thích từng khóa (21 dòng, giống nhau ở mọi mục)

Bảng dưới lấy mục `[1]` (dòng 1–22) làm mẫu. Các mục khác dùng đúng các khóa này. Chú thích `--` sau mỗi khóa **giống hệt nhau ở cả 5 mục**, nên chỉ dịch một lần ở bảng này; bảng của từng mục bên dưới chỉ ghi giá trị riêng của mục đó.

| # | Dòng gốc (mục `[1]`) | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `[1]` | Mốc cấp độ 1 | Tên mục là cấp độ bắt đầu áp dụng (xem bảng trên). |
| 2 | `怪物过滤=...` (danh sách dài, xem bên dưới) | Lọc quái = danh sách quái/NPC **không đánh** | Tên cách nhau bằng dấu phẩy `,`. Bot không chủ động tấn công các tên này: lính gác, NPC, quái quá mạnh, thú vô hại... Danh sách đầy đủ ở bảng "Danh sách quái" bên dưới. |
| 3 | `反击怪物=史萊姆,漂浮之眼,石頭高崙` | Quái phản công | Các quái này có trong danh sách lọc (không chủ động đánh), nhưng **nếu chúng đánh bạn thì bot đánh trả**. Mặc định: `史萊姆` (Slime), `漂浮之眼` (Mắt lơ lửng, Floating Eye), `石頭高崙` (Golem đá, Stone Golem). |
| 4 | `拾取过滤=...` (danh sách dài, xem bên dưới) | Lọc nhặt đồ = danh sách đồ **không nhặt** (?) | Tên vật phẩm cách nhau bằng dấu phẩy. File không giải thích; theo cách hiểu giống `怪物过滤` (lọc = loại ra), đây là các món bot **bỏ qua, không nhặt**, chủ yếu là đồ rẻ hoặc nặng (?). |
| 5 | `负重回城=80` | Về thành khi tải trọng đạt 80 | Chú thích gốc: "Đạt mức này thì kích hoạt về thành để tiếp tế và bán đồ. Dưới 50 thì máu/mana tự hồi, vượt quá thì ngừng hồi." Đơn vị: **% tải trọng** (负重); file không ghi đơn vị, nhưng trong Lineage tải trọng hiển thị theo %. 💡 Theo chú thích, khi tải trọng vượt 50% thì nhân vật **ngừng tự hồi** máu/mana. Với giá trị 80, từ 50% đến 80% nhân vật vẫn đánh tiếp nhưng không tự hồi. Muốn an toàn hơn thì hạ xuống ≤ 50. |
| 6 | `打怪范围=25` | Phạm vi đánh quái = 25 | Chú thích gốc: "Phạm vi tìm quái." Bot chỉ tìm quái trong bán kính này quanh tọa độ đánh quái. Đơn vị nhiều khả năng là **ô bản đồ** (?). |
| 7 | `定点挂机=0` | Treo máy cố định tại chỗ | Chú thích gốc: "`=1`: đứng yên tại tọa độ đánh quái để đánh, không di chuyển." `=0` (mặc định): tắt, bot đi lại trong phạm vi để tìm quái. |
| 8 | `瞬移找怪=0` | Dịch chuyển tức thời để tìm quái | Chú thích gốc: "Chỉ có tác dụng ở 说话之岛 (Talking Island); `=0` là tắt, `=1` là bật." Khi bật, bot dịch chuyển (nhảy chỗ) để tìm quái thay vì đi bộ (?). `瞬移` là viết tắt của "瞬間移動" (dịch chuyển tức thời), nên nhiều khả năng bot dùng cuộn `瞬間移動卷軸` để nhảy ngẫu nhiên quanh đảo; vì Talking Island là một hòn đảo kín nên cách này chỉ hữu ích ở đó (?). |
| 9 | `内挂挂机=0` | Treo máy bằng "nội quải" (`内挂`, chế độ auto có sẵn trong game) (?) | Chú thích gốc: "Nội quải có phạm vi đánh quái khá nhỏ, và không nhặt vàng do người khác làm rơi. Tự cân nhắc có dùng hay không. 0 tắt, 1 bật." |
| 10 | `打怪地图=說話之島` | Bản đồ đánh quái | `說話之島` = Talking Island (Đảo Nói Chuyện). |
| 11 | `打怪坐标=32526,32830` | Tọa độ đánh quái | Dạng `x,y`. Có thể đặt nhiều điểm, ngăn cách bằng `\|` (ví dụ mục `[7]`: `32694,32872\|32668,32848`). |
| 12 | `优先传送=0,0` | Ưu tiên dịch chuyển | Chú thích gốc: "Ưu tiên dịch chuyển đến điểm dịch chuyển có trên cuộn `说话卷轴` (cuộn dịch chuyển về Talking Island) gần tọa độ này, sau đó mới đi bộ tới tọa độ đánh quái." `0,0` = không dùng (?). 💡 Theo chú thích, `说话卷轴` có sẵn **nhiều điểm dịch chuyển** để chọn; bot chọn điểm gần tọa độ bạn ghi ở đây nhất. `BaseConfig.txt` có các khóa `自动领取说话卷轴` (tự nhận cuộn này) và `无说话卷轴时停止脚本` (dừng bot khi trong túi không có cuộn này). |
| 13 | `走向挂机点线路=` | Lộ trình đi đến điểm treo máy | Chú thích gốc: "Ví dụ đặt các tọa độ `x,y\|x,y\|x,y`, bot sẽ đi theo lộ trình này đến tọa độ đánh quái. Có thể tự đặt để đi vòng, tránh một số chỗ." Để trống (mặc định) thì bot tự tìm đường. |
| 14 | `攻击寻路到挂机点路上怪物=0` | Đánh quái gặp trên đường tới điểm treo máy | `=0` tắt; `=1` đánh **mọi** quái trên đường; `=2` chỉ đánh quái trên đường trong **hầm ngục** (地监); `=3` chỉ đánh quái trên đường **cùng tầng** hầm ngục. |
| 15 | `反击全部怪物=0` | Phản công mọi quái | `=0` tắt, `=1` bật: hễ quái nào đang đánh bạn là đánh trả. |
| 16 | `拾取别人金币=1` | Nhặt vàng của người khác | `=0` tắt, `=1` bật: khi **không còn quái** để đánh **và** không còn đồ do chính mình giết quái rơi ra để nhặt, thì nhặt vàng người khác làm rơi. Tắt thì không nhặt. Mặc định: bật. |
| 17 | `不拾取物品=0` | Không nhặt đồ | `=0` tắt, `=1` bật: **không nhặt bất kỳ** vật phẩm và vàng nào. |
| 18 | `低于多少金币不拾取=0` | Không nhặt vàng dưới bao nhiêu | `=0` tắt. Lớn hơn 0, ví dụ `=5`: không nhặt đống vàng **từ 5 trở xuống**. |
| 19 | `记忆卷轴传送=0` | Dịch chuyển bằng cuộn ghi nhớ vị trí | `=0` tắt. `=1` bật, dịch chuyển tới **điểm ghi nhớ thứ 1**; `=2` tới điểm thứ 2; `=3` tới điểm thứ 3; cứ thế tiếp. **Phải tự ghi nhớ vị trí bằng tay** trong game trước. Nếu dùng `地監記憶書` (sách ghi nhớ hầm ngục) thì điền `1` là được. 💡 Danh sách bản đồ hỗ trợ `地監記憶書` có trong `01-huong-dan-su-dung.md`. |
| 20 | `优先攻击在拾取=0` | Ưu tiên đánh quái rồi mới nhặt | `=0` tắt, `=1` bật. Chú thích gốc: "Dành cho hầm ngục: quái quá nhiều thì có thể bật." (Chữ `在` trong tên khóa là viết nhầm của `再` = "rồi mới", nhưng vẫn phải giữ nguyên `在`.) |
| 21 | `出门血量=100` | Máu để ra khỏi làng | Chú thích gốc: "Nếu `=100` nghĩa là máu đạt **100%** thì mới xuất phát từ làng." Đơn vị: % máu (HP). |
| 22 | `出门蓝量=95` | Mana để ra khỏi làng | Chú thích gốc: "Nếu `=100` nghĩa là mana đạt 100% thì mới xuất phát từ làng." Giá trị hiện tại `95` = chờ mana đạt **95%**. Đơn vị: % mana (MP). |

### Danh sách quái dùng trong `怪物过滤` và `反击怪物`

Bảng gộp mọi tên xuất hiện trong 5 mục. Cột cuối cho biết tên đó có trong `怪物过滤` (không đánh) của những mục nào.

| Tên gốc | Nghĩa | Có trong `怪物过滤` của mục |
|---|---|---|
| `巡守` | Lính tuần tra (Patrol) | [1] [5] [7] [10] [15] |
| `史萊姆` | Slime (quái chất nhờn) | [1] [5] [7] [10] [15]; cũng có trong `反击怪物` ở mọi mục |
| `長老` | Trưởng lão (Elder), NPC | [1] [5] [7] [10] (không có ở [15]) |
| `警衛` | Lính gác (Guard) | [1] [5] [7] [10] [15] |
| `奇岩警衛` | Lính gác Giran (`奇岩` = Giran) | [1] [5] [7] [10] [15] |
| `肯特城警衛` | Lính gác thành Kent | [1] [5] [7] [10] [15] (ở [10] và [15] tên này bị ghi **2 lần**, không sao) |
| `風木城警衛` | Lính gác thành Windawood (`風木`) | [1] [5] [7] [10] [15] |
| `海音警衛` | Lính gác Heine (`海音` = Heine) | [1] [5] [7] [10] [15] |
| `侏儒警衛` | Lính gác Người lùn (Dwarf Guard) | [1] [5] [7] [10] [15] |
| `城堡守衛` | Vệ binh lâu đài (Castle guard) | [1] [5] [7] [10] [15] |
| `守門人` | Người gác cổng (Gatekeeper) | [1] [5] [7] [10] [15] |
| `漂浮之眼` | Mắt lơ lửng (Floating Eye) | [1] [5] [7] [10] (không có ở [15]); có trong `反击怪物` ở mọi mục |
| `克特` | Kurtz (?), tên một quái/boss | [1] [5] [7] [10] [15] |
| `石頭高崙` | Golem đá (Stone Golem) | [1] [5] [7] [10] (không có ở [15]); có trong `反击怪物` ở mọi mục |
| `牧羊犬` | Chó chăn cừu (Shepherd dog) | chỉ [5] |
| `葛林` | Gremlin (?) | [10] [15] |
| `杜賓狗` | Chó Doberman | chỉ [10] |
| `飛龍` | Phi long (rồng bay, Drake) | [1] [5] [7] [10] [15] |
| `青蛙` | Ếch (Frog) | [1] [5] [7] [10] [15] |
| `兔子` | Thỏ (Rabbit) | [1] [5] [7] [10] [15] |
| `鹿` | Hươu (Deer) | [1] [5] [7] [10] [15] |
| `安特` | Ent (người cây) | [1] [5] [7] [10] [15] |
| `強盜` | Cướp (Bandit) | [1] [5] [7] [10] [15] |
| `魚` | Cá (Fish) | [1] [5] [7] [10] [15] |

💡 Ở mục `[15]`, `漂浮之眼`, `石頭高崙`, `長老` không còn trong danh sách lọc, nghĩa là ở cấp này bot sẽ **chủ động đánh** chúng (`漂浮之眼`, `石頭高崙` vẫn có trong `反击怪物` nhưng điều đó không còn ý nghĩa vì đằng nào cũng đánh).

### Danh sách đồ trong `拾取过滤` (đồ không nhặt)

Có 2 phiên bản danh sách: **A** dùng ở mục `[1]`, `[5]`, `[7]`; **B** dùng ở mục `[10]`, `[15]`.

| Tên gốc | Nghĩa | Có trong danh sách |
|---|---|---|
| `盾` | Khiên (Shield) | A |
| `短劍` | Đoản kiếm (Dagger / Short sword) | A, B |
| `侏儒斗篷` | Áo choàng Người lùn (Dwarvish Cloak) | A, B |
| `斧` | Rìu (Axe) | A |
| `頭盔` | Mũ giáp (Helmet) | A |
| `木棒` | Gậy gỗ (Club) | A, B |
| `燈` | Đèn (Lamp / Lantern) | A, B |
| `環甲` | Giáp vòng (Ring mail) | A |
| `亞連` | "Á Liên", có lẽ là một loại vũ khí cấp thấp (?) | A |
| `皮甲` | Giáp da (Leather armor) | A |
| `弗萊爾` | Chùy xích (Flail) | A, B |
| `短統靴` | Ủng cổ ngắn (Low boots) | A |
| `烏木魔杖` | Gậy phép gỗ mun (Ebony wand) | A, B |
| `侏儒鐵盔` | Mũ sắt Người lùn (Dwarvish Iron Helm) | A |
| `斗篷` | Áo choàng (Cloak) | A |
| `釘錘` | Chùy gai (Mace / Morning star) | A, B |
| `歐西斯鏈甲` | Giáp xích Orcish (`歐西斯` = Orcish (?)) | A |
| `保護罩` | Khiên bảo vệ (?): cùng tên với phép `保護罩` (Shield) trong `BaseConfig.txt`; ở đây là một món đồ rơi trên đất, chưa xác định chính xác | B |
| `漂浮之眼肉` | Thịt Floating Eye | B |
| `松木魔杖` | Gậy phép gỗ thông (Pine wand) | B |
| `純粹的米索莉塊` | Khối Mithril tinh khiết (Pure Mithril) | B |
| `肉` | Thịt (Meat) | A, B |
| `胡蘿蔔` | Cà rốt (Carrot) | A, B |
| `蘋果` | Táo (Apple) | A, B |
| `檸檬` | Chanh (Lemon) | A, B |
| `香蕉` | Chuối (Banana) | A, B |
| `蛋` | Trứng (Egg) | A, B |
| `橘子` | Quýt (Orange) | A, B |

💡 Từ mục `[10]`, các món `盾`, `斧`, `頭盔`, `環甲`, `亞連`, `皮甲`, `短統靴`, `侏儒鐵盔`, `斗篷`, `歐西斯鏈甲` bị bỏ khỏi danh sách lọc, nên bot sẽ **nhặt** chúng (nhiều món trong số này có NPC mua trong `SellList.txt`).

### Mục `[1]` (dòng 1–22): cấp 1 trở lên (?)

Ba dòng danh sách (chép nguyên văn):

```
怪物过滤=巡守,史萊姆,長老,警衛,奇岩警衛,肯特城警衛,風木城警衛,海音警衛,侏儒警衛,城堡守衛,守門人,漂浮之眼,克特,石頭高崙,飛龍,青蛙,兔子,鹿,安特,強盜,魚
反击怪物=史萊姆,漂浮之眼,石頭高崙
拾取过滤=盾,短劍,侏儒斗篷,斧,頭盔,木棒,燈,環甲,亞連,皮甲,弗萊爾,短統靴,烏木魔杖,侏儒鐵盔,斗篷,釘錘,歐西斯鏈甲,肉,胡蘿蔔,蘋果,檸檬,香蕉,蛋,橘子
```

- `怪物过滤` (dòng 2): 21 tên, gồm: `巡守`, `史萊姆`, `長老`, `警衛`, `奇岩警衛`, `肯特城警衛`, `風木城警衛`, `海音警衛`, `侏儒警衛`, `城堡守衛`, `守門人`, `漂浮之眼`, `克特`, `石頭高崙`, `飛龍`, `青蛙`, `兔子`, `鹿`, `安特`, `強盜`, `魚` (nghĩa xem bảng "Danh sách quái").
- `反击怪物` (dòng 3): `史萊姆`, `漂浮之眼`, `石頭高崙`.
- `拾取过滤` (dòng 4): danh sách **A** (24 món).

| # | Dòng gốc | Nghĩa | Ghi chú cho mục này |
|---|---|---|---|
| 5 | `负重回城=80` | Về thành khi tải trọng 80% | Mặc định. |
| 6 | `打怪范围=25` | Phạm vi tìm quái 25 | |
| 7 | `定点挂机=0` | Treo cố định | Tắt. |
| 8 | `瞬移找怪=0` | Dịch chuyển tìm quái | Tắt (bản đồ là Talking Island nên bật được). |
| 9 | `内挂挂机=0` | Treo bằng auto trong game | Tắt. |
| 10 | `打怪地图=說話之島` | Bản đồ: Talking Island | |
| 11 | `打怪坐标=32526,32830` | Tọa độ đánh quái | 1 điểm. |
| 12 | `优先传送=0,0` | Ưu tiên dịch chuyển | Không dùng. |
| 13 | `走向挂机点线路=` | Lộ trình đi tới điểm treo | Trống = tự tìm đường. |
| 14 | `攻击寻路到挂机点路上怪物=0` | Đánh quái trên đường | Tắt. |
| 15 | `反击全部怪物=0` | Phản công mọi quái | Tắt. |
| 16 | `拾取别人金币=1` | Nhặt vàng người khác | Bật. |
| 17 | `不拾取物品=0` | Không nhặt gì cả | Tắt (vẫn nhặt). |
| 18 | `低于多少金币不拾取=0` | Ngưỡng vàng không nhặt | Tắt (nhặt mọi đống vàng). |
| 19 | `记忆卷轴传送=0` | Dịch chuyển bằng cuộn ghi nhớ | Tắt. |
| 20 | `优先攻击在拾取=0` | Đánh trước, nhặt sau | Tắt. |
| 21 | `出门血量=100` | Máu để ra khỏi làng | 100%. |
| 22 | `出门蓝量=95` | Mana để ra khỏi làng | 95%. |

### Mục `[5]` (dòng 24–45): cấp 5 trở lên (?)

```
怪物过滤=巡守,史萊姆,長老,警衛,奇岩警衛,肯特城警衛,風木城警衛,海音警衛,侏儒警衛,城堡守衛,守門人,漂浮之眼,克特,石頭高崙,牧羊犬,飛龍,青蛙,兔子,鹿,安特,強盜,魚
反击怪物=史萊姆,漂浮之眼,石頭高崙
拾取过滤=盾,短劍,侏儒斗篷,斧,頭盔,木棒,燈,環甲,亞連,皮甲,弗萊爾,短統靴,烏木魔杖,侏儒鐵盔,斗篷,釘錘,歐西斯鏈甲,肉,胡蘿蔔,蘋果,檸檬,香蕉,蛋,橘子
```

- `怪物过滤` (dòng 25): 22 tên: `巡守`, `史萊姆`, `長老`, `警衛`, `奇岩警衛`, `肯特城警衛`, `風木城警衛`, `海音警衛`, `侏儒警衛`, `城堡守衛`, `守門人`, `漂浮之眼`, `克特`, `石頭高崙`, `牧羊犬`, `飛龍`, `青蛙`, `兔子`, `鹿`, `安特`, `強盜`, `魚`. Khác mục `[1]`: **thêm `牧羊犬`** (chó chăn cừu).
- `反击怪物` (dòng 26): `史萊姆`, `漂浮之眼`, `石頭高崙`.
- `拾取过滤` (dòng 27): danh sách **A**.

| # | Dòng gốc | Nghĩa | Ghi chú cho mục này |
|---|---|---|---|
| 28 | `负重回城=80` | Về thành khi tải trọng 80% | |
| 29 | `打怪范围=25` | Phạm vi tìm quái 25 | |
| 30 | `定点挂机=0` | Treo cố định | Tắt. |
| 31 | `瞬移找怪=0` | Dịch chuyển tìm quái | Tắt. |
| 32 | `内挂挂机=0` | Treo bằng auto trong game | Tắt. |
| 33 | `打怪地图=說話之島` | Bản đồ: Talking Island | |
| 34 | `打怪坐标=32574,33100` | Tọa độ đánh quái | 1 điểm, khác mục `[1]`. |
| 35 | `优先传送=0,0` | Ưu tiên dịch chuyển | Không dùng. |
| 36 | `走向挂机点线路=` | Lộ trình đi tới điểm treo | Trống. |
| 37 | `攻击寻路到挂机点路上怪物=0` | Đánh quái trên đường | Tắt. |
| 38 | `反击全部怪物=0` | Phản công mọi quái | Tắt. |
| 39 | `拾取别人金币=1` | Nhặt vàng người khác | Bật. |
| 40 | `不拾取物品=0` | Không nhặt gì cả | Tắt. |
| 41 | `低于多少金币不拾取=0` | Ngưỡng vàng không nhặt | Tắt. |
| 42 | `记忆卷轴传送=0` | Dịch chuyển bằng cuộn ghi nhớ | Tắt. |
| 43 | `优先攻击在拾取=0` | Đánh trước, nhặt sau | Tắt. |
| 44 | `出门血量=100` | Máu để ra khỏi làng | 100%. |
| 45 | `出门蓝量=95` | Mana để ra khỏi làng | 95%. |

### Mục `[7]` (dòng 47–68): cấp 7 trở lên (?)

```
怪物过滤=巡守,史萊姆,長老,警衛,奇岩警衛,肯特城警衛,風木城警衛,海音警衛,侏儒警衛,城堡守衛,守門人,漂浮之眼,克特,石頭高崙,飛龍,青蛙,兔子,鹿,安特,強盜,魚
反击怪物=史萊姆,漂浮之眼,石頭高崙
拾取过滤=盾,短劍,侏儒斗篷,斧,頭盔,木棒,燈,環甲,亞連,皮甲,弗萊爾,短統靴,烏木魔杖,侏儒鐵盔,斗篷,釘錘,歐西斯鏈甲,肉,胡蘿蔔,蘋果,檸檬,香蕉,蛋,橘子
打怪坐标=32694,32872|32668,32848
```

- `怪物过滤` (dòng 48): giống hệt mục `[1]` (21 tên: `巡守`, `史萊姆`, `長老`, `警衛`, `奇岩警衛`, `肯特城警衛`, `風木城警衛`, `海音警衛`, `侏儒警衛`, `城堡守衛`, `守門人`, `漂浮之眼`, `克特`, `石頭高崙`, `飛龍`, `青蛙`, `兔子`, `鹿`, `安特`, `強盜`, `魚`).
- `反击怪物` (dòng 49): `史萊姆`, `漂浮之眼`, `石頭高崙`.
- `拾取过滤` (dòng 50): danh sách **A**.

| # | Dòng gốc | Nghĩa | Ghi chú cho mục này |
|---|---|---|---|
| 51 | `负重回城=80` | Về thành khi tải trọng 80% | |
| 52 | `打怪范围=25` | Phạm vi tìm quái 25 | |
| 53 | `定点挂机=0` | Treo cố định | Tắt. |
| 54 | `瞬移找怪=0` | Dịch chuyển tìm quái | Tắt. |
| 55 | `内挂挂机=0` | Treo bằng auto trong game | Tắt. |
| 56 | `打怪地图=說話之島` | Bản đồ: Talking Island | |
| 57 | `打怪坐标=32694,32872\|32668,32848` | Tọa độ đánh quái | **2 điểm** (xem dòng chép nguyên văn trong khối code ở trên): `32694,32872` và `32668,32848`. |
| 58 | `优先传送=0,0` | Ưu tiên dịch chuyển | Không dùng. |
| 59 | `走向挂机点线路=` | Lộ trình đi tới điểm treo | Trống. |
| 60 | `攻击寻路到挂机点路上怪物=0` | Đánh quái trên đường | Tắt. |
| 61 | `反击全部怪物=0` | Phản công mọi quái | Tắt. |
| 62 | `拾取别人金币=1` | Nhặt vàng người khác | Bật. |
| 63 | `不拾取物品=0` | Không nhặt gì cả | Tắt. |
| 64 | `低于多少金币不拾取=0` | Ngưỡng vàng không nhặt | Tắt. |
| 65 | `记忆卷轴传送=0` | Dịch chuyển bằng cuộn ghi nhớ | Tắt. |
| 66 | `优先攻击在拾取=0` | Đánh trước, nhặt sau | Tắt. |
| 67 | `出门血量=100` | Máu để ra khỏi làng | 100%. |
| 68 | `出门蓝量=95` | Mana để ra khỏi làng | 95%. |

### Mục `[10]` (dòng 70–91): cấp 10 trở lên (?)

```
怪物过滤=巡守,史萊姆,長老,警衛,奇岩警衛,肯特城警衛,風木城警衛,海音警衛,侏儒警衛,城堡守衛,守門人,漂浮之眼,克特,石頭高崙,葛林,杜賓狗,肯特城警衛,飛龍,青蛙,兔子,鹿,安特,強盜,魚
反击怪物=史萊姆,漂浮之眼,石頭高崙
拾取过滤=短劍,侏儒斗篷,木棒,燈,弗萊爾,保護罩,烏木魔杖,釘錘,漂浮之眼肉,松木魔杖,純粹的米索莉塊,肉,胡蘿蔔,蘋果,檸檬,香蕉,蛋,橘子
```

- `怪物过滤` (dòng 71): 24 mục: `巡守`, `史萊姆`, `長老`, `警衛`, `奇岩警衛`, `肯特城警衛`, `風木城警衛`, `海音警衛`, `侏儒警衛`, `城堡守衛`, `守門人`, `漂浮之眼`, `克特`, `石頭高崙`, `葛林`, `杜賓狗`, `肯特城警衛` (lặp lại), `飛龍`, `青蛙`, `兔子`, `鹿`, `安特`, `強盜`, `魚`. Khác mục `[1]`: **thêm `葛林`** (Gremlin (?)) và **`杜賓狗`** (chó Doberman).
- `反击怪物` (dòng 72): `史萊姆`, `漂浮之眼`, `石頭高崙`.
- `拾取过滤` (dòng 73): danh sách **B** (18 món): `短劍`, `侏儒斗篷`, `木棒`, `燈`, `弗萊爾`, `保護罩`, `烏木魔杖`, `釘錘`, `漂浮之眼肉`, `松木魔杖`, `純粹的米索莉塊`, `肉`, `胡蘿蔔`, `蘋果`, `檸檬`, `香蕉`, `蛋`, `橘子`.

| # | Dòng gốc | Nghĩa | Ghi chú cho mục này |
|---|---|---|---|
| 74 | `负重回城=80` | Về thành khi tải trọng 80% | |
| 75 | `打怪范围=25` | Phạm vi tìm quái 25 | |
| 76 | `定点挂机=0` | Treo cố định | Tắt. |
| 77 | `瞬移找怪=0` | Dịch chuyển tìm quái | Tắt (và cũng không có tác dụng vì không phải Talking Island). |
| 78 | `内挂挂机=0` | Treo bằng auto trong game | Tắt. |
| 79 | `打怪地图=古魯丁` | Bản đồ: Gludin (`古魯丁`) | Đổi sang vùng Gludin. |
| 80 | `打怪坐标=32923,32831` | Tọa độ đánh quái | 1 điểm. |
| 81 | `优先传送=0,0` | Ưu tiên dịch chuyển | Không dùng. |
| 82 | `走向挂机点线路=` | Lộ trình đi tới điểm treo | Trống. |
| 83 | `攻击寻路到挂机点路上怪物=0` | Đánh quái trên đường | Tắt. |
| 84 | `反击全部怪物=0` | Phản công mọi quái | Tắt. |
| 85 | `拾取别人金币=1` | Nhặt vàng người khác | Bật. |
| 86 | `不拾取物品=0` | Không nhặt gì cả | Tắt. |
| 87 | `低于多少金币不拾取=0` | Ngưỡng vàng không nhặt | Tắt. |
| 88 | `记忆卷轴传送=0` | Dịch chuyển bằng cuộn ghi nhớ | Tắt. |
| 89 | `优先攻击在拾取=0` | Đánh trước, nhặt sau | Tắt. |
| 90 | `出门血量=100` | Máu để ra khỏi làng | 100%. |
| 91 | `出门蓝量=95` | Mana để ra khỏi làng | 95%. |

### Mục `[15]` (dòng 93–114): cấp 15 trở lên (?)

```
怪物过滤=巡守,史萊姆,警衛,奇岩警衛,肯特城警衛,風木城警衛,海音警衛,侏儒警衛,城堡守衛,守門人,克特,葛林,肯特城警衛,飛龍,青蛙,兔子,鹿,安特,強盜,魚
反击怪物=史萊姆,漂浮之眼,石頭高崙
拾取过滤=短劍,侏儒斗篷,木棒,燈,弗萊爾,保護罩,烏木魔杖,釘錘,漂浮之眼肉,松木魔杖,純粹的米索莉塊,肉,胡蘿蔔,蘋果,檸檬,香蕉,蛋,橘子
```

- `怪物过滤` (dòng 94): 20 mục: `巡守`, `史萊姆`, `警衛`, `奇岩警衛`, `肯特城警衛`, `風木城警衛`, `海音警衛`, `侏儒警衛`, `城堡守衛`, `守門人`, `克特`, `葛林`, `肯特城警衛` (lặp lại), `飛龍`, `青蛙`, `兔子`, `鹿`, `安特`, `強盜`, `魚`. So với mục `[10]`: **bỏ** `長老`, `漂浮之眼`, `石頭高崙`, `杜賓狗` (bot sẽ đánh các quái này).
- `反击怪物` (dòng 95): `史萊姆`, `漂浮之眼`, `石頭高崙`.
- `拾取过滤` (dòng 96): danh sách **B** (giống mục `[10]`).

| # | Dòng gốc | Nghĩa | Ghi chú cho mục này |
|---|---|---|---|
| 97 | `负重回城=80` | Về thành khi tải trọng 80% | |
| 98 | `打怪范围=25` | Phạm vi tìm quái 25 | |
| 99 | `定点挂机=0` | Treo cố định | Tắt. |
| 100 | `瞬移找怪=0` | Dịch chuyển tìm quái | Tắt. |
| 101 | `内挂挂机=0` | Treo bằng auto trong game | Tắt. |
| 102 | `打怪地图=銀騎士地區` | Bản đồ: Khu vực Hiệp sĩ Bạc (Silver Knight) | |
| 103 | `打怪坐标=32931,33375` | Tọa độ đánh quái | 1 điểm. |
| 104 | `优先传送=0,0` | Ưu tiên dịch chuyển | Không dùng. |
| 105 | `走向挂机点线路=` | Lộ trình đi tới điểm treo | Trống. |
| 106 | `攻击寻路到挂机点路上怪物=0` | Đánh quái trên đường | Tắt. |
| 107 | `反击全部怪物=0` | Phản công mọi quái | Tắt. |
| 108 | `拾取别人金币=1` | Nhặt vàng người khác | Bật. |
| 109 | `不拾取物品=0` | Không nhặt gì cả | Tắt. |
| 110 | `低于多少金币不拾取=0` | Ngưỡng vàng không nhặt | Tắt. |
| 111 | `记忆卷轴传送=0` | Dịch chuyển bằng cuộn ghi nhớ | Tắt. |
| 112 | `优先攻击在拾取=0` | Đánh trước, nhặt sau | Tắt. |
| 113 | `出门血量=100` | Máu để ra khỏi làng | 100%. |
| 114 | `出门蓝量=95` | Mana để ra khỏi làng | 95%. |

---

## PersonageStorage.txt

**File này điều khiển gì:** `Personage` = cá nhân, `Storage` = cất kho. Đây là danh sách vật phẩm bot **tự cất vào kho cá nhân** (仓库 = kho đồ) của nhân vật.

**Khi nào bot dùng:** theo chú thích dòng 1, **chỉ khi nhân vật về thành vì đầy tải trọng** (`负重回城` trong `gj.txt`) thì mới cất các món trong file này. Mỗi dòng một tên vật phẩm.

✏️ **Khi sửa:** mỗi dòng ghi đúng một tên vật phẩm, chép y nguyên tên trong game (chữ Phồn thể); muốn tắt một dòng thì thêm `--` ở đầu.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `--此文件为个人仓库存入的物品配置   在负重满了回城时 才会存入此文件物品` | Chú thích | "File này cấu hình các vật phẩm **cất vào kho cá nhân**. Chỉ khi **đầy tải trọng và về thành** thì mới cất các vật phẩm trong file này." |
| 2 | `--金屬塊		前面2个符号  代表这行注释  不会存入` | Chú thích kiêm ví dụ | `金屬塊` = Khối kim loại. Phần còn lại: "Hai ký hiệu ở đầu dòng nghĩa là dòng này là chú thích, sẽ **không** được cất kho." 💡 Muốn cất khối kim loại thì sửa dòng này thành đúng `金屬塊` (bỏ `--` **và** bỏ phần chữ phía sau). |
| 3 | `金疮药` | "Kim sang dược" (thuốc trị thương) | Dòng đang **có hiệu lực**. |
| 4 | `太阳水` | "Nước Mặt Trời" | Dòng đang **có hiệu lực**. |

💡 **Lưu ý:** `金疮药` và `太阳水` được viết bằng chữ **Giản thể**, trong khi tên vật phẩm Lineage Classic là chữ Phồn thể. Hai tên này trông giống **tên ví dụ** (tên thuốc quen thuộc của game khác) (?), nhiều khả năng không trùng với vật phẩm nào trong game nên thực tế bot không cất gì. Muốn dùng, hãy thay bằng tên vật phẩm thật trong game, ví dụ `金屬塊`.

---

## PersonageTakeOutTheItem.txt

**File này điều khiển gì:** `Take Out The Item` = lấy vật phẩm ra. File cấu hình việc **tự động lấy vật phẩm từ kho cá nhân**: khi số lượng trong túi ít hơn mức chỉ định thì lấy ra số lượng đã đặt.

**Khi nào bot dùng:** khi số lượng một vật phẩm trong túi chạm ngưỡng; tùy cột thứ 4, bot lấy **ngay khi dùng hết** hoặc **chỉ khi nhân vật đang ở trong làng**. (File tương tự cho kho huyết minh/clan là `BloodTakeOutTheItem.txt`.)

✏️ **Khi sửa:** giữ nguyên tên vật phẩm (chữ Trung), chỉ đổi các con số sau dấu `=`.

### Định dạng mỗi dòng

```
Tên vật phẩm=Số lượng lấy ra=Ngưỡng kích hoạt=Dùng hết thì lấy ngay
```

| Cột | Ý nghĩa | Giá trị |
|---|---|---|
| 1 | Tên vật phẩm | Tên đúng như trong game. |
| 2 | Số lượng lấy ra (`取出数量`) | `0` = **không bao giờ lấy** món này. |
| 3 | Ngưỡng kích hoạt (`达到数量触发取出`) | Khi số lượng trong túi chạm mức này thì kích hoạt đi lấy. `-1` = món này **không tự kích hoạt**, nhưng khi bot đi lấy món khác thì **lấy kèm** món này. |
| 4 | Dùng hết thì lấy ngay (`用完马上触发`) | `=1`: kích hoạt ngay khi dùng hết; `=0` hoặc **bỏ trống**: chỉ kích hoạt khi nhân vật đang ở trong làng. |

### Dịch từng dòng

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `--此文件为 个人仓库自动取物品触发文件，少于指定数量，取出设置数量` | Chú thích | "File này là file kích hoạt **tự lấy vật phẩm từ kho cá nhân**: khi ít hơn số lượng chỉ định thì lấy ra số lượng đã đặt." |
| 2 | `--格式为  物品名字=取出数量=达到数量触发取出=用完马上触发（=1触发 =0在村庄才触发）` | Chú thích: định dạng | "Định dạng: `Tên vật phẩm=Số lượng lấy ra=Đạt số lượng này thì kích hoạt lấy=Dùng hết thì kích hoạt ngay` (`=1` kích hoạt ngay, `=0` chỉ kích hoạt khi ở trong làng)." |
| 4 | `--比如  瞬間移動卷軸=10=0=1 最后面填1表示用完马上触发   不填或者填0表示角色在村庄才触发` | Chú thích: ví dụ | "Ví dụ `瞬間移動卷軸=10=0=1` (cuộn dịch chuyển tức thời): ô cuối điền `1` nghĩa là **dùng hết thì kích hoạt ngay**; không điền hoặc điền `0` nghĩa là chỉ kích hoạt khi nhân vật ở trong làng." |
| 5 | `--比如  瞬間移動卷軸=10=0=0 最后面填0表示角色在村庄才触发` | Chú thích: ví dụ | "Ví dụ `瞬間移動卷軸=10=0=0`: ô cuối điền `0` nghĩa là chỉ kích hoạt khi nhân vật ở trong làng." |
| 7 | `--注意 瞬間移動卷軸  这个一定要设置在村庄才触发，要不然，传送过去结果没了，又触发回来取` | Chú thích: cảnh báo | "**Chú ý:** `瞬間移動卷軸` **nhất định phải đặt là chỉ kích hoạt khi ở làng**, nếu không thì vừa dịch chuyển đi, hết cuộn, lại kích hoạt quay về lấy (lặp mãi)." 💡 Tức là cột 4 của cuộn dịch chuyển phải là `0` hoặc bỏ trống. |
| 10 | `--比如  瞬間移動卷軸=10=0  表示 背包中数量=0时触发血盟取物品 在血盟取出10个` | Chú thích: ví dụ | "Ví dụ `瞬間移動卷軸=10=0`: khi số lượng trong túi = 0 thì kích hoạt lấy đồ từ **huyết minh** (血盟 = clan), lấy ra 10 cái." 💡 Dòng này giống hệt dòng 11 của file kho clan `BloodTakeOutTheItem.txt`, nên chữ "huyết minh" nhiều khả năng bị chép sang nguyên văn; trong file này nên hiểu là **kho cá nhân** (?). |
| 11 | `--比如  瞬間移動卷軸=10=-1 表示 不用此物品触发    但是取其他物品时 顺便取出10个` | Chú thích: ví dụ | "Ví dụ `瞬間移動卷軸=10=-1`: **không dùng vật phẩm này để kích hoạt**, nhưng khi lấy vật phẩm khác thì **tiện tay lấy ra 10 cái**." |
| 12 | `--比如  治癒藥水=0=0   不会取出此物品（因为你的取出数量为0）` | Chú thích: ví dụ | "Ví dụ `治癒藥水=0=0` (thuốc trị liệu): sẽ **không lấy** vật phẩm này (vì số lượng lấy ra của bạn là 0)." |
| 13 | `--比如  解毒藥水=0=-1  不会取出此物品（因为你的取出数量为0）` | Chú thích: ví dụ | "Ví dụ `解毒藥水=0=-1` (thuốc giải độc): sẽ **không lấy** vật phẩm này (vì số lượng lấy ra là 0)." |
| 15 | `瞬間移動卷軸=0=-1` | Cuộn dịch chuyển tức thời (Scroll of Teleportation) | Lấy 0 cái, ngưỡng -1 → **không lấy**. |
| 16 | `治癒藥水=0=0` | Thuốc trị liệu (Healing Potion) | Lấy 0 cái → **không lấy**. |
| 17 | `安特的樹枝=0=-1` | Cành cây của Ent (Ent's branch) | **Không lấy**. |
| 18 | `解毒藥水=0=-1` | Thuốc giải độc (Cure Poison potion) | **Không lấy**. |
| 19 | `翡翠藥水=0=-1` | Thuốc Phỉ thúy (Emerald Potion) (?) | **Không lấy**. |
| 20 | `活力自我加速藥水=0=-1` | Thuốc tự tăng tốc Hoạt lực (Vitality Haste Potion) | **Không lấy**. |
| 21 | `自我加速藥水=0=-1` | Thuốc tự tăng tốc (Haste potion) | **Không lấy**. |
| 22 | `強化自我加速藥水=0=-1` | Thuốc tự tăng tốc cường hóa (Greater Haste potion) | **Không lấy**. |

💡 **Lưu ý:** mặc định **mọi dòng đều có số lượng lấy ra = 0**, nên tính năng này coi như **tắt**. Muốn bật, ví dụ khi hết cuộn dịch chuyển thì lấy 10 cuộn (chỉ khi ở làng), sửa dòng 15 thành `瞬間移動卷軸=10=0=0` (đúng như ví dụ trong file). Dĩ nhiên trong kho cá nhân phải có sẵn vật phẩm đó.

---

## saveitem.txt

**File này điều khiển gì:** danh sách vật phẩm **giữ lại, không bao giờ bán**. Khi về làng bán đồ, mọi món có tên trong file này được giữ lại trong túi.

**Khi nào bot dùng:** mỗi lần bot bán đồ cho NPC (khi về thành). Theo nhật ký cập nhật của gói, `敏捷魔法頭盔` và `力量魔法頭盔` đã đổi thành **mặc định không giữ lại**, muốn giữ phải ghi trong file này (hiện đã có sẵn ở dòng 34–35).

✏️ **Khi sửa:** mỗi dòng một tên vật phẩm, chép y nguyên tên trong game (chữ Phồn thể); xóa dòng nào thì món đó có thể bị bán.

| # | Dòng gốc | Nghĩa | Ghi chú |
|---|---|---|---|
| 1 | `--此文件为保留的物品  不会出售` | Chú thích | "File này là các vật phẩm giữ lại, sẽ không bán." |
| 2 | `變形卷軸` | Cuộn biến hình (Polymorph scroll) | |
| 3 | `治癒藥水` | Thuốc trị liệu (Healing Potion) | |
| 4 | `勇敢藥水` | Thuốc Dũng cảm (Brave Potion, tăng tốc đánh) | |
| 5 | `惡魔之血` | Máu Ác quỷ (Devil's Blood) (?) | |
| 6 | `精靈餅乾` | Bánh quy Tiên (Elven Wafer) | |
| 7 | `金屬塊` | Khối kim loại | |
| 8 | `復活卷軸` | Cuộn hồi sinh (Resurrection scroll) | |
| 9 | `自我加速藥水` | Thuốc tự tăng tốc (Haste potion) | |
| 10 | `強化自我加速藥水` | Thuốc tự tăng tốc cường hóa (Greater Haste potion) | |
| 11 | `對盔甲施法的卷軸` | Cuộn phù phép giáp (Scroll of Enchant Armor) | Cuộn cường hóa (+) giáp. |
| 12 | `對武器施法的卷軸` | Cuộn phù phép vũ khí (Scroll of Enchant Weapon) | Cuộn cường hóa (+) vũ khí. |
| 13 | `武器強化卷軸` | Cuộn cường hóa vũ khí | |
| 14 | `防具強化卷軸` | Cuộn cường hóa giáp | |
| 15 | `祝福武器強化卷軸` | Cuộn cường hóa vũ khí **được ban phước** (Blessed) | |
| 16 | `祝福防具強化卷軸` | Cuộn cường hóa giáp được ban phước | |
| 17 | `歐琳飾品強化卷軸` | Cuộn cường hóa trang sức Orim (`歐琳`) (?) | |
| 18 | `祝福歐琳飾品強化卷軸` | Cuộn cường hóa trang sức Orim được ban phước (?) | |
| 19 | `倫提斯耳環強化卷軸` | Cuộn cường hóa bông tai Roomtis (`倫提斯`) (?) | |
| 20 | `倫提斯安全強化卷軸` | Cuộn cường hóa an toàn Roomtis (?) | "An toàn" = cường hóa không làm vỡ đồ (?). |
| 21 | `倫提斯墜飾安全強化卷軸` | Cuộn cường hóa an toàn mặt dây chuyền Roomtis (?) | |
| 22 | `斯奈普強化卷軸` | Cuộn cường hóa Snapper (`斯奈普`, nhẫn Snapper) (?) | |
| 23 | `斯奈普安全強化卷軸` | Cuộn cường hóa an toàn Snapper (?) | |
| 24 | `蛇夫座強化卷軸` | Cuộn cường hóa Xà Phu (Ophiuchus) | |
| 25 | `覺醒徽章強化卷` | Cuộn cường hóa Huy hiệu Thức tỉnh (Awakening badge) | Tên kết thúc bằng `卷` (không có `軸`), giữ nguyên. |
| 26 | `瞬間移動卷軸` | Cuộn dịch chuyển tức thời (Scroll of Teleportation) | |
| 27 | `摺紙傳令鳥` | Chim đưa tin gấp giấy (Origami messenger bird) (?) | Dùng cho tính năng tố cáo `举报附近的人` trong `BaseConfig.txt`. |
| 28 | `獵人之弓` | Cung Thợ săn (Hunter's Bow) | |
| 29 | `精靈弓` | Cung Tiên (Elven Bow) | |
| 30 | `十字弓` | Nỏ (Crossbow) | |
| 31 | `尤米弓` | Cung Yumi (Yumi bow) | |
| 32 | `伊娃的祝福` | Phước lành của Eva (Blessing of Eva) | `伊娃` = Eva. |
| 33 | `安特的樹枝` | Cành cây của Ent | |
| 34 | `敏捷魔法頭盔` | Mũ phép thuật Nhanh nhẹn (Agility magic helm) | Mặc định không giữ, phải ghi ở đây mới giữ. |
| 35 | `力量魔法頭盔` | Mũ phép thuật Sức mạnh (Power magic helm) | Như trên. |

---

## SellBuy.txt

**File này điều khiển gì:** danh sách vật phẩm bot **tự mua ở làng** khi về thành, chia theo mốc cấp độ giống `gj.txt`. Dù tên file là "SellBuy" (bán-mua), nội dung chỉ có các dòng **mua**; việc bán do `SellList.txt` + `saveitem.txt` quyết định.

**Khi nào bot dùng:** khi nhân vật về làng (tiếp tế), hoặc khi một vật phẩm trong túi tụt xuống ngưỡng (?). `BaseConfig.txt` cũng nhắc tới file này: muốn dùng tính năng tố cáo (`举报附近的人`) thì phải đặt tự mua `摺紙傳令鳥` ở NPC `艾伊拉` tại Talking Island trong `SellBuy.txt`.

✏️ **Khi sửa:** giữ nguyên tên làng và tên vật phẩm (chữ Trung), chỉ đổi các con số.

### Định dạng (suy luận, file không có chú thích)

```
Làng mua=Tên vật phẩm=Số lượng mua=Ngưỡng kích hoạt
```

- **Làng mua**: ví dụ `說話之島村` = làng Talking Island, `奇岩村` = làng Giran.
- **Số lượng mua**: `0` = không mua món này. Chưa rõ là "mua thêm N" hay "mua cho đủ N" (?).
- **Ngưỡng kích hoạt** (?): hiểu theo cùng quy ước với `PersonageTakeOutTheItem.txt`: khi số lượng trong túi chạm mức này thì đi mua; `-1` = món này không tự kích hoạt chuyến mua, nhưng khi đã về làng thì mua kèm.
- Các mục `[1]`, `[7]`, `[8]`, `[10]` là **mốc cấp độ** (?): cấp 1–6 dùng `[1]`, cấp 7 dùng `[7]`, cấp 8–9 dùng `[8]`, cấp 10 trở lên dùng `[10]`.

### Dịch từng dòng

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `[1]` | Mốc cấp 1 | Cấp 1 trở lên (?). |
| 2 | `說話之島村=箭=100=-1` | Làng Talking Island, tên (mũi tên, `箭`), mua 100, ngưỡng -1 | Không tự kích hoạt; khi về làng thì mua 100 mũi tên (?). Dùng cho nghề đánh cung (Elf). |
| 3 | `說話之島村=治癒藥水=0=-1` | Làng Talking Island, thuốc trị liệu (`治癒藥水`), mua 0 | **Không mua**. |
| 5 | `[7]` | Mốc cấp 7 | |
| 6 | `說話之島村=箭=1000=0` | Làng Talking Island, tên, mua 1000, ngưỡng 0 | Khi hết tên (còn 0) thì đi mua 1000 (?). |
| 7 | `說話之島村=治癒藥水=0=0` | Làng Talking Island, thuốc trị liệu (`治癒藥水`), mua 0 | **Không mua**. |
| 9 | `[8]` | Mốc cấp 8 | |
| 10 | `說話之島村=箭=2500=0` | Làng Talking Island, tên, mua 2500, ngưỡng 0 | Hết tên thì mua 2500 (?). |
| 11 | `說話之島村=治癒藥水=0=0` | Thuốc trị liệu, mua 0 | **Không mua**. |
| 12 | `說話之島村=肉=0=0` | Làng Talking Island, thịt (`肉`), mua 0 | **Không mua**. (Thịt dùng để ăn hồi độ no.) |
| 14 | `[10]` | Mốc cấp 10 | |
| 15 | `奇岩村=銀箭=2500=10` | Làng **Giran** (`奇岩村`), tên bạc (`銀箭`, Silver arrow), mua 2500, ngưỡng 10 | Khi tên bạc trong túi còn khoảng 10 thì đi Giran mua 2500 (?). 💡 Bot sẽ phải di chuyển tới Giran để mua. |
| 16 | `說話之島村=治癒藥水=0=0` | Thuốc trị liệu, mua 0 | **Không mua**. |
| 17 | `說話之島村=肉=0=0` | Thịt, mua 0 | **Không mua**. |

💡 **Lưu ý:**
- Muốn bot tự mua thuốc trị liệu (`治癒藥水`), đổi số `0` đầu tiên thành số lượng muốn mua, ví dụ `說話之島村=治癒藥水=50=5` (mua 50 khi còn khoảng 5) (?). Hãy thử và quan sát vì file không ghi rõ quy tắc.
- Mua nhiều quá sẽ làm tăng tải trọng; nhớ tải trọng vượt 50% thì không tự hồi máu/mana (xem `负重回城` trong `gj.txt`).
- `BaseConfig.txt` có riêng `死亡复活后自动购买肉` (mua thịt sau khi chết và hồi sinh), không liên quan tới dòng `肉` ở đây. Ngoài ra, theo nhật ký cập nhật, khi độ no chưa đầy bot **tự mua thịt và ăn** trước khi ra khỏi làng (bật mặc định), nên để `肉=0=0` ở đây vẫn không làm nhân vật bị đói.
- Theo nhật ký cập nhật, khi nhân vật đang **tên đỏ** (红名, do PK) thì bot **không mua và không bán** vật phẩm (áp dụng cho cả file này lẫn `SellList.txt`).

---

## SellList.txt

**File này điều khiển gì:** cấu hình **bán vật phẩm chỉ định cho NPC thương nhân chỉ định**. Mỗi `[Tên NPC]` là một thương nhân, các dòng bên dưới là vật phẩm bán cho NPC đó. Dòng `-------------Tên làng` chỉ là **chú thích** (bắt đầu bằng `--`) để chia nhóm theo làng.

**Khi nào bot dùng:** khi về thành bán đồ (trừ lúc nhân vật đang tên đỏ, xem lưu ý ở `SellBuy.txt`). Món nào có trong `saveitem.txt` thì không bán. NPC để trống (không có vật phẩm bên dưới) thì bot không bán gì cho NPC đó; bạn có thể tự thêm tên vật phẩm vào dưới NPC tương ứng.

✏️ **Khi sửa:** giữ nguyên tên NPC trong ngoặc vuông và tên vật phẩm (chữ Trung); mỗi dòng một vật phẩm, đặt ngay dưới dòng `[Tên NPC]` muốn bán.

💡 Tên NPC dưới đây là **phiên âm gần đúng**; nhiều tên chưa đối chiếu được với bản tiếng Anh nên có đánh dấu (?). Trong file luôn dùng tên Trung gốc.

### Đầu file và làng Talking Island (`說話之島村`)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `--此文件为指定物品卖给指定商人的配置` | Chú thích | "File này cấu hình bán vật phẩm chỉ định cho thương nhân chỉ định." |
| 2 | `-------------說話之島村` | Chú thích: làng Talking Island | Đường kẻ phân nhóm. |
| 3 | `[潘朵拉]` | NPC Pandora | Thương nhân vũ khí/giáp ở Talking Island (?). |
| 4 | `木棒` | Gậy gỗ (Club) | Bán cho `潘朵拉`. |
| 5 | `銀釘皮甲` | Giáp da đinh bạc (Studded leather armor) | Bán cho `潘朵拉`. |
| 6 | `弓` | Cung (Bow) | Bán cho `潘朵拉`. |
| 7 | `亞連` | "Á Liên", có lẽ là một loại vũ khí cấp thấp (?) | Bán cho `潘朵拉`. |
| 8 | `巴迪須` | Bardiche (rìu cán dài) | Bán cho `潘朵拉`. |
| 9 | `闊劍` | Kiếm bản rộng (Broad sword) | Bán cho `潘朵拉`. |
| 10 | `矛` | Giáo (Spear) | Bán cho `潘朵拉`. |
| 11 | `短劍` | Đoản kiếm (Dagger / Short sword) | Bán cho `潘朵拉`. |
| 12 | `彎刀` | Đao cong (Scimitar / Cutlass) | Bán cho `潘朵拉`. |
| 13 | `長劍` | Trường kiếm (Long sword) | Bán cho `潘朵拉`. |
| 14 | `小盾牌` | Khiên nhỏ (Small shield) | Bán cho `潘朵拉`. |
| 15 | `釘錘` | Chùy gai (Mace / Morning star) | Bán cho `潘朵拉`. |
| 17 | `[馬修]` | NPC Matthew (?) | Trống, không bán gì. |
| 19 | `[巴辛]` | NPC Bassin (?) | Trống. |

### Làng Gludin (`古魯丁村`)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 23 | `-------------古魯丁村` | Chú thích: làng Gludin | |
| 24 | `[露西]` | NPC Lucy | |
| 25 | `短統靴` | Ủng cổ ngắn (Low boots) | Bán cho `露西`. |
| 28 | `[凱蒂]` | NPC Katie (?) | |
| 29 | `斧` | Rìu (Axe) | Bán cho `凱蒂`. |
| 30 | `歐西斯頭盔` | Mũ Orcish (`歐西斯` = Orcish (?)) | Bán cho `凱蒂`. |
| 31 | `歐西斯環甲` | Giáp vòng Orcish | Bán cho `凱蒂`. |
| 32 | `歐西斯鏈甲` | Giáp xích Orcish | Bán cho `凱蒂`. |
| 33 | `歐西斯匕首` | Dao găm Orcish | Bán cho `凱蒂`. |
| 34 | `阿克海盾牌` | Khiên Akhai (?) | Bán cho `凱蒂`. |
| 35 | `歐西斯弓` | Cung Orcish | Bán cho `凱蒂`. |
| 36 | `歐西斯之矛` | Giáo Orcish | Bán cho `凱蒂`. |
| 37 | `歐西斯斗篷` | Áo choàng Orcish | Bán cho `凱蒂`. |
| 38 | `歐西斯短劍` | Đoản kiếm Orcish | Bán cho `凱蒂`. |

### Làng Giran (`奇岩村`)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 42 | `-------------奇岩村` | Chú thích: làng Giran | |
| 43 | `[邁爾]` | NPC Mayer (?) | |
| 44 | `長靴` | Ủng cổ cao (High boots) | Bán cho `邁爾`. |
| 46 | `[溫諾]` | NPC Winno (?) | |
| 47 | `侏儒鐵斧` | Rìu sắt Người lùn (Dwarvish Iron Axe) | Bán cho `溫諾`. |
| 49 | `[范吉爾]` | NPC Vangel (?) | |
| 50 | `頭盔` | Mũ giáp (Helmet) | Bán cho `范吉爾`. |
| 51 | `鏈甲` | Giáp xích (Chain mail) | Bán cho `范吉爾`. |
| 53 | `[愛弗特]` | NPC Evert (?) | |
| 54 | `抗魔法斗篷` | Áo choàng kháng phép (Cloak of Magic Resistance) | Bán cho `愛弗特`. |
| 56 | `[瑪格瑞特]` | NPC Margaret | Có vẻ là người bán thực phẩm (?). |
| 57 | `胡蘿蔔` | Cà rốt | Bán cho `瑪格瑞特`. |
| 58 | `蘋果` | Táo | Bán cho `瑪格瑞特`. |
| 59 | `檸檬` | Chanh | Bán cho `瑪格瑞特`. |
| 60 | `香蕉` | Chuối | Bán cho `瑪格瑞特`. |
| 61 | `蛋` | Trứng | Bán cho `瑪格瑞特`. |
| 62 | `橘子` | Quýt | Bán cho `瑪格瑞特`. |

### Các làng còn lại (NPC đều đang để trống)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 63 | `-------------燃柳村` | Chú thích: làng Woodbec (`燃柳` nghĩa đen là "liễu cháy") | |
| 64 | `[傑克森]` | NPC Jackson | Trống. |
| 69 | `-------------肯特村` | Chú thích: làng Kent | |
| 70 | `[索拉雅]` | NPC Soraya | Trống. |
| 74 | `[安迪]` | NPC Andy | Trống. |
| 78 | `-------------風木村` | Chú thích: làng Windawood | |
| 79 | `[艾米娜]` | NPC Amina (?) | Trống. |
| 82 | `-------------銀騎士村` | Chú thích: làng Hiệp sĩ Bạc (Silver Knight) | |
| 83 | `[梅林]` | NPC Merlin | Trống. |
| 87 | `[格林]` | NPC Glen (?) | Trống. |
| 89 | `-------------海音村` | Chú thích: làng Heine | |
| 90 | `[比特]` | NPC Bitt (?) | Trống. |
| 93 | `[須凡]` | NPC Sven (?) | Trống. |
| 95 | `-------------威頓村` | Chú thích: làng Werldern | |
| 96 | `[蓓莉]` | NPC Belly (?) | Trống. |
| 98 | `[瑞福]` | NPC Reef (?) | Trống. |
| 100 | `-------------歐瑞村` | Chú thích: làng Oren | |
| 101 | `[畢伍斯]` | NPC Bius (?) | Trống. |
| 103 | `[曼德拉]` | NPC Mandra (?) | Trống. |
| 106 | `-------------亞丁村` | Chú thích: làng Aden | |
| 107 | `[拉溫]` | NPC Rawin (?) | Trống. |
| 109 | `[戴夫曼]` | NPC Daveman (?) | Trống. |
| 111 | `[菲卡]` | NPC Fika (?) | Trống. |

💡 **Lưu ý:**
- Muốn bán thêm món gì, thêm một dòng tên vật phẩm ngay dưới `[Tên NPC]` có thu mua món đó trong game (NPC phải thực sự mua loại hàng đó).
- Một số món trong file này (vd. `短統靴`, `斧`, `頭盔`) nằm trong danh sách **không nhặt** của `gj.txt` ở cấp thấp; từ mục `[10]` chúng không còn bị lọc nên bot sẽ nhặt rồi đem bán.

---

## TradedConfig.txt

**File này điều khiển gì:** cấu hình **giao dịch** giữa các nhân vật. Tác giả gọi là `倒货` ("chuyển hàng"): nhân vật treo máy (acc phụ) mang vàng/vật phẩm về giao cho **người nhận hàng** (`收货人`, acc chính). Vàng còn có thể chuyển qua **người bày sạp** (`摆摊人`, nhân vật mở sạp bán hàng cá nhân).

**Khi nào bot dùng:** khi vàng trong túi đạt `达到金币触发交易`, hoặc khi một vật phẩm trong `Tradeditems.txt` đạt số lượng (nếu `达到材料触发交易=1`). Chỉ cần thỏa **một trong hai** điều kiện là kích hoạt. Kiểu thao tác (bàn phím-chuột hay bộ nhớ) do khóa `内存交易` trong `BaseConfig.txt` quyết định.

✏️ **Khi sửa:** giữ nguyên tên khóa, tên mục, tên làng và tên server (chữ Trung); chỉ đổi số, tọa độ, và điền **tên nhân vật** sau dấu `=`.

### Mục `[config]`

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `--此文件为交易配置` | Chú thích | "File này là cấu hình giao dịch." |
| 2 | `[config]` | Mục cấu hình | |
| 3 | `达到金币触发交易=0` | Đạt số vàng thì kích hoạt giao dịch | Chú thích gốc: "`=0`: **không** tự động chuyển hàng; số khác: đạt số vàng đó thì kích hoạt. `达到金币触发交易` và `达到材料触发交易`, thỏa **bất kỳ một** điều kiện nào là kích hoạt chuyển hàng." Ví dụ `=500000` = khi có 500.000 vàng thì đi giao (?). Mặc định: tắt. |
| 4 | `达到材料触发交易=0` | Đạt số nguyên liệu thì kích hoạt giao dịch | Chú thích gốc: "`=1`: khi **bất kỳ dòng nào** trong `Tradeditems.txt` đạt số lượng đã đặt, nhân vật quay về để chuyển hàng. Cần thiết lập trước thông tin người nhận hàng." `=0` tắt (mặc định). |
| 5 | `金币采用摆摊模式=0` | Chuyển vàng bằng chế độ bày sạp | Chú thích gốc: "`=0` không dùng sạp để chuyển vàng; `=1` chuyển vàng bằng chế độ bày sạp: dựa vào các thiết lập về người bày sạp để tìm người bày sạp và giao dịch." |
| 6 | `保留金币=1000` | Vàng giữ lại | Chú thích gốc: "Số vàng giữ lại trong túi." Bot giữ 1000 vàng, phần dư mới chuyển đi. 💡 Nên giữ đủ tiền để mua thuốc/tên ở `SellBuy.txt`. |
| 7 | `交易失败间隔=60` | Khoảng chờ sau khi giao dịch thất bại | Chú thích gốc: "Giao dịch thất bại thì cách bao nhiêu **phút** mới giao dịch lại." Mặc định 60 phút. |
| 9 | `收货人位置=說話之島村` | Vị trí người nhận hàng | Làng Talking Island. Acc nhận hàng phải đứng ở làng này. |
| 10 | `收货人坐标=32581,32950` | Tọa độ người nhận hàng | `x,y`, nơi acc phụ đi tới để giao dịch. |
| 12 | `摆摊人位置=說話之島村` | Vị trí người bày sạp | Làng Talking Island. |
| 13 | `摆摊人坐标=32581,32939` | Tọa độ người bày sạp | `x,y`. |

### Mục `[收货人角色名]` (dòng 16–41) và `[摆摊人角色名]` (dòng 44–69)

- `[收货人角色名]` = **Tên nhân vật người nhận hàng**.
- `[摆摊人角色名]` = **Tên nhân vật người bày sạp**.

Mỗi dòng có dạng `Tên server=tên nhân vật 1,tên nhân vật 2,...`. Vế trái là tên **máy chủ (server)** của Lineage Classic (đặt theo tên thần thoại Hy Lạp; danh sách đầy đủ ở `config/ServerText.txt`, xem `03-cau-hinh-chung-va-cau-truc-goi.md`); vế phải là tên các nhân vật trên server đó, cách nhau bằng dấu phẩy `,`. Bỏ trống sau dấu `=` nghĩa là chưa đặt cho server đó.

Dòng đầu mỗi mục có giá trị **mẫu** (placeholder), phải thay bằng tên nhân vật thật của bạn:

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 16 | `[收货人角色名]` | Tên nhân vật người nhận hàng | Tiêu đề mục. |
| 17 | `太陽神阿波羅=收货人1,收货人2,收货人3` | Server Thần Mặt Trời Apollo = người nhận 1, người nhận 2, người nhận 3 | `收货人1`... là **tên mẫu**, thay bằng tên nhân vật nhận hàng thật trên server này. |
| 44 | `[摆摊人角色名]` | Tên nhân vật người bày sạp | Tiêu đề mục. |
| 45 | `太陽神阿波羅=摆摊人1,摆摊人2,摆摊人3` | Server Thần Mặt Trời Apollo = người bày sạp 1, 2, 3 | `摆摊人1`... là **tên mẫu**, thay bằng tên nhân vật bày sạp thật. |

Các dòng còn lại trong hai mục giống nhau, đều **để trống** (dạng `Tên server=`). Cột "#" ghi số dòng ở mục người nhận / mục người bày sạp:

| # (nhận / sạp) | Dòng gốc | Nghĩa (tên server) |
|---|---|---|
| 18 / 46 | `愛神邱比特=` | Thần Tình yêu Cupid |
| 19 / 47 | `勝利女神雅典娜=` | Nữ thần Chiến thắng Athena |
| 20 / 48 | `美神維納斯=` | Nữ thần Sắc đẹp Venus |
| 21 / 49 | `天神宙斯=` | Thần Zeus |
| 22 / 50 | `天后海拉=` | Thiên hậu Hera |
| 23 / 51 | `戰神馬爾斯=` | Thần Chiến tranh Mars |
| 24 / 52 | `月亮女神阿緹蜜斯=` | Nữ thần Mặt Trăng Artemis |
| 25 / 53 | `海神波塞頓=` | Thần Biển Poseidon |
| 26 / 54 | `冥王黑帝斯=` | Diêm vương Hades |
| 27 / 55 | `火神赫發斯特斯=` | Thần Lửa Hephaestus |
| 28 / 56 | `收穫女神帝蜜特=` | Nữ thần Mùa màng Demeter |
| 29 / 57 | `蛇髮女墨杜沙=` | Nữ yêu tóc rắn Medusa |
| 30 / 58 | `半人馬涅索斯=` | Nhân mã Nessus |
| 31 / 59 | `牛人彌諾陶洛斯=` | Người bò Minotaur |
| 32 / 60 | `俄雷恩=` | Orion (?) (phiên âm; không phải làng Oren `歐瑞`) |
| 33 / 61 | `獨眼巨人庫克羅普斯=` | Khổng lồ một mắt Cyclops |
| 34 / 62 | `獅子涅墨亞=` | Sư tử Nemea |
| 35 / 63 | `飛馬珀伽索斯=` | Ngựa bay Pegasus |
| 36 / 64 | `水蛇許德拉=` | Rắn nước Hydra |
| 37 / 65 | `公牛克里特=` | Bò mộng xứ Crete |
| 38 / 66 | `女妖塞壬=` | Nữ yêu Siren |
| 39 / 67 | `巨龍拉冬=` | Rồng khổng lồ Ladon |
| 40 / 68 | `百眼怪阿爾戈斯=` | Quái vật trăm mắt Argus |
| 41 / 69 | `大地之神蓋亞=` | Thần Đất Gaia |

💡 **Lưu ý:**
- Ví dụ điền (tên nhân vật là giả định): `天神宙斯=TênNhânVậtA,TênNhânVậtB`. Tên nhân vật phải gõ **đúng y như trong game**.
- Acc nhận hàng / bày sạp phải **đang online** và đứng đúng `收货人位置` + `收货人坐标` (hoặc `摆摊人位置` + `摆摊人坐标`). Nếu không, giao dịch thất bại và bot chờ `交易失败间隔` phút rồi thử lại.
- Cả hai điều kiện kích hoạt đều đang `=0`, nên mặc định **tính năng giao dịch tắt**.

---

## Tradeditems.txt

**File này điều khiển gì:** danh sách vật phẩm sẽ được **giao cho người nhận hàng** và **số lượng kích hoạt** việc giao.

**Khi nào bot dùng:** khi `达到材料触发交易=1` trong `TradedConfig.txt`. Khi bất kỳ dòng nào có số lượng đạt mức đã đặt, nhân vật quay về giao hàng.

✏️ **Khi sửa:** giữ nguyên tên vật phẩm (chữ Trung), chỉ đổi số sau dấu `=` (hoặc thêm `=số` cho dòng chưa có).

**Định dạng:** `Tên vật phẩm=Số lượng kích hoạt`. Dòng **không có** `=số` có lẽ không tự kích hoạt giao dịch, nhưng vẫn được **giao kèm** khi đi giao hàng (?).

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `--此文件为交易的物品与触发数量的配置` | Chú thích | "File này cấu hình vật phẩm giao dịch và số lượng kích hoạt." |
| 2 | `金屬塊=30` | Khối kim loại = 30 | Có 30 khối kim loại thì kích hoạt giao hàng. |
| 3 | `復活卷軸` | Cuộn hồi sinh | Không có số: giao kèm (?). |
| 4 | `強化自我加速藥水=30` | Thuốc tự tăng tốc cường hóa = 30 | Có 30 lọ thì kích hoạt giao hàng. |
| 5 | `對盔甲施法的卷軸` | Cuộn phù phép giáp (Scroll of Enchant Armor) | Giao kèm (?). |
| 6 | `對武器施法的卷軸` | Cuộn phù phép vũ khí (Scroll of Enchant Weapon) | Giao kèm (?). |
| 7 | `武器強化卷軸` | Cuộn cường hóa vũ khí | Giao kèm (?). |
| 8 | `防具強化卷軸` | Cuộn cường hóa giáp | Giao kèm (?). |
| 9 | `祝福武器強化卷軸` | Cuộn cường hóa vũ khí được ban phước | Giao kèm (?). |
| 10 | `祝福防具強化卷軸` | Cuộn cường hóa giáp được ban phước | Giao kèm (?). |
| 11 | `歐琳飾品強化卷軸` | Cuộn cường hóa trang sức Orim (?) | Giao kèm (?). |
| 12 | `祝福歐琳飾品強化卷軸` | Cuộn cường hóa trang sức Orim được ban phước (?) | Giao kèm (?). |
| 13 | `倫提斯耳環強化卷軸` | Cuộn cường hóa bông tai Roomtis (?) | Giao kèm (?). |
| 14 | `倫提斯安全強化卷軸` | Cuộn cường hóa an toàn Roomtis (?) | Giao kèm (?). |
| 15 | `倫提斯墜飾安全強化卷軸` | Cuộn cường hóa an toàn mặt dây chuyền Roomtis (?) | Giao kèm (?). |
| 16 | `斯奈普強化卷軸` | Cuộn cường hóa Snapper (?) | Giao kèm (?). |
| 17 | `斯奈普安全強化卷軸` | Cuộn cường hóa an toàn Snapper (?) | Giao kèm (?). |
| 18 | `蛇夫座強化卷軸` | Cuộn cường hóa Xà Phu (Ophiuchus) | Giao kèm (?). |
| 19 | `覺醒徽章強化卷` | Cuộn cường hóa Huy hiệu Thức tỉnh | Giao kèm (?). |

💡 **Lưu ý:** các món trong file này cũng có trong `saveitem.txt` (không bán), nên chúng được giữ trong túi cho tới khi giao cho acc nhận hàng.

---

## TreasureName.txt

**File này điều khiển gì:** danh sách **tên bảo vật** (`宝物`). Nếu trong túi có các vật phẩm này, **số lượng sẽ hiện trên bảng điều khiển** (`控制台`, console) của bot. Theo nhật ký cập nhật, file này mới có từ bản 9.16, và `大中控` (trung tâm điều khiển lớn) cũng hiển thị bảo vật.

**Khi nào bot dùng:** liên tục, chỉ để **hiển thị/thống kê**, không thay đổi hành vi treo máy.

✏️ **Khi sửa:** mỗi dòng một tên vật phẩm, chép đúng tên trong game (chữ Phồn thể), **không** có `--` ở đầu.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `--此文件为宝物的名字 背包中存在这些物品会在控制台上显示数量` | Chú thích | "File này là tên các bảo vật; nếu trong túi có những vật phẩm này thì số lượng sẽ hiện trên bảng điều khiển." |
| 2 | `--太阳神` | Ví dụ (đang tắt): "Thần Mặt Trời" | Có `--` ở đầu nên là chú thích, không có tác dụng. |
| 3 | `--金疮药` | Ví dụ (đang tắt): "Kim sang dược" | Như trên. |

💡 **Lưu ý:** mặc định cả hai dòng đều là chú thích, nên **chưa theo dõi bảo vật nào**. Hai tên ví dụ này viết bằng chữ Giản thể và có lẽ không phải tên vật phẩm Lineage Classic (?). Muốn theo dõi món nào, thêm một dòng ghi đúng tên trong game, ví dụ `金屬塊`.
