"""
Generate concise exam-focused notes for 5 PowerPoint lessons.
Replaces the raw transcript notes with structured cheat-sheets.
"""

import os

NOTES_DIR = r"d:\Dev n Code\CNTT co ban\Notes\PowerPoint lecture"
LECTURE   = "PowerPoint lecture"

NOTES = {
1: (
"Tạo và Trình Chiếu các Slide",
"""### Tạo phiên trình bày

| Cách | Thao tác |
|------|---------|
| Dùng Template | Khởi động → chọn **Theme** → Create |
| Dùng Presentation mẫu | Khởi động → chọn **Presentation** → Create |
| File trống | File → **Blank Presentation** → tự thiết kế |

> **Nhớ nhanh:** Theme = mẫu trống · Presentation = mẫu + nội dung sẵn

---

### Cấu trúc Slide

| Vị trí | Loại |
|--------|------|
| Slide 1 | **Title Slide** — tiêu đề + sub-title |
| Slide 2+ | **Content Slide** — nội dung bài |

**Layout hay dùng:** Title Only · Two Content · Section Header · Comparison

---

### Thao tác với Slide

| Thao tác | Lệnh |
|----------|------|
| Tạo slide mới | `Home → New Slide` → chọn layout |
| Sao chép slide | `Ctrl + D` hoặc chuột phải → **Duplicate Slide** |
| Di chuyển | Kéo thả trong bảng slide bên trái |
| Xóa | Chọn slide → `Delete` |

---

### Chế độ hiển thị (`View`)

| Chế độ | Dùng khi |
|--------|---------|
| **Normal** | Soạn thảo thông thường |
| **Outline View** | Xem nội dung dạng văn bản |
| **Slide Sorter** | Sắp xếp, di chuyển nhiều slide |
| **Notes** | Gõ ghi chú cho từng slide |
| **Reading View** | Đọc nội dung |

---

### Trình chiếu

| Phím | Chức năng |
|------|-----------|
| `F5` | Trình chiếu từ slide đầu |
| `Shift + F5` | Trình chiếu từ slide hiện tại |
| `B` | Tạm dừng → màn hình **đen** |
| `W` | Tạm dừng → màn hình **trắng** |
| `Esc` | Kết thúc trình chiếu |

⚠️ Laptop một số dòng cần nhấn `Fn + F5`
"""),

2: (
"Sử Dụng Slide Master",
"""### Slide Master là gì?

> Mẫu định dạng **chung** cho tất cả slide trong phiên trình bày (nền, font, màu sắc, footer, số trang)

---

### Vào / Thoát Slide Master

`View → Slide Master`  →  chỉnh sửa  →  `Slide Master → Close Master View`

---

### Thành phần của Slide Master (slide số 1)

| Thành phần | Vai trò |
|-----------|---------|
| Background | Nền chung tất cả slide |
| Title | Vùng tiêu đề slide |
| Content | Vùng nội dung |
| Footer | Chân trang |
| Date | Ngày giờ |
| Slide Number | Số trang |

---

### Thiết kế từ đầu

1. File → **Blank Presentation**
2. `View → Slide Master` → chọn **slide số 1** (slide chủ)
3. Đặt background: `Background Styles → Format Background → Picture → Insert`
4. Định dạng Title, Content, Footer (Home → chọn màu / cỡ chữ)
5. `Slide Master → Close Master View`

> **Nhớ nhanh:** Thiết kế 1 lần → áp dụng toàn bộ slide

---

### Định dạng riêng cho một Layout

1. `View → Slide Master`
2. Chọn **layout** cần thay đổi (ví dụ: Two Content)
3. Đổi nền / font riêng cho layout đó
4. `Close Master View`

⚠️ Không chỉnh trực tiếp trên slide thường — phải vào Slide Master
"""),

3: (
"Thao Tác với Các Đối Tượng trên Slide",
"""### WordArt

| Cách | Lệnh |
|------|------|
| Tạo mới | `Insert → WordArt → chọn kiểu → gõ nội dung` |
| Từ text có sẵn | Chọn text → `Shape Format → Word Styles` → `Text Effects` |

---

### Shape (Hình vẽ)

`Insert → Shapes → chọn kiểu → vẽ lên slide`

| Thao tác | Lệnh |
|----------|------|
| Sao chép Shape | `Ctrl + kéo` |
| Gõ chữ vào Shape | Nhấp đôi vào Shape |
| Đổi màu nền | Shape Format → **Shape Fill** |
| Đổi màu viền | Shape Format → **Shape Outline** |
| **Gom nhóm** | `Shift + click` các đối tượng → `Shape Format → Group → Group` |

> **Nhớ nhanh:** Luôn Group sau khi vẽ xong sơ đồ để dễ di chuyển

---

### Lồng hình vào Shape

1. Nhấp phải vào Shape → **Format Shape**
2. Chọn **Picture** → **Insert** → chọn file ảnh

---

### Picture

`Insert → Pictures → This Device → chọn hình → Insert`
→ Chọn kiểu: `Picture Format → Picture Styles`

---

### SmartArt (Sơ đồ)

`Insert → SmartArt → chọn kiểu → OK`

| Thao tác | Lệnh |
|----------|------|
| Nhập nội dung | Bật **Text Pane** → gõ |
| Thêm mục con | Sau mục cha → `Tab` |
| Thêm mục ngang cấp | `Enter` |
| Đổi màu | **Change Colors** |

---

### Table

`Insert → Table → kéo chọn cột × dòng` → nhập dữ liệu → `Table Design → Table Styles`

---

### Chart (Đồ thị)

`Insert → Chart → Column → OK` → nhập số liệu vào Excel → **Close**
→ Chỉnh kiểu: `Chart Design → Change Chart Type`
→ Thêm nhãn số: nhấp dấu `+` bên đồ thị → **Data Labels**

⚠️ Sau khi chèn hình vào slide phải Group các đối tượng liên quan lại
"""),

4: (
"Tạo Hiệu Ứng Transitions và Animations",
"""### Transitions (Hiệu ứng chuyển tiếp Slide)

1. Chọn slide → thẻ **Transitions**
2. Chọn hiệu ứng trong danh sách
3. Tùy chọn: **Sound** (âm thanh) · **Duration** (tốc độ)
4. `Apply to All` — áp dụng tất cả slide

**Chuyển slide tự động (không cần nhấn phím):**
- Bỏ chọn **On Mouse Click**
- Chọn **After** → nhập số giây

**Xóa transition:** chọn slide → Transitions → chọn **None**

---

### Animations (Hiệu ứng đối tượng)

Chọn đối tượng → thẻ **Animations** → chọn hiệu ứng

#### 4 nhóm Animation

| Nhóm | Màu | Ý nghĩa |
|------|-----|---------|
| **Entrance** | Xanh lá | Đối tượng xuất hiện |
| **Emphasis** | Vàng | Nhấn mạnh (gây chú ý) |
| **Exit** | Đỏ | Đối tượng biến mất |
| **Motion Path** | — | Đối tượng di chuyển theo đường vẽ |

**Thêm nhiều animation cho 1 đối tượng:** `Add Animation`

---

### Animation Pane

`Animations → Animation Pane` — xem danh sách & thứ tự hoạt hóa

| Thuộc tính | Ý nghĩa |
|-----------|---------|
| **Start: On Mouse Click** | Nhấn phím/chuột mới chạy |
| **Start: With Previous** | Chạy cùng lúc với đối tượng trước |
| **Start: After Previous** | Chạy sau khi đối tượng trước xong |
| **Duration** | Tốc độ nhanh/chậm |
| **Delay** | Độ trễ trước khi chạy |

**Đổi thứ tự:** Move Earlier / Move Later
**Xóa animation:** chọn animation → combo box → **Remove**

⚠️ Mặc định Start = On Mouse Click → phải nhấn phím mới hoạt hóa
"""),

5: (
"Trình Chiếu và Xuất Bản Slide",
"""### Nút lệnh (Action Button)

`Insert → Shapes → Action Buttons` → chọn nút → vẽ lên slide → hội thoại **Action Settings** tự mở

| Nút | Chức năng |
|-----|---------|
| Home | Về slide đầu |
| Back/Previous | Về slide trước |
| Forward/Next | Đến slide sau |
| Beginning | Về slide đầu tiên |
| End | Đến slide cuối |

---

### Hyperlink tùy chỉnh

Nhấp phải đối tượng bất kỳ → **Hyperlink** → **Place in This Document**

| Tùy chọn | Đến |
|----------|-----|
| First Slide | Slide đầu |
| Last Slide | Slide cuối |
| Next Slide | Slide kế |
| Previous Slide | Slide trước |
| Slide N | Slide cụ thể |

**Sửa link:** nhấp phải → **Edit Link** → chọn lại slide

---

### Trình chiếu liên tục (loop)

`Slideshow → Set Up Slide Show → Loop Continuously Until Escape → OK`

---

### Xuất bản Slide

`File → Save As → chọn folder → mục Save as type:`

| Định dạng | Dùng khi |
|-----------|---------|
| **PowerPoint Show (.ppsx)** | File trình chiếu (không cần PowerPoint) |
| **MP4 / Windows Media Video** | Xuất video |
| **PNG / JPEG** | Xuất hình ảnh |
| **PDF** | Xuất tài liệu PDF |

Khi xuất PNG/JPEG → chọn **Current Slide** (slide hiện tại) hoặc **All Slides**

⚠️ File `.ppsx` không sửa được — lưu thêm `.pptx` bản gốc
"""),
}

