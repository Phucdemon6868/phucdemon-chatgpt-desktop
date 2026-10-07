# Nhật ký cập nhật

> **File gốc:** `更新说明.txt` (trong gói có tên `#U66f4#U65b0#U8bf4#U660e.txt`), nghĩa là "Ghi chú cập nhật" của bot **天堂经典版 Bd** (bot treo máy cho Lineage Classic).
> **Độ dài gốc:** 434 dòng, gồm 51 phiên bản. Bản **mới nhất nằm trên cùng**, đi từ `9.16` ngược về `7.1.1`.

---

## File này dùng để làm gì?

Đây là nhật ký thay đổi (changelog) do tác giả bot viết. Mỗi lần game cập nhật, hoặc bot có tính năng mới hay được sửa lỗi, tác giả thêm một khối mới vào đầu file. Mỗi khối gồm:

- **Dòng tiêu đề** `天堂经典版Bd 更新X`, nghĩa là "Lineage Classic (`天堂经典版`, nghĩa đen là "Thiên Đường bản Kinh điển") – bot Bd – bản cập nhật X".
- **Các mục đánh số** `1.` `2.` …: nội dung thay đổi của bản đó.
- **Hai dòng `注：`** (Chú ý): cho biết cần thay những file nào và số phiên bản EXE mới nhất.
- **Dòng gạch** `-------------------------------------------`: chỉ là đường kẻ ngăn cách giữa các bản, không mang nghĩa gì khác.

💡 **Lưu ý:** số phiên bản có vẻ được đặt theo **tháng.ngày** phát hành (?). Ví dụ `9.16` = ngày 16/9, còn `9.10.1` = lần phát hành thứ hai trong ngày 10/9.

## ⚠️ Quy tắc khi sửa file cấu hình

Bot đọc **nguyên văn chữ Trung** trong các file cấu hình. Khi làm theo một mục trong nhật ký này để sửa file (ví dụ `BaseConfig.txt`), bạn phải **giữ nguyên** mọi chữ Trung: tên key, tên mục trong ngoặc vuông `[...]`, tên bản đồ, tên vật phẩm, tên NPC và tên server. **Chỉ đổi con số hoặc giá trị** phía sau dấu `=`. Trong tài liệu này, mọi chữ gốc đều nằm trong `khung code` để bạn chép cho chính xác. Phần tiếng Việt chỉ giúp bạn hiểu nghĩa, đừng chép phần tiếng Việt vào file cấu hình.

---

## Các cụm từ lặp lại trong file

| Cụm gốc | Nghĩa | Giải thích |
|---|---|---|
| `更新` | Cập nhật | Dùng trong dòng tiêu đề của mỗi bản. |
| `随游戏更新` | Cập nhật theo bản game mới | NCSOFT vừa cập nhật game nên tác giả sửa bot cho chạy được với bản game mới. Gần như lúc nào cũng phải thay EXE và Lua. |
| `需要替换EXE` | Cần thay file EXE | Chép file chương trình `.exe` mới của bot (bảng điều khiển `控制台`) đè lên file cũ. |
| `需要替换lua` | Cần thay các file Lua | Chép các file mới trong thư mục `lua` (các script quyết định cách bot hành động) đè lên file cũ. |
| `（版本是X可不换）` | (Nếu đang dùng bản X thì không cần thay) | Ví dụ `（版本是9.10.1可不换）`: nếu EXE của bạn đã là bản `9.10.1` thì giữ nguyên EXE, chỉ cần thay Lua. |
| `下载lua即可` / `可下载lua` | Chỉ cần tải Lua là đủ / Có thể tải riêng Lua | Lỗi này chỉ cần thay thư mục `lua`, không cần thay EXE. |
| `注：` | Chú ý / Ghi chú | Hai dòng cuối của mỗi khối. |
| `最新EXE为 X` | EXE mới nhất là bản X | Phiên bản EXE của bảng điều khiển `控制台` nên dùng. |
| `大中控EXE为 Y` | EXE của `大中控` là bản Y | `大中控` = trung tâm điều khiển lớn, phần mềm quản lý nhiều máy và nhiều tài khoản. Phiên bản của nó tách riêng với EXE chính. |
| `中控` | Trung tâm điều khiển | Cách viết tắt của `大中控`. |
| `控制台` | Bảng điều khiển (console) | Cửa sổ chính của bot trên mỗi máy. |
| `修复…的问题` | Sửa lỗi … | |
| `增加` | Thêm (tính năng hoặc cài đặt mới) | |
| `具体看文件说明` / `具体看里面说明` | Xem chi tiết trong phần hướng dẫn của file đó / bên trong file | Hướng dẫn nằm ngay trong file cấu hình tương ứng (thường là các dòng chú thích). |
| `默认开启` / `此功能为默认开启` | Mặc định bật / Tính năng này mặc định bật | |
| `发呆` | Đứng đơ | Nhân vật đứng yên, không làm gì. |
| `小号` / `主号` | Tài khoản phụ / Tài khoản chính | Trong nhật ký này, `主号` (thường viết `buff主号`) là acc chính **đứng buff** (hay ngồi ở nhà trọ hồi mana), còn `小号` là các acc phụ đi đánh quái, được gọi về để **nhận buff** (`小号加buff`). |
| `红名` | Tên đỏ | Nhân vật bị đỏ tên vì giết người chơi khác (PK). |
| `地监` (trong file gốc thường viết `地监`, dạng phồn thể là `地監`) | Hầm ngục (dungeon) | |

---

## Các file được nhắc tới và vị trí trong gói

