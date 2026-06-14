"""
Generate concise exam-focused notes for all 15 Word lessons.
Replaces the raw transcript notes with structured cheat-sheets.
"""

import os

NOTES_DIR = r"d:\Dev n Code\CNTT co ban\Notes\Word lecture"
LECTURE   = "Word lecture"

NOTES = {
1: (
"Các Thiết Lập Mặc Định",
"""## Bài 1 — Các Thiết Lập Mặc Định

### 3 thiết lập cần làm TRƯỚC KHI soạn thảo

---

#### 1. Đơn vị đo lường

`File → Options → Advanced → Show measurements in units of → Cm → OK`

---

#### 2. Lề & Kích cỡ trang

`Layout → Page Setup (↘) → Margins`

| Vị trí | Giá trị |
|--------|---------|
| Top (Trên) | 2 cm |
| Bottom (Dưới) | 2 cm |
| Left (Trái) | **3 cm** |
| Right (Phải) | 2 cm |

> **Nhớ nhanh: 2 – 2 – 3 – 2**

Sau đó: `Paper → A4 → Set As Default → Yes`

---

#### 3. Font chữ & Khoảng cách

`Home → Styles → Normal → chuột phải → Modify → Formatting`

| Thuộc tính | Giá trị |
|-----------|---------|
| Font | Times New Roman |
| Size | **12** hoặc **13** |
| Color | Auto (đen) |

`Format → Paragraph → Spacing`

| Thuộc tính | Giá trị |
|-----------|---------|
| Before | 6 pt |
| After | 6 pt |
| Line Spacing | Multiple → **1.1** |

Cuối cùng chọn **"New documents based on this template"** → OK
"""),

2: (
"Các Thao Tác Cơ Bản Khi Bắt Đầu Soạn Thảo",
"""## Bài 2 — Các Thao Tác Cơ Bản

### Tạo & lưu file

> **Nên dùng Cách 2** (tránh lưu nhầm ổ C):
> Mở folder cần lưu → chuột phải → New → Microsoft Word Document → đặt tên → Enter

- Lưu: `Ctrl + S` (làm thường xuyên, mỗi 10–20 dòng)
- Không lưu vào **ổ C** (ổ hệ thống)

---

### Phím tắt quan trọng

| Phím | Chức năng |
|------|-----------|
| `Ctrl + S` | Lưu |
| `Ctrl + F4` | Đóng tài liệu |
| `Alt + F4` | Thoát Word |
| `Ctrl + O` | Mở tài liệu có sẵn |
| `Ctrl + N` | Tạo tài liệu mới |
| `Ctrl + C` | Sao chép |
| `Ctrl + X` | Cắt |
| `Ctrl + V` | Dán |

---

### Tiếng Việt

- Dùng **Unikey** → bật "Khởi động cùng Windows"
- Kiểm tra góc dưới taskbar: **V** = tiếng Việt, **E** = tiếng Anh
"""),

3: (
"Các Thao Tác Định Dạng Đoạn Văn Bản",
"""## Bài 3 — Định Dạng Đoạn Văn Bản

> **Quy tắc:** Nhập nội dung **TRƯỚC** → định dạng **SAU**

---

### Định dạng tiêu đề

1. Chọn dòng tiêu đề (click trái lề, mũi tên hướng phải → click)
2. `Home → Change Case → UPPERCASE`
3. **Bold**: `Ctrl + B` | **In nghiêng**: `Ctrl + I` | **Gạch chân**: `Ctrl + U`
4. Font Size: **16** hoặc **18** (tiêu đề hành chính)
5. Canh giữa: `Ctrl + E`

---

### Định dạng đoạn văn

| Thao tác | Phím tắt / Lệnh |
|----------|----------------|
| Canh đều 2 bên | `Ctrl + J` (Justify) |
| Bật thước | `View → Ruler` |
| Lề dòng đầu | Kéo **First Line Indent** trên thước |
| Lề trái đoạn | Kéo **Left Indent** trên thước |

---

### Khoảng cách dòng & đoạn

`Home → Line Spacing → Line Spacing Options`

| Thuộc tính | Ý nghĩa |
|-----------|---------|
| Before | Khoảng cách trước đoạn |
| After | Khoảng cách sau đoạn |
| Multiple | Nhân khoảng cách dòng (vd: 1.5, 2) |

> **12 pt = 1 dòng**, **6 pt = ½ dòng**
"""),

4: (
"Định Dạng Bullets and Numbering",
"""## Bài 4 — Bullets and Numbering

### Numbering (đánh số)

1. Chọn các dòng tiêu đề (Ctrl + click để chọn không liên tiếp)
2. `Home → Numbering → chọn kiểu` (1 2 3, I II III, a b c...)
3. Để tạo **mục con** (level 2): chọn dòng → **Increase Indent** → đổi Numbering

---

### Bullets (dấu đầu dòng)

1. Chọn dòng → `Home → Bullets`
2. Đổi biểu tượng: nhấp mũi tên bên cạnh Bullets → chọn biểu tượng khác
3. Tạo mức con: **Increase Indent** rồi đổi biểu tượng

---

### Quy tắc các cấp

| Cấp | Thao tác |
|-----|---------|
| Level 1 | Chọn Numbering/Bullets thẳng |
| Level 2 | Increase Indent 1 lần → đổi kiểu |
| Level 3 | Increase Indent 2 lần → đổi kiểu |

> **Hoàn tác:** `Ctrl + Z`
"""),

5: (
"Sử Dụng Tab Tạo Văn Bản Dạng Cột",
"""## Bài 5 — Tab Tạo Văn Bản Dạng Cột

### Các loại Tab

| Ký hiệu | Loại | Căn |
|---------|------|-----|
| `L` | Tab trái | Trái |
| `⊥` (lật L) | Tab giữa | Giữa |
| `⌐` | Tab phải | Phải |

> Nhấp vào biểu tượng **ở góc trái thước** để chuyển loại Tab

---

### Tạo Tab

1. `View → Ruler` (bật thước nếu chưa có)
2. Chọn loại Tab (click góc trái thước)
3. Nhấp lên **thước** tại vị trí mong muốn → Tab được tạo
4. Nhấn `Tab` để di chuyển giữa các cột khi gõ

---

### Hiệu chỉnh & Xóa Tab

- **Di chuyển Tab**: kéo biểu tượng Tab trên thước sang trái/phải
- **Xóa Tab**: kéo biểu tượng Tab xuống **khỏi thước** (thả xuống vùng trắng)

---

### Lưu ý

- Enter xuống dòng → Tab **tự copy** xuống dòng mới
- Chỉ cần định nghĩa Tab ở **dòng đầu tiên**
"""),

6: (
"Sử Dụng Tab Tạo Văn Bản Dạng Biểu Mẫu (Form)",
"""## Bài 6 — Tab Tạo Văn Bản Dạng Biểu Mẫu (Form)

### Điểm khác với bài 5

> Khi nhấn Tab → tạo ra **dấu chấm dẫn** (leader) thay vì khoảng trắng

---

### Tạo dấu dẫn (chấm liên tục)

1. Nhấp đôi chuột vào **biểu tượng Tab** trên thước
2. Chọn Tab cần thêm dấu dẫn
3. Chọn **Leader số 2** (chấm liên tục `............`)
4. Nhấn **Set** → **OK**

---

### Xóa hết Tab của đoạn

> `Ctrl + Q` — xóa toàn bộ Tab trên dòng hiện tại

---

### Copy định dạng Tab sang dòng khác

`Home → Format Painter` → quét vào dòng cần copy

---

### Quy trình

1. Gõ nội dung trước dấu hai chấm
2. Nhấn `Tab` → nhảy đến điểm dừng (không dấu dẫn)
3. Nhấn `Tab` lần 2 → nhảy đến cuối dòng (có dấu dẫn)
4. Nhấp đôi Tab trên thước để thêm dấu dẫn cho Tab cần thiết
"""),

7: (
"Định Dạng Kẻ Khung và Tô Nền (Border and Shading)",
"""## Bài 7 — Kẻ Khung và Tô Nền

### Kẻ khung (Border)

**Cách nhanh:** `Home → Border → Outside Border`

**Cách tùy chỉnh:**
`Home → Border → Borders and Shading`

| Tùy chọn | Ý nghĩa |
|----------|---------|
| Box | Khung vuông thông thường |
| Shadow | Khung có bóng đổ |
| 3D | Khung nổi 3D |
| Style | Nét liền, nét đứt, nét đôi... |
| Color | Màu đường kẻ |
| Width | Độ dày nét kẻ |
| **Apply to: Paragraph** | Áp dụng cho cả đoạn |
| Apply to: Text | Áp dụng từng dòng riêng lẻ |

> **Lưu ý:** Luôn chọn **Apply to: Paragraph** cho văn bản hành chính

---

### Tô nền (Shading)

`Home → Shading → chọn màu`
"""),

8: (
"Tạo và Định Dạng Font Chữ Nghệ Thuật (WordArt)",
"""## Bài 8 — WordArt (Font Chữ Nghệ Thuật)

### Tạo WordArt

1. Chọn từ/đoạn cần chuyển
2. `Insert → WordArt → chọn kiểu`

---

### Định dạng màu sắc

| Thành phần | Lệnh |
|-----------|------|
| Màu nền khung | Shape Format → **Shape Fill** |
| Màu viền khung | Shape Format → **Shape Outline** |
| Màu chữ | **Text Fill** |
| Màu viền chữ | **Text Outline** |

> Bỏ màu: chọn **No Fill** / **No Outline**

---

### Hiệu ứng

| Hiệu ứng | Đường dẫn |
|----------|-----------|
| Uốn chữ | Shape Format → Text Effects → **Transform** |
| Bóng đổ | Text Effects → **Shadow → Outer** |
| Đổi kiểu | Shape Format → **Quick Styles** |
"""),

9: (
"Định Dạng Column và Dropcap",
"""## Bài 9 — Column và Dropcap

> **Quy tắc bắt buộc:** Chia cột **TRƯỚC** → Drop Cap **SAU**

---

### Chia cột (Column)

1. Chọn đoạn văn
2. `Layout → Columns → Two / Three / Left / Right`

**Tùy chỉnh nâng cao:** `More Columns`

| Tùy chọn | Ý nghĩa |
|----------|---------|
| Line between | Đường phân cách giữa các cột |
| Equal column width | Bỏ tick → tùy chỉnh độ rộng từng cột |
| Spacing | Khoảng cách giữa các cột |

---

### Drop Cap (chữ hoa rớt dòng)

1. Đặt con trỏ vào **chữ cái đầu tiên** của đoạn
2. `Insert → Drop Cap → Dropped`

**Tùy chỉnh:** `Drop Cap Options`

| Tùy chọn | Ý nghĩa |
|----------|---------|
| Font | Font riêng cho chữ Drop Cap |
| Lines to drop | Rớt bao nhiêu dòng (mặc định: 3) |
| Distance from text | Khoảng cách từ chữ đến văn bản |
"""),

10: (
"Tạo và Định Dạng Picture",
"""## Bài 10 — Picture (Hình Ảnh)

### Chèn hình

`Insert → Pictures → This Device → chọn hình → Insert`

> Chèn nhiều hình: Ctrl + click lần lượt rồi Insert

---

### ⚠️ Quan trọng: Định dạng vị trí (bắt buộc sau khi chèn)

Nhấp hình → **Layout Options** → chọn **Square**

| Kiểu | Ý nghĩa |
|------|---------|
| **Square** | Văn bản bao quanh hình (hay dùng nhất) |
| Behind Text | Hình nằm sau văn bản |
| In Line | Hình nằm trên dòng (khó di chuyển) |

---

### Các thao tác định dạng hình

| Thao tác | Lệnh |
|----------|------|
| Thay đổi kích cỡ | Kéo góc hình |
| Cắt xén hình | Picture Format → **Crop** |
| Áp style khung | Picture Format → **Quick Styles** |
| Hiệu ứng | Picture Format → **Picture Effects** |
| Độ sáng/tương phản | Picture Format → **Corrections** |
| Đổi màu | Picture Format → **Color** |
| Xóa nền | Picture Format → **Remove Background** |
"""),

11: (
"Thao Tác với Văn Bản Con (Textbox)",
"""## Bài 11 — Textbox (Văn Bản Con)

### Tạo Textbox

**Chưa có nội dung:**
`Insert → Text Box → Draw Text Box → vẽ trên văn bản → gõ nội dung`

**Đã có nội dung:**
`Chọn đoạn văn → Insert → Text Box → Draw Text Box`

---

### Định dạng màu & đường viền

| Thành phần | Lệnh |
|-----------|------|
| Màu nền đặc | Shape Format → Shape Fill → chọn màu |
| Màu nền gradient | Shape Fill → Gradient → More Gradients |
| Màu đường viền | Shape Format → **Shape Outline → Color** |
| Độ dày viền | Shape Outline → **Weight** |
| Kiểu nét | Shape Outline → **Dashes** |

---

### Vị trí

Nhấp Textbox → **Layout Options → Square** (di chuyển tự do)

---

### Lưu ý

- Textbox không bị ảnh hưởng bởi lề văn bản
- Dễ dàng đặt ở bất kỳ vị trí nào trên trang
"""),

12: (
"Thao Tác với Đối Tượng Hình Vẽ (Shape)",
"""## Bài 12 — Shape (Hình Vẽ)

### Vẽ Shape

`Insert → Shapes → chọn kiểu → vẽ lên văn bản`

---

### Thao tác cơ bản

| Thao tác | Cách làm |
|----------|---------|
| Nhập chữ vào Shape | Nhấp đôi vào Shape → gõ |
| Sao chép Shape | **Ctrl + kéo** |
| Chọn nhiều Shape | **Shift + click** từng Shape |
| Đổi kiểu Shape | Shape Format → Edit Shape → **Change Shape** |
| Màu nền | Shape Format → **Shape Fill** |
| Màu viền | Shape Format → **Shape Outline** |
| Màu chữ | **Text Fill** |

---

### ⚠️ Gom nhóm (GROUP) — Quan trọng nhất

Sau khi vẽ xong **phải Group** để dễ di chuyển cả sơ đồ:

1. `Shift + click` chọn **tất cả** đối tượng
2. `Shape Format → Group → Group`

> Sau khi Group: kéo 1 chỗ → cả sơ đồ di chuyển

**Bỏ Group:** `Shape Format → Group → Ungroup`
"""),

13: (
"Tạo và Định Dạng Bảng Table",
"""## Bài 13 — Tạo Bảng Table

### Tạo bảng

`Insert → Table → kéo chọn số cột × dòng → click`

---

### Các thao tác thiết yếu

| Thao tác | Lệnh |
|----------|------|
| Độ rộng cột bằng nhau | Chọn các cột → Table Layout → **Distribute Columns** |
| **Nối ô** | Chọn ô → Table Layout → **Merge Cells** |
| Thêm dòng | Nhấp dấu **+** bên trái bảng, hoặc Tab ở ô cuối cùng |
| Canh giữa ô (ngang+dọc) | Table Layout → **Align Center** (giữa hàng nút Alignment) |

---

### Kẻ khung bảng

`Home → Border → Borders and Shading`

| Tùy chọn | Ý nghĩa |
|----------|---------|
| All | Tất cả đường (trong + ngoài) |
| Box | Chỉ đường ngoài |
| Style | Nét đơn, nét đôi, nét đứt... |
| Apply to: **Table** | Áp dụng cho toàn bảng |

---

### Tô nền dòng

`Chọn dòng → Home → Shading → chọn màu`
"""),

14: (
"Các Thao Tác Định Dạng Bảng Table",
"""## Bài 14 — Định Dạng Bảng Table (Nâng Cao)

### Thêm / Xóa cột & dòng

| Thao tác | Lệnh |
|----------|------|
| Thêm cột trái | Table Layout → **Insert Left** |
| Thêm cột phải | Table Layout → **Insert Right** |
| Xóa cột | Table Layout → Delete → **Delete Columns** |
| Thêm dòng trên | Table Layout → **Insert Above** |
| Thêm dòng dưới | Table Layout → **Insert Below** |
| Xóa dòng | Table Layout → Delete → **Delete Rows** |

---

### Nối & Chia ô

| Thao tác | Lệnh |
|----------|------|
| Nối ô | Chọn ô → **Merge Cells** (hoặc chuột phải → Merge) |
| Chia ô | **Split Cells** → nhập số cột / số dòng → OK |

---

### Xoay chữ trong ô

`Table Layout → Text Direction` (nhấp nhiều lần để xoay)

---

### Áp style có sẵn

`Table Design → Table Styles → chọn kiểu`

---

### Canh lề nội dung trong ô

`Table Layout → Alignment` → 9 kiểu canh khác nhau
"""),

15: (
"Cách Tạo Công Thức Toán Học",
"""## Bài 15 — Công Thức Toán Học (Equation)

### Tạo công thức

`Insert → Symbol → Equation`

---

### ⚠️ 2 Nguyên tắc cốt lõi

> **1. Tạo từ NGOÀI VÀO TRONG**
> Ví dụ: Căn ngoài → Ngoặc trong căn → Phân số trong ngoặc

> **2. Đối tượng tiếp theo phải CÙNG CẤP**
> Nội dung bên trong phải **được tô xám** trước khi tạo đối tượng mới
> Dùng **phím mũi tên →** để thoát ra cấp ngoài (tô xám cấp ngoài)

---

### Các ký hiệu hay dùng

| Ký hiệu | Vị trí trong Equation |
|---------|----------------------|
| Phân số | Fraction |
| Căn thức | Radical |
| Ngoặc | Bracket |
| Chỉ số trên (x²) | Script → **Superscript** |
| Chỉ số dưới (x₁) | Script → **Subscript** |
| Delta (Δ) | Symbol → tìm Delta |

---

### Ký tự trên bàn phím → gõ thẳng

`+  −  =  (  )  a  b  c  1  2 ...`

---

### Quy trình ví dụ: x₁ = (-b + √Δ) / 2a

1. Tạo Equation
2. Chọn Bracket (ngoặc ngoài cùng)
3. Tạo Matrix 2 dòng
4. Dòng 1: Subscript → gõ x và 1 → **→** → gõ `=` → Fraction → ...
5. **Luôn dùng → để thoát đối tượng con** trước khi gõ ký tự cùng cấp
"""),
}

NAV_PREV = "← [[{p} - {pt}|Bài {p}]]  |  "
NAV_INDEX = "[[{lec}|📋 Mục lục]]"
NAV_NEXT  = "  |  [[{n} - {nt}|Bài {n}]] →"

TITLES = {n: t for n, (t, _) in NOTES.items()}

def nav(n, lec):
    prev = (NAV_PREV.format(lec=lec, p=n-1, pt=TITLES[n-1]) if n > 1 else "")
    nxt  = (NAV_NEXT.format(lec=lec, n=n+1, nt=TITLES[n+1]) if n < 15 else "")
    return prev + NAV_INDEX.format(lec=lec) + nxt

def build(n, title, body, lec):
    return f"""---
title: "{lec} - Bài {n}: {title}"
tags:
  - word
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