NAV_PREV = "← [[{p} - {pt}|Bài {p}]]  |  "
NAV_INDEX = "[[{lec}|📋 Mục lục]]"
NAV_NEXT  = "  |  [[{n} - {nt}|Bài {n}]] →"

TITLES = {n: t for n, (t, _) in NOTES.items()}

def nav(n, lec):
    prev = (NAV_PREV.format(lec=lec, p=n-1, pt=TITLES[n-1]) if n > 1 else "")
    nxt  = (NAV_NEXT.format(lec=lec, n=n+1, nt=TITLES[n+1]) if n < len(NOTES) else "")
    return prev + NAV_INDEX.format(lec=lec) + nxt

def build(n, title, body, lec):
    return f"""---
title: "{lec} - Bài {n}: {title}"
tags:
  - powerpoint
  - cntt-co-ban
  - exam-note
---

# Bài {n}: {title}

{nav(n, lec)}

---

{body.strip()}

---

## Ghi Chú Cá Nhân

> [!question] Chưa hiểu
> -

> [!check] Đã nắm
> -

---

{nav(n, lec)}
"""

def main():
    os.makedirs(NOTES_DIR, exist_ok=True)
    lec = LECTURE
    for n, (title, body) in NOTES.items():
        filename = f"{n} - {title}.md"
        path = os.path.join(NOTES_DIR, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(build(n, title, body, lec))
        print(f"  Written: {filename}")
    print("Done.")

if __name__ == "__main__":
    main()