| File | Nằm ở | Ghi chú |
|---|---|---|
| `BaseConfig.txt` | `Game_Config\` | File cấu hình chính, chứa các mục `[基础配置]`, `[角色保护]`, `[组队配置]`, `[吃药配置]`, `[触发回城休息配置]`, `[登录配置]`, … |
| `TreasureName.txt` | `Game_Config\` | Danh sách tên bảo vật (thêm ở bản 9.16). |
| `ActivityConfig.txt` | `Game_Config\` | Cấu hình sự kiện (event). |
| `PersonageStorage.txt` / `PersonageTakeOutTheItem.txt` | `Game_Config\` | Gửi đồ vào / rút đồ ra kho cá nhân. |
| `BloodTakeOutTheItem.txt` | `Game_Config\` | Lấy đồ từ kho huyết minh (clan). |
| `saveitem.txt` | `Game_Config\` | Danh sách đồ giữ lại, không bán. |
| `CounterattackPeoples.txt` | `Game_Config\` | Cài đặt phản công người chơi. |
| `gj.txt` | `Game_Config\` | Cấu hình treo máy (`挂机`). |
| `ServerText.txt` | `config\` | Danh sách server. `大中控\Data\` cũng có một bản. |
| `config.ini` | `config\` | Cấu hình chương trình. |
| `launcher_TTGame_max_new.bmp`, `launcher_TTGame_max_new2.bmp`, `launcher_TTGame_max_new3.bmp` | `bmp\` | Ảnh mẫu để bot nhận ra giao diện launcher (?). |
| `JSBProxy64.dll` | Thư mục gốc của bot | Có sẵn trong gói (khoảng 23 MB). Bản 8.8 cần file này cho tính năng proxy IP. |

---

## Tóm tắt 5 thay đổi quan trọng gần đây

1. **Bản 9.16 (mới nhất):** cập nhật theo game mới. `大中控` hiển thị được **bảo vật** (`宝物`) và có thêm file `TreasureName.txt` để khai báo tên bảo vật. Sửa lỗi **đánh quái tại điểm cố định không đứng yên được**. Bản đồ mới **Aden (`亞丁`) chưa được hỗ trợ**, tác giả hẹn sẽ thêm sau. Cần thay EXE, Lua và `大中控` lên bản `9.16`.
2. **Bản 9.13:** ngưỡng **hồi máu cho đồng đội** (`为队员加血`) nay đặt được theo % (giá trị `0` = tắt, `1` = mặc định 65%, `70` = dưới 70%, …). Sửa lỗi đứng đơ và lỗi bắn tên khi có cây chắn.
3. **Bản 9.10.1:** khi tài khoản mới đăng nhập, launcher Purple (`紫P`) **tự bấm Đồng ý điều khoản**. Sửa lỗi cộng điểm khi tạo nhân vật và lỗi sửa tài khoản trên `大中控`.
4. **Bản 9.9:** **đổi logic đăng nhập, bắt buộc thay Lua**. Sửa lỗi `大中控` bị crash, cho phép đổi tên máy tính hiển thị ngay trên `中控`, sửa lỗi không dùng cuộn biến hình.
5. **Các bản 9.2, 9.1.1, 8.31.2, 8.31.1:** liên tục **sửa lỗi đăng nhập launcher Purple**, mỗi lần cần chép các ảnh `launcher_TTGame_max_new*.bmp` mới vào thư mục `bmp`. Nếu bot không bấm được launcher, hãy kiểm tra trước tiên xem các ảnh này đã là bản mới nhất chưa.

💡 **Muốn lên bản mới nhất thì làm gì?** Thay EXE bản `9.16`, thay toàn bộ thư mục `lua` và thay `大中控` bản `9.16`. Nhớ sao lưu thư mục `Game_Config` trước khi chép đè, để không mất cấu hình của bạn.

💡 **Lưu ý chung:** một vài dòng (bản 7.9 và 7.8.1) là lời tác giả nói rằng bot đã "xử lý" việc bị phát hiện hoặc khóa tài khoản. Đó chỉ là lời quảng cáo của tác giả. Dùng bot vi phạm điều khoản của NCSOFT, và tài khoản vẫn có thể bị khóa.

---

## Bản 9.16

Tiêu đề gốc: `天堂经典版Bd 更新9.16` (Lineage Classic Bd – cập nhật 9.16)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `随游戏更新` | Cập nhật theo bản game mới | Sửa bot để chạy được với bản game mới nhất. |
| 2 | `大中控增加宝物显示（版本为9.16）` | `大中控` (trung tâm điều khiển lớn) thêm phần hiển thị bảo vật (`宝物`) (phiên bản `大中控` là `9.16`) | Muốn thấy bảo vật trên `大中控` thì phải dùng `大中控` bản `9.16`. |
| 3 | `增加新配置 TreasureName.txt 宝物名字（背包的宝物显示控制台上）` | Thêm file cấu hình mới `TreasureName.txt` chứa tên bảo vật (`宝物名字`). Bảo vật có trong túi đồ (`背包`) sẽ hiện lên bảng điều khiển (`控制台`) | Tên vật phẩm ghi trong file phải đúng y chữ Trung như trong game. |
| 4 | `新地图亞丁晚一点支持` | Bản đồ mới `亞丁` (Aden) sẽ được hỗ trợ muộn hơn một chút | Hiện chưa treo máy ở Aden được. |
| 5 | `修复定点打怪定不住的问题` | Sửa lỗi đánh quái tại điểm cố định (`定点打怪`) nhưng nhân vật không đứng yên được ở điểm đó | Trước đây nhân vật hay chạy lệch khỏi điểm đã đặt. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: Chú ý, bản cập nhật này cần thay EXE và cần thay Lua.
- `注：最新EXE为 9.16 大中控EXE为 9.16`: EXE mới nhất là `9.16`, EXE của `大中控` là `9.16`.

---

## Bản 9.13

Tiêu đề gốc: `天堂经典版Bd 更新9.13` (Lineage Classic Bd – cập nhật 9.13)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复打怪偶然发呆与隔树射箭的问题` | Sửa lỗi thỉnh thoảng đứng đơ (`发呆`) khi đánh quái và lỗi bắn tên khi có cây chắn (`隔树射箭`) | Bắn khi có cây chắn giữa thì mũi tên không trúng, phí tên và phí thời gian. |
| 2 | `组队功能为队员加血改为可设置的百分比` | Trong chức năng tổ đội (`组队`), mục hồi máu cho đồng đội (`为队员加血`) nay đặt được ngưỡng theo phần trăm | Xem các dòng ngay bên dưới. |
| ↳ | `为队员加血=1` … `默认血量低于65%才会加` | `为队员加血=1`: mặc định chỉ hồi khi máu đồng đội dưới 65% | `1` = bật, dùng ngưỡng mặc định 65%. |
| ↳ | `=70 表示血量低于70%` | `=70` nghĩa là máu dưới 70% thì hồi | |
| ↳ | `=80 表示血量低于80%` | `=80` nghĩa là máu dưới 80% thì hồi | |
| ↳ | `以此类推` | Các số khác cũng tính theo cách đó | Ví dụ `=50` là máu dưới 50%. `=0` là **tắt**. Nhật ký không nói điều này, nhưng chú thích trong `BaseConfig.txt` ghi rõ (`=0关闭`). |

Dòng 16 trong file gốc, chép nguyên văn:

```
为队员加血=1默认血量低于65%才会加  =70 表示血量低于70% =80 表示血量低于80% 以此类推
```

💡 **Lưu ý:** khi sửa trong `BaseConfig.txt`, chỉ đổi con số sau `为队员加血=`, giữ nguyên chữ Trung. Key này xuất hiện ở **hai** mục: `[组队配置]` (tổ đội thường) và `[局域网组队配置]` (tổ đội qua mạng LAN). Hãy sửa đúng mục bạn đang dùng. Giá trị mặc định trong file là `0` (tắt).

**Ghi chú (`注`):**

- `注：更新需要替换EXE （版本是9.10.1可不换） 需要替换lua`: cần thay EXE (đang dùng EXE `9.10.1` thì không cần thay) và cần thay Lua.
- `注：最新EXE为 9.10.1 大中控EXE为 9.10`: EXE mới nhất là `9.10.1`, EXE của `大中控` là `9.10`.

---

## Bản 9.10.1

Tiêu đề gốc: `天堂经典版Bd 更新9.10.1` (Lineage Classic Bd – cập nhật 9.10.1)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复大中控编辑账号的问题（版本为9.10）` | Sửa lỗi khi chỉnh sửa tài khoản trên `大中控` (`大中控` bản `9.10`) | |
| 2 | `修复创建角色加点的问题` | Sửa lỗi cộng điểm chỉ số khi tạo nhân vật (`创建角色加点`) | |
| 3 | `增加新号登录时，紫P会自动点同意，勾选用户协议` | Thêm: khi tài khoản mới (`新号`) đăng nhập, launcher Purple (`紫P`) sẽ tự bấm "Đồng ý" và tích vào ô điều khoản người dùng (`用户协议`) | Acc mới không còn bị kẹt ở màn hình điều khoản. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 9.10.1 大中控EXE为 9.10`: EXE mới nhất là `9.10.1`, EXE của `大中控` là `9.10`.

---

## Bản 9.10

Tiêu đề gốc: `天堂经典版Bd 更新9.10` (Lineage Classic Bd – cập nhật 9.10)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复说话卷不会传 送寵物保管人 的问题(下载lua即可)` | Sửa lỗi cuộn dịch chuyển về Talking Island (`说话卷`) không dịch chuyển (`传 送`) đến NPC `寵物保管人` (Người giữ thú cưng) (?) (chỉ cần tải Lua) | Trong file gốc, chữ `传 送` bị dư dấu cách, đúng ra là `传送` (dịch chuyển). Chỉ cần thay thư mục `lua`. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE（版本是9.9可不换） 需要替换lua`: cần thay EXE (đang dùng EXE `9.9` thì không cần thay) và cần thay Lua.
- `注：最新EXE为 9.9 大中控EXE为 9.9`: EXE mới nhất là `9.9`, EXE của `大中控` là `9.9`.

---

## Bản 9.9.1

