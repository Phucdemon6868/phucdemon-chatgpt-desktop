# Game_Config: chiến đấu, máu, buff, lọc quái và vật phẩm

> **Gói:** `天堂经典版 Bd` bản 9.16, bot treo máy (auto farm) cho Lineage Classic.
> **Phạm vi tài liệu này:** 9 file trong thư mục `Game_Config/`. Tất cả đều mã hóa UTF-8, xuống dòng kiểu Windows (CRLF).
>
> | File | Số dòng | Nội dung chính |
> |---|---|---|
> | [`ActivityConfig.txt`](#activityconfigtxt) | 27 | Tự tham gia sự kiện: Nữ hoàng Băng, đổi Trứng màu |
> | [`BloodConfig.txt`](#bloodconfigtxt) | 43 | Huyết minh (clan): tự xin vào clan, gửi vàng/đồ vào kho clan |
> | [`BloodStorage.txt`](#bloodstoragetxt) | 19 | Danh sách vật phẩm gửi vào kho huyết minh |
> | [`BloodTakeOutTheItem.txt`](#bloodtakeouttheitemtxt) | 23 | Tự lấy vật phẩm từ kho huyết minh khi thiếu |
> | [`Buff.txt`](#bufftxt) | 85 | Acc chính (Hoàng tộc/Hiệp sĩ) buff `加速術` (Haste) cho acc phụ |
> | [`CounterattackPeoples.txt`](#counterattackpeoplestxt) | 88 | Danh sách người chơi cần phản công/tấn công (PvP) |
> | [`Deleteitem.txt`](#deleteitemtxt) | 3 | Vật phẩm cần xóa khỏi túi |
> | [`G_Filtering_Monster_And_Item.txt`](#g_filtering_monster_and_itemtxt) | 62 | Lọc quái, quái phản công, lọc nhặt đồ (toàn cục) |
> | [`UseItems.txt`](#useitemstxt) | 11 | Tự mở/dùng vật phẩm (hộp, rương) theo chu kỳ |

## ⚠️ Quy tắc chung khi sửa các file này

1. **Giữ nguyên mọi chữ Trung Quốc.** Bot đọc chữ đúng từng ký tự: tên mục `[...]`, tên khóa (bên trái dấu `=`), tên server, tên bản đồ, vật phẩm, quái, kỹ năng, NPC. Khi sửa, **chỉ thay số/giá trị**. Phần tiếng Việt trong tài liệu chỉ để bạn hiểu, **đừng** gõ tiếng Việt vào file.
2. Dòng bắt đầu bằng `--` là **chú thích** (bot bỏ qua). Trên một dòng `khóa=giá trị    -- ...`, phần sau `--` cũng là chú thích.
3. File trộn chữ **Phồn thể** và **Giản thể**. Chép **y nguyên** như trong file/trong game, không tự chuyển đổi.
4. Danh sách nhiều giá trị dùng **dấu phẩy tiếng Anh** `,`. Dấu `|` ngăn cách các khung giờ.
5. 💡 Lưu file lại ở mã hóa **UTF-8** như bản gốc, nếu không chữ Trung sẽ bị hỏng và bot không đọc được.

**Quy ước:** `=0` thường là **tắt**, `=1` là **bật** (trừ khi file ghi khác). `秒` = giây, `分钟` = phút.
Cột **#** là số dòng trong file gốc. Dấu `\|` trong bảng chính là ký tự `|` trong file (viết vậy để bảng không bị vỡ). Các dòng trống trong file gốc không được liệt kê.

**Từ dùng chung trong các file này:**

| Gốc | Nghĩa |
|---|---|
| `血盟` | Huyết minh (Blood Pledge), tức **clan/bang hội** trong Lineage |
| `区服` / `大区服务器` / `服务器` | Server (máy chủ). "大区" = "đại khu" |
| `主号` / `小号` | Acc chính / acc phụ (tài khoản hoặc nhân vật phụ) |
| `中控` | Trung tâm điều khiển (central control), tức chương trình điều phối nhiều máy/tài khoản; chính là `大中控` (nhật ký cập nhật gọi tắt là `中控`, xem `02-nhat-ky-cap-nhat.md`) |
| `回城` | Về thành (về làng) |
| `背包` | Túi đồ |
| `村庄` / `村` | Làng |
| `触发` | Kích hoạt |
| `张三111`, `李四111` | Tên mẫu (giống "Nguyễn Văn A", "Trần Văn B" ở Việt Nam). Thay bằng tên nhân vật thật của bạn. |

**Danh sách tên server** (xuất hiện trong `BloodConfig.txt`, `Buff.txt`, `CounterattackPeoples.txt`). Server Lineage Classic được đặt theo tên thần thoại Hy Lạp:

| Gốc | Nghĩa |
|---|---|
| `太陽神阿波羅` | Thần Mặt Trời Apollo |
| `愛神邱比特` | Thần Tình yêu Cupid |
| `勝利女神雅典娜` | Nữ thần Chiến thắng Athena |
| `美神維納斯` | Nữ thần Sắc đẹp Venus |
| `天神宙斯` | Thần Zeus |
| `天后海拉` | Thiên hậu Hera |
| `戰神馬爾斯` | Thần Chiến tranh Mars |
| `月亮女神阿緹蜜斯` | Nữ thần Mặt Trăng Artemis |
| `海神波塞頓` | Thần Biển Poseidon |
| `冥王黑帝斯` | Diêm vương Hades |
| `火神赫發斯特斯` | Thần Lửa Hephaestus |
| `收穫女神帝蜜特` | Nữ thần Mùa màng Demeter |
| `蛇髮女墨杜沙` | Nữ yêu tóc rắn Medusa |
| `半人馬涅索斯` | Nhân mã Nessus |
| `牛人彌諾陶洛斯` | Người bò Minotaur |
| `牛人彌諾陶洛斯2` | Người bò Minotaur 2 (server thứ hai cùng tên) |
| `俄雷恩` | Orion (?) (phiên âm; không phải làng Oren `歐瑞`) |
| `獨眼巨人庫克羅普斯` | Khổng lồ một mắt Cyclops |
| `獅子涅墨亞` | Sư tử Nemea |
| `飛馬珀伽索斯` | Ngựa bay Pegasus |
| `水蛇許德拉` | Rắn nước Hydra |
| `公牛克里特` | Bò mộng xứ Crete |
| `女妖塞壬` | Nữ yêu Siren |
| `巨龍拉冬` | Rồng khổng lồ Ladon |
| `百眼怪阿爾戈斯` | Quái vật trăm mắt Argus |
| `大地之神蓋亞` | Thần Đất Gaia |
| `泰坦女神瑞亞 non-pvp` | Nữ thần Titan Rhea (server **non-PvP**, không PK được) |
| `水蛇許德拉 non-pvp` | Rắn nước Hydra (server **non-PvP**) |

---

## ActivityConfig.txt

**File này điều khiển gì:** cho bot **tự tham gia sự kiện** (`活动` = event) trong game:

- `[冰之女王活动]`: sự kiện **Nữ hoàng Băng** (Ice Queen). Trong các khung giờ bạn đặt, bot tự đi vào bản đồ sự kiện, đứng ở tọa độ chờ boss xuất hiện rồi đánh.
- `[彩蛋活动]`: sự kiện **Trứng màu** (Easter Egg). Khi nhân vật về thành, nếu đủ số trứng, bot tự đổi trứng lấy các vật phẩm "Hoạt lực" (`活力`).

**Khi nào bot dùng:** sự kiện Nữ hoàng Băng chạy theo **đồng hồ máy tính**. Sự kiện Trứng màu chạy **mỗi lần nhân vật về thành**.

> Nhắc lại: giữ nguyên chữ Trung (tên mục, tên khóa, tên vật phẩm, tên làng). Chỉ đổi số/giá trị.

### `[冰之女王活动]`: Sự kiện Nữ hoàng Băng

Chú thích đầu mục:

| # | Dòng gốc | Dịch |
|---|---|---|
| 1 | `[冰之女王活动]` | [Sự kiện Nữ hoàng Băng] (`冰之女王` = Nữ hoàng Băng, Ice Queen) |
| 2 | `--调整好本机的时间，时间段需要自己设置实际的时间` | "Hãy chỉnh đúng giờ của máy tính này. Các khung giờ phải tự đặt theo giờ thực tế (của sự kiện)." |
| 3 | `-- 最好提前進入占位，太遲進入人頭太多不好打怪，会被阻碍` | "Tốt nhất nên vào sớm để giữ chỗ. Vào quá muộn thì đông người, khó đánh quái, sẽ bị cản đường." |

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 4 | `开启=0` | Bật sự kiện | `=0` tắt (mặc định), `=1` bật. File không ghi chú, đây là quy ước chung của bot. |
| 5 | `时间段=10:35-11:10\|14:35-15:10\|18:35-19:10\|20:35-21:10` | Khung giờ | Mặc định có 4 khung giờ, ngăn cách bằng `\|`. Mỗi khung có dạng `giờ bắt đầu-giờ kết thúc`. Chú thích gốc: "`10:50-11:10` nghĩa là giờ bắt đầu - giờ kết thúc của khung giờ; trong khoảng đó sẽ kích hoạt." (Ví dụ 10:50 trong chú thích chỉ để minh họa, khác với giá trị 10:35 thật.) |
| 6 | `首选村庄=` | Làng ưu tiên (lối vào sự kiện) | Chú thích gốc: "Để trống thì vào ngẫu nhiên. Nếu điền thì vào theo lối vào bạn đặt **[phải là 1 trong 4 lối vào được hỗ trợ]**. Tự đặt theo định dạng: `tên bản đồ,tọa độ x,tọa độ y`. Ví dụ: `首选村庄=奇岩村,33440,32792`". `奇岩村` = làng Giran (`奇岩`). Mặc định để trống (= ngẫu nhiên). |
| 7 | `Boss坐标=32768,32895` | Tọa độ chờ boss | Chú thích gốc: "Tọa độ đứng chờ Nữ hoàng Băng (`冰之女王`) xuất hiện sau khi vào bản đồ. Nếu để trống thì mặc định dùng tọa độ điểm trung tâm có sẵn `32768,32895`." |

Dòng 5 nguyên văn (kèm chú thích gốc):

```
时间段=10:35-11:10|14:35-15:10|18:35-19:10|20:35-21:10    --10:50-11:10表述这个时间段的开始时间-结束时间内会触发
```

💡 **Lưu ý:**
- Giờ ở đây là **giờ trên máy tính chạy bot**. Nếu múi giờ máy bạn khác múi giờ server (Việt Nam UTC+7, Đài Loan UTC+8, Hàn Quốc UTC+9) thì phải tự quy đổi giờ, hoặc chỉnh giờ máy như chú thích dòng 2 gợi ý.
- Theo chú thích dòng 3, nên để giờ bắt đầu **sớm hơn** giờ boss xuất hiện một chút để nhân vật vào giữ chỗ.
- Muốn thêm hoặc bớt khung giờ thì thêm/bớt đoạn `HH:MM-HH:MM` và ngăn cách bằng `|`.

### `[彩蛋活动]`: Sự kiện Trứng màu

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 14 | `[彩蛋活动]` | [Sự kiện Trứng màu] | `彩蛋` = trứng màu (Easter egg). |
| 15 | `兑换触发总数=0` | Tổng số trứng để kích hoạt đổi | Chú thích gốc: "Khi nhân vật thực hiện về thành: đặt 50 → khi số trứng màu đạt 50 quả thì kích hoạt (đổi)." `=0` có lẽ là không đổi (tắt) (suy luận, file không ghi rõ). |
| 16 | `活力紅色藥水=0` | Thuốc đỏ Hoạt lực (Vitality Red Potion, thuốc hồi máu) | Chú thích gốc: "Lớn hơn 0, ví dụ `=50`, là số lượng muốn đổi vật phẩm này: nếu trong túi đã có 50 cái thì không đổi nữa." Tức là con số là **mức muốn giữ trong túi**. `=0` = không đổi món này. Quy tắc này áp dụng cho mọi dòng vật phẩm bên dưới. |
| 17 | `活力自我加速藥水=0` | Thuốc tự tăng tốc Hoạt lực (Vitality Haste Potion) | Như dòng 16. |
| 18 | `活力瞬間移動卷軸=0` | Cuộn dịch chuyển tức thời Hoạt lực (Teleport Scroll) | Như dòng 16. |
| 19 | `活力返回卷軸=0` | Cuộn trở về Hoạt lực (Return Scroll, cuộn về thành) | Như dòng 16. |
| 20 | `活力變形卷軸=0` | Cuộn biến hình Hoạt lực (Polymorph Scroll) | Như dòng 16. |
| 21 | `活力勇敢藥水=0` | Thuốc Dũng cảm Hoạt lực (Brave Potion) | Như dòng 16. |
| 22 | `活力精靈餅乾=0` | Bánh quy Tiên Hoạt lực (Elven Wafer) | Như dòng 16. |
| 23 | `活力慎重藥水=0` | Thuốc Thận trọng Hoạt lực (Wisdom Potion) | Như dòng 16. |
| 24 | `活力惡魔之血=0` | Máu Ác quỷ Hoạt lực (Devil's Blood) | Như dòng 16. |
| 25 | `活力藍色藥水=0` | Thuốc xanh lam Hoạt lực (Blue Potion, hồi mana) | Như dòng 16. |
| 26 | `產下黃金蛋的貝雷帽=0` | Mũ nồi đẻ trứng vàng (Beret that lays golden eggs) | Như dòng 16. |
| 27 | `產下黃金蛋的草帽=0` | Mũ rơm đẻ trứng vàng (Straw hat that lays golden eggs) | Như dòng 16. |

💡 **Lưu ý:** muốn dùng tính năng này phải đặt **cả hai**: `兑换触发总数` lớn hơn 0 **và** ít nhất một vật phẩm lớn hơn 0. Ví dụ `兑换触发总数=50` và `活力紅色藥水=100`: mỗi lần về thành mà có từ 50 trứng trở lên, bot sẽ đổi thuốc đỏ cho tới khi túi có 100 bình.

---

## BloodConfig.txt

**File này điều khiển gì:** chức năng **huyết minh** (`血盟` = Blood Pledge, tức clan/bang hội): tự xin vào clan theo từng server, tự gửi vàng và vật phẩm vào **kho clan** khi vàng trong túi đạt mức đặt sẵn.

**Khi nào bot dùng:** khi nhân vật chưa có clan (tự xin vào), và khi vàng trong túi chạm ngưỡng (về làng có kho để gửi). Danh sách vật phẩm được gửi nằm trong `BloodStorage.txt`.

> Nhắc lại: giữ nguyên chữ Trung (tên khóa, tên server, tên làng). Chỉ đổi số/giá trị và tên clan của bạn.

**Chú thích đầu file:**

| # | Dòng gốc | Dịch |
|---|---|---|
| 1 | `--自动血盟加入=1  角色会自动加入你对应的服务器的血盟，如果是多个可以 太陽神阿波羅=血盟名字1,血盟名字2` | "`自动血盟加入=1`: nhân vật sẽ tự gia nhập huyết minh của server tương ứng. Nếu có nhiều clan thì viết, ví dụ: `太陽神阿波羅=血盟名字1,血盟名字2`" (`血盟名字1` = "tên huyết minh 1"). |
| 2 | `--如果这个服务器有多个血盟，角色会随机加入一个` | "Nếu server này có nhiều huyết minh (trong danh sách), nhân vật sẽ vào ngẫu nhiên một cái." |
| 3 | `--当达到触发存入血盟金币时，会存入金币的同时也会存入物品` | "Khi đạt điều kiện kích hoạt gửi vàng vào huyết minh, bot gửi vàng đồng thời gửi luôn vật phẩm." |
| 4 | `--存入间隔的设定是为了人多时，都挤在一起排队存入的时候，就不要在存了，间隔一段时间在过来` | "Cài đặt khoảng cách gửi là để khi đông người chen nhau xếp hàng gửi thì thôi đừng gửi nữa, đợi một khoảng thời gian rồi quay lại." |

### `[config]`: Cấu hình

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 6 | `[config]` | Mục cấu hình | |
| 7 | `达到金币触发存仓=0` | Đạt số vàng thì kích hoạt gửi kho | Chú thích gốc: "`=0` nghĩa là không tự gửi vật phẩm vào huyết minh; khác 0 thì khi đạt số lượng sẽ kích hoạt." Con số là **số vàng** trong túi. Ví dụ `=500000`: khi có 500.000 vàng, bot về làng gửi. Mặc định `0` = tắt. |
| 8 | `保留金币=1000` | Vàng giữ lại | Chú thích gốc: "Số vàng giữ lại trong túi sau khi gửi." Mặc định 1000 (để còn tiền mua thuốc, cuộn...). |
| 9 | `自动血盟加入=1` | Tự gia nhập huyết minh | Chú thích gốc: "`=0` không tự vào huyết minh, `=1` tự vào huyết minh." Mặc định bật. Tên clan lấy ở mục `[血盟加入]` bên dưới. |
| 10 | `自动存入物品=1` | Tự gửi vật phẩm | Chú thích gốc: "`=0` không gửi vật phẩm; `=1` khi vàng đạt điều kiện gửi thì gửi luôn vật phẩm." Danh sách vật phẩm ở `BloodStorage.txt`. |
| 11 | `存入失败间隔=2` | Khoảng chờ khi gửi thất bại | Chú thích gốc: "`=0` gửi liên tục cho tới khi thành công. Nếu khác 0, khi gửi thất bại, ví dụ `=60`, thì cách 60 phút mới quay lại gửi." Đơn vị: **phút**. Mặc định 2 phút. |
| 12 | `仓库位置=說話之島村,古魯丁村` | Vị trí kho | Chú thích gốc: "Có thể là 1 làng hoặc nhiều làng (chọn ngẫu nhiên kho của một làng để gửi)." `說話之島村` = làng Talking Island (Đảo Nói Chuyện), `古魯丁村` = làng Gludin. |

💡 **Lưu ý:** dòng 7 là "công tắc chính" của việc gửi **vàng** vào kho. Để `0` thì `保留金币`, `自动存入物品`, `存入失败间隔` gần như không có tác dụng, trừ khi một vật phẩm trong `BloodStorage.txt` có ngưỡng `=số` riêng (ngưỡng đó tự kích hoạt về thành gửi đồ, xem phần `BloodStorage.txt`) (?). Nhân vật phải **đã ở trong clan** thì mới gửi được.

### `[血盟加入]`: Gia nhập huyết minh (theo server)

Mỗi dòng có dạng `tên server=tên clan 1,tên clan 2,...`. Bot xem nhân vật đang ở server nào và xin vào (ngẫu nhiên) một clan trong danh sách của server đó. Để trống sau dấu `=` thì không xin vào clan nào ở server đó.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 16 | `[血盟加入]` | [Gia nhập huyết minh] | |
| 17 | `太陽神阿波羅=血盟名字1,血盟名字2,血盟名字3` | Server Thần Mặt Trời Apollo | Giá trị mẫu: `血盟名字1`, `血盟名字2`, `血盟名字3` = "tên huyết minh 1, 2, 3". Thay bằng tên clan thật. |
| 18 | `愛神邱比特=` | Server Thần Tình yêu Cupid | Trống |
| 19 | `勝利女神雅典娜=` | Server Nữ thần Chiến thắng Athena | Trống |
| 20 | `美神維納斯=` | Server Nữ thần Sắc đẹp Venus | Trống |
| 21 | `天神宙斯=` | Server Thần Zeus | Trống |
| 22 | `天后海拉=` | Server Thiên hậu Hera | Trống |
| 23 | `戰神馬爾斯=` | Server Thần Chiến tranh Mars | Trống |
| 24 | `月亮女神阿緹蜜斯=血盟名字1` | Server Nữ thần Mặt Trăng Artemis | Giá trị mẫu: `血盟名字1` = "tên huyết minh 1". |
| 25 | `海神波塞頓=` | Server Thần Biển Poseidon | Trống |
| 26 | `冥王黑帝斯=` | Server Diêm vương Hades | Trống |
| 27 | `火神赫發斯特斯=` | Server Thần Lửa Hephaestus | Trống |
| 28 | `收穫女神帝蜜特=` | Server Nữ thần Mùa màng Demeter | Trống |
| 29 | `蛇髮女墨杜沙=` | Server Nữ yêu tóc rắn Medusa | Trống |
| 30 | `半人馬涅索斯=` | Server Nhân mã Nessus | Trống |
| 31 | `牛人彌諾陶洛斯=` | Server Người bò Minotaur | Trống |
| 32 | `俄雷恩=` | Server Orion (?) | Trống |
| 33 | `獨眼巨人庫克羅普斯=` | Server Khổng lồ một mắt Cyclops | Trống |
| 34 | `獅子涅墨亞=` | Server Sư tử Nemea | Trống |
| 35 | `飛馬珀伽索斯=` | Server Ngựa bay Pegasus | Trống |
| 36 | `水蛇許德拉=` | Server Rắn nước Hydra | Trống |
| 37 | `公牛克里特=` | Server Bò mộng xứ Crete | Trống |
| 38 | `女妖塞壬=` | Server Nữ yêu Siren | Trống |
| 39 | `巨龍拉冬=` | Server Rồng khổng lồ Ladon | Trống |
| 40 | `百眼怪阿爾戈斯=` | Server Quái vật trăm mắt Argus | Trống |
| 41 | `大地之神蓋亞=` | Server Thần Đất Gaia | Trống |

💡 **Lưu ý:** danh sách này **không có** `牛人彌諾陶洛斯2`, `泰坦女神瑞亞 non-pvp`, `水蛇許德拉 non-pvp` (khác với `Buff.txt` và `CounterattackPeoples.txt`). Nếu bạn chơi ở các server đó và muốn tự vào clan, có lẽ phải tự thêm một dòng với **đúng tên server** như trong danh sách server của bot (?).

---

## BloodStorage.txt

**File này điều khiển gì:** danh sách **vật phẩm được gửi vào kho huyết minh** (kho clan). Đây là file đi kèm `BloodConfig.txt`.

**Khi nào bot dùng:** khi bot về làng gửi đồ vào kho clan (do vàng đạt ngưỡng trong `BloodConfig.txt` với `自动存入物品=1`), hoặc khi số lượng một vật phẩm có ghi `=số` trong túi đạt ngưỡng đó.

> Nhắc lại: giữ nguyên chữ Trung (tên vật phẩm phải đúng như trong game). Chỉ đổi số.

| # | Dòng gốc | Dịch |
|---|---|---|
| 1 | `--此文件为血盟存入的物品配置   物品名=0  等号后面填入数量代表背包达到数量触发回城存入物品` | "File này cấu hình vật phẩm gửi vào kho huyết minh. Dạng `物品名=0` (`物品名` = tên vật phẩm): số sau dấu `=` là số lượng; khi túi đạt số lượng đó thì kích hoạt về thành gửi đồ." |

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 2 | `金屬塊=0` | Khối kim loại (Metal block) | Dòng duy nhất có `=số`. `=0` có lẽ là không dùng món này để kích hoạt về thành (?), chỉ gửi kèm. |
| 3 | `復活卷軸` | Cuộn hồi sinh (Scroll of Resurrection) | Chỉ có tên, không có `=số`. |
| 4 | `強化自我加速藥水` | Thuốc tự tăng tốc cường hóa (Greater Haste Potion) | Chỉ có tên. |
| 5 | `對盔甲施法的卷軸` | Cuộn phù phép giáp (Scroll of Enchant Armor) | Chỉ có tên. |
| 6 | `對武器施法的卷軸` | Cuộn phù phép vũ khí (Scroll of Enchant Weapon) | Chỉ có tên. |
| 7 | `武器強化卷軸` | Cuộn cường hóa vũ khí | Chỉ có tên. Là một loại cuộn khác với dòng 6 (tên khác trong game). |
| 8 | `防具強化卷軸` | Cuộn cường hóa giáp | Chỉ có tên. |
| 9 | `祝福武器強化卷軸` | Cuộn cường hóa vũ khí được ban phước (Blessed) | Chỉ có tên. |
| 10 | `祝福防具強化卷軸` | Cuộn cường hóa giáp được ban phước | Chỉ có tên. |
| 11 | `歐琳飾品強化卷軸` | Cuộn cường hóa trang sức Orim (?) | Chỉ có tên. `歐琳` phiên âm là "Âu Lâm", có lẽ là Orim (?). `飾品` = trang sức (phụ kiện). |
| 12 | `祝福歐琳飾品強化卷軸` | Cuộn cường hóa trang sức Orim được ban phước (?) | Chỉ có tên. |
| 13 | `倫提斯耳環強化卷軸` | Cuộn cường hóa bông tai Roomtis (?) | Chỉ có tên. `倫提斯` phiên âm "Luân Đề Tư", có lẽ là bông tai Roomtis (?). `耳環` = bông tai. |
| 14 | `倫提斯安全強化卷軸` | Cuộn cường hóa an toàn Roomtis (?) | Chỉ có tên. `安全強化` = cường hóa an toàn (thường là thất bại không mất đồ). |
| 15 | `倫提斯墜飾安全強化卷軸` | Cuộn cường hóa an toàn mặt dây chuyền Roomtis (?) | Chỉ có tên. `墜飾` = mặt dây chuyền. |
| 16 | `斯奈普強化卷軸` | Cuộn cường hóa Snapper (?) | Chỉ có tên. `斯奈普` phiên âm "Tư Nại Phổ", có lẽ là nhẫn Snapper (?). |
| 17 | `斯奈普安全強化卷軸` | Cuộn cường hóa an toàn Snapper (?) | Chỉ có tên. |
| 18 | `蛇夫座強化卷軸` | Cuộn cường hóa Xà Phu (Ophiuchus) | Chỉ có tên. `蛇夫座` = chòm sao Xà Phu. |
| 19 | `覺醒徽章強化卷` | Cuộn cường hóa Huy hiệu Thức tỉnh (Awakening Badge) | Chỉ có tên. Lưu ý tên kết thúc bằng `卷` (không phải `卷軸`), giữ đúng như vậy. |

💡 **Lưu ý:**
- Các dòng chỉ có tên (không có `=số`): có lẽ bot vẫn gửi vào kho mỗi khi đi gửi đồ, nhưng bản thân chúng không kích hoạt việc về thành (?).
- Muốn một vật phẩm **tự kích hoạt** về thành gửi đồ, thêm `=số` theo chú thích dòng 1, ví dụ `復活卷軸=20` (có 20 cuộn trong túi thì về gửi).
- Tên vật phẩm phải khớp **từng ký tự** với tên trong game (chữ phồn thể).

---

## BloodTakeOutTheItem.txt

**File này điều khiển gì:** tự **lấy vật phẩm từ kho huyết minh** khi túi thiếu. Ví dụ bạn gửi sẵn nhiều cuộn/thuốc vào kho clan, acc phụ hết thì tự đến lấy một phần.

**Khi nào bot dùng:** khi nhân vật **đang ở làng** (hoặc ngay khi dùng hết, nếu trường cuối `C` = `1`, xem bảng 4 trường bên dưới), và phải **có clan**.

> Nhắc lại: giữ nguyên chữ Trung (tên vật phẩm). Chỉ đổi các con số.

**Chú thích đầu file:**

| # | Dòng gốc | Dịch |
|---|---|---|
| 1 | `--此文件为 血盟自动取物品触发文件（角色在村庄才触发，必须保证有血盟），少于指定数量，取出设置数量` | "File này là file kích hoạt tự lấy đồ từ huyết minh (chỉ kích hoạt khi nhân vật ở làng, phải đảm bảo có huyết minh). Khi ít hơn số lượng chỉ định thì lấy ra số lượng đã đặt." |
| 2 | `--你可以在血盟存入大量物品，小号缺少时，会自动取出一部分` | "Bạn có thể gửi nhiều vật phẩm vào kho huyết minh; khi acc phụ thiếu, bot tự lấy ra một phần." |
| 3 | `--格式为  物品名字=取出数量=达到数量触发取出=用完马上触发（=1触发 =0在村庄才触发）` | "Định dạng: `tên vật phẩm=số lượng lấy ra=số lượng kích hoạt lấy=hết là kích hoạt ngay` (`=1` kích hoạt ngay, `=0` chỉ kích hoạt khi ở làng)." |
| 5 | `--比如  瞬間移動卷軸=10=0=1 最后面填1表示用完马上触发   不填或者填0表示角色在村庄才触发` | "Ví dụ `瞬間移動卷軸=10=0=1`: số cuối là 1 nghĩa là dùng hết thì kích hoạt ngay. Không điền hoặc điền 0 nghĩa là chỉ kích hoạt khi nhân vật ở làng." |
| 6 | `--比如  瞬間移動卷軸=10=0=0 最后面填0表示角色在村庄才触发` | "Ví dụ `瞬間移動卷軸=10=0=0`: số cuối là 0 nghĩa là chỉ kích hoạt khi nhân vật ở làng." |
| 8 | `--注意 瞬間移動卷軸  这个一定要设置在村庄才触发，要不然，传送过去结果没了，又触发回来取` | "**Chú ý:** `瞬間移動卷軸` nhất định phải đặt là chỉ kích hoạt khi ở làng. Nếu không thì dịch chuyển đi tới khi hết cuộn, lại kích hoạt quay về lấy (lặp đi lặp lại)." |
| 11 | `--比如  瞬間移動卷軸=10=0  表示 背包中数量=0时触发血盟取物品 在血盟取出10个` | "Ví dụ `瞬間移動卷軸=10=0`: khi số lượng trong túi = 0 thì kích hoạt lấy đồ từ huyết minh, lấy ra 10 cái." |
| 12 | `--比如  瞬間移動卷軸=10=-1 表示 不用此物品触发    但是取其他物品时 顺便取出10个` | "Ví dụ `瞬間移動卷軸=10=-1`: không dùng vật phẩm này để kích hoạt, nhưng khi đi lấy vật phẩm khác thì lấy luôn 10 cái." |
| 13 | `--比如  治癒藥水=0=0   不会取出此物品（因为你的取出数量为0）` | "Ví dụ `治癒藥水=0=0`: sẽ không lấy vật phẩm này (vì số lượng lấy ra là 0)." |
| 14 | `--比如  解毒藥水=0=-1  不会取出此物品（因为你的取出数量为0）` | "Ví dụ `解毒藥水=0=-1`: sẽ không lấy vật phẩm này (vì số lượng lấy ra là 0)." |

**Giải thích 4 trường** của `tên=A=B=C`:

| Trường | Ý nghĩa | Giá trị |
|---|---|---|
| `A` (`取出数量`) | Số lượng lấy ra mỗi lần | `0` = không bao giờ lấy món này |
| `B` (`达到数量触发取出`) | Khi số lượng trong túi xuống tới mức này thì kích hoạt đi lấy | `0` = hết sạch mới đi lấy; `-1` = món này không tự kích hoạt, chỉ được lấy kèm khi đi lấy món khác |
| `C` (`用完马上触发`, tùy chọn) | Kích hoạt ngay hay chỉ khi ở làng | `1` = hết là đi lấy ngay; `0` hoặc bỏ trống = chỉ khi ở làng |

**Các dòng cấu hình:**

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 16 | `瞬間移動卷軸=0=-1` | Cuộn dịch chuyển tức thời (Scroll of Teleportation, dịch chuyển ngẫu nhiên) | Lấy 0 cái, không tự kích hoạt → hiện **không lấy**. |
| 17 | `治癒藥水=0=0` | Thuốc trị liệu (Healing Potion) | Lấy 0 cái → hiện **không lấy** (dù hết sạch). |
| 18 | `安特的樹枝=0=-1` | Cành cây của Ent (Ent's Branch) | Hiện không lấy. `安特` = Ent (người cây). |
| 19 | `解毒藥水=0=-1` | Thuốc giải độc (Cure Poison Potion) | Hiện không lấy. |
| 20 | `翡翠藥水=0=-1` | Thuốc Phỉ thúy (Emerald Potion) (?) | Hiện không lấy. |
| 21 | `活力自我加速藥水=0=-1` | Thuốc tự tăng tốc Hoạt lực (Vitality Haste Potion) | Hiện không lấy. |
| 22 | `自我加速藥水=0=-1` | Thuốc tự tăng tốc (Haste Potion) | Hiện không lấy. |
| 23 | `強化自我加速藥水=0=-1` | Thuốc tự tăng tốc cường hóa (Greater Haste Potion) | Hiện không lấy. |

💡 **Lưu ý:**
- Mặc định **mọi dòng đều có số lượng lấy = 0**, nên chức năng này coi như tắt. Muốn dùng, sửa **số đầu tiên** (A). Ví dụ `治癒藥水=50=0`: hết thuốc trị liệu thì (khi ở làng) lấy 50 bình.
- Với `瞬間移動卷軸`, đừng đặt `C=1` (xem chú thích dòng 8).
- Bot chỉ lấy được món mà kho clan **đang có**. Hãy gửi sẵn vào kho clan bằng acc chính.

---

## Buff.txt

**File này điều khiển gì:** cho nhân vật **Hoàng tộc** (`王族`) hoặc **Hiệp sĩ** (`骑士`) đội **mũ Nhanh nhẹn** (`敏捷头盔`) làm "acc chính buff", đứng ở một chỗ cố định và **buff kỹ năng `加速術` (Haste, tăng tốc)** cho các acc phụ Elf (`妖精`). Acc phụ tự chạy đến tọa độ để nhận buff.

**Khi nào bot dùng:** khi `开启=1` hoặc `开启=2`. Acc chính buff đứng chờ ở tọa độ; acc phụ khi cần buff (hoặc khi mất buff, nếu bật `小号buff消失回城`) thì đến tọa độ đó.

> Nhắc lại: giữ nguyên chữ Trung (tên khóa, tên server, tên bản đồ, tên kỹ năng). Chỉ đổi số và tên nhân vật.

**Phần giới thiệu đầu file** (các dòng này **không có** `--` nhưng nằm trước mục `[config]`, nên có lẽ bot bỏ qua và chúng chỉ là chữ mô tả (?)):

| # | Dòng gốc | Dịch |
|---|---|---|
| 1 | `此文件为王族或者骑士带有敏捷头盔，为妖精加buff配置` | "File này là cấu hình để Hoàng tộc (`王族`) hoặc Hiệp sĩ (`骑士`) có đội mũ Nhanh nhẹn (`敏捷头盔`) buff cho Elf (`妖精`)." |
| 2 | `区服下面填名字，代表优先会为区服下面的名字角色添加buff，如果没有，则为 全局小号列表 的名字角色添加buff` | "Điền tên dưới mục server nghĩa là ưu tiên buff cho các nhân vật có tên dưới server đó. Nếu không có thì buff cho các nhân vật có tên trong `全局小号列表` (danh sách acc phụ toàn cục)." |
| 3 | `如果你无视区服，直接删除下面所有区服下面的名字，只保留 全局小号列表 下面的名字` | "Nếu bạn không quan tâm server thì xóa hết các tên dưới mọi mục server, chỉ giữ tên dưới `全局小号列表`." |
| 4 | `当你设置 开启=1 时，如果你的角色名字在 加buff主号角色名 之中，那么这个角色就会视为有加速术技能的buff主号` | "Khi đặt `开启=1`, nếu tên nhân vật của bạn nằm trong `加buff主号角色名` thì nhân vật đó được coi là acc chính buff, có kỹ năng `加速术` (Haste)." |
| 5 | `当你设置 开启=2 时，加buff主号与小号，不需要填入小号列表，以及区服下面不需要填入名字` | "Khi đặt `开启=2`, acc chính buff và acc phụ không cần điền vào danh sách acc phụ, cũng không cần điền tên dưới các mục server." |
| 6 | `此模式必须连接中控，当buff主号与小号连接中控后，中控会自动分配其中1个小号过来，加完后在通知另外1个小号过来` | "Chế độ này bắt buộc kết nối trung tâm điều khiển (`中控`). Khi acc chính buff và acc phụ đã kết nối `中控`, `中控` tự cử 1 acc phụ tới; buff xong lại báo 1 acc phụ khác tới." |
| 7 | `可以同时存在多个加buff主号与中控连接，不同的加buff主号会与连接中控的小号一对一进行加buff` | "Có thể có nhiều acc chính buff cùng kết nối `中控`. Mỗi acc chính buff sẽ buff 1-đối-1 cho các acc phụ đang kết nối `中控`." |
| 9 | `小号buff消失回城 当 加速術 状态消失时回城` | "`小号buff消失回城` (acc phụ mất buff thì về thành): khi trạng thái `加速術` biến mất thì về thành." |
| 10 | `支持的技能   加速術 等等` | "Kỹ năng hỗ trợ: `加速術` (Haste) v.v." |
| 11 | `-------------------------------------------------` | Đường kẻ trang trí. |

### `[config]`: Cấu hình

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 12 | `[config]` | Mục cấu hình | |
| 13 | `开启=0` | Bật chức năng buff | Chú thích gốc: "`=0` tắt, `=1` bật, `=2` dùng `中控` cử acc phụ tới; không cần điền tên vào danh sách acc phụ và danh sách server, `中控` tự phân ai tới." Mặc định `0` (tắt). |
| 14 | `地图=說話之島` | Bản đồ buff | Bản đồ nơi acc chính buff đứng. `說話之島` = Talking Island (Đảo Nói Chuyện). |
| 15 | `坐标=32524,32827` | Tọa độ buff | Tọa độ `x,y` trên bản đồ trên, nơi acc chính đứng và acc phụ chạy tới. |
| 16 | `小号buff消失回城=0` | Acc phụ mất buff thì về thành | Chú thích gốc: "`=1` nghĩa là khi trạng thái `加速術` biến mất" (thì về thành để đi nhận buff). `=0` = tắt. |
| 17 | `小号buff消失间隔过来时间=1200` | Thời gian chờ trước khi acc phụ quay lại | Chú thích gốc: "Đơn vị = giây. 1800 = 30 phút, 3600 = 60 phút. Khi `开启=1`, nếu acc phụ tới tọa độ mà không thấy acc buff ở đó thì lần sau phải cách khoảng thời gian này mới tới lại." Mặc định 1200 giây = 20 phút. |
| 18 | `小号加buff停留时间=10` | Thời gian acc phụ đứng chờ buff | Chú thích gốc: "Đơn vị = giây." Acc phụ đứng ở tọa độ 10 giây để nhận buff. |
| 20 | `加buff主号没蓝回旅馆=1` | Acc chính buff hết mana thì về nhà trọ | Dòng này **không có chú thích** trong file; giải thích theo tên khóa: `=1` bật (mặc định): hết MP (`没蓝` = hết mana) thì về nhà trọ (`旅馆`) hồi mana. `=0` tắt. |
| 21 | `加buff主号角色名=角色名1,角色名2` | Tên nhân vật acc chính buff | Giá trị mẫu: `角色名1`, `角色名2` = "tên nhân vật 1, 2". Thay bằng tên thật, cách nhau dấu phẩy `,`. Dùng khi `开启=1`. |
| 22 | `加buff主号放技能=加速術,某某技能` | Kỹ năng acc chính buff sẽ dùng | `加速術` = Haste (tăng tốc). `某某技能` = "kỹ năng XYZ" (chỗ trống mẫu, thay bằng tên kỹ năng thật đúng như trong game, hoặc xóa đi). |
| 23 | `同角色加buff间隔=60` | Khoảng cách buff cùng một nhân vật | Chú thích gốc: "Đơn vị = giây." Một nhân vật vừa được buff thì phải chờ 60 giây mới được buff lại. |
| 24 | `加buff主号对角色连续加几次=1` | Số lần buff liên tiếp cho một nhân vật | Chú thích gốc: "Ví dụ `=3`: dùng `加速術` liên tiếp 3 lần; 1 lần 20 phút, 3 lần cộng dồn thành trạng thái 60 phút." Mặc định 1 lần. |

### `[全局小号列表]`: Danh sách acc phụ toàn cục

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 26 | `[全局小号列表]` | [Danh sách acc phụ toàn cục] | Tên các nhân vật được buff ở **mọi server** (khi không có tên dưới mục server). Mỗi dòng một tên. |
| 27 | `张三111` | Tên mẫu | Thay bằng tên nhân vật thật. |
| 28 | `李四111` | Tên mẫu | Thay bằng tên nhân vật thật. |

### Các mục server (tên acc phụ theo từng server)

Mỗi mục `[tên server]` chứa tên các acc phụ ở server đó, mỗi dòng một tên. Những tên này được **ưu tiên** buff trước (xem dòng 2). Mặc định chỉ `[太陽神阿波羅]` có 2 tên mẫu, các mục khác trống.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 31 | `[太陽神阿波羅]` | Server Thần Mặt Trời Apollo | Có 2 tên mẫu bên dưới. |
| 32 | `张三111` | Tên mẫu | Thay bằng tên thật hoặc xóa. |
| 33 | `李四111` | Tên mẫu | Thay bằng tên thật hoặc xóa. |
| 35 | `[愛神邱比特]` | Server Thần Tình yêu Cupid | Trống |
| 37 | `[勝利女神雅典娜]` | Server Nữ thần Chiến thắng Athena | Trống |
| 39 | `[美神維納斯]` | Server Nữ thần Sắc đẹp Venus | Trống |
| 41 | `[天神宙斯]` | Server Thần Zeus | Trống |
| 43 | `[天后海拉]` | Server Thiên hậu Hera | Trống |
| 45 | `[戰神馬爾斯]` | Server Thần Chiến tranh Mars | Trống |
| 47 | `[月亮女神阿緹蜜斯]` | Server Nữ thần Mặt Trăng Artemis | Trống |
| 49 | `[海神波塞頓]` | Server Thần Biển Poseidon | Trống |
| 51 | `[冥王黑帝斯]` | Server Diêm vương Hades | Trống |
| 53 | `[火神赫發斯特斯]` | Server Thần Lửa Hephaestus | Trống |
| 55 | `[收穫女神帝蜜特]` | Server Nữ thần Mùa màng Demeter | Trống |
| 57 | `[蛇髮女墨杜沙]` | Server Nữ yêu tóc rắn Medusa | Trống |
| 59 | `[半人馬涅索斯]` | Server Nhân mã Nessus | Trống |
| 61 | `[牛人彌諾陶洛斯]` | Server Người bò Minotaur | Trống |
| 63 | `[牛人彌諾陶洛斯2]` | Server Người bò Minotaur 2 | Trống |
| 65 | `[俄雷恩]` | Server Orion (?) | Trống |
| 67 | `[獨眼巨人庫克羅普斯]` | Server Khổng lồ một mắt Cyclops | Trống |
| 69 | `[獅子涅墨亞]` | Server Sư tử Nemea | Trống |
| 71 | `[飛馬珀伽索斯]` | Server Ngựa bay Pegasus | Trống |
| 73 | `[公牛克里特]` | Server Bò mộng xứ Crete | Trống |
| 75 | `[女妖塞壬]` | Server Nữ yêu Siren | Trống |
| 77 | `[巨龍拉冬]` | Server Rồng khổng lồ Ladon | Trống |
| 79 | `[百眼怪阿爾戈斯]` | Server Quái vật trăm mắt Argus | Trống |
| 81 | `[大地之神蓋亞]` | Server Thần Đất Gaia | Trống |
| 83 | `[泰坦女神瑞亞 non-pvp]` | Server Nữ thần Titan Rhea (non-PvP) | Trống |
| 85 | `[水蛇許德拉 non-pvp]` | Server Rắn nước Hydra (non-PvP) | Trống. Lưu ý: file này **không có** mục `[水蛇許德拉]` (bản thường). |

💡 **Lưu ý:**
- **Chế độ `开启=1`:** điền tên acc chính vào `加buff主号角色名`, điền tên acc phụ vào `[全局小号列表]` hoặc dưới mục server tương ứng.
- **Chế độ `开启=2`:** không cần điền danh sách tên, nhưng mọi acc chính và acc phụ phải **kết nối `中控`**. `中控` sẽ tự cử từng acc phụ tới lần lượt.
- Theo ví dụ ở dòng 24, mỗi lần `加速術` kéo dài khoảng 20 phút. Nếu đặt buff 3 lần liên tiếp thì nên tăng `同角色加buff间隔` cho phù hợp (suy luận).
- Nếu muốn dùng `小号buff消失回城=1`, nhớ đặt đúng tên acc chính và tọa độ, nếu không acc phụ sẽ chạy về đứng chờ vô ích (sau đó chờ `小号buff消失间隔过来时间` mới thử lại).

---

## CounterattackPeoples.txt

**File này điều khiển gì:** danh sách **người chơi để phản công hoặc chủ động tấn công** (PvP). Bạn tự điền tên người chơi: khi gặp, bot sẽ đánh trả (bị động) hoặc tấn công trước (chủ động), tùy chế độ `开启`. Có danh sách trắng (không đánh) và danh sách đen (cần đánh).

**Khi nào bot dùng:** khi `开启` khác 0. Bot quét người chơi xung quanh trong lúc treo máy. (`开启=0` tắt chức năng của cả file; file không nói rõ `主动攻红名玩家=1` có chạy riêng khi `开启=0` hay không (?).)

> Nhắc lại: giữ nguyên chữ Trung (tên khóa, tên mục server). Tên người chơi phải gõ **đúng y như trong game**.

**Chú thích đầu file:**

| # | Dòng gốc | Dịch |
|---|---|---|
| 1 | `--此文件为反击玩家列表配置` | "File này cấu hình danh sách người chơi cần phản công." |
| 2 | `--这里的反击玩家与BaseConfig.txt中的反击人有所不同` | "Người chơi phản công ở đây khác với mục phản công người (`反击人`) trong `BaseConfig.txt`." |
| 3 | `--这里是自己填入指定的玩家名字，发现后进行主动或者被动攻击` | "Ở đây bạn tự điền tên người chơi chỉ định; khi phát hiện thì tấn công chủ động hoặc bị động." |
| 5 | `--黑名单列表 可以不用在区服下面填入名字，在黑名单列表中填入代表所有区服` | "`黑名单列表` (danh sách đen): không cần điền tên dưới mục server; điền vào danh sách đen nghĩa là áp dụng cho **mọi server**." |
| 6 | `--黑名单列表 代表需要攻击的角色名字` | "`黑名单列表` là tên các nhân vật cần tấn công." |
| 8 | `--开启=0关闭此文件的功能` | "`开启=0`: tắt chức năng của file này." |
| 9 | `--开启=1黑名单列表 或者 区服列表下面的角色 如果正在攻击其他人(包括自己)时进行反击` | "`开启=1`: nhân vật trong danh sách đen hoặc dưới mục server, **nếu đang tấn công người khác (kể cả mình)** thì phản công." |
| 10 | `--开启=2黑名单列表 或者 区服列表下面的角色 发现在周围就主动攻击` | "`开启=2`: nhân vật trong danh sách đen hoặc dưới mục server, **thấy ở xung quanh là chủ động tấn công**." |
| 11 | `--开启=3主动攻击周围所有玩家，除了白名单列表的角色名不会攻击` | "`开启=3`: chủ động tấn công **mọi người chơi xung quanh**, trừ tên trong danh sách trắng." |
| 12 | `--开启=4需要连接中控，主动攻击周围所有玩家，除了白名单列表的角色名不会攻击，与中控连接的机器的账号角色不会被攻击` | "`开启=4`: cần kết nối `中控`. Chủ động tấn công mọi người chơi xung quanh, trừ tên trong danh sách trắng; nhân vật của các tài khoản trên những máy đang kết nối `中控` cũng **không** bị tấn công." |
| 13 | `--开启=5需要连接中控，如果正在攻击其他人(包括自己)时进行反击，除了白名单列表的角色名不会攻击，与中控连接的机器的账号角色不会被攻击` | "`开启=5`: cần kết nối `中控`. Nếu (ai đó) đang tấn công người khác (kể cả mình) thì phản công; trừ tên trong danh sách trắng; nhân vật của các tài khoản trên những máy đang kết nối `中控` cũng không bị tấn công." |
| 15 | `--主动攻红名玩家 开启时 不会攻击白名单列表的玩家` | "Khi bật `主动攻红名玩家` (chủ động đánh người tên đỏ), bot sẽ không đánh người trong danh sách trắng." |

**Tóm tắt các chế độ `开启`:**

| Giá trị | Đánh ai | Cách đánh | Cần `中控` |
|---|---|---|---|
| `0` | Không ai | Tắt | Không |
| `1` | Danh sách đen + tên dưới mục server | Phản công khi họ đang đánh người khác hoặc đánh mình | Không |
| `2` | Danh sách đen + tên dưới mục server | Thấy là đánh trước | Không |
| `3` | Mọi người chơi xung quanh, trừ danh sách trắng | Thấy là đánh trước | Không |
| `4` | Mọi người chơi xung quanh, trừ danh sách trắng và acc của mình trên `中控` | Thấy là đánh trước | Có |
| `5` | Người đang đánh người khác/đánh mình, trừ danh sách trắng và acc của mình trên `中控` | Phản công | Có |

### `[config]`: Cấu hình

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 17 | `[config]` | Mục cấu hình | |
| 18 | `开启=0` | Chế độ | Xem bảng tóm tắt ở trên. Mặc định `0` (tắt). |
| 19 | `相性数值低于多少停止攻击=-999999` | Chỉ số thiện/ác thấp hơn bao nhiêu thì ngừng tấn công | `相性` ở đây có lẽ là chỉ số thiện/ác (alignment, Lawful/Chaotic) (?). File không nói rõ là chỉ số của mình hay của đối thủ; nhiều khả năng là của chính nhân vật mình (?). Trong Lineage, PK (giết) người chơi không tên đỏ sẽ làm chỉ số này giảm. Khi chỉ số xuống dưới mức này, bot ngừng tấn công. Mặc định `-999999` = thực tế không bao giờ ngừng. |
| 20 | `主动攻红名玩家=0` | Chủ động đánh người chơi tên đỏ | Chú thích gốc: "`=0` tắt, `=1` bật." Người chơi tên đỏ = người đang có chỉ số ác (Chaotic, thường do PK). Không đánh người trong danh sách trắng (xem dòng 15). |

### `[白名单列表]` và `[黑名单列表]`

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 23 | `[白名单列表]` | [Danh sách trắng] | Tên người chơi **không bao giờ bị đánh** (bạn bè, acc của mình...). Mỗi dòng một tên. Mặc định trống. |
| 26 | `[黑名单列表]` | [Danh sách đen] | Tên người chơi **cần đánh**, áp dụng cho **mọi server**. Mỗi dòng một tên. Mặc định trống. |

### Các mục server (tên người chơi cần đánh theo từng server)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 31 | `[太陽神阿波羅]` | Server Thần Mặt Trời Apollo | Mục mẫu, có 3 dòng hướng dẫn và 2 tên mẫu. |
| 32 | `这里填入你要攻击的角色名字` | "Ở đây điền tên nhân vật bạn muốn tấn công." | Dòng hướng dẫn **không có `--`** (xem lưu ý bên dưới). |
| 33 | `可以为多行表示多个玩家名字` | "Có thể viết nhiều dòng để ghi nhiều tên người chơi." | Dòng hướng dẫn không có `--`. |
| 34 | `自动攻击对应的大区服务器的玩家` | "Tự động tấn công người chơi ở server (đại khu) tương ứng." | Dòng hướng dẫn không có `--`. |
| 35 | `张三111` | Tên mẫu | Thay bằng tên thật hoặc xóa. |
| 36 | `李四111` | Tên mẫu | Thay bằng tên thật hoặc xóa. |
| 38 | `[愛神邱比特]` | Server Thần Tình yêu Cupid | Trống |
| 40 | `[勝利女神雅典娜]` | Server Nữ thần Chiến thắng Athena | Trống |
| 42 | `[美神維納斯]` | Server Nữ thần Sắc đẹp Venus | Trống |
| 44 | `[天神宙斯]` | Server Thần Zeus | Trống |
| 46 | `[天后海拉]` | Server Thiên hậu Hera | Trống |
| 48 | `[戰神馬爾斯]` | Server Thần Chiến tranh Mars | Trống |
| 50 | `[月亮女神阿緹蜜斯]` | Server Nữ thần Mặt Trăng Artemis | Trống |
| 52 | `[海神波塞頓]` | Server Thần Biển Poseidon | Trống |
| 54 | `[冥王黑帝斯]` | Server Diêm vương Hades | Trống |
| 56 | `[火神赫發斯特斯]` | Server Thần Lửa Hephaestus | Trống |
| 58 | `[收穫女神帝蜜特]` | Server Nữ thần Mùa màng Demeter | Trống |
| 60 | `[蛇髮女墨杜沙]` | Server Nữ yêu tóc rắn Medusa | Trống |
| 62 | `[半人馬涅索斯]` | Server Nhân mã Nessus | Trống |
| 64 | `[牛人彌諾陶洛斯]` | Server Người bò Minotaur | Trống |
| 66 | `[牛人彌諾陶洛斯2]` | Server Người bò Minotaur 2 | Trống |
| 68 | `[俄雷恩]` | Server Orion (?) | Trống |
| 70 | `[獨眼巨人庫克羅普斯]` | Server Khổng lồ một mắt Cyclops | Trống |
| 72 | `[獅子涅墨亞]` | Server Sư tử Nemea | Trống |
| 74 | `[飛馬珀伽索斯]` | Server Ngựa bay Pegasus | Trống |
| 76 | `[公牛克里特]` | Server Bò mộng xứ Crete | Trống |
| 78 | `[女妖塞壬]` | Server Nữ yêu Siren | Trống |
| 80 | `[巨龍拉冬]` | Server Rồng khổng lồ Ladon | Trống |
| 82 | `[百眼怪阿爾戈斯]` | Server Quái vật trăm mắt Argus | Trống |
| 84 | `[大地之神蓋亞]` | Server Thần Đất Gaia | Trống |
| 86 | `[泰坦女神瑞亞 non-pvp]` | Server Nữ thần Titan Rhea (non-PvP) | Trống. Server non-PvP không đánh người được, nên mục này gần như không có tác dụng (suy luận). |
| 88 | `[水蛇許德拉 non-pvp]` | Server Rắn nước Hydra (non-PvP) | Trống. Như trên. File này cũng **không có** mục `[水蛇許德拉]` (bản thường). |

💡 **Lưu ý:**
- **Dòng 32–34 không bắt đầu bằng `--`**, nên bot có thể hiểu chúng là **tên người chơi** (?). Khi điền danh sách thật, nên **xóa 3 dòng hướng dẫn đó** và 2 tên mẫu `张三111`, `李四111`.
- Chế độ `3` và `4` đánh **tất cả** người chơi xung quanh. Hãy điền đủ bạn bè/acc của mình vào `[白名单列表]` trước khi bật.
- PK (giết) người chơi không tên đỏ sẽ làm giảm chỉ số thiện/ác, có thể khiến nhân vật thành tên đỏ (Chaotic). Dùng `相性数值低于多少停止攻击` để bot dừng lại trước khi chỉ số xuống quá thấp, ví dụ `-1000` (?).

---

## Deleteitem.txt

**File này điều khiển gì:** danh sách **vật phẩm cần xóa** (hủy/bỏ khỏi túi đồ), để túi không bị đầy vì đồ rác.

**Khi nào bot dùng:** khi trong túi có vật phẩm trùng tên với một dòng trong file (thời điểm cụ thể file không ghi rõ).

> Nhắc lại: giữ nguyên chữ Trung. Tên vật phẩm phải đúng y như trong game, mỗi dòng một tên.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 1 | `--此文件为需要删除物品的设置` | "File này cài đặt các vật phẩm cần xóa." | Chú thích. |
| 2 | `金疮药1` | "Kim sang dược 1" (thuốc trị vết thương) | **Tên mẫu**. `金疮药` không phải tên vật phẩm Lineage (đây là tên thuốc trong các game kiếm hiệp Trung Quốc), lại có thêm số `1` ở cuối, nên gần như chắc chắn chỉ là ví dụ. |
| 3 | `太阳水1` | "Nước Mặt Trời 1" | **Tên mẫu**, tương tự dòng 2 (`太阳水` là thuốc trong game Mir/Truyền Kỳ). |

💡 **Lưu ý:** với 2 tên mẫu này bot sẽ không xóa gì trong Lineage. Muốn bot xóa đồ rác, thay chúng bằng **tên chính xác** vật phẩm trong game, mỗi dòng một tên. **Cẩn thận:** đồ đã xóa thì không lấy lại được, đừng điền nhầm tên đồ quý.

---

## G_Filtering_Monster_And_Item.txt

**File này điều khiển gì:** cấu hình **toàn cục** (cho mọi nhân vật) của 3 danh sách:

- `[怪物过滤]` **lọc quái**: những quái/NPC bot **không đánh**.
- `[反击怪物]` **quái phản công**: những quái bình thường bot không đánh, nhưng **nếu nó đánh mình thì đánh trả** (file không giải thích; suy ra từ tên mục `反击` = phản công, và cả 3 quái trong mục này cũng nằm trong `[怪物过滤]`).
- `[拾取过滤]` **lọc nhặt đồ**: những vật phẩm bot **không nhặt**.

**Khi nào bot dùng:** chỉ khi `开启=1`. Khi đó 3 danh sách này **thay thế** các danh sách cùng tên trong `gj.txt` (file cấu hình treo máy của từng nhân vật; "gj" = `挂机`, treo máy).

> Nhắc lại: giữ nguyên chữ Trung. Tên quái và vật phẩm phải đúng y như trong game, mỗi dòng một tên.

| # | Dòng gốc | Dịch |
|---|---|---|
| 1 | `--此文件为全局 怪物过滤 反击怪物 拾取过滤 的设置` | "File này cài đặt toàn cục cho: lọc quái (`怪物过滤`), quái phản công (`反击怪物`), lọc nhặt đồ (`拾取过滤`)." |
| 2 | `--当开启=1  gj.txt里面的设置则无效（怪物过滤 反击怪物 拾取过滤）` | "Khi `开启=1` thì các cài đặt trong `gj.txt` mất hiệu lực (lọc quái, quái phản công, lọc nhặt đồ)." |
| 3 | `--当开启=0  gj.txt则生效` | "Khi `开启=0` thì `gj.txt` có hiệu lực." |

### `[config]`

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 4 | `[config]` | Mục cấu hình | |
| 5 | `开启=0` | Dùng cấu hình toàn cục | Chú thích gốc: "`=0` tắt, `=1` bật, dùng cấu hình toàn cục ở đây." Mặc định `0`: mỗi nhân vật dùng danh sách trong `gj.txt` của nó. |

### `[怪物过滤]`: Lọc quái (không đánh)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 7 | `[怪物过滤]` | [Lọc quái] | Các tên dưới đây sẽ **không bị đánh**. |
| 8 | `巡守` | Lính tuần tra (Patrol) | |
| 9 | `史萊姆` | Slime | Cũng có trong `[反击怪物]`. |
| 10 | `長老` | Trưởng lão (Elder) | |
| 11 | `警衛` | Lính gác (Guard) | |
| 12 | `漂浮之眼` | Mắt lơ lửng (Floating Eye) | Cũng có trong `[反击怪物]`. |
| 13 | `克特` | Kurtz (?) | Phiên âm "Khắc Đặc". |
| 14 | `石頭高崙` | Golem đá (Stone Golem) | Cũng có trong `[反击怪物]`. |
| 15 | `飛龍` | Phi long (Drake) | |
| 16 | `青蛙` | Ếch (Frog) | |
| 17 | `兔子` | Thỏ (Rabbit) | |
| 18 | `鹿` | Hươu (Deer) | |
| 19 | `安特` | Ent (người cây) | |
| 20 | `強盜` | Cướp (Bandit) | |
| 21 | `魚` | Cá (Fish) | |
| 22 | `奇岩警衛` | Lính gác Giran (`奇岩`) | |
| 23 | `肯特城警衛` | Lính gác thành Kent | |
| 24 | `風木城警衛` | Lính gác thành Windawood | `風木` = Windawood. |
| 25 | `海音警衛` | Lính gác Heine (`海音`) | |
| 26 | `侏儒警衛` | Lính gác Người lùn (Dwarf Guard) | |
| 27 | `城堡守衛` | Vệ binh lâu đài (Castle Guard) | |
| 28 | `守門人` | Người gác cổng (Gatekeeper) | |
| 29 | `亞丁警衛` | Lính gác Aden (`亞丁`) | |
| 30 | `亞丁近衛隊` | Đội cận vệ Aden (Aden Royal Guard) | |

### `[反击怪物]`: Quái phản công (bị đánh thì đánh trả)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 32 | `[反击怪物]` | [Quái phản công] | Không chủ động đánh, nhưng nếu chúng đánh mình thì đánh trả. |
| 33 | `史萊姆` | Slime | |
| 34 | `漂浮之眼` | Mắt lơ lửng (Floating Eye) | |
| 35 | `石頭高崙` | Golem đá (Stone Golem) | |

### `[拾取过滤]`: Lọc nhặt đồ (không nhặt)

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 38 | `[拾取过滤]` | [Lọc nhặt đồ] | Các vật phẩm dưới đây sẽ **không được nhặt** (đồ rác giá thấp). |
| 39 | `盾` | Khiên (Shield) | |
| 40 | `短劍` | Đoản kiếm (Dagger) | |
| 41 | `侏儒斗篷` | Áo choàng Người lùn (Dwarf Cloak) | |
| 42 | `斧` | Rìu (Axe) | |
| 43 | `頭盔` | Mũ giáp (Helmet) | |
| 44 | `木棒` | Gậy gỗ (Club) | |
| 45 | `燈` | Đèn (Lamp) | |
| 46 | `環甲` | Giáp vòng (Ring Mail) | |
| 47 | `亞連` | "Á Liên", có lẽ là một loại vũ khí cấp thấp (?) | Phiên âm "Á Liên", chưa xác định chính xác món đồ (thương nhân vũ khí `潘朵拉` trong `SellList.txt` có thu mua món này). Cứ giữ nguyên. |
| 48 | `皮甲` | Giáp da (Leather Armor) | |
| 49 | `弗萊爾` | Chùy xích (Flail) | |
| 50 | `短統靴` | Ủng cổ ngắn (Low Boots) | |
| 51 | `烏木魔杖` | Gậy phép gỗ mun (Ebony Wand) | |
| 52 | `侏儒鐵盔` | Mũ sắt Người lùn (Dwarf Iron Helm) | |
| 53 | `斗篷` | Áo choàng (Cloak) | |
| 54 | `釘錘` | Chùy gai (Mace) | |
| 55 | `歐西斯鏈甲` | Giáp xích Orcish (?) | `鏈甲` = giáp xích (Chain Mail). `歐西斯` phiên âm "Âu Tây Tư", có lẽ là "Orcish" (?). |
| 56 | `肉` | Thịt (Meat) | |
| 57 | `胡蘿蔔` | Cà rốt (Carrot) | |
| 58 | `蘋果` | Táo (Apple) | |
| 59 | `檸檬` | Chanh (Lemon) | |
| 60 | `香蕉` | Chuối (Banana) | |
| 61 | `蛋` | Trứng (Egg) | |
| 62 | `橘子` | Quýt (Orange) | |

💡 **Lưu ý:**
- File này chỉ có tác dụng khi `开启=1`. Bật lên thì danh sách trong **mọi** `gj.txt` bị bỏ qua, nên hãy gộp đủ tên vào đây.
- Danh sách lọc quái có sẵn **lính gác các thành** (`警衛`, `奇岩警衛`, `亞丁警衛`...). Đừng xóa chúng, nếu không bot có thể đi đánh lính gác.
- `安特` (Ent) đang nằm trong danh sách **không đánh**. Nếu bạn muốn farm Ent (ví dụ ở Rừng Tiên `妖精森林`) thì phải xóa dòng 19.
- Muốn nhặt thêm đồ nào thì **xóa** tên đó khỏi `[拾取过滤]`. Muốn bỏ qua đồ nào thì **thêm** tên vào.

---

## UseItems.txt

**File này điều khiển gì:** tự **dùng (mở) vật phẩm theo chu kỳ**, chủ yếu là các hộp, rương, khối bí ẩn phải bấm dùng nhiều lần để ra đồ.

**Khi nào bot dùng:** cứ mỗi khoảng thời gian (phút) đặt cho từng vật phẩm.

> Nhắc lại: giữ nguyên chữ Trung (tên vật phẩm, kể cả phần trong ngoặc như `(30次)`). Chỉ đổi các con số.

**Chú thích đầu file:**

| # | Dòng gốc | Dịch |
|---|---|---|
| 1 | `--间隔使用物品配置` | "Cấu hình dùng vật phẩm theo chu kỳ." |
| 2 | `--神秘方塊=间隔时间(分钟)=同时对几个格子使用=每个格子可使用的次数` | "Định dạng: `神秘方塊=chu kỳ (phút)=dùng cùng lúc cho mấy ô=số lần dùng mỗi ô`." (`神秘方塊` = Khối bí ẩn, dùng làm ví dụ; `格子` = ô trong túi đồ.) |
| 3 | `--比如 神秘方塊 占用了10个格子，间隔60分钟对10个格子的 神秘方塊 的每个格子用N次` | "Ví dụ `神秘方塊` chiếm 10 ô trong túi: cứ 60 phút, với mỗi ô trong 10 ô `神秘方塊` đó thì dùng N lần." |
| 4 | `--某个物品箱子使用后需要选择第几个道具  这种不支持` | "Loại hộp vật phẩm mà sau khi mở phải **chọn lấy món thứ mấy** thì không hỗ trợ." |

**Giải thích 3 con số** của `tên=A=B=C`: `A` = chu kỳ, tính bằng **phút**. `B` = số ô (chồng vật phẩm) dùng cùng lúc. `C` = số lần dùng mỗi ô trong một chu kỳ.

| # | Dòng gốc | Nghĩa | Giải thích |
|---|---|---|---|
| 5 | `冰之女王的神秘方塊=60=10=10` | Khối bí ẩn của Nữ hoàng Băng (Ice Queen's Mysterious Cube) | Mỗi 60 phút, tối đa 10 ô, mỗi ô dùng 10 lần. |
| 6 | `神秘方塊=60=10=10` | Khối bí ẩn (Mysterious Cube) | Mỗi 60 phút, tối đa 10 ô, mỗi ô dùng 10 lần. |
| 7 | `因納得立的寶箱(30次)=60=10=10` | Rương báu Innadril (30 lần) | `因納得立` = Innadril (tên địa danh trong Lineage). `(30次)` = "(30 lần)" là một phần của tên vật phẩm, phải giữ nguyên. Mỗi 60 phút, tối đa 10 ô, mỗi ô dùng 10 lần. |
| 8 | `矮人的齒輪=60=10=1` | Bánh răng của Người lùn (Dwarf's Gear) | Mỗi 60 phút, tối đa 10 ô, mỗi ô dùng 1 lần. |
| 9 | `地監記憶書箱=60=10=1` | Hộp Sách ghi nhớ hầm ngục (`地監記憶書`) | Hộp chứa sách ghi nhớ vị trí trong hầm ngục. Mỗi 60 phút, tối đa 10 ô, mỗi ô dùng 1 lần. |
| 10 | `GM的便當=60=10=1` | Hộp cơm của GM (GM's Lunch Box) | `便當` = hộp cơm (bento), vật phẩm quà tặng. Mỗi 60 phút, tối đa 10 ô, mỗi ô dùng 1 lần. |

💡 **Lưu ý:**
- Hộp nào khi mở hiện bảng **chọn phần thưởng** thì bot **không** tự mở được (chú thích dòng 4). Đừng thêm loại đó vào.
- Muốn mở nhanh hơn thì giảm chu kỳ `A` (ví dụ `=10` là 10 phút một lần). Muốn ngừng tự mở một món thì xóa dòng đó.
- Thêm vật phẩm mới theo đúng định dạng `tên=A=B=C`, với tên đúng y như trong game.
