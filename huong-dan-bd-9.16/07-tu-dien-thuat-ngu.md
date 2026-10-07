# Từ điển thuật ngữ

Bảng tra cứu mọi thuật ngữ tiếng Trung xuất hiện trong bộ tài liệu dịch gói bot **天堂经典版 Bd 9.16** (bot treo máy cho *Lineage Classic*). Mỗi thuật ngữ chỉ có **một** cách dịch tiếng Việt, dùng thống nhất trong cả 6 file hướng dẫn.

## Cách dùng bảng này

- **Cột "Nguyên văn (code)"** là chữ gốc mà bot đọc. Khi sửa file cấu hình, **giữ nguyên chữ Trung từng ký tự**: tên mục `[...]`, tên khóa, tên bản đồ, vật phẩm, quái, NPC, server. **Chỉ đổi số hoặc giá trị** sau dấu `=`. Phần tiếng Việt chỉ để bạn hiểu nghĩa, đừng gõ tiếng Việt vào file.
- Nhiều thuật ngữ có cả **chữ Phồn thể** và **chữ Giản thể** (ví dụ `說話之島` / `说话之岛`). Các dạng được ghi chung một ô, ngăn bằng ` / `. Với máy tính, hai dạng này **khác nhau**: khi điền cấu hình, hãy chép đúng dạng mà file cấu hình gốc đang dùng (tên trong game thường là Phồn thể).
- **(?)** nghĩa là cách dịch hoặc tên tiếng Anh chưa chắc chắn 100%. Cột "Tiếng Anh" ghi "—" khi không biết tên tiếng Anh chính thức.
- Ba mục `驱动模式`, `目录保护`, `自动接码验证设备` chỉ có nhãn trung tính. ⚠️ Tài liệu này không hướng dẫn phần này.
- **Cột "Xuất hiện ở"** cho biết thuật ngữ có mặt trong file hướng dẫn nào (bấm để mở):

| Mã | File hướng dẫn | Nội dung |
|---|---|---|
| 01 | [01-huong-dan-su-dung.md](01-huong-dan-su-dung.md) | `使用说明.txt` và `组队服务器/使用说明.txt` |
| 02 | [02-nhat-ky-cap-nhat.md](02-nhat-ky-cap-nhat.md) | `更新说明.txt` |
| 03 | [03-cau-hinh-chung-va-cau-truc-goi.md](03-cau-hinh-chung-va-cau-truc-goi.md) | Cấu trúc gói, `config/`, `大中控/`, `组队服务器/`, `Account.txt` |
| 04 | [04-baseconfig.md](04-baseconfig.md) | `Game_Config/BaseConfig.txt` |
| 05 | [05-game-config-chien-dau-va-vat-pham.md](05-game-config-chien-dau-va-vat-pham.md) | `Game_Config`: sự kiện, huyết minh, buff, phản công, lọc quái, dùng vật phẩm |
| 06 | [06-game-config-treo-may-kho-va-giao-dich.md](06-game-config-treo-may-kho-va-giao-dich.md) | `Game_Config`: `gj.txt`, kho cá nhân, mua bán, giao dịch, bảo vật |

## Các quy ước dịch đã thống nhất (dễ nhầm)

| Nguyên văn | Cách dịch thống nhất | Lý do |
|---|---|---|
| `俄雷恩` | Orion (?) | Tên server, theo chủ đề thần thoại Hy Lạp. **Không** phải Oren: làng Oren là `歐瑞` / `欧瑞`. |
| `對盔甲施法的卷軸` / `防具強化卷軸` | cuộn **phù phép** giáp / cuộn **cường hóa** giáp | Hai vật phẩm khác nhau, dịch khác nhau để không lẫn. Tương tự `對武器施法的卷軸` (phù phép vũ khí) / `武器強化卷軸` (cường hóa vũ khí). |
| `说话卷` / `说话卷轴` | cuộn dịch chuyển về Talking Island | Dùng một cách gọi ở mọi file. |
| `精靈` (trong tên vật phẩm) / `妖精` | Tiên (Elven) / Elf (Tiên tộc) | `精靈餅乾` = Bánh quy Tiên, `精靈弓` = Cung Tiên. Riêng bản đồ `精靈之地` vẫn để "Vùng đất Tinh linh (?)". |
| `治癒藥水` | Thuốc trị liệu (Healing Potion) | Thay cho các cách gọi "thuốc hồi máu", "thuốc trị thương" trước đây. |
| `歐琳` / `倫提斯` / `斯奈普` | Orim (?) / Roomtis (?) / Snapper (?) | Phiên âm tên trang sức, dùng giống nhau ở mọi file. |
| `中控` | trung tâm điều khiển (= `大中控`) | Nhật ký cập nhật dùng `中控` và `大中控` cho cùng một chương trình. |

**Mục lục:** 1. Bản đồ & địa điểm · 2. Server · 3. Nghề (class) · 4. Vật phẩm · 5. Quái vật & NPC · 6. Kỹ năng · 7. Thuật ngữ của bot & cấu hình (7.1 Thuật ngữ chung, 7.2 Tên mục, 7.3 Khóa cấu hình)

---

## 1. Bản đồ & địa điểm