Tiêu đề gốc: `天堂经典版Bd 更新9.9.1` (Lineage Classic Bd – cập nhật 9.9.1)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复不会使用变身卷轴的问题(下载lua即可)` | Sửa lỗi không dùng cuộn biến hình (`变身卷轴`, Polymorph) (chỉ cần tải Lua) | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE（版本是9.9可不换） 需要替换lua`: cần thay EXE (đang dùng EXE `9.9` thì không cần thay) và cần thay Lua.
- `注：最新EXE为 9.9 大中控EXE为 9.9`: EXE mới nhất là `9.9`, EXE của `大中控` là `9.9`.

---

## Bản 9.9

Tiêu đề gốc: `天堂经典版Bd 更新9.9` (Lineage Classic Bd – cập nhật 9.9)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `随游戏更新` | Cập nhật theo bản game mới | |
| 2 | `修复大中控会崩溃的问题，增加可在中控上修改显示计算机名（版本为9.9）` | Sửa lỗi `大中控` bị crash (`崩溃`). Thêm khả năng đổi tên máy tính (`计算机名`) hiển thị ngay trên `中控` (`大中控` bản `9.9`) | Tiện khi quản lý nhiều máy: đặt tên dễ nhớ cho từng máy. |
| 3 | `修复不会使用变身卷轴的问题` | Sửa lỗi không dùng cuộn biến hình (`变身卷轴`) | |
| 4 | `BaseConfig.txt` → `[登录配置]` → `自动接码验证设备` | Thêm một mục cài đặt mới trong phần cấu hình đăng nhập (`[登录配置]`): tự động nhận mã SMS để xác minh thiết bị | ⚠️ Tài liệu này không hướng dẫn phần này. |
| 5 | `更改了登录逻辑，必须替换lua` | Đã thay đổi logic đăng nhập, **bắt buộc** phải thay Lua | 💡 Nếu chỉ thay EXE mà giữ Lua cũ thì có thể không đăng nhập được. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 9.9 大中控EXE为 9.9`: EXE mới nhất là `9.9`, EXE của `大中控` là `9.9`.

---

## Bản 9.2

Tiêu đề gốc: `天堂经典版Bd 更新9.2` (Lineage Classic Bd – cập nhật 9.2)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `随游戏更新` | Cập nhật theo bản game mới | |
| 2 | `变身卷改为随等级变不同的人物（无需设置）` | Cuộn biến hình (`变身卷`) nay biến thành hình dạng khác nhau tùy theo cấp độ nhân vật (không cần cài đặt gì) | Bot tự chọn hình biến phù hợp với cấp của bạn. |
| 3 | `修复登录紫P的问题` | Sửa lỗi đăng nhập qua launcher Purple (`紫P`) | Cần thay 3 file ảnh ở các dòng dưới. |
| ↳ | `需要替换bmp\launcher_TTGame_max_new.bmp` | Cần thay file `bmp\launcher_TTGame_max_new.bmp` | |
| ↳ | `需要替换bmp\launcher_TTGame_max_new2.bmp` | Cần thay file `bmp\launcher_TTGame_max_new2.bmp` | |
| ↳ | `需要替换bmp\launcher_TTGame_max_new3.bmp` | Cần thay file `bmp\launcher_TTGame_max_new3.bmp` | |
| ↳ | `到bmp文件夹中` | (chép) vào thư mục `bmp` | Các ảnh này có lẽ là ảnh mẫu để bot nhận ra nút trên launcher (?). Ảnh cũ sẽ khiến bot không bấm được. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 9.2 大中控EXE为8.7`: EXE mới nhất là `9.2`, EXE của `大中控` là `8.7`.

---

## Bản 9.1.1

Tiêu đề gốc: `天堂经典版Bd 更新9.1.1` (Lineage Classic Bd – cập nhật 9.1.1)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复登录紫P的问题` | Sửa lỗi đăng nhập qua launcher Purple (`紫P`) | |
| ↳ | `需要替换bmp\launcher_TTGame_max_new.bmp` | Cần thay file `bmp\launcher_TTGame_max_new.bmp` | |
| ↳ | `需要替换bmp\launcher_TTGame_max_new2.bmp` | Cần thay file `bmp\launcher_TTGame_max_new2.bmp` | |
| ↳ | `需要替换bmp\launcher_TTGame_max_new3.bmp` | Cần thay file `bmp\launcher_TTGame_max_new3.bmp` | |
| ↳ | `到bmp文件夹中` | (chép) vào thư mục `bmp` | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 9.1.1 大中控EXE为8.7`: EXE mới nhất là `9.1.1`, EXE của `大中控` là `8.7`.

---

## Bản 8.31.2

Tiêu đề gốc: `天堂经典版Bd 更新8.31.2` (Lineage Classic Bd – cập nhật 8.31.2)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复登录紫P的问题` | Sửa lỗi đăng nhập qua launcher Purple (`紫P`) | |
| ↳ | `需要替换bmp\launcher_TTGame_max_new.bmp` | Cần thay file `bmp\launcher_TTGame_max_new.bmp` | |
| ↳ | `需要替换bmp\launcher_TTGame_max_new2.bmp` | Cần thay file `bmp\launcher_TTGame_max_new2.bmp` | |
| ↳ | `到bmp文件夹中` | (chép) vào thư mục `bmp` | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 8.31.2 大中控EXE为8.7`: EXE mới nhất là `8.31.2`, EXE của `大中控` là `8.7`.

---

## Bản 8.31.1

Tiêu đề gốc: `天堂经典版Bd 更新8.31.1` (Lineage Classic Bd – cập nhật 8.31.1)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复登录紫P的问题（需要替换bmp\launcher_TTGame_max_new.bmp 到bmp文件夹中）` | Sửa lỗi đăng nhập qua launcher Purple (cần chép file `bmp\launcher_TTGame_max_new.bmp` mới vào thư mục `bmp`) | |
| 2 | `增加 BaseConfig.txt [基础配置] 自动领取说话卷轴=1 的开关（默认开启）` | Trong `BaseConfig.txt`, mục `[基础配置]` (cấu hình cơ bản), thêm công tắc `自动领取说话卷轴=1`: tự động nhận cuộn `说话卷轴` (cuộn dịch chuyển về Talking Island) (mặc định bật) | `=1` là bật, `=0` là tắt. Cuộn này được nhận từ kho nạp, xem thêm bản 8.8 mục 5. |
| 3 | `增加 ActivityConfig.txt 文件中 冰之女王活动 （具体看里面说明）` | Thêm sự kiện Nữ hoàng Băng (`冰之女王活动`) vào file `ActivityConfig.txt` (xem hướng dẫn chi tiết bên trong file) | Trong thư mục `lua` cũng có file `ActivityIceQueen.lua` cho sự kiện này. |
| 4 | `解决8.31的无法登录的问题` | Khắc phục lỗi không đăng nhập được của bản 8.31 | Ai còn dùng bản 8.31 thì phải lên bản này. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 8.31.1 大中控EXE为8.7`: EXE mới nhất là `8.31.1`, EXE của `大中控` là `8.7`.

---

## Bản 8.28.1

Tiêu đề gốc: `天堂经典版Bd 更新8.28.1` (Lineage Classic Bd – cập nhật 8.28.1)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `随游戏更新` | Cập nhật theo bản game mới | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 8.28.1 大中控EXE为8.7`: EXE mới nhất là `8.28.1`, EXE của `大中控` là `8.7`.

---

## Bản 8.26

Tiêu đề gốc: `天堂经典版Bd 更新8.26` (Lineage Classic Bd – cập nhật 8.26)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `随游戏更新` | Cập nhật theo bản game mới | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 8.26 大中控EXE为8.7`: EXE mới nhất là `8.26`, EXE của `大中控` là `8.7`.

---

## Bản 8.20.1

Tiêu đề gốc: `天堂经典版Bd 更新8.20.1` (Lineage Classic Bd – cập nhật 8.20.1)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复为队员放加速术的bug` | Sửa lỗi (bug) khi thi triển phép Tăng tốc (`加速术`, Haste) cho đồng đội | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE（版本是8.20可不换） 需要替换lua`: cần thay EXE (đang dùng EXE `8.20` thì không cần thay) và cần thay Lua.
- `注：最新EXE为 8.20 大中控EXE为8.7`: EXE mới nhất là `8.20`, EXE của `大中控` là `8.7`.

---

## Bản 8.20

Tiêu đề gốc: `天堂经典版Bd 更新8.20` (Lineage Classic Bd – cập nhật 8.20)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `增加 BaseConfig.txt [角色保护]低蓝量使用回城卷（针对王族为周围队员加buff没蓝时）` | Trong `BaseConfig.txt`, mục `[角色保护]` (bảo vệ nhân vật), thêm tùy chọn `低蓝量使用回城卷`: dùng cuộn về thành (`回城卷`) khi mana thấp (`低蓝量`). Tùy chọn này dành cho trường hợp Hoàng tộc (`王族`) buff cho đồng đội xung quanh đến hết mana | Hết mana thì Hoàng tộc không tự bảo vệ được, nên về thành cho an toàn. Theo chú thích trong `BaseConfig.txt`: khi mana dưới 30%, bot dùng cuộn `说话卷`, cuộn về thành hoặc phép `世界樹的呼喚` (Tiếng gọi Cây Thế giới, Teleport to Mother). `=0` là không dùng (mặc định). |
| 2 | `增加 BaseConfig.txt [组队配置]为队员放技能 指定buff技能 比如 通暢氣脈術` | Trong `BaseConfig.txt`, mục `[组队配置]` (cấu hình tổ đội), thêm mục `为队员放技能` (dùng kỹ năng cho đồng đội) để chỉ định kỹ năng buff, ví dụ `通暢氣脈術` | `通暢氣脈術` = Thông suốt khí mạch, phép tăng Nhanh nhẹn (DEX), tên tiếng Anh "Physical Enchant: DEX". Tên kỹ năng phải ghi đúng chữ Trung như trong game. Theo chú thích trong `BaseConfig.txt`: muốn ghi nhiều kỹ năng thì ngăn cách bằng dấu phẩy, ví dụ `通暢氣脈術,加速術`. Mặc định, mỗi đồng đội được buff lại 19 phút một lần. |
| 3 | `修复控制台与中控连接断开后不会重连的问题` | Sửa lỗi bảng điều khiển (`控制台`) không tự kết nối lại sau khi mất kết nối với `中控` | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 8.20 大中控EXE为8.7`: EXE mới nhất là `8.20`, EXE của `大中控` là `8.7`.

---

## Bản 8.19

Tiêu đề gốc: `天堂经典版Bd 更新8.19` (Lineage Classic Bd – cập nhật 8.19)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `随游戏更新` | Cập nhật theo bản game mới | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 8.19 大中控EXE为8.7`: EXE mới nhất là `8.19`, EXE của `大中控` là `8.7`.

---

## Bản 8.15

Tiêu đề gốc: `天堂经典版Bd 更新8.15` (Lineage Classic Bd – cập nhật 8.15)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `增加 PersonageStorage.txt 个人仓库存入 设置（具体看文件说明）` | Thêm file `PersonageStorage.txt` để cài đặt việc gửi đồ vào kho cá nhân (`个人仓库存入`) (xem hướng dẫn trong file) | |
| 2 | `增加 PersonageTakeOutTheItem.txt 个人仓库取出 设置（具体看文件说明）` | Thêm file `PersonageTakeOutTheItem.txt` để cài đặt việc rút đồ từ kho cá nhân (`个人仓库取出`) (xem hướng dẫn trong file) | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE（版本是8.12可不换） 需要替换lua`: cần thay EXE (đang dùng EXE `8.12` thì không cần thay) và cần thay Lua.
- `注：最新EXE为 8.12 大中控EXE为8.7`: EXE mới nhất là `8.12`, EXE của `大中控` là `8.7`.

---

## Bản 8.14

Tiêu đề gốc: `天堂经典版Bd 更新8.14` (Lineage Classic Bd – cập nhật 8.14)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `增加 BaseConfig.txt 旅馆为自己放加速次数 设置` | Thêm cài đặt `旅馆为自己放加速次数` trong `BaseConfig.txt`: số lần tự thi triển Tăng tốc (`加速`, Haste) cho bản thân khi ở nhà trọ (`旅馆`) | Điền một con số. Theo chú thích trong `BaseConfig.txt` (mục `[角色保护]`): `=0` là tắt (mặc định), `=1` đến `=5` là số lần thi triển, tối đa 5. |
| 2 | `增加 BloodTakeOutTheItem.txt 血盟取物品 角色在村庄才触发 的条件改为可设置 用完就触发（具体看文件说明）` | Trong file `BloodTakeOutTheItem.txt` (lấy đồ từ kho huyết minh, `血盟取物品`), điều kiện "chỉ kích hoạt khi nhân vật đang ở làng" (`角色在村庄才触发`) nay có thể cài thành "dùng hết là kích hoạt" (`用完就触发`) (xem hướng dẫn trong file) | `血盟` = huyết minh, tức clan hoặc guild. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE（版本是8.12可不换） 需要替换lua`: cần thay EXE (đang dùng EXE `8.12` thì không cần thay) và cần thay Lua.
- `注：最新EXE为 8.12 大中控EXE为8.7`: EXE mới nhất là `8.12`, EXE của `大中控` là `8.7`.

---

## Bản 8.12

Tiêu đề gốc: `天堂经典版Bd 更新8.12` (Lineage Classic Bd – cập nhật 8.12)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `随游戏更新` | Cập nhật theo bản game mới | |
| 2 | `增加 BaseConfig.txt [触发回城休息配置] 设置` | Thêm mục `[触发回城休息配置]` trong `BaseConfig.txt`: cấu hình các điều kiện để về thành nghỉ ngơi | |
| 3 | `使用变身卷轴改为在挂机点才用，平时不会用` | Cuộn biến hình (`变身卷轴`) nay chỉ được dùng khi đã tới điểm treo máy (`挂机点`), lúc khác không dùng | 💡 Giúp tiết kiệm cuộn biến hình. |
| 4 | `红名状态下改为不会购买与出售物品` | Khi đang tên đỏ (`红名`), bot sẽ không mua và bán vật phẩm nữa | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 8.12 大中控EXE为8.7`: EXE mới nhất là `8.12`, EXE của `大中控` là `8.7`.

---

## Bản 8.8.1

Tiêu đề gốc: `天堂经典版Bd 更新8.8.1` (Lineage Classic Bd – cập nhật 8.8.1)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `随游戏更新` | Cập nhật theo bản game mới | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 8.8.1 大中控EXE为8.7`: EXE mới nhất là `8.8.1`, EXE của `大中控` là `8.7`.

---

## Bản 8.8