| Nguyên văn (code) | Tiếng Việt | Tiếng Anh (nếu biết) | Xuất hiện ở |
|---|---|---|---|
| `說話之島` / `说话之岛` | Talking Island (Đảo Nói Chuyện) | Talking Island | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `說話之島村` / `说话之岛村` / `说话岛村` | làng Talking Island | Talking Island Village | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `說話之島地監1樓` / `說話之島地監2樓` | Hầm ngục Talking Island tầng 1, tầng 2 | Talking Island Dungeon 1F, 2F | [01](01-huong-dan-su-dung.md) |
| `說話之島地監1樓(網咖)` / `說話之島地監2樓(網咖)` | Hầm ngục Talking Island tầng 1, 2 (bản quán net) | Talking Island Dungeon (PC bang) | [01](01-huong-dan-su-dung.md) |
| `古魯丁` / `古鲁丁` | Gludin (vùng quanh làng Gludin) | Gludin | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `古魯丁村` / `古鲁丁村` | làng Gludin | Gludin Village | [01](01-huong-dan-su-dung.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `古魯丁地監1樓` / `古魯丁地監2樓` / `古魯丁地監3樓` / `古魯丁地監4樓` / `古魯丁地監5樓` / `古魯丁地監6樓` / `古魯丁地監7樓` | Hầm ngục Gludin tầng 1 → 7 | Gludin Dungeon 1F–7F | [01](01-huong-dan-su-dung.md) |
| `古魯丁地監1樓(網咖)` / `古魯丁地監2樓(網咖)` / `古魯丁地監3樓(網咖)` / `古魯丁地監4樓(網咖)` / `古魯丁地監5樓(網咖)` / `古魯丁地監6樓(網咖)` / `古魯丁地監7樓(網咖)` | Hầm ngục Gludin tầng 1 → 7 (bản quán net) | Gludin Dungeon (PC bang) | [01](01-huong-dan-su-dung.md) |
| `古鲁丁7楼` | tầng 7 hầm ngục Gludin (cách viết giản thể trong ghi chú) | Gludin Dungeon 7F | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `奇岩` | Giran | Giran | [01](01-huong-dan-su-dung.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `奇岩村` | làng Giran | Giran Village | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `奇岩地監1樓` / `奇岩地監2樓` / `奇岩地監3樓` / `奇岩地監4樓` | Hầm ngục Giran tầng 1 → 4 | Giran Dungeon 1F–4F | [01](01-huong-dan-su-dung.md) |
| `龍之谷` | Thung lũng Rồng | Dragon Valley | [01](01-huong-dan-su-dung.md) |
| `龍之谷地監1樓` / `龍之谷地監2樓` / `龍之谷地監3樓` / `龍之谷地監4樓` / `龍之谷地監5樓` / `龍之谷地監6樓` | Hầm ngục Thung lũng Rồng tầng 1 → 6 | Dragon Valley Dungeon 1F–6F | [01](01-huong-dan-su-dung.md) |
| `龍之谷地監1樓2` / `龍之谷地監1樓3` / `龍之谷地監1樓4` | Hầm ngục Thung lũng Rồng tầng 1 – khu 2, 3, 4 (có lẽ là các lối vào khác nhau) (?) | — | [01](01-huong-dan-su-dung.md) |
| `象牙塔` | Tháp Ngà | Ivory Tower | [01](01-huong-dan-su-dung.md) |
| `象牙塔1樓` / `象牙塔2樓` / `象牙塔3樓` / `象牙塔4樓` / `象牙塔5樓` / `象牙塔6樓` / `象牙塔7樓` / `象牙塔8樓` | Tháp Ngà tầng 1 → 8 | Ivory Tower 1F–8F | [01](01-huong-dan-su-dung.md) |
| `海音` | Heine | Heine | [01](01-huong-dan-su-dung.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `海音村` | làng Heine | Heine Village | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `海音地监` | hầm ngục Heine (tiêu đề giản thể trong hướng dẫn) | Heine Dungeon | [01](01-huong-dan-su-dung.md) |
| `地下通道` | Đường hầm ngầm (không có số tầng; có lẽ ở khu Talking Island) (?) | — | [01](01-huong-dan-su-dung.md) |
| `地下通道1樓` / `地下通道2樓` / `地下通道3樓` | Đường hầm ngầm tầng 1 → 3 (khu Heine) | — | [01](01-huong-dan-su-dung.md) |
| `伊娃王國` | Vương quốc Eva | Kingdom of Eva | [01](01-huong-dan-su-dung.md) |
| `伊娃` | Eva (tên nữ thần, tên vương quốc) | Eva | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `亞丁` | Aden (bản đồ mới, bản 9.16 chưa hỗ trợ) | Aden | [02](02-nhat-ky-cap-nhat.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `亞丁村` | làng Aden | Aden | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `妖精森林` | Rừng Tiên | Elven Forest | [01](01-huong-dan-su-dung.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `沙漠` | Sa mạc | Desert | [01](01-huong-dan-su-dung.md) |
| `沙漠地監1樓` / `沙漠地監2樓` / `沙漠地監3樓` / `沙漠地監4樓` | Hầm ngục Sa mạc tầng 1 → 4 | Desert Dungeon 1F–4F | [01](01-huong-dan-su-dung.md) |
| `沙漠地監1樓(網咖)` / `沙漠地監2樓(網咖)` / `沙漠地監3樓(網咖)` / `沙漠地監4樓(網咖)` | Hầm ngục Sa mạc tầng 1 → 4 (bản quán net) | Desert Dungeon (PC bang) | [01](01-huong-dan-su-dung.md) |
| `螞蟻洞窟` / `蚂蚁洞窟` | Hang Kiến | Ant Cave | [01](01-huong-dan-su-dung.md) |
| `螞蟻洞窟地監1樓` / `螞蟻洞窟地監1樓1` | Hầm ngục Hang Kiến tầng 1 – cửa 1 (hai cách viết, xem `01`) | Ant Cave 1F (entrance 1) | [01](01-huong-dan-su-dung.md) |
| `螞蟻洞窟地監1樓2` / `螞蟻洞窟地監1樓3` / `螞蟻洞窟地監1樓4` / `螞蟻洞窟地監1樓5` / `螞蟻洞窟地監1樓6` / `螞蟻洞窟地監1樓7` / `螞蟻洞窟地監1樓8` | Hầm ngục Hang Kiến tầng 1 – cửa 2 → 8 | Ant Cave 1F (entrances 2–8) | [01](01-huong-dan-su-dung.md) |
| `螞蟻洞窟地監2樓` | Hầm ngục Hang Kiến tầng 2 | Ant Cave 2F | [01](01-huong-dan-su-dung.md) |
| `1樓` / `1樓2` / `1樓3` / `1樓4` | tầng 1 / tầng 1 – cửa (khu) 2, 3, 4… (cách ghi tắt trong danh sách tọa độ cửa hang) | — | [01](01-huong-dan-su-dung.md) |
| `眠龍洞穴` | Hang Rồng Ngủ (?) | — | [01](01-huong-dan-su-dung.md) |
| `眠龍洞穴1樓` / `眠龍洞穴2樓` / `眠龍洞穴3樓` | Hang Rồng Ngủ tầng 1 → 3 (?) | — | [01](01-huong-dan-su-dung.md) |
| `被遺棄者之地` | Vùng đất bị ruồng bỏ | — | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md) |
| `深淵` | Vực thẳm | Abyss | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md) |
| `被遺棄者之地 : 深淵` | Vùng đất bị ruồng bỏ : Vực thẳm (tên bản đồ đầy đủ, có dấu cách hai bên dấu `:`) | — | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md) |
| `污染的祝福之地` | Vùng đất Ban phước bị ô nhiễm (bản đồ sự kiện, vào từ làng Gludin) | — | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md) |
| `污染的祝福之地(網咖)` | Vùng đất Ban phước bị ô nhiễm (bản quán net; bot vào khu đầu tiên) | — | [01](01-huong-dan-su-dung.md) |
| `墮落的祝福之地` | Vùng đất Ban phước sa đọa (bản đồ sự kiện theo mùa) | — | [01](01-huong-dan-su-dung.md) |
| `精靈之地` | Vùng đất Tinh linh (?) (khu con của hai vùng trên) | — | [01](01-huong-dan-su-dung.md) |
| `妖魔之地` | Vùng đất Yêu ma (?) (khu con) | — | [01](01-huong-dan-su-dung.md) |
| `人類之地` | Vùng đất Loài người (khu con) | — | [01](01-huong-dan-su-dung.md) |
| `妖精之地` | Vùng đất Tiên tộc (khu con) | — | [01](01-huong-dan-su-dung.md) |
| `冬` / `秋` / `夏` / `春` / `冬/秋/夏/春` | mùa Đông / Thu / Hạ / Xuân (trong tên `墮落的祝福之地 - <mùa> - <khu>`) | Winter / Autumn / Summer / Spring | [01](01-huong-dan-su-dung.md) |
| `污染的祝福之地 - 精靈之地` / `污染的祝福之地 - 妖魔之地` / `污染的祝福之地 - 人類之地` / `污染的祝福之地 - 妖精之地` | tên đầy đủ: Vùng đất Ban phước bị ô nhiễm – <khu> (thêm `(網咖)` ở cuối = bản quán net) | — | [01](01-huong-dan-su-dung.md) |
| `墮落的祝福之地 - 春 - 妖精之地` / `墮落的祝福之地 - 春 - 人類之地` / `墮落的祝福之地 - 冬 - 精靈之地` | ví dụ tên đầy đủ: Vùng đất Ban phước sa đọa – <mùa> – <khu> (đủ 16 tên ở `01`, mục A5); bản quán net không có mùa | — | [01](01-huong-dan-su-dung.md) |
| `網咖` / `网咖` / `(網咖)` | quán net (PC bang); `(網咖)` là hậu tố tên bản đồ dành cho quán net | PC bang (Internet café) | [01](01-huong-dan-su-dung.md) |
| `地監` / `地监` | hầm ngục | dungeon | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `樓` / `楼` | tầng | floor | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `地监门口` | cửa hầm ngục | dungeon entrance | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `活动地图` | bản đồ sự kiện | event map | [01](01-huong-dan-su-dung.md) |
| `火龍窟` | Hang Rồng Lửa (?) | — | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `夢幻之島` | Đảo Mộng Ảo (?) | Island of Dreams (?) | [02](02-nhat-ky-cap-nhat.md) |
| `世界树` / `世界樹` | Cây Thế giới (nơi Elf trở về) | World Tree / Mother Tree | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `歐瑞` / `欧瑞` | Oren | Oren | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `歐瑞村` | làng Oren | Oren | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `欧瑞旅馆` | nhà trọ Oren | Oren Inn | [02](02-nhat-ky-cap-nhat.md) |
| `肯特村` | làng Kent | Kent | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `風木` / `風木村` | Windawood; làng Windawood | Windawood | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `枫木村` | làng Phong Mộc, có lẽ là Windawood (?) (chỉ có trong ví dụ) | Windawood (?) | [04](04-baseconfig.md) |
| `燃柳` / `燃柳村` | làng Woodbec (nghĩa đen "liễu cháy") | Woodbec | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `威頓村` | làng Werldern | Werldern | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `銀騎士村` | làng Hiệp sĩ Bạc | Silver Knight Town | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `銀騎士地區` | Khu vực Hiệp sĩ Bạc (bản đồ treo máy mốc `[15]`) | Silver Knight area | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `因納得立` | Innadril (địa danh, trong tên rương báu) | Innadril | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `旅馆` | nhà trọ | inn | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `村庄` / `村` | làng | village | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `城镇` | thị trấn, thành | town | [02](02-nhat-ky-cap-nhat.md) |

## 2. Server

| Nguyên văn (code) | Tiếng Việt | Tiếng Anh (nếu biết) | Xuất hiện ở |
|---|---|---|---|
| `大区` / `[大区]` | server (nghĩa đen "đại khu"); `[大区]` là tiêu đề danh sách server | server / world | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `伺服器` / `(伺服器)` | máy chủ (server); `(伺服器)` là một phần của tên hai server | server | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `服务器` / `大区服务器` / `区服` | server (máy chủ) | server | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `不同区服` | server khác | different server | [02](02-nhat-ky-cap-nhat.md) |
| `新区` | server mới | new server | [02](02-nhat-ky-cap-nhat.md) |
| `台服` | server Đài Loan | Taiwan server | [01](01-huong-dan-su-dung.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `韩服` | server Hàn Quốc | Korea server | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `太陽神阿波羅` | Thần Mặt Trời Apollo | Apollo | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `愛神邱比特` | Thần Tình yêu Cupid | Cupid | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `勝利女神雅典娜` | Nữ thần Chiến thắng Athena | Athena | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `美神維納斯` | Nữ thần Sắc đẹp Venus | Venus | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `天神宙斯` | Thần Zeus | Zeus | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `天后海拉` | Thiên hậu Hera | Hera | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `戰神馬爾斯` | Thần Chiến tranh Mars | Mars | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `月亮女神阿緹蜜斯` | Nữ thần Mặt Trăng Artemis | Artemis | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `海神波塞頓` | Thần Biển Poseidon | Poseidon | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `冥王黑帝斯` | Diêm vương Hades (thần Âm phủ) | Hades | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `火神赫發斯特斯` | Thần Lửa Hephaestus | Hephaestus | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `收穫女神帝蜜特` | Nữ thần Mùa màng Demeter | Demeter | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `蛇髮女墨杜沙` | Nữ yêu tóc rắn Medusa | Medusa | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `半人馬涅索斯` | Nhân mã Nessus | Nessus | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `牛人彌諾陶洛斯` | Người bò Minotaur | Minotaur | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `牛人彌諾陶洛斯2` | Người bò Minotaur 2 (server thứ hai cùng tên) | Minotaur 2 | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `俄雷恩` / `俄雷恩(伺服器)` | Orion (?) (phiên âm; không phải làng Oren `歐瑞`). Trong `config/ServerText.txt` viết `俄雷恩(伺服器)`, trong `Game_Config` viết `俄雷恩` | Orion (?) | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `凱斯特` / `凱斯特(伺服器)` | Castor (?) (phiên âm; chỉ có trong `ServerText.txt`) | Castor (?) | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `獅子涅墨亞` | Sư tử Nemea | Nemean Lion | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `獅子涅墨亞2` | Sư tử Nemea 2 | Nemean Lion 2 | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `獨眼巨人庫克羅普斯` | Khổng lồ một mắt Cyclops | Cyclops | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `飛馬珀伽索斯` | Ngựa bay Pegasus | Pegasus | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `飛馬珀伽索斯2` | Ngựa bay Pegasus 2 | Pegasus 2 | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `公牛克里特` | Bò mộng xứ Crete | Cretan Bull | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `女妖塞壬` | Nữ yêu Siren | Siren | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `巨龍拉冬` | Rồng khổng lồ Ladon | Ladon | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `百眼怪阿爾戈斯` | Quái vật trăm mắt Argus | Argus | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `大地之神蓋亞` | Thần Đất Gaia | Gaia | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `泰坦女神瑞亞 non-pvp` / `[泰坦女神瑞亞 non-pvp]` | Nữ thần Titan Rhea (server non-PvP, không PK được) | Rhea (non-PvP) | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `水蛇許德拉` | Rắn nước Hydra | Hydra | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `水蛇許德拉 non-pvp` / `[水蛇許德拉 non-pvp]` | Rắn nước Hydra (server non-PvP) | Hydra (non-PvP) | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `地獄犬刻耳柏洛斯` | Chó địa ngục Cerberus | Cerberus | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `[太陽神阿波羅]` / `[愛神邱比特]` / `[勝利女神雅典娜]` / `[美神維納斯]` / `[天神宙斯]` / `[天后海拉]` / `[戰神馬爾斯]` / `[月亮女神阿緹蜜斯]` / `[海神波塞頓]` / `[冥王黑帝斯]` / `[火神赫發斯特斯]` / `[收穫女神帝蜜特]` / `[蛇髮女墨杜沙]` / `[半人馬涅索斯]` / `[牛人彌諾陶洛斯]` / `[牛人彌諾陶洛斯2]` / `[俄雷恩]` / `[獨眼巨人庫克羅普斯]` / `[獅子涅墨亞]` / `[飛馬珀伽索斯]` / `[公牛克里特]` / `[女妖塞壬]` / `[巨龍拉冬]` / `[百眼怪阿爾戈斯]` / `[大地之神蓋亞]` / `[水蛇許德拉]` | tên server đặt trong ngoặc vuông = tên mục theo server trong `Buff.txt`, `CounterattackPeoples.txt` (nghĩa như các dòng trên) | — | [05](05-game-config-chien-dau-va-vat-pham.md) |

## 3. Nghề (class)

| Nguyên văn (code) | Tiếng Việt | Tiếng Anh (nếu biết) | Xuất hiện ở |
|---|---|---|---|
| `王族` | Hoàng tộc | Prince / Princess (Royal) | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `骑士` | Hiệp sĩ | Knight | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `妖精` | Elf (Tiên tộc) | Elf | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `法师` / `魔法师` | Pháp sư | Wizard (Mage) | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `_骑士` / `_王族` / `_法师` | hậu tố tên mục kỹ năng theo nghề (không cần đổi, mọi nghề dùng `[技能配置_妖精]`) | — | [04](04-baseconfig.md) |
| `职业` | nghề (class); trong `[创建角色配置]`: `1` Hoàng tộc, `2` Hiệp sĩ, `3` Elf, `4` Pháp sư | class | [04](04-baseconfig.md) |
| `近战职业` | nghề cận chiến | melee class | [02](02-nhat-ky-cap-nhat.md) |

## 4. Vật phẩm

| Nguyên văn (code) | Tiếng Việt | Tiếng Anh (nếu biết) | Xuất hiện ở |
|---|---|---|---|
| `说话卷` / `说话卷轴` / `說話卷軸` | cuộn dịch chuyển về Talking Island | Talking Island teleport scroll | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `回城卷` | cuộn về thành | Scroll of Return (town) | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `随机卷` | cuộn dịch chuyển ngẫu nhiên | random teleport scroll | [04](04-baseconfig.md) |
| `瞬間移動卷軸` / `瞬移卷轴` | cuộn dịch chuyển tức thời (dịch chuyển ngẫu nhiên) | Scroll of Teleportation | [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `返回卷軸` | cuộn trở về (cuộn về thành) | Scroll of Return | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `活力返回卷軸` | cuộn trở về Hoạt lực | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `活力瞬間移動卷軸` | cuộn dịch chuyển tức thời Hoạt lực | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `地監記憶書` | Sách ghi nhớ hầm ngục (dịch chuyển thẳng tới tầng hầm ngục) | Dungeon memory book | [01](01-huong-dan-su-dung.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `地監記憶書箱` | Hộp Sách ghi nhớ hầm ngục | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `变身卷轴` / `变身卷` | cuộn biến hình (cách gọi chung trong ghi chú) | Scroll of Polymorph | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md) |
| `變形卷軸` | cuộn biến hình (loại mua hoặc rơi ra) | Scroll of Polymorph | [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `輕量變形卷軸` | cuộn biến hình hạng nhẹ (loại được tặng) | — | [04](04-baseconfig.md) |
| `活力變形卷軸` | cuộn biến hình Hoạt lực | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `復活卷軸` | cuộn hồi sinh | Scroll of Resurrection | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `對盔甲施法的卷軸` | cuộn phù phép giáp (dùng để cường hóa giáp) | Scroll of Enchant Armor | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `對武器施法的卷軸` | cuộn phù phép vũ khí | Scroll of Enchant Weapon | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `武器強化卷軸` | cuộn cường hóa vũ khí | — | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `防具強化卷軸` | cuộn cường hóa giáp | — | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `祝福武器強化卷軸` | cuộn cường hóa vũ khí được ban phước | Blessed weapon enchant scroll | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `祝福防具強化卷軸` | cuộn cường hóa giáp được ban phước | Blessed armor enchant scroll | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `歐琳` | Orim (?) (tên riêng trong tên cuộn) | Orim (?) | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `歐琳飾品強化卷軸` | cuộn cường hóa trang sức Orim (?) | Orim's accessory enchant scroll (?) | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `祝福歐琳飾品強化卷軸` | cuộn cường hóa trang sức Orim được ban phước (?) | — | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `倫提斯` | Roomtis (?) (bông tai) | Roomtis (?) | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `倫提斯耳環強化卷軸` | cuộn cường hóa bông tai Roomtis (?) | — | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `倫提斯安全強化卷軸` | cuộn cường hóa an toàn Roomtis (?) | — | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `倫提斯墜飾安全強化卷軸` | cuộn cường hóa an toàn mặt dây chuyền Roomtis (?) | — | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `斯奈普` | Snapper (?) (nhẫn) | Snapper (?) | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `斯奈普強化卷軸` | cuộn cường hóa Snapper (?) | — | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `斯奈普安全強化卷軸` | cuộn cường hóa an toàn Snapper (?) | — | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `蛇夫座` | Xà Phu (chòm sao) | Ophiuchus | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `蛇夫座強化卷軸` | cuộn cường hóa Xà Phu | Ophiuchus enchant scroll | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `覺醒徽章強化卷` | cuộn cường hóa Huy hiệu Thức tỉnh (tên kết thúc bằng `卷`) | Awakening badge enchant scroll | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `飾品` | trang sức (phụ kiện) | accessory | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `耳環` | bông tai | earring | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `墜飾` | mặt dây chuyền | pendant | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `安全強化` | cường hóa an toàn (thất bại không mất đồ) | safe enchant | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `卷` / `卷軸` / `軸` | cuộn (giấy phép); tên `覺醒徽章強化卷` thiếu chữ `軸` | scroll | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `金屬塊` | Khối kim loại | Metal block | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `自我加速藥水` | Thuốc tự tăng tốc | Haste Potion (Green Potion) | [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `輕量自我加速藥水` | Thuốc tự tăng tốc hạng nhẹ | — | [04](04-baseconfig.md) |
| `強化自我加速藥水` | Thuốc tự tăng tốc cường hóa | Greater Haste Potion | [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `活力自我加速藥水` | Thuốc tự tăng tốc Hoạt lực | Vitality Haste Potion | [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `精靈餅乾` | Bánh quy Tiên (tăng tốc đánh của Elf) | Elven Wafer | [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `輕量精靈餅乾` | Bánh quy Tiên hạng nhẹ | — | [04](04-baseconfig.md) |
| `活力精靈餅乾` | Bánh quy Tiên Hoạt lực | — | [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `勇敢藥水` | Thuốc Dũng cảm (tăng tốc đánh) | Brave Potion | [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `輕量勇敢藥水` | Thuốc Dũng cảm hạng nhẹ | — | [04](04-baseconfig.md) |
| `活力勇敢藥水` | Thuốc Dũng cảm Hoạt lực | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `惡魔之血` | Máu Ác quỷ (?) | Devil's Blood (?) | [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `輕量惡魔之血` | Máu Ác quỷ hạng nhẹ (?) | — | [04](04-baseconfig.md) |
| `活力惡魔之血` | Máu Ác quỷ Hoạt lực (?) | — | [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `藍色藥水` | Thuốc xanh lam (tăng hồi mana) | Blue Potion | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `活力藍色藥水` | Thuốc xanh lam Hoạt lực | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `魔力回復藥水` | Thuốc hồi phục ma lực | Mana recovery potion | [04](04-baseconfig.md) |
| `活力慎重藥水` | Thuốc Thận trọng Hoạt lực | Potion of Wisdom | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `治癒藥水` | Thuốc trị liệu (hồi máu) | Healing Potion | [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `輕量紅色藥水` | Thuốc đỏ hạng nhẹ (hồi máu) | Light Red Potion | [04](04-baseconfig.md) |
| `活力紅色藥水` | Thuốc đỏ Hoạt lực (hồi máu) | Vitality Red Potion | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `解毒藥水` | Thuốc giải độc | Cure Poison Potion | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `翡翠藥水` | Thuốc Phỉ thúy (?) | Emerald Potion (?) | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `活力` / `活力…` | "Hoạt lực": tiền tố các vật phẩm đổi được từ sự kiện Trứng màu | Vitality | [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `彩蛋` | trứng màu (vật phẩm và tên sự kiện) | Easter egg | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `產下黃金蛋的貝雷帽` | Mũ nồi đẻ trứng vàng | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `產下黃金蛋的草帽` | Mũ rơm đẻ trứng vàng | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `冰之女王的神秘方塊` | Khối bí ẩn của Nữ hoàng Băng | Ice Queen's Mysterious Cube | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `神秘方塊` | Khối bí ẩn | Mysterious Cube | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `因納得立的寶箱(30次)` | Rương báu Innadril (30 lần) | Innadril treasure chest | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `(30次)` | "(30 lần)", một phần của tên vật phẩm | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `矮人的齒輪` | Bánh răng của Người lùn | Dwarf's Gear | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `GM的便當` / `便當` | Hộp cơm của GM (quà tặng) | GM's Lunch Box | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `摺紙傳令鳥` | Chim đưa tin gấp giấy (?) (dùng cho tính năng tố cáo) | Origami messenger bird (?) | [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `安特的樹枝` | Cành cây của Ent | Ent's Branch | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `伊娃的祝福` | Phước lành của Eva | Blessing of Eva | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `獵人之弓` | Cung Thợ săn | Hunter's Bow | [01](01-huong-dan-su-dung.md), [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `精靈弓` | Cung Tiên | Elven Bow | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `十字弓` | Nỏ | Crossbow | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `尤米弓` | Cung Yumi | Yumi Bow | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `弓` | Cung | Bow | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `箭` | tên (mũi tên) | Arrow | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `銀箭` | tên bạc | Silver Arrow | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `箭头` | mũi tên (trong `血盟取箭头`) | arrow | [02](02-nhat-ky-cap-nhat.md) |
| `敏捷魔法頭盔` | Mũ phép thuật Nhanh nhẹn | Magic Helm of Agility | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `力量魔法頭盔` | Mũ phép thuật Sức mạnh | Magic Helm of Strength | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `敏捷头盔` | mũ Nhanh nhẹn (cách gọi tắt; giúp Hoàng tộc/Hiệp sĩ niệm `加速術`) | Agility helm | [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `头盔` / `頭盔` | mũ giáp | Helmet | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `盾` | Khiên | Shield | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `小盾牌` | Khiên nhỏ | Small Shield | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `阿克海盾牌` | Khiên Akhai (?) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `短劍` | Đoản kiếm | Dagger / Short Sword | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `長劍` | Trường kiếm | Long Sword | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `闊劍` | Kiếm bản rộng | Broad Sword | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `彎刀` | Đao cong | Scimitar / Cutlass | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `矛` | Giáo | Spear | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `巴迪須` | Bardiche (rìu cán dài) | Bardiche | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `斧` | Rìu | Axe | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `侏儒鐵斧` | Rìu sắt Người lùn | Dwarvish Iron Axe | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `木棒` | Gậy gỗ | Club | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `釘錘` | Chùy gai | Mace / Morning Star | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `弗萊爾` | Chùy xích | Flail | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `烏木魔杖` | Gậy phép gỗ mun | Ebony Wand | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `松木魔杖` | Gậy phép gỗ thông | Pine Wand | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `亞連` | "Á Liên", có lẽ là một loại vũ khí cấp thấp (?) | — | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `皮甲` | Giáp da | Leather Armor | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `銀釘皮甲` | Giáp da đinh bạc | Studded Leather Armor | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `環甲` | Giáp vòng | Ring Mail | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `鏈甲` | Giáp xích | Chain Mail | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `斗篷` | Áo choàng | Cloak | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `侏儒斗篷` | Áo choàng Người lùn | Dwarvish Cloak | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `抗魔法斗篷` | Áo choàng kháng phép | Cloak of Magic Resistance | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `侏儒鐵盔` | Mũ sắt Người lùn | Dwarvish Iron Helm | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `短統靴` | Ủng cổ ngắn | Low Boots | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `長靴` | Ủng cổ cao | High Boots | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `歐西斯` | Orcish (?) (tiền tố trang bị) | Orcish (?) | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `歐西斯頭盔` | Mũ Orcish (?) | Orcish Helm (?) | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `歐西斯環甲` | Giáp vòng Orcish (?) | Orcish Ring Mail (?) | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `歐西斯鏈甲` | Giáp xích Orcish (?) | Orcish Chain Mail (?) | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `歐西斯匕首` | Dao găm Orcish (?) | Orcish Dagger (?) | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `歐西斯弓` | Cung Orcish (?) | Orcish Bow (?) | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `歐西斯之矛` | Giáo Orcish (?) | Orcish Spear (?) | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `歐西斯斗篷` | Áo choàng Orcish (?) | Orcish Cloak (?) | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `歐西斯短劍` | Đoản kiếm Orcish (?) | Orcish Short Sword (?) | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `保護罩` | (vật phẩm trong `拾取过滤`) Khiên bảo vệ (?), cùng tên với phép `保護罩`; xem mục Kỹ năng | — | [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `燈` | Đèn | Lamp / Lantern | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `漂浮之眼肉` | Thịt Mắt lơ lửng | Floating Eye Meat | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `純粹的米索莉塊` | Khối Mithril tinh khiết | Pure Mithril | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `肉` | Thịt (ăn để giữ độ no) | Meat | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `胡蘿蔔` | Cà rốt | Carrot | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `蘋果` | Táo | Apple | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `檸檬` | Chanh | Lemon | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `香蕉` | Chuối | Banana | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `蛋` | Trứng | Egg | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `橘子` | Quýt | Orange | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `沙漏` | đồng hồ cát (server Đài Loan dùng cho bản đồ quán net) (?) | Hourglass | [01](01-huong-dan-su-dung.md) |
| `宝物` / `宝物名字` | bảo vật; tên bảo vật (hiển thị trên bảng điều khiển) | treasure | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `金疮药` / `金疮药1` | "Kim sang dược" (tên mẫu, không phải vật phẩm Lineage) | — | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `太阳水` / `太阳水1` | "Nước Mặt Trời" (tên mẫu) | — | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `太阳神` | "Thần Mặt Trời" (tên mẫu trong `TreasureName.txt`) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `物品名` / `物品名字` | tên vật phẩm (chỗ trống mẫu trong định dạng) | item name | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |

## 5. Quái vật & NPC

| Nguyên văn (code) | Tiếng Việt | Tiếng Anh (nếu biết) | Xuất hiện ở |
|---|---|---|---|
| `安特` | Ent (người cây) | Ent | [01](01-huong-dan-su-dung.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `潘` | Pan | Pan | [01](01-huong-dan-su-dung.md) |
| `巡守` | Lính tuần tra | Patrol | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `史萊姆` | Slime | Slime | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `長老` | Trưởng lão (NPC) | Elder | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `警衛` | Lính gác | Guard | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `奇岩警衛` | Lính gác Giran | Giran Guard | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `肯特城警衛` | Lính gác thành Kent | Kent Castle Guard | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `風木城警衛` | Lính gác thành Windawood | Windawood Castle Guard | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `海音警衛` | Lính gác Heine | Heine Guard | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `侏儒警衛` | Lính gác Người lùn | Dwarf Guard | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `城堡守衛` | Vệ binh lâu đài | Castle Guard | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `守門人` | Người gác cổng | Gatekeeper | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `亞丁警衛` | Lính gác Aden | Aden Guard | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `亞丁近衛隊` | Đội cận vệ Aden | Aden Royal Guard | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `漂浮之眼` | Mắt lơ lửng | Floating Eye | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `克特` | Kurtz (?) | Kurtz (?) | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `石頭高崙` | Golem đá | Stone Golem | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `飛龍` | Phi long (rồng bay) | Drake | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `青蛙` | Ếch | Frog | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `兔子` | Thỏ | Rabbit | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `鹿` | Hươu | Deer | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `強盜` | Cướp | Bandit | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `魚` | Cá | Fish | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `牧羊犬` | Chó chăn cừu | Shepherd Dog | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `杜賓狗` | Chó Doberman | Doberman | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `葛林` | Gremlin (?) | Gremlin (?) | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `史巴托` | Spartoi (?) (quái biết ẩn mình) | Spartoi (?) | [02](02-nhat-ky-cap-nhat.md) |
| `冰之女王` | Nữ hoàng Băng (boss sự kiện) | Ice Queen | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `远程怪物` | quái tầm xa | ranged monster | [02](02-nhat-ky-cap-nhat.md) |
| `狗` / `反击狗` | "chó" = thú cưng của người chơi khác (?); `反击狗` = phản công chó | pet | [04](04-baseconfig.md) |
| `法师宝宝` | "cưng" của Pháp sư (quái do Pháp sư triệu hồi/thuần phục) (?) | summon / tamed pet (?) | [04](04-baseconfig.md) |
| `怪物名21` / `怪物名12111` / `怪物A` / `怪物B` / `怪物C` | tên quái mẫu ("tên quái 21", "quái A"…) | — | [04](04-baseconfig.md) |
| `艾伊拉` | NPC Aira (?) (bán `摺紙傳令鳥` ở Talking Island) | Aira (?) | [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `寵物保管人` | Người giữ thú cưng (NPC) | Pet keeper | [02](02-nhat-ky-cap-nhat.md) |
| `潘朵拉` / `[潘朵拉]` | NPC Pandora (thương nhân Talking Island) | Pandora | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `馬修` / `[馬修]` | NPC Matthew (?) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `巴辛` / `[巴辛]` | NPC Bassin (?) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `露西` / `[露西]` | NPC Lucy (làng Gludin) | Lucy | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `凱蒂` / `[凱蒂]` | NPC Katie (?) (làng Gludin) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `邁爾` / `[邁爾]` | NPC Mayer (?) (làng Giran) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `溫諾` / `[溫諾]` | NPC Winno (?) (làng Giran) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `范吉爾` / `[范吉爾]` | NPC Vangel (?) (làng Giran) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `愛弗特` / `[愛弗特]` | NPC Evert (?) (làng Giran) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `瑪格瑞特` / `[瑪格瑞特]` | NPC Margaret (làng Giran, thực phẩm) | Margaret | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `傑克森` / `[傑克森]` | NPC Jackson (làng Woodbec) | Jackson | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `索拉雅` / `[索拉雅]` | NPC Soraya (làng Kent) | Soraya | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `安迪` / `[安迪]` | NPC Andy (làng Kent) | Andy | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `艾米娜` / `[艾米娜]` | NPC Amina (?) (làng Windawood) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `梅林` / `[梅林]` | NPC Merlin (làng Hiệp sĩ Bạc) | Merlin | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `格林` / `[格林]` | NPC Glen (?) (làng Hiệp sĩ Bạc) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `比特` / `[比特]` | NPC Bitt (?) (làng Heine) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `須凡` / `[須凡]` | NPC Sven (?) (làng Heine) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `蓓莉` / `[蓓莉]` | NPC Belly (?) (làng Werldern) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `瑞福` / `[瑞福]` | NPC Reef (?) (làng Werldern) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `畢伍斯` / `[畢伍斯]` | NPC Bius (?) (làng Oren) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `曼德拉` / `[曼德拉]` | NPC Mandra (?) (làng Oren) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `拉溫` / `[拉溫]` | NPC Rawin (?) (làng Aden) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `戴夫曼` / `[戴夫曼]` | NPC Daveman (?) (làng Aden) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `菲卡` / `[菲卡]` | NPC Fika (?) (làng Aden) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |

## 6. Kỹ năng

| Nguyên văn (code) | Tiếng Việt | Tiếng Anh (nếu biết) | Xuất hiện ở |
|---|---|---|---|
| `加速術` / `加速术` | Tăng tốc (phép) | Haste | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `加速` | tăng tốc (Haste nói chung) | Haste | [02](02-nhat-ky-cap-nhat.md) |
| `保護罩` | Khiên bảo vệ (phép) | Shield | [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `負重強化` | Tăng sức mang vác | Decrease Weight | [04](04-baseconfig.md) |
| `擬似魔法武器` | Vũ khí ma pháp giả | Enchant Weapon | [04](04-baseconfig.md) |
| `神聖武器` | Vũ khí thần thánh | Holy Weapon | [04](04-baseconfig.md) |
| `初級治癒術` | Trị liệu sơ cấp | Lesser Heal | [04](04-baseconfig.md) |
| `中級治癒術` | Trị liệu trung cấp | Heal | [04](04-baseconfig.md) |
| `心靈轉換` / `心灵转换` | Chuyển hóa tâm linh (đổi máu lấy mana) | Body to Mind | [04](04-baseconfig.md) |
| `魔法防禦` | Phòng ngự ma pháp | Resist Magic | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `通暢氣脈術` | Thông suốt khí mạch (tăng Nhanh nhẹn) | Physical Enchant: DEX | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `體魄強健術` | Cường kiện thể phách (tăng Sức mạnh) | Physical Enchant: STR | [04](04-baseconfig.md) |
| `大地防護` | Bảo hộ Đất (tăng giáp) | Earth Skin | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `大地防御` | Phòng ngự Đất; có lẽ chính là `大地防護` (?) | Earth Skin (?) | [02](02-nhat-ky-cap-nhat.md) |
| `風之疾走` | Phong tật tẩu (chạy nhanh như gió) | Wind Walk | [04](04-baseconfig.md) |
| `風之神射` | Thần xạ của gió | Wind Shot | [04](04-baseconfig.md) |
| `淨化精神` | Tịnh hóa tinh thần | Clear Mind | [04](04-baseconfig.md) |
| `屬性防禦` | Phòng ngự thuộc tính | Resist Elemental | [04](04-baseconfig.md) |
| `單屬性防禦` | Phòng ngự đơn thuộc tính | Protection from Elemental (?) | [04](04-baseconfig.md) |
| `火焰武器` | Vũ khí lửa | Fire Weapon | [04](04-baseconfig.md) |
| `暴風之眼` | Mắt bão | Storm Eye | [04](04-baseconfig.md) |
| `世界樹的呼喚` | Tiếng gọi Cây Thế giới (phép Elf đưa về Cây Thế giới) | Teleport to Mother | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `传送术` | phép dịch chuyển | Teleport | [04](04-baseconfig.md) |
| `无所遁形` | phép làm lộ mục tiêu ẩn | Detection | [02](02-nhat-ky-cap-nhat.md) |
| `转血` / `转蓝` | "chuyển máu" / "chuyển mana" (dùng kỹ năng đổi máu ↔ mana) | — | [04](04-baseconfig.md) |
| `某某技能` | "kỹ năng XYZ" (chỗ trống mẫu) | — | [05](05-game-config-chien-dau-va-vat-pham.md) |

## 7. Thuật ngữ của bot & cấu hình

### 7.1 Thuật ngữ chung

| Nguyên văn (code) | Tiếng Việt | Tiếng Anh (nếu biết) | Xuất hiện ở |
|---|---|---|---|
| `天堂经典版` | Lineage Classic (nghĩa đen "Thiên Đường bản Kinh điển") | Lineage Classic | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `使用说明.txt` | file "Hướng dẫn sử dụng" (thư mục gốc và thư mục `组队服务器`) | usage guide | [01](01-huong-dan-su-dung.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `更新说明.txt` | file "Ghi chú cập nhật" (nhật ký thay đổi) | changelog | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `大中控.exe` / `大中控/大中控.exe` | chương trình trung tâm điều khiển lớn | central console program | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `组队服务器.exe` / `组队服务器/组队服务器.exe` | chương trình server tổ đội LAN | party server program | [01](01-huong-dan-su-dung.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `挂机范围` | phạm vi treo máy (vùng quanh tọa độ đánh quái) | farming range | [04](04-baseconfig.md) |
| `临时点` | điểm tạm (điểm đáp sau khi dịch chuyển chạy trốn, dùng để lánh nạn) | temporary spot | [04](04-baseconfig.md) |
| `拉黑` | đưa vào danh sách đen (tạm cấm điểm treo máy) | blacklist | [04](04-baseconfig.md) |
| `寻路` | tìm đường | pathfinding | [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `紫P` / `紫p` | launcher Purple của NCSOFT | Purple launcher | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md) |
| `登录器` / `紫p登录器` | launcher (trình đăng nhập) | launcher | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `控制台` | bảng điều khiển (console) của bot, tức `Bd.exe` | console | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `脚本控制台` | bảng điều khiển của script (= `控制台`) | script console | [01](01-huong-dan-su-dung.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `大中控` | trung tâm điều khiển lớn (quản lý nhiều máy/tài khoản) | central console | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `中控` | trung tâm điều khiển (= `大中控`) | central console | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `中控台` | bàn trung tâm điều khiển; "ZKT" trong `ZKT.ini` có lẽ là viết tắt (?) | — | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `组队服务器` | server tổ đội (LAN) | party server | [01](01-huong-dan-su-dung.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md) |
| `服务端` | phía server (chương trình server) | server side | [01](01-huong-dan-su-dung.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `客户机` | máy khách | client machine | [01](01-huong-dan-su-dung.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `局域网` | mạng LAN (mạng nội bộ) | LAN | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md) |
| `端口` | cổng mạng | port | [01](01-huong-dan-su-dung.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `上号` | đưa tài khoản vào game (đăng nhập) | log an account in | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `掉线` | rớt mạng | disconnect | [02](02-nhat-ky-cap-nhat.md) |
| `多开` | mở nhiều cửa sổ game | multi-client | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `挂机` | treo máy (auto farm); "gj" trong `gj.txt` | AFK farming / botting | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `挂机点` | điểm treo máy | farming spot | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `打怪` | đánh quái | fight monsters | [04](04-baseconfig.md) |
| `坐标` | tọa độ | coordinates | [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `进洞坐标` | tọa độ vào hang | cave entrance coordinates | [01](01-huong-dan-su-dung.md) |
| `回城` | về thành | return to town | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `仓库` | kho đồ | warehouse | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md) |
| `个人仓库存入` / `个人仓库取出` | gửi đồ vào / lấy đồ ra kho cá nhân | personal warehouse | [02](02-nhat-ky-cap-nhat.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `加值仓库` | kho nạp (vật phẩm nạp tiền / quà tặng) (?) | premium warehouse (?) | [02](02-nhat-ky-cap-nhat.md) |
| `血盟` | huyết minh (clan) | Blood Pledge (clan) | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `血盟取物品` | lấy đồ từ kho huyết minh | — | [02](02-nhat-ky-cap-nhat.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `血盟取箭头` | lấy mũi tên từ kho huyết minh | — | [02](02-nhat-ky-cap-nhat.md) |
| `血量` | máu (HP) | HP | [02](02-nhat-ky-cap-nhat.md) |
| `蓝量` | mana (MP) | MP | [02](02-nhat-ky-cap-nhat.md) |
| `没蓝` / `低蓝量` | hết mana / mana thấp | out of / low MP | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `背包` | túi đồ | inventory | [02](02-nhat-ky-cap-nhat.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `格子` | ô (trong túi đồ) | slot | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `饱食度` | độ no | satiety | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `吃肉` | ăn thịt (để giữ độ no) | eat meat | [02](02-nhat-ky-cap-nhat.md) |
| `键鼠模式` | chế độ bàn phím-chuột (điều khiển trực tiếp trên màn hình) | keyboard-mouse mode | [01](01-huong-dan-su-dung.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md) |
| `前台键鼠模式` / `前台` | chế độ bàn phím-chuột tiền cảnh (foreground) | foreground mode | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `内存模式` | chế độ bộ nhớ (đọc/ghi bộ nhớ game) | memory mode | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md) |
| `内存…` | các khóa `内存…` = làm thao tác đó bằng chế độ bộ nhớ | — | [01](01-huong-dan-su-dung.md) |
| `config\键鼠模式` | khóa `键鼠模式` trong thư mục `config` (file `config.ini`) | — | [01](01-huong-dan-su-dung.md), [04](04-baseconfig.md) |
| `协议登录` | đăng nhập bằng giao thức (không qua giao diện launcher) | protocol login | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `模拟登录` | đăng nhập mô phỏng (bấm trên giao diện launcher) | simulated login | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `验证` / `账号被验证` | xác minh (tài khoản bị game yêu cầu xác minh) | verification | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `假验证` / `假认证` | "xác thực giả" (màn hình xác thực không bắt buộc lúc đăng nhập) (?) | — | [04](04-baseconfig.md) |
| `等待` | trạng thái "chờ" của tài khoản trên bảng điều khiển | waiting | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `账号` / `密码` | tài khoản / mật khẩu | account / password | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `账号1` / `密码1` / `账号2----密码2` | dòng mẫu trong `Account.txt` ("tài khoản 1, mật khẩu 1"…) | — | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `反击` | phản công | counterattack | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `过滤` | lọc (loại ra) | filter | [01](01-huong-dan-su-dung.md) |
| `发呆` | đứng đơ (nhân vật đứng yên không làm gì) | idle / stuck | [02](02-nhat-ky-cap-nhat.md) |
| `小号` | acc phụ | alt account | [02](02-nhat-ky-cap-nhat.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `主号` / `buff主号` | acc chính; acc chính chuyên buff | main account / buffer | [02](02-nhat-ky-cap-nhat.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `小号加buff` | acc phụ được gọi về nhận buff | — | [02](02-nhat-ky-cap-nhat.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `红名` | tên đỏ (do PK) | red name (Chaotic) | [02](02-nhat-ky-cap-nhat.md) |
| `白名单` / `黑名单` | danh sách trắng (không đánh) / danh sách đen (cần đánh) | whitelist / blacklist | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `相性` | chỉ số thiện/ác (?) | alignment (?) | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `集火` | tập trung đánh một mục tiêu | focus fire | [02](02-nhat-ky-cap-nhat.md) |
| `队长` | đội trưởng | party leader | [02](02-nhat-ky-cap-nhat.md) |
| `组队` / `一直组队` | tổ đội; tổ đội liên tục (lỗi đã sửa) | party | [02](02-nhat-ky-cap-nhat.md) |
| `倒货` | chuyển hàng (giao vàng/đồ sang acc nhận) | item transfer | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `收货人` / `收货人1` / `收货人2` / `收货人3` | người nhận hàng; tên mẫu người nhận 1, 2, 3 | receiver | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `摆摊人` / `摆摊人1` / `摆摊人2` / `摆摊人3` | người bày sạp; tên mẫu 1, 2, 3 | shop (stall) character | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `张三111` / `李四111` | tên nhân vật mẫu (như "Nguyễn Văn A") | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `角色名1` / `角色名2` | "tên nhân vật 1, 2" (mẫu) | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `玩家A` / `玩家B` / `玩家C` | "người chơi A, B, C" (mẫu) | — | [04](04-baseconfig.md) |
| `血盟名字1` / `血盟名字2` / `血盟名字3` | "tên huyết minh 1, 2, 3" (mẫu) | — | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `定点打怪` | đánh quái tại điểm cố định | — | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `定点挂机` | treo máy tại điểm cố định (khóa trong `gj.txt`) | — | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `内挂` / `内挂挂机` | "nội quải": chế độ auto có sẵn trong game (?) | built-in auto-hunt (?) | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `瞬移` | dịch chuyển tức thời (viết tắt của 瞬間移動) | teleport | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `传送` | dịch chuyển | teleport | [02](02-nhat-ky-cap-nhat.md) |
| `随机传送` | dịch chuyển ngẫu nhiên | random teleport | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `封号` / `封号检测` | khóa tài khoản; cơ chế phát hiện để khóa tài khoản | ban / ban detection | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `过检测` / `优化过检测` / `针对封号检测进行有效处理` | "vượt kiểm tra" (lời quảng cáo của tác giả, không bảo đảm) | — | [02](02-nhat-ky-cap-nhat.md) |
| `单进程ip代理加速` | tăng tốc bằng proxy IP riêng cho từng tiến trình game | per-process IP proxy | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `导入ip` | nhập IP (menu chuột phải trên bảng điều khiển) | import IP | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `远程同步专家` | phần mềm "Remote Sync Expert" (Chuyên gia đồng bộ từ xa) (?) | Remote Sync Expert (?) | [01](01-huong-dan-su-dung.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `游戏进程` | tiến trình game | game process | [02](02-nhat-ky-cap-nhat.md) |
| `韩文系统` | Windows tiếng Hàn | Korean Windows | [02](02-nhat-ky-cap-nhat.md) |
| `蓝屏` | màn hình xanh (BSOD) | blue screen | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `桌面` | màn hình (desktop) | desktop | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `计算机名` | tên máy tính | computer name | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `崩溃` | bị crash | crash | [02](02-nhat-ky-cap-nhat.md) |
| `用户协议` | điều khoản người dùng | user agreement | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `新号` | tài khoản mới | new account | [02](02-nhat-ky-cap-nhat.md) |
| `创建角色加点` | cộng điểm khi tạo nhân vật | stat allocation | [02](02-nhat-ky-cap-nhat.md) |
| `隔墙` / `隔树射箭` | đánh qua tường; bắn tên khi có cây chắn | — | [02](02-nhat-ky-cap-nhat.md) |
| `立马飞走` | "bay đi ngay" (dịch chuyển đi ngay) | — | [02](02-nhat-ky-cap-nhat.md) |
| `活动` | sự kiện (event) | event | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `冰之女王活动` | sự kiện Nữ hoàng Băng | Ice Queen event | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `踢` | "đá", ở đây hiểu là đánh tay không (?) | — | [01](01-huong-dan-su-dung.md) |
| `随游戏更新` | cập nhật theo bản game mới | — | [02](02-nhat-ky-cap-nhat.md) |
| `更新` | cập nhật | update | [02](02-nhat-ky-cap-nhat.md) |
| `需要替换EXE` / `需要替换lua` | cần thay EXE / cần thay Lua | — | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `下载lua即可` / `可下载lua` | chỉ cần tải Lua / có thể tải riêng Lua | — | [02](02-nhat-ky-cap-nhat.md) |
| `完整包` | gói đầy đủ | full package | [02](02-nhat-ky-cap-nhat.md) |
| `注` | chú ý, ghi chú | note | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `修复…的问题` | sửa lỗi … | fix | [02](02-nhat-ky-cap-nhat.md) |
| `增加` | thêm (tính năng/cài đặt) | add | [02](02-nhat-ky-cap-nhat.md) |
| `增加支持…` | bổ sung hỗ trợ… | — | [01](01-huong-dan-su-dung.md) |
| `增加新地图` | thêm bản đồ mới | — | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md) |
| `设置方法如下` / `如下设置` / `这样设置` | cách cài đặt như sau / cài như thế này | — | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md) |
| `具体看文件说明` / `具体看里面说明` | xem chi tiết trong file / bên trong file | — | [02](02-nhat-ky-cap-nhat.md) |
| `默认开启` / `此功能为默认开启` | mặc định bật | enabled by default | [02](02-nhat-ky-cap-nhat.md) |
| `以此类推` | cứ thế suy ra | and so on | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `开启` | bật (công tắc chính của một mục) | enable | [01](01-huong-dan-su-dung.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `本机` | máy này | this machine | [04](04-baseconfig.md) |
| `触发` | kích hoạt | trigger | [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `秒` | giây | second | [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `分钟` / `15分钟` | phút; "15 phút" | minute | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `百分比` | phần trăm | percent | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `用完就触发` / `用完马上触发` / `角色在村庄才触发` | dùng hết là kích hoạt ngay / chỉ kích hoạt khi nhân vật ở làng | — | [02](02-nhat-ky-cap-nhat.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `取出数量` / `达到数量触发取出` | số lượng lấy ra; số lượng (trong túi) để kích hoạt lấy | — | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `在` / `再` | lỗi chính tả: `在` viết thay cho `再` ("rồi mới"); trong tên khóa vẫn phải giữ `在` | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `不在` / `不再` | lỗi chính tả: `不在` viết thay cho `不再` ("không … nữa") | — | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `卡主` / `卡住` | lỗi chính tả: `卡主` viết thay cho `卡住` ("bị kẹt") | — | [02](02-nhat-ky-cap-nhat.md) |
| `够买` / `购买` | lỗi chính tả: `够买` viết thay cho `购买` ("mua") | — | [02](02-nhat-ky-cap-nhat.md) |
| `登录` / `登陆` | đăng nhập (`登陆` là cách viết khác, giữ nguyên trong tên khóa) | login | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |

### 7.2 Tên mục `[...]` trong file cấu hình

| Nguyên văn (code) | Tiếng Việt | Tiếng Anh (nếu biết) | Xuất hiện ở |
|---|---|---|---|
| `[登录配置]` | Cấu hình đăng nhập (`BaseConfig.txt`) | — | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `[角色保护]` | Bảo vệ nhân vật | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `[NPC特殊购买]` | Mua đặc biệt ở NPC | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `[挂机全局配置]` | Cấu hình treo máy toàn cục | — | [01](01-huong-dan-su-dung.md), [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `[触发随机传送配置]` / `触发随机传送配置` | Kích hoạt dịch chuyển ngẫu nhiên | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `[触发回城休息配置]` | Kích hoạt về thành nghỉ / né tránh | — | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md) |
| `[休息配置]` | Lịch nghỉ | — | [04](04-baseconfig.md) |
| `[按时间切换挂机配置]` | Đổi cấu hình treo máy theo giờ | — | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `[键鼠模式附加内存功能]` | Chức năng bộ nhớ bổ sung cho chế độ bàn phím-chuột | — | [01](01-huong-dan-su-dung.md), [04](04-baseconfig.md) |
| `[基础配置]` | Cấu hình cơ bản | — | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `[创建角色配置]` | Cấu hình tạo nhân vật | — | [04](04-baseconfig.md) |
| `[使用加速药水]` | Dùng thuốc tăng tốc | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `[解释技能配置说明 这里为无效字段]` | Giải thích cách cấu hình kỹ năng (mục không có hiệu lực) | — | [04](04-baseconfig.md) |
| `[技能配置_妖精]` | Cấu hình kỹ năng (Elf; dùng chung cho mọi nghề) | — | [04](04-baseconfig.md) |
| `[吃药配置]` | Cấu hình uống thuốc | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `[反击配置]` | Cấu hình phản công | — | [04](04-baseconfig.md) |
| `[组队配置]` | Tổ đội trên cùng máy | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `[局域网组队配置]` | Tổ đội qua mạng LAN | — | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md) |
| `[config]` | Mục "cấu hình" (nhiều file) | config | [01](01-huong-dan-su-dung.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `[中控配置]` | Cấu hình trung tâm điều khiển (`大中控/Data/Config.ini`) | — | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `[冰之女王活动]` | Sự kiện Nữ hoàng Băng | — | [03](03-cau-hinh-chung-va-cau-truc-goi.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `[彩蛋活动]` | Sự kiện Trứng màu | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `[血盟加入]` | Gia nhập huyết minh (theo server) | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `[全局小号列表]` / `全局小号列表` | Danh sách acc phụ toàn cục | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `[白名单列表]` | Danh sách trắng | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `[黑名单列表]` / `黑名单列表` | Danh sách đen | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `[怪物过滤]` | Lọc quái (không đánh) | — | [01](01-huong-dan-su-dung.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `[反击怪物]` | Quái phản công | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `[拾取过滤]` | Lọc nhặt đồ (không nhặt) | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `[收货人角色名]` | Tên nhân vật người nhận hàng | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `[摆摊人角色名]` | Tên nhân vật người bày sạp | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `[1]` / `[5]` / `[7]` / `[8]` / `[10]` / `[15]` | mốc cấp độ nhân vật trong `gj.txt` / `SellBuy.txt` (?) | level bracket (?) | [01](01-huong-dan-su-dung.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |

### 7.3 Khóa cấu hình (tên bên trái dấu `=`)

Chỉ đổi **giá trị** bên phải dấu `=`; tên khóa phải giữ nguyên từng chữ. Ý nghĩa chi tiết của từng giá trị xem ở file được ghi trong cột cuối.

| Nguyên văn (code) | Tiếng Việt | Tiếng Anh (nếu biết) | Xuất hiện ở |
|---|---|---|---|
| `登录器路径` | đường dẫn thư mục launcher Purple (`config.ini`) | — | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `协议登录等待最大时间` | thời gian chờ tối đa khi đăng nhập bằng giao thức | — | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `模拟登录等待最大时间` | thời gian chờ tối đa khi đăng nhập mô phỏng | — | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `每次登陆前先关闭紫p` | đóng launcher Purple trước mỗi lần đăng nhập | — | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `登录失败停止上号` | đăng nhập thất bại N lần thì ngừng đưa tài khoản đó vào game | — | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `出现验证停止上号` | gặp xác minh thì ngừng đưa tài khoản đó vào game | — | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `控制台韩文显示` | bảng điều khiển hiển thị tiếng Hàn | — | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `自动运行` | tự động chạy khi mở bảng điều khiển | — | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `多开数量` | số cửa sổ game mở cùng lúc | — | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `窗口布局` | bố cục cửa sổ game | — | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `驱动模式` | chế độ driver (dùng driver kernel của Windows). ⚠️ Tài liệu này không hướng dẫn phần này. | — | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `目录保护` | bảo vệ/ẩn thư mục của bot. ⚠️ Tài liệu này không hướng dẫn phần này. | — | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `中控显示计算机名` | tên máy hiển thị trên trung tâm điều khiển (`ZKT.ini`) | — | [03](03-cau-hinh-chung-va-cau-truc-goi.md) |
| `组队密码` | mật khẩu tổ đội LAN (mặc định `666`) | — | [01](01-huong-dan-su-dung.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md) |
| `队伍最大人数` | số người tối đa mỗi đội LAN (`0` = tắt) | — | [01](01-huong-dan-su-dung.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md) |
| `认证界面等待时间` | thời gian chờ ở màn hình xác thực | — | [04](04-baseconfig.md) |
| `自动跳过假验证` | tự động bỏ qua xác thực giả | — | [04](04-baseconfig.md) |
| `自动接码验证设备` | tự động nhận mã SMS để xác minh thiết bị. ⚠️ Tài liệu này không hướng dẫn phần này. | — | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md) |
| `几分钟内回城` | khoảng thời gian (phút) đếm số lần về thành | — | [04](04-baseconfig.md) |
| `连续回城几次` | số lần về thành liên tiếp để kích hoạt nghỉ | — | [04](04-baseconfig.md) |
| `连续掉线几次` | số lần rớt mạng liên tiếp | — | [04](04-baseconfig.md) |
| `休息几分钟` | nghỉ bao nhiêu phút | — | [04](04-baseconfig.md) |
| `低血量使用回城卷` | máu thấp (%) thì dùng cuộn về thành | — | [04](04-baseconfig.md) |
| `低血量使用随机卷` | máu thấp (%) thì dùng cuộn dịch chuyển ngẫu nhiên | — | [04](04-baseconfig.md) |
| `低蓝量使用回城卷` | mana thấp (%) thì dùng cuộn về thành | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `旅馆休息回血` | nghỉ ở nhà trọ để hồi máu | — | [04](04-baseconfig.md) |
| `旅馆休息村庄` | làng có nhà trọ để nghỉ | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `旅馆为自己放加速次数` | số lần tự niệm Tăng tốc khi ở nhà trọ (tối đa 5) | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `最大执行次数` | số lần thực hiện tối đa (mua đặc biệt) | — | [04](04-baseconfig.md) |
| `最大执行时间` | thời gian thực hiện tối đa (giây) | — | [04](04-baseconfig.md) |
| `下次触发等待时间` | thời gian chờ trước lần kích hoạt sau (giây) | — | [04](04-baseconfig.md) |
| `寻路时反击怪物` | phản công quái khi đang tìm đường | — | [04](04-baseconfig.md) |
| `关闭古鲁丁7楼怪物反击` | tắt phản công quái ở tầng 7 Gludin | — | [04](04-baseconfig.md) |
| `启用全局配置` | bật cấu hình treo máy toàn cục (thay `gj.txt`) | — | [01](01-huong-dan-su-dung.md), [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `攻击寻路到挂机点路上怪物` | đánh quái trên đường tới điểm treo máy | — | [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `反击全部怪物` | phản công mọi quái | — | [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `拾取别人金币` | nhặt vàng của người khác | — | [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `不拾取物品` | không nhặt đồ | — | [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `低于多少金币不拾取` | không nhặt đống vàng nhỏ hơn bao nhiêu | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `记忆卷轴传送` / `记忆卷轴` | dịch chuyển bằng cuộn/sách ghi nhớ vị trí (`=1` điểm thứ 1…) | — | [01](01-huong-dan-su-dung.md), [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `优先攻击在拾取` | ưu tiên đánh quái rồi mới nhặt (chữ `在` là lỗi chính tả, giữ nguyên) | — | [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `出门血量` / `出门蓝量` | máu / mana (%) để ra khỏi làng | — | [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `地监途中路径被堵时` | thời gian (giây) xác định bị chặn đường khi đi tới hầm ngục | — | [04](04-baseconfig.md) |
| `无金币变化秒数` | số giây tiền vàng không thay đổi | — | [04](04-baseconfig.md) |
| `被指定怪攻击时` | khi bị quái chỉ định tấn công | — | [04](04-baseconfig.md) |
| `使用冷却` | thời gian hồi giữa hai lần dịch chuyển | — | [04](04-baseconfig.md) |
| `检测位置停滞秒数` | số giây vị trí đứng yên để kích hoạt | — | [04](04-baseconfig.md) |
| `位置变动判定半径` | bán kính coi như chưa di chuyển | — | [04](04-baseconfig.md) |
| `无怪物触发秒数` | số giây không có quái thì kích hoạt | — | [04](04-baseconfig.md) |
| `被玩家攻击随机传送` / `被宠物攻击随机传送` | bị người chơi / thú cưng tấn công thì dịch chuyển ngẫu nhiên | — | [04](04-baseconfig.md) |
| `首次进入地监随机传送` | dịch chuyển ngẫu nhiên khi vào hầm ngục lần đầu | — | [04](04-baseconfig.md) |
| `指定地图触发随机传送` / `指定地图出发随机传送` / `出发` | chỉ định bản đồ kích hoạt dịch chuyển ngẫu nhiên (dòng thật dùng `触发`; chú thích viết `出发`) | — | [04](04-baseconfig.md) |
| `被玩家PK连续次数` / `被玩家PK持续时间` / `被玩家PK触发休息` | số lần bị PK liên tiếp; khoảng thời gian đếm; thời gian nghỉ khi bị PK | — | [04](04-baseconfig.md) |
| `被玩家攻击才触发` / `被怪物攻击才触发` | chỉ kích hoạt khi bị người chơi / quái tấn công | — | [04](04-baseconfig.md) |
| `躲避玩家名单` / `躲避怪物名单` | danh sách người chơi / quái cần né | — | [04](04-baseconfig.md) |
| `躲避检测距离` | khoảng cách phát hiện để né | — | [04](04-baseconfig.md) |
| `回城休息时间_分钟` | thời gian nghỉ sau khi về thành (phút) | — | [04](04-baseconfig.md) |
| `挂机点过滤_分钟` / `挂机点过滤半径` | thời gian (phút) và bán kính lọc (cấm) điểm treo máy | — | [04](04-baseconfig.md) |
| `开启分模式1和模式2` | bật thì chia chế độ 1 và chế độ 2 | — | [04](04-baseconfig.md) |
| `休息模式` / `运行几分钟` / `休息时间段` | chế độ nghỉ; chạy bao nhiêu phút; các khung giờ nghỉ | — | [04](04-baseconfig.md) |
| `开启切换` / `分段挂机配置` | bật đổi file treo máy theo giờ; cấu hình từng khung giờ | — | [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `内存寻路` / `内存打怪` / `内存拾取` / `内存放技能` | tìm đường / đánh quái / nhặt đồ / dùng kỹ năng bằng chế độ bộ nhớ | — | [01](01-huong-dan-su-dung.md), [04](04-baseconfig.md) |
| `内存使用物品` / `内存删除物品` / `内存交易` / `内存组队` | dùng vật phẩm / xóa vật phẩm / giao dịch / tổ đội bằng chế độ bộ nhớ | — | [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `使用变身卷轴` / `使用购买变身卷轴` | dùng cuộn biến hình loại được tặng / loại mua | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `自动换装到等级` | tự động đổi trang bị đến cấp | — | [04](04-baseconfig.md) |
| `自动学习技能` | tự động học kỹ năng | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `举报附近的人` | tố cáo (report) người ở gần | — | [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `打怪拾取使用血蓝转换` | dùng chuyển hóa máu/mana khi đánh quái và nhặt đồ | — | [04](04-baseconfig.md) |
| `自动购买装备` | tự động mua trang bị (`獵人之弓`) | — | [01](01-huong-dan-su-dung.md), [04](04-baseconfig.md) |
| `无说话卷轴时停止脚本` | hết cuộn dịch chuyển về Talking Island thì dừng script | — | [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `自动领取说话卷轴` | tự động nhận cuộn dịch chuyển về Talking Island | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `死亡复活后自动购买肉` | sau khi chết và hồi sinh thì tự mua thịt (số miếng) | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `自动切换敏捷力量头盔` | tự động đổi mũ Nhanh nhẹn / Sức mạnh | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `自动穿戴头盔` | tự động đội lại mũ (điền tên mũ) | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `村庄传送到地监门口间隔` | khoảng thời gian (phút) giữa các lần dịch chuyển từ làng tới cửa hầm ngục | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `角色名类型` | kiểu tên nhân vật khi tạo (Anh / Trung / Hàn) | — | [04](04-baseconfig.md) |
| `吃药血量` | ngưỡng máu (%) để uống thuốc | — | [04](04-baseconfig.md) |
| `吃蓝药百分比` | ngưỡng mana (%) để uống thuốc xanh lam | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `反击人` | phản công người chơi (`BaseConfig.txt`) | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `反击法师宝宝` | phản công "cưng" của Pháp sư | — | [04](04-baseconfig.md) |
| `本机自动组队` | tự tổ đội các tài khoản trên máy này | — | [04](04-baseconfig.md) |
| `集火打怪` | tập trung đánh quái | — | [04](04-baseconfig.md) |
| `为队员放加速术` | niệm Tăng tốc cho đội viên | — | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md) |
| `为队员加血` | hồi máu cho đội viên (`1` = dưới 65%, `70` = dưới 70%…) | — | [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md) |
| `为队员放技能` | dùng kỹ năng buff chỉ định cho đội viên | — | [02](02-nhat-ky-cap-nhat.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md) |
| `怪物过滤` / `反击怪物` / `拾取过滤` | lọc quái / quái phản công / lọc nhặt đồ (khóa trong `gj.txt`) | — | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md), [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `负重回城` | về thành khi tải trọng đạt (%) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `打怪范围` | phạm vi tìm quái | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `瞬移找怪` | dịch chuyển tức thời để tìm quái (chỉ ở Talking Island) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `打怪地图` / `打怪坐标` | bản đồ đánh quái / tọa độ đánh quái | — | [01](01-huong-dan-su-dung.md), [02](02-nhat-ky-cap-nhat.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `优先传送` | ưu tiên dịch chuyển tới điểm gần tọa độ này (`0,0` = không dùng) | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `走向挂机点线路` | lộ trình đi đến điểm treo máy | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `时间段` | khung giờ (sự kiện) | — | [04](04-baseconfig.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `首选村庄` | làng ưu tiên (lối vào sự kiện) | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `Boss坐标` | tọa độ chờ boss | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `兑换触发总数` | tổng số trứng để kích hoạt đổi | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `达到金币触发存仓` | đạt số vàng thì gửi kho huyết minh | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `保留金币` | vàng giữ lại trong túi | — | [05](05-game-config-chien-dau-va-vat-pham.md), [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `自动血盟加入` | tự gia nhập huyết minh | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `自动存入物品` | tự gửi vật phẩm vào kho huyết minh | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `存入失败间隔` | khoảng chờ (phút) khi gửi thất bại | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `仓库位置` | vị trí (làng) có kho | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `地图` | bản đồ nơi acc chính đứng buff (khóa trong `Buff.txt`, đi cùng khóa `坐标`) | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `小号buff消失回城` | acc phụ mất buff thì về thành | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `小号buff消失间隔过来时间` | thời gian chờ (giây) trước khi acc phụ quay lại | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `小号加buff停留时间` | thời gian (giây) acc phụ đứng chờ buff | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `加buff主号没蓝回旅馆` | acc chính buff hết mana thì về nhà trọ | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `加buff主号角色名` | tên nhân vật acc chính buff | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `加buff主号放技能` | kỹ năng acc chính buff sẽ dùng | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `同角色加buff间隔` | khoảng cách (giây) buff lại cùng một nhân vật | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `加buff主号对角色连续加几次` | số lần buff liên tiếp cho một nhân vật | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `相性数值低于多少停止攻击` | chỉ số thiện/ác thấp hơn bao nhiêu thì ngừng tấn công (?) | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `主动攻红名玩家` | chủ động đánh người chơi tên đỏ | — | [02](02-nhat-ky-cap-nhat.md), [05](05-game-config-chien-dau-va-vat-pham.md) |
| `间隔时间(分钟)` / `同时对几个格子使用` / `每个格子可使用的次数` | chu kỳ (phút); dùng cùng lúc cho mấy ô; số lần dùng mỗi ô (`UseItems.txt`) | — | [05](05-game-config-chien-dau-va-vat-pham.md) |
| `达到金币触发交易` / `达到材料触发交易` | đạt số vàng / số nguyên liệu thì kích hoạt giao dịch | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `金币采用摆摊模式` | chuyển vàng bằng chế độ bày sạp | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `交易失败间隔` | khoảng chờ (phút) sau khi giao dịch thất bại | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `收货人位置` / `收货人坐标` | vị trí (làng) / tọa độ người nhận hàng | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `摆摊人位置` / `摆摊人坐标` | vị trí (làng) / tọa độ người bày sạp | — | [06](06-game-config-treo-may-kho-va-giao-dich.md) |
| `ip` / `port` | địa chỉ IP / cổng mạng (`ZKT.ini`, `[局域网组队配置]`, `组队服务器/config.ini`) | IP / port | [01](01-huong-dan-su-dung.md), [03](03-cau-hinh-chung-va-cau-truc-goi.md), [04](04-baseconfig.md) |