Tiêu đề gốc: `天堂经典版Bd 更新8.8` (Lineage Classic Bd – cập nhật 8.8)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `恢复单进程ip代理加速（控制台右键单击 导入ip 目录需要JSBProxy64.dll文件）` | Khôi phục tính năng tăng tốc bằng proxy IP riêng cho từng tiến trình game (`单进程ip代理加速`). Cách dùng: nhấp chuột phải trên bảng điều khiển (`控制台`) rồi chọn `导入ip` (nhập IP). Thư mục bot cần có file `JSBProxy64.dll` | Mỗi cửa sổ game có thể đi qua một proxy riêng. Trong gói có file `ip.txt` (đang trống), có lẽ dùng cho tính năng này (?). |
| 2 | `修复红名了，设置血盟取箭头不会在仓库取箭头的问题` | Sửa lỗi: khi bị tên đỏ (`红名`), dù đã cài lấy mũi tên từ kho huyết minh (`血盟取箭头`), bot vẫn không vào kho (`仓库`) lấy mũi tên | |
| 3 | `增加妖精24级自动学习 魔法防禦` | Thêm: Elf (`妖精`) lên cấp 24 sẽ tự học phép `魔法防禦` | `魔法防禦` = Phòng ngự ma pháp (Resist Magic). |
| 4 | `修复韩文系统 中控通知小号加buff不过来的问题，需要替换中控为8.7` | Sửa lỗi trên Windows tiếng Hàn (`韩文系统`): `中控` báo acc phụ (`小号`) về nhận buff nhưng acc phụ không về. Cần thay `中控` lên bản `8.7` | Chỉ ảnh hưởng máy cài Windows tiếng Hàn. |
| 5 | `说话卷轴在背包中时，不在领取加值仓库物品（不会在领取第2个多余说话卷轴）` | Khi trong túi đồ đã có cuộn `说话卷轴`, bot không nhận vật phẩm từ kho nạp (`加值仓库`) nữa (để không nhận thêm cuộn `说话卷轴` thứ 2 dư thừa) | `加值仓库` = kho chứa vật phẩm nạp tiền hoặc quà tặng (?). Trong file gốc, chữ `不在` là viết nhầm của `不再` (không … nữa). |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 8.8 大中控EXE为8.7`: EXE mới nhất là `8.8`, EXE của `大中控` là `8.7`.

---

## Bản 8.6

Tiêu đề gốc: `天堂经典版Bd 更新8.6` (Lineage Classic Bd – cập nhật 8.6)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复 反击人 无效 以及会反击白名单角色的问题` | Sửa lỗi phản công người chơi (`反击人`) không có tác dụng, và lỗi phản công cả những nhân vật nằm trong danh sách trắng (`白名单`) | Danh sách trắng là những người bot không được đánh. |
| 2 | `出售物品时 敏捷魔法頭盔 力量魔法頭盔 改为默认不保留，需要在saveitem.txt中设置` | Khi bán đồ, `敏捷魔法頭盔` (Mũ phép thuật Nhanh nhẹn) và `力量魔法頭盔` (Mũ phép thuật Sức mạnh) nay **mặc định không được giữ lại**, tức là sẽ bị bán. Muốn giữ thì phải khai báo trong `saveitem.txt` | 💡 Nếu bạn đang dùng tính năng tự đổi mũ (bản 7.31), nhớ thêm 2 tên mũ này vào `saveitem.txt`. File `saveitem.txt` đi kèm gói này đã có sẵn cả hai tên. |
| ↳ | `要穿的或者切换的装备请锁定在背包中` | Trang bị bạn đang mặc hoặc dùng để đổi qua lại, hãy khóa (lock) chúng trong túi đồ | Đồ đã khóa sẽ không bị bot bán. |
| 3 | `修复近战职业被远程怪物攻击时发呆的问题` | Sửa lỗi nhân vật nghề cận chiến (`近战职业`) đứng đơ khi bị quái tầm xa (`远程怪物`) tấn công | |
| 4 | `修复buff主号在旅馆蓝量没满就出去的问题` | Sửa lỗi acc chính chuyên buff (`buff主号`) rời nhà trọ khi mana (`蓝量`) chưa đầy | Acc chính ngồi ở nhà trọ để hồi mana rồi buff cho các acc phụ. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE（版本是8.5.1可不换） 需要替换lua`: cần thay EXE (đang dùng EXE `8.5.1` thì không cần thay) và cần thay Lua.
- `注：最新EXE为 8.5.1 大中控EXE为7.20`: EXE mới nhất là `8.5.1`, EXE của `大中控` là `7.20`.

---

## Bản 8.5.2

Tiêu đề gốc: `天堂经典版Bd 更新8.5.2` (Lineage Classic Bd – cập nhật 8.5.2)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `增加 村庄传送到地监门口间隔 BaseConfig.txt [基础配置] 设置` | Thêm cài đặt `村庄传送到地监门口间隔` trong `BaseConfig.txt`, mục `[基础配置]`: khoảng thời gian giữa hai lần dịch chuyển từ làng đến cửa hầm ngục | Đơn vị là **phút**. Nhật ký không ghi, nhưng chú thích trong `BaseConfig.txt` có ghi: `=0` là tắt (mặc định), `=10` là trong 10 phút chỉ dịch chuyển 1 lần. Khi chưa hết thời gian chờ, bot đi bộ tới hầm ngục. Bản 7.29.1 từng đặt cố định 15 phút. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE（版本是8.5.1可不换） 需要替换lua`: cần thay EXE (đang dùng EXE `8.5.1` thì không cần thay) và cần thay Lua.
- `注：最新EXE为 8.5.1 大中控EXE为7.20`: EXE mới nhất là `8.5.1`, EXE của `大中控` là `7.20`.

---

## Bản 8.5

Tiêu đề gốc: `天堂经典版Bd 更新8.5` (Lineage Classic Bd – cập nhật 8.5)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `随游戏更新` | Cập nhật theo bản game mới | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为8.5 大中控EXE为7.20`: EXE mới nhất là `8.5`, EXE của `大中控` là `7.20`.

---

## Bản 8.4.1

Tiêu đề gốc: `天堂经典版Bd 更新8.4.1` (Lineage Classic Bd – cập nhật 8.4.1)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复8.4版本控制台崩溃问题` | Sửa lỗi bảng điều khiển (`控制台`) bị crash ở bản 8.4 | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE（版本是7.31可不换） 需要替换lua`: cần thay EXE (đang dùng EXE `7.31` thì không cần thay) và cần thay Lua.
- `注：最新EXE为 7.31 大中控EXE为7.20`: EXE mới nhất là `7.31`, EXE của `大中控` là `7.20`.

---

## Bản 8.4

Tiêu đề gốc: `天堂经典版Bd 更新8.4` (Lineage Classic Bd – cập nhật 8.4)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复小号加buff后设置等待时间，加完会立马飞走的问题` | Sửa lỗi acc phụ (`小号`) đã được đặt thời gian chờ sau khi nhận buff, nhưng nhận buff xong vẫn dịch chuyển đi ngay (`立马飞走`, "bay đi ngay") | |
| 2 | `修复在城镇发呆不出去打怪的问题` | Sửa lỗi đứng đơ trong thị trấn (`城镇`), không chịu ra ngoài đánh quái | |
| 3 | `增加 自动穿戴头盔 BaseConfig.txt 中 [基础配置] 设置（当设置自动切换头盔后，需要换回穿戴的头盔）` | Thêm cài đặt `自动穿戴头盔` (tự động đội mũ) trong `BaseConfig.txt`, mục `[基础配置]`. Dùng khi đã bật tự đổi mũ và cần đổi lại về chiếc mũ thường đội | Đi cùng tính năng `自动切换敏捷力量头盔` của bản 7.31. Theo chú thích trong `BaseConfig.txt`: điền **tên chiếc mũ** (chữ Trung, đúng như trong game) sau `自动穿戴头盔=`. Mũ đó phải được khóa trong túi đồ. |
| 4 | `修复吃肉开关失效的问题` | Sửa lỗi công tắc ăn thịt (`吃肉`) không có tác dụng | Ăn thịt để giữ độ no, xem bản 8.2. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE（版本是7.31可不换） 需要替换lua`: cần thay EXE (đang dùng EXE `7.31` thì không cần thay) và cần thay Lua.
- `注：最新EXE为 7.31 大中控EXE为7.20`: EXE mới nhất là `7.31`, EXE của `大中控` là `7.20`.

---

## Bản 8.2

Tiêu đề gốc: `天堂经典版Bd 更新8.2` (Lineage Classic Bd – cập nhật 8.2)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `增加饱食度满了在出门（饱食度不满时自动买肉在吃肉 此功能为默认开启）` | Thêm: độ no (`饱食度`) phải đầy thì mới ra ngoài. Khi độ no chưa đầy, bot tự mua thịt rồi ăn. Tính năng này mặc định bật | Chữ `在` trong câu gốc là viết nhầm của `再` (rồi mới). |
| 2 | `增加 王族骑士 在旅馆自为自己增加2个小时的buff在出旅馆（此功能为默认开启）` | Thêm: Hoàng tộc (`王族`) và Hiệp sĩ (`骑士`) ở nhà trọ (`旅馆`) tự buff cho bản thân loại buff kéo dài 2 giờ rồi mới rời nhà trọ (mặc định bật) | `2个小时` = 2 giờ. |
| 3 | `修复 自动切换敏捷力量头盔 会一直来回切换并且取下头盔的问题` | Sửa lỗi tính năng `自动切换敏捷力量头盔` (tự đổi giữa mũ Nhanh nhẹn và mũ Sức mạnh) cứ đổi qua đổi lại liên tục và tháo mũ ra | |
| 4 | `修复 自动传送到地监门口经常失效的问题` | Sửa lỗi tự dịch chuyển đến cửa hầm ngục (`地监门口`) thường xuyên không hoạt động | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE（版本是7.31可不换） 需要替换lua`: cần thay EXE (đang dùng EXE `7.31` thì không cần thay) và cần thay Lua.
- `注：最新EXE为 7.31 大中控EXE为7.20`: EXE mới nhất là `7.31`, EXE của `大中控` là `7.20`.

---

## Bản 7.31

Tiêu đề gốc: `天堂经典版Bd 更新7.31` (Lineage Classic Bd – cập nhật 7.31)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `增加 自动切换敏捷力量头盔 BaseConfig.txt 中 [基础配置] 设置` | Thêm cài đặt `自动切换敏捷力量头盔` (tự đổi giữa mũ Nhanh nhẹn và mũ Sức mạnh) trong `BaseConfig.txt`, mục `[基础配置]` | Xem thêm bản 8.2, 8.4 và 8.6 (cần giữ hai chiếc mũ này trong `saveitem.txt`). |
| 2 | `修复 欧瑞旅馆休息无法进去的问题` | Sửa lỗi không vào được nhà trọ Oren (`欧瑞旅馆`) để nghỉ | `欧瑞` = Oren. |
| 3 | `修复 触发随机传送配置 开启时 走向挂机点路上就触发的问题` | Sửa lỗi: khi bật `触发随机传送配置` (cấu hình kích hoạt dịch chuyển ngẫu nhiên), nhân vật bị kích hoạt dịch chuyển ngay trên đường đi đến điểm treo máy | Giờ chỉ kích hoạt khi đã tới điểm treo máy. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.31 大中控EXE为7.20`: EXE mới nhất là `7.31`, EXE của `大中控` là `7.20`.

---

## Bản 7.30.1

Tiêu đề gốc: `天堂经典版Bd 更新7.30.1` (Lineage Classic Bd – cập nhật 7.30.1)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `增加 死亡复活后自动购买肉 BaseConfig.txt 中 [基础配置] 设置` | Thêm cài đặt `死亡复活后自动购买肉` (tự động mua thịt sau khi chết và hồi sinh) trong `BaseConfig.txt`, mục `[基础配置]` | Theo chú thích trong `BaseConfig.txt`: giá trị là **số miếng thịt** cần mua. `=0` là tắt. Mặc định `=19`: mua 19 miếng và ăn đến khi no, thường 19 miếng là vừa đủ no. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.29.2（版本是7.29.2可不换） 大中控EXE为7.20`: EXE mới nhất là `7.29.2` (đang dùng `7.29.2` thì không cần thay), EXE của `大中控` là `7.20`.

---

## Bản 7.30

Tiêu đề gốc: `天堂经典版Bd 更新7.30` (Lineage Classic Bd – cập nhật 7.30)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复血盟取物品，背包数量充足还是会取的问题` | Sửa lỗi lấy đồ từ kho huyết minh (`血盟取物品`): trong túi đồ đã đủ số lượng mà bot vẫn đi lấy thêm | |
| 2 | `修复不会去指定村庄旅馆休息，还会到说话之岛村旅馆的问题` | Sửa lỗi không đến nghỉ ở nhà trọ của làng đã chỉ định mà lại về nhà trọ làng Talking Island (`说话之岛村`) | Trong file gốc tên làng viết dạng giản thể `说话之岛村` (dạng phồn thể là `說話之島村`). 💡 Làng nghỉ được chọn ở key `旅馆休息村庄=` trong `BaseConfig.txt`, mục `[角色保护]`. File cấu hình dùng dạng **phồn thể** (`旅馆休息村庄=說話之島村`), nên khi đổi làng hãy chép tên theo file cấu hình, đừng chép theo nhật ký. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.29.2（版本是7.29.2可不换） 大中控EXE为7.20`: EXE mới nhất là `7.29.2` (đang dùng `7.29.2` thì không cần thay), EXE của `大中控` là `7.20`.

---

## Bản 7.29.2

Tiêu đề gốc: `天堂经典版Bd 更新7.29.2` (Lineage Classic Bd – cập nhật 7.29.2)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `随游戏更新` | Cập nhật theo bản game mới | |
| 2 | `增加 主动攻红名玩家 在配置 CounterattackPeoples.txt 设置` | Thêm tùy chọn chủ động tấn công người chơi tên đỏ (`主动攻红名玩家`), cài trong file `CounterattackPeoples.txt` | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.29.2 大中控EXE为7.20`: EXE mới nhất là `7.29.2`, EXE của `大中控` là `7.20`.

---

## Bản 7.29.1

Tiêu đề gốc: `天堂经典版Bd 更新7.29.1` (Lineage Classic Bd – cập nhật 7.29.1)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `随游戏更新` | Cập nhật theo bản game mới | |
| 2 | `修复走向 火龍窟 会经常卡住并绕远路的问题` | Sửa lỗi khi đi đến `火龍窟` (Hang Rồng Lửa) (?) thường bị kẹt và đi đường vòng xa | |
| 3 | `修复组队队员不接受邀请的问题` | Sửa lỗi thành viên tổ đội không chấp nhận lời mời vào đội | |
| 4 | `修复玩家隔墙攻击自己时会反击的问题` | Sửa lỗi: người chơi khác đánh mình từ bên kia tường (`隔墙`) thì bot lại phản công | Giờ bot không phản công qua tường nữa, vì đánh qua tường cũng không trúng. |
| 5 | `进地监改为间隔15分钟传送1次到门口` | Khi vào hầm ngục, đổi thành cứ 15 phút mới dịch chuyển đến cửa hầm 1 lần | `15分钟` = 15 phút. Từ bản 8.5.2 khoảng này cài được trong `BaseConfig.txt`. |
| 6 | `增加新地图 被遺棄者之地 : 深淵 打怪地图=被遺棄者之地 : 深淵 这样设置` | Thêm bản đồ mới `被遺棄者之地 : 深淵` (Vùng đất bị ruồng bỏ: Vực thẳm). Cài theo cách này (`这样设置`): `打怪地图=被遺棄者之地 : 深淵` | `打怪地图` = bản đồ đánh quái. |
| 7 | `修复7.29更新使用物品地址错误的问题` | Sửa lỗi sai địa chỉ (bộ nhớ) dùng vật phẩm của bản 7.29 | Ở bản 7.29, bot dùng vật phẩm bị lỗi. |

Dòng cài đặt ở mục 6, chép nguyên văn:

```
打怪地图=被遺棄者之地 : 深淵
```

💡 **Lưu ý:** tên bản đồ có dấu cách ở **hai bên** dấu hai chấm (`之地 : 深淵`). Dấu hai chấm là dấu `:` thường, nửa độ rộng, không phải dấu `：` toàn độ rộng của chữ Trung. Phải chép đúng y như vậy, thiếu một dấu cách là bot có thể không nhận ra bản đồ. Key `打怪地图=` nằm trong file cấu hình treo máy `gj.txt` (thư mục `Game_Config`).

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.29.1 大中控EXE为7.20`: EXE mới nhất là `7.29.1`, EXE của `大中控` là `7.20`.

---

## Bản 7.26.1

Tiêu đề gốc: `天堂经典版Bd 更新7.26.1` (Lineage Classic Bd – cập nhật 7.26.1)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `增加 吃蓝药百分比 BaseConfig.txt 中 [吃药配置] 设置` | Thêm cài đặt `吃蓝药百分比` (uống thuốc mana khi MP dưới bao nhiêu %) trong `BaseConfig.txt`, mục `[吃药配置]` (cấu hình uống thuốc) | Điền số %, ví dụ `50` = MP dưới 50% thì uống. Mặc định trong file là `70`. ⚠️ Theo chú thích trong `BaseConfig.txt`, bot chỉ uống khi đồng thời đã bật `藍色藥水=1` trong mục `[使用加速药水]`. |
| 2 | `增加 法师为队员加血（与妖精一样组队中可开启）` | Thêm: Pháp sư (`法师`) hồi máu cho đồng đội (bật được trong phần tổ đội, giống Elf `妖精`) | |
| 3 | `增加 法师自动学习技能（默认自动学习）` | Thêm: Pháp sư tự học kỹ năng (mặc định tự học) | |
| 4 | `优化进地监的方式 所有地监采用附近村庄npc传送到门口，在走进地监` | Tối ưu cách vào hầm ngục: mọi hầm ngục đều nhờ NPC ở làng gần đó dịch chuyển đến cửa hầm, rồi mới đi bộ vào trong | Chữ `在` là viết nhầm của `再` (rồi mới). |
| 5 | `gj.txt 配置中增加字段 低于多少金币不拾取` | Thêm trường `低于多少金币不拾取` (đống vàng dưới bao nhiêu thì không nhặt) vào file cấu hình `gj.txt` | 💡 Giúp bot không mất thời gian nhặt những đống vàng nhỏ. Theo chú thích trong `gj.txt`: `=0` là tắt (nhặt hết, mặc định). Đặt số lớn hơn 0, ví dụ `=5`, thì bot **không nhặt** đống vàng từ 5 trở xuống. Key này lặp lại trong từng khối cấu hình treo máy của `gj.txt`. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.23.1（版本是7.23.1可不换） 大中控EXE为7.20`: EXE mới nhất là `7.23.1` (đang dùng `7.23.1` thì không cần thay), EXE của `大中控` là `7.20`.

---

## Bản 7.26

Tiêu đề gốc: `天堂经典版Bd 更新7.26` (Lineage Classic Bd – cập nhật 7.26)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复血量正常下回世界树或者回城的问题（下载lua或者用完整包里面的Lua）` | Sửa lỗi máu (`血量`) vẫn bình thường mà bot lại về Cây Thế giới (`世界树`) hoặc về thành (`回城`). Cách cập nhật: tải Lua, hoặc lấy Lua trong gói đầy đủ (`完整包`) | `世界树` (World Tree) là nơi Elf trở về. Chỉ cần thay thư mục `lua`. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.23.1（版本是7.23.1可不换） 大中控EXE为7.20`: EXE mới nhất là `7.23.1` (đang dùng `7.23.1` thì không cần thay), EXE của `大中控` là `7.20`.

---

## Bản 7.23.2

Tiêu đề gốc: `天堂经典版Bd 更新7.23.2` (Lineage Classic Bd – cập nhật 7.23.2)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `增加新区 飛馬珀伽索斯2 在config\ServerText.txt 中` | Thêm server mới `飛馬珀伽索斯2` (Ngựa bay Pegasus 2) vào file `config\ServerText.txt` | `新区` = server (khu) mới. |
| ↳ | `需要替换lua 与 ServerText.txt` | Cần thay Lua và file `ServerText.txt` | |
| ↳ | `然后在控制台设置 服务器为 飛馬珀伽索斯2` | Sau đó, trên bảng điều khiển (`控制台`) đặt server (`服务器`) là `飛馬珀伽索斯2` | Chọn đúng tên server bằng chữ Trung. |
| ↳ | `如果是 飛馬珀伽索斯 会选最底下的区的需要替换lua` | Nếu bạn chơi server `飛馬珀伽索斯` (Ngựa bay Pegasus) mà bot chọn nhầm server nằm dưới cùng danh sách thì cần thay Lua | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.23.1（版本是7.23.1可不换） 大中控EXE为7.20`: EXE mới nhất là `7.23.1` (đang dùng `7.23.1` thì không cần thay), EXE của `大中控` là `7.20`.

---

## Bản 7.23.1

Tiêu đề gốc: `天堂经典版Bd 更新7.23.1` (Lineage Classic Bd – cập nhật 7.23.1)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `随游戏更新` | Cập nhật theo bản game mới | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.23.1 大中控EXE为7.20`: EXE mới nhất là `7.23.1`, EXE của `大中控` là `7.20`.

---

## Bản 7.23

Tiêu đề gốc: `天堂经典版Bd 更新7.23` (Lineage Classic Bd – cập nhật 7.23)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `增加新区 獅子涅墨亞2 在config\ServerText.txt 中` | Thêm server mới `獅子涅墨亞2` (Sư tử Nemea 2) vào file `config\ServerText.txt` | |
| ↳ | `需要替换lua 与 ServerText.txt` | Cần thay Lua và file `ServerText.txt` | |
| ↳ | `然后在控制台设置 服务器为 獅子涅墨亞2` | Sau đó, trên bảng điều khiển đặt server là `獅子涅墨亞2` | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.22（版本是7.22可不换） 大中控EXE为7.20`: EXE mới nhất là `7.22` (đang dùng `7.22` thì không cần thay), EXE của `大中控` là `7.20`.

---

## Bản 7.22

Tiêu đề gốc: `天堂经典版Bd 更新7.22` (Lineage Classic Bd – cập nhật 7.22)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `随游戏更新` | Cập nhật theo bản game mới | |
| 2 | `增加新区 獅子涅墨亞 在config\ServerText.txt 中` | Thêm server mới `獅子涅墨亞` (Sư tử Nemea) vào file `config\ServerText.txt` | |
| 3 | `中控更新7.20 修复中控呼叫小号加buff会把不同区服的人叫过来的问题` | `中控` lên bản `7.20`, sửa lỗi: khi `中控` gọi acc phụ (`小号`) về nhận buff thì gọi luôn cả nhân vật ở server khác (`不同区服`) | |
| 4 | `修复集火时队长掉线队员发呆的问题` | Sửa lỗi đang tập trung đánh một mục tiêu (`集火`) mà đội trưởng (`队长`) rớt mạng (`掉线`) thì các thành viên đứng đơ | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.22 大中控EXE为7.20`: EXE mới nhất là `7.22`, EXE của `大中控` là `7.20`.

---

## Bản 7.18

Tiêu đề gốc: `天堂经典版Bd 更新7.18` (Lineage Classic Bd – cập nhật 7.18)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 (2 dòng) | `config\config.ini` → `驱动模式` | Bản này chỉ có một ghi chú về mục `驱动模式`, tức chế độ driver (dùng driver kernel của Windows), nằm trong file `config\config.ini` | ⚠️ Tài liệu này không hướng dẫn phần này. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.18 大中控EXE为7.20`: EXE mới nhất là `7.18`, EXE của `大中控` là `7.20`.

---

## Bản 7.16

Tiêu đề gốc: `天堂经典版Bd 更新7.16` (Lineage Classic Bd – cập nhật 7.16)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `随游戏更新` | Cập nhật theo bản game mới | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.16 大中控EXE为5.25`: EXE mới nhất là `7.16`, EXE của `大中控` là `5.25`.

---

## Bản 7.15.3

Tiêu đề gốc: `天堂经典版Bd 更新7.15.3` (Lineage Classic Bd – cập nhật 7.15.3)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复史巴托一直打，不会用无所遁形的问题` | Sửa lỗi cứ đánh mãi quái `史巴托` (Spartoi) (?) mà không dùng phép `无所遁形` (Detection, làm lộ mục tiêu đang ẩn) | Quái này có lúc ẩn đi, cần phép làm lộ mới đánh tiếp được (?). |
| 2 | `修复污染的祝福之地进入失败的问题` | Sửa lỗi vào bản đồ `污染的祝福之地` (Vùng đất Ban phước bị ô nhiễm) không thành công | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.15.3 大中控EXE为5.25`: EXE mới nhất là `7.15.3`, EXE của `大中控` là `5.25`.

---

## Bản 7.15.1

Tiêu đề gốc: `天堂经典版Bd 更新7.15.1` (Lineage Classic Bd – cập nhật 7.15.1)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复一直组队的问题` | Sửa lỗi tổ đội liên tục (`一直组队`) | Bot cứ mời hoặc lập tổ đội lặp đi lặp lại không dừng (?). |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.15.1 大中控EXE为5.25`: EXE mới nhất là `7.15.1`, EXE của `大中控` là `5.25`.

---

## Bản 7.15

Tiêu đề gốc: `天堂经典版Bd 更新7.15` (Lineage Classic Bd – cập nhật 7.15)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `随游戏更新` | Cập nhật theo bản game mới | |
| 2 | `增加30级妖精自动学习大地防御技能` | Thêm: Elf (`妖精`) cấp 30 tự học kỹ năng `大地防御` (Phòng ngự Đất; có lẽ chính là kỹ năng `大地防護` = Bảo hộ Đất, "Earth Skin", tăng giáp, trong `BaseConfig.txt`) (?) | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.15 大中控EXE为5.25`: EXE mới nhất là `7.15`, EXE của `大中控` là `5.25`.

---

## Bản 7.12

Tiêu đề gốc: `天堂经典版Bd 更新7.12` (Lineage Classic Bd – cập nhật 7.12)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `\config\config.ini中增加 协议登录等待最大时间 的设置` | Thêm cài đặt `协议登录等待最大时间` (thời gian chờ tối đa khi đăng nhập bằng giao thức) vào file `\config\config.ini` | `协议登录` = đăng nhập bằng giao thức, không đi qua giao diện launcher. Nếu chờ quá thời gian này mà chưa vào được, bot sẽ coi là thất bại (?). Trong `config\config.ini` đi kèm gói, giá trị hiện là `协议登录等待最大时间=120`. Ngay dưới có `模拟登录等待最大时间=200`, là thời gian chờ tối đa cho kiểu đăng nhập mô phỏng. File không ghi đơn vị, có lẽ là **giây** (?). |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.12 大中控EXE为5.25`: EXE mới nhất là `7.12`, EXE của `大中控` là `5.25`.

---

## Bản 7.9

Tiêu đề gốc: `天堂经典版Bd 更新7.9` (Lineage Classic Bd – cập nhật 7.9)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `针对封号检测进行有效处理` | Đã "xử lý hiệu quả" đối với cơ chế phát hiện để khóa tài khoản (`封号检测`) | Đây là lời tác giả, không kèm chi tiết. Tài khoản dùng bot vẫn có thể bị khóa. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.9 大中控EXE为5.25`: EXE mới nhất là `7.9`, EXE của `大中控` là `5.25`.

---

## Bản 7.8.4

Tiêu đề gốc: `天堂经典版Bd 更新7.8.4` (Lineage Classic Bd – cập nhật 7.8.4)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复游戏进程cpu占用过高，替换版本需要重启电脑` | Sửa lỗi tiến trình game (`游戏进程`) chiếm CPU quá cao. Sau khi thay bản này **cần khởi động lại máy tính** | 💡 Nhớ khởi động lại máy sau khi thay. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.8.4 大中控EXE为5.25`: EXE mới nhất là `7.8.4`, EXE của `大中控` là `5.25`.

---

## Bản 7.8.2

Tiêu đề gốc: `天堂经典版Bd 更新7.8.2` (Lineage Classic Bd – cập nhật 7.8.2)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `随游戏更新` | Cập nhật theo bản game mới | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.8.2 大中控EXE为5.25`: EXE mới nhất là `7.8.2`, EXE của `大中控` là `5.25`.

---

## Bản 7.8.1

Tiêu đề gốc: `天堂经典版Bd 更新7.8.1` (Lineage Classic Bd – cập nhật 7.8.1)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `优化过检测` | Tối ưu khả năng vượt qua kiểm tra, phát hiện (`过检测`) | Đây là lời tác giả, không kèm chi tiết. |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.8.1 大中控EXE为5.25`: EXE mới nhất là `7.8.1`, EXE của `大中控` là `5.25`.

---

## Bản 7.8

Tiêu đề gốc: `天堂经典版Bd 更新7.8` (Lineage Classic Bd – cập nhật 7.8)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `随游戏更新` | Cập nhật theo bản game mới | |
| 2 | `修复世界树卡主随机传送后，无法回到打怪位置` | Sửa lỗi: bị kẹt ở Cây Thế giới (`世界树`), sau khi dịch chuyển ngẫu nhiên (`随机传送`) thì không quay lại được vị trí đánh quái | Chữ `卡主` trong file gốc là viết nhầm của `卡住` (bị kẹt). |
| 3 | `增加 古鲁丁7楼够买 對盔甲施法的卷軸 需要在BaseConfig.txt中设置` | Thêm: mua cuộn `對盔甲施法的卷軸` (cuộn phù phép giáp, Scroll of Enchant Armor) ở tầng 7 Gludin (`古鲁丁7楼`, Hầm ngục Gludin tầng 7). Cần bật trong `BaseConfig.txt` | Chữ `够买` là viết nhầm của `购买` (mua). Tên vật phẩm phải giữ đúng chữ phồn thể `對盔甲施法的卷軸`. Trong `BaseConfig.txt` hiện nay, công tắc này là `對盔甲施法的卷軸=`, nằm ở mục `[NPC特殊购买]` (mua đặc biệt từ NPC): `=1` là bật, `=0` là tắt (mặc định). |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.8 大中控EXE为5.25`: EXE mới nhất là `7.8`, EXE của `大中控` là `5.25`.

---

## Bản 7.4

Tiêu đề gốc: `天堂经典版Bd 更新7.4` (Lineage Classic Bd – cập nhật 7.4)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复有些机器cpu占用过高的问题（需要重启电脑）` | Sửa lỗi một số máy bị chiếm CPU quá cao (cần khởi động lại máy tính) | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.4 大中控EXE为5.25`: EXE mới nhất là `7.4`, EXE của `大中控` là `5.25`.

---

## Bản 7.3

Tiêu đề gốc: `天堂经典版Bd 更新7.3` (Lineage Classic Bd – cập nhật 7.3)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复定点挂机=1时 定不住的问题` | Sửa lỗi khi `定点挂机=1` (bật treo máy tại điểm cố định) mà nhân vật không đứng yên ở điểm đó | `=1` là bật, `=0` là tắt (treo máy di chuyển tự do). Theo chú thích trong `gj.txt`: `=1` nghĩa là đứng yên tại tọa độ đánh quái mà đánh. Mặc định là `0`. |
| 2 | `修复在地监路上不反击怪物的问题` | Sửa lỗi trên đường đi trong hầm ngục, bị quái đánh mà không phản công (`反击`) | |
| 3 | `增加支持新地图 夢幻之島 的挂机` | Hỗ trợ treo máy ở bản đồ mới `夢幻之島` (Đảo Mộng Ảo, "Island of Dreams") (?) | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE 需要替换lua`: cần thay EXE và cần thay Lua.
- `注：最新EXE为 7.3 大中控EXE为5.25`: EXE mới nhất là `7.3`, EXE của `大中控` là `5.25`.

---

## Bản 7.1.1

Tiêu đề gốc: `天堂经典版Bd 更新7.1.1` (Lineage Classic Bd – cập nhật 7.1.1)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `修复打怪发呆的问题` | Sửa lỗi đứng đơ khi đánh quái | |

**Ghi chú (`注`):**

- `注：更新需要替换EXE（版本是7.1可不换） 需要替换lua（可下载lua）`: cần thay EXE (đang dùng EXE `7.1` thì không cần thay) và cần thay Lua (có thể tải riêng Lua).
- `注：最新EXE为 7.1 大中控EXE为5.25`: EXE mới nhất là `7.1`, EXE của `大中控` là `5.25`.

---

*Hết file `更新说明.txt` (434 dòng, 51 phiên bản).*
