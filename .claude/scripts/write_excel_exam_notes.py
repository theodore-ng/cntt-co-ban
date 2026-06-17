"""
Generate concise exam-focused notes for 8 Excel lessons.
"""

import os

NOTES_DIR = r"d:\Dev n Code\CNTT co ban\Notes\Excel lecture"
LECTURE   = "Excel lecture"

NOTES = {
1: (
"Trình Bày và Định Dạng Bảng Tính",
"""### Cấu trúc bảng tính chuẩn

1. Tiêu đề bảng tính → nhập vào **A1** hoặc **A2**
2. Cách **ít nhất 1 dòng** trống trước nội dung (để `Ctrl + A` chọn đúng bảng)
3. Tiêu đề cột nên gõ trên **1 dòng** (dễ sắp xếp, lọc dữ liệu sau này)

---

### Nối ô & Định dạng tiêu đề

| Thao tác | Lệnh |
|----------|------|
| Nối ô + căn giữa | Chọn ô → `Home → Merge & Center` |
| Xoay chữ dọc | `Home → Orientation → Rotate Text Down` |
| Xoay chữ ngang lại | `Home → Orientation → Format Cells → Alignment → chỉnh góc 0°` |
| Canh giữa tiêu đề bảng | Chọn A1:N1 → `Merge & Center` |

---

### Điều chỉnh kích thước

| Thao tác | Cách làm |
|----------|---------|
| Thu/mở rộng cột | Kéo đường phân cách giữa tiêu đề cột |
| Nhiều cột bằng nhau | Chọn các cột → kéo 1 cột, các cột còn lại tự đồng đều |
| Thay đổi chiều cao dòng | Kéo đường phân cách giữa số dòng |

---

### Kẻ khung & Tô nền

`Ctrl + A` → chọn toàn bảng → `Home → Border → All Borders`

**Bỏ đường kẻ giữa ô:** Chọn vùng → `Border → More Borders` → nhấp bỏ đường giữa → OK

**Tô nền:** Chọn vùng → `Home → Fill Color → chọn màu`

⚠️ Tiêu đề bảng và nội dung phải cách nhau ≥ 1 dòng — nếu không `Ctrl+A` sẽ chọn cả tiêu đề vào bảng
"""),

2: (
"Các Kiểu Dữ Liệu trong Excel",
"""### 4 kiểu dữ liệu

| Kiểu | Căn | Ví dụ |
|------|-----|-------|
| **Chuỗi (Text)** | Trái | "Hùng", "A1", "Khá" |
| **Số (Number)** | Phải | 145000, 8.5, 75% |
| **Ngày (Date)** | Phải | 12/24/2024 |
| **Logic** | Giữa | TRUE / FALSE |

---

### Nhập số dưới dạng chuỗi

| Cách | Ví dụ |
|------|-------|
| Thêm dấu `'` trước | `'89` → Excel hiểu là chuỗi |
| Đổi định dạng trước | `Home → Number Format → Text` rồi gõ |

---

### Nhập ngày

- Mặc định Windows: **tháng/ngày/năm** → gõ `12/24/2024`
- Sau khi đổi Windows: **ngày/tháng/năm** → gõ `24/12/2024`
- Ngày căn phải = đúng · Ngày căn trái = Excel hiểu là chuỗi (sai)
- **Phép trừ ngày:** ngày lớn − ngày nhỏ = số ngày chênh lệch

---

### Đổi dấu phân cách (Control Panel)

`Control Panel → Region → Additional Settings`

| Thẻ | Cần đổi |
|-----|---------|
| **Number** | Decimal symbol (thập phân) · Digit grouping symbol (hàng nghìn) · List separator (phân cách đối số hàm) |
| **Date** | Short date format (dd/MM/yyyy hoặc MM/dd/yyyy) |

> **Nhớ nhanh:** Decimal = phẩy → Hàng nghìn = chấm (chuẩn Việt Nam)

⚠️ Dấu phân cách đối số hàm (List separator) phải đúng — thường dùng dấu **chấm phẩy** `;`
"""),

3: (
"Các Loại Địa Chỉ Ô",
"""### 3 loại địa chỉ

| Loại | Ký hiệu | Đặc điểm |
|------|---------|---------|
| **Tương đối** | `G7` | Thay đổi khi sao chép |
| **Tuyệt đối** | `$G$7` | Không thay đổi khi sao chép |
| **Hỗn hợp** | `$G7` hoặc `G$7` | Chỉ cố định cột hoặc dòng |

---

### Quy tắc địa chỉ tương đối khi sao chép

| Hướng sao chép | Thay đổi |
|---------------|---------|
| Sao chép **dọc** (xuống/lên) | **Dòng** thay đổi |
| Sao chép **ngang** (phải/trái) | **Cột** thay đổi |

---

### Chuyển sang địa chỉ tuyệt đối

Đặt con trỏ vào địa chỉ trong công thức → nhấn **F4** (hoặc `Fn + F4` trên laptop)

> Nhấn F4 nhiều lần để xoay vòng: `G7` → `$G$7` → `G$7` → `$G7` → `G7`

---

### Khi nào dùng địa chỉ tuyệt đối?

Khi sao chép công thức mà **một ô tham chiếu phải giữ nguyên** (không được dịch theo).

Ví dụ: Đơn giá tiền lương ở `C3` — khi sao chép xuống phải luôn là `$C$3`.

---

### Format số thứ tự 2 chữ số (01, 02...)

`Home → Number Format → Custom → gõ "00" → OK`

⚠️ Nếu quên F4 khi lập công thức → sao chép xuống sẽ ra kết quả sai
"""),

4: (
"Các Hàm Cơ Bản",
"""### Hàm xử lý chuỗi

| Hàm | Cú pháp | Ý nghĩa |
|-----|---------|---------|
| `LEFT` | `LEFT(text, n)` | Lấy n ký tự bên **trái** |
| `RIGHT` | `RIGHT(text, n)` | Lấy n ký tự bên **phải** |
| `MID` | `MID(text, start, n)` | Lấy n ký tự từ vị trí start |
| `CONCAT` | `CONCAT(text1, text2)` | Nối hai chuỗi |
| `&` | `text1 & text2` | Toán tử nối chuỗi (tương đương CONCAT) |
| `VALUE` | `VALUE(text)` | Đổi chuỗi số → kiểu **số** |

> Kết quả LEFT/RIGHT/MID/CONCAT là **chuỗi** · VALUE trả về **số**

---

### Hàm xử lý số

| Hàm | Ý nghĩa | Ví dụ |
|-----|---------|-------|
| `INT(n)` | Phần nguyên | `INT(3.9)` = 3 |
| `QUOTIENT(a,b)` | Thương nguyên của a÷b | `QUOTIENT(10,3)` = 3 |
| `MOD(a,b)` | Phần dư của a÷b | `MOD(10,3)` = 1 |
| `ROUND(n, d)` | Làm tròn đến d chữ số lẻ | `ROUND(3.14,1)` = 3.1 |

> `ROUND(n, 0)` = làm tròn số nguyên · `ROUND(n, -1)` = làm tròn đến hàng chục

---

### Hàm xử lý ngày

| Hàm | Trả về |
|-----|--------|
| `DAY(date)` | Ngày (số) |
| `MONTH(date)` | Tháng (số) |
| `YEAR(date)` | Năm (số) |

> Ba hàm này luôn trả về **kiểu số**

⚠️ MID(text, start, n): start đếm từ 1, không phải từ 0
"""),

5: (
"Hàm IF, AND, OR",
"""### Hàm IF

`=IF(điều kiện, giá trị nếu đúng, giá trị nếu sai)`

**Lồng IF** (nhiều trường hợp):
```
=IF(dk1, kq1, IF(dk2, kq2, IF(dk3, kq3, kq_còn_lại)))
```
> Dùng **n hàm IF** → cuối công thức đóng **n dấu ngoặc**

---

### Hàm RANK (xếp vị thứ)

`=RANK(ô_cần_xét, $vùng_toàn_bộ$, 0)`

- `0` = xếp giảm dần (điểm cao → vị thứ 1)
- `1` = xếp tăng dần
- Vùng toàn bộ **phải dùng địa chỉ tuyệt đối** ($)

---

### Hàm AND & OR

| Hàm | Ý nghĩa |
|-----|---------|
| `AND(dk1, dk2,...)` | **Tất cả** điều kiện đúng → TRUE |
| `OR(dk1, dk2,...)` | **Ít nhất 1** điều kiện đúng → TRUE |

**Kết hợp với IF:**
```
=IF(AND(dk1, dk2), kq_đúng, kq_sai)
=IF(OR(dk1, dk2), kq_đúng, kq_sai)
```

---

### Ví dụ điển hình

```
Nếu ĐTB ≥ 9 → Giỏi
Nếu ĐTB ≥ 7 → Khá
Nếu ĐTB ≥ 5 → Trung Bình
Còn lại     → Yếu

=IF(L5>=9,"Giỏi",IF(L5>=7,"Khá",IF(L5>=5,"Trung Bình","Yếu")))
```

⚠️ Điều kiện trong IF phải xét từ lớn đến nhỏ (≥9 trước, ≥7 sau...)
"""),

6: (
"Hàm VLOOKUP, HLOOKUP và Hàm Thống Kê",
"""### VLOOKUP — Tìm theo cột

`=VLOOKUP(giá_trị_tìm, bảng_dò, cột_lấy, 0)`

| Đối số | Ý nghĩa |
|--------|---------|
| giá_trị_tìm | Ô chứa mã cần tra |
| bảng_dò | Bảng tra cứu — **nhấn F4** để cố định |
| cột_lấy | Số thứ tự cột cần lấy trong bảng dò (cột 1 là cột tìm kiếm) |
| 0 | Tìm **chính xác** (luôn dùng 0 trong CNTT cơ bản) |

> VLOOKUP tìm trên **cột đầu tiên** của bảng dò → lấy dữ liệu ở cột thứ n

---

### HLOOKUP — Tìm theo dòng

`=HLOOKUP(giá_trị_tìm, bảng_dò, dòng_lấy, 0)`

> HLOOKUP tìm trên **dòng đầu tiên** của bảng dò → lấy dữ liệu ở dòng thứ n

---

### Các hàm thống kê cơ bản

| Hàm | Ý nghĩa |
|-----|---------|
| `COUNT(vùng)` | Đếm ô chứa dữ liệu **kiểu số** |
| `COUNTA(vùng)` | Đếm ô chứa dữ liệu **bất kỳ** (số, chuỗi, ngày) |
| `SUM(vùng)` | Tính tổng |
| `MAX(vùng)` | Giá trị lớn nhất |
| `MIN(vùng)` | Giá trị nhỏ nhất |
| `AVERAGE(vùng)` | Giá trị trung bình |

> AutoSum nhanh: đặt con trỏ vào ô cần tính → `Home → AutoSum → chọn hàm → quét vùng → Enter`

⚠️ VLOOKUP/HLOOKUP bảng dò phải cố định bằng F4, nếu không sao chép công thức xuống sẽ bị lệch
"""),

7: (
"Hàm Thống Kê theo Điều Kiện",
"""### COUNTIF — Đếm 1 điều kiện

`=COUNTIF(range, criteria)`

| Đối số | Ý nghĩa |
|--------|---------|
| range | Vùng cần đếm |
| criteria | Điều kiện (chuỗi trong `"..."`, số viết thẳng) |

---

### COUNTIFS — Đếm nhiều điều kiện

`=COUNTIFS(range1, criteria1, range2, criteria2, ...)`

---

### SUMIF — Tính tổng 1 điều kiện

`=SUMIF(range, criteria, sum_range)`

| Đối số | Ý nghĩa |
|--------|---------|
| range | Vùng kiểm tra điều kiện |
| criteria | Điều kiện |
| sum_range | Vùng cần tính tổng |

---

### SUMIFS — Tính tổng nhiều điều kiện

`=SUMIFS(sum_range, range1, criteria1, range2, criteria2, ...)`

> ⚠️ **sum_range đứng ĐẦU** trong SUMIFS (khác SUMIF)

---

### Ký tự đại diện (Wildcard)

| Ký tự | Ý nghĩa | Ví dụ |
|-------|---------|-------|
| `*` | Nhiều ký tự bất kỳ | `"A*"` = bắt đầu bằng A |
| `?` | Đúng 1 ký tự bất kỳ | `"A?"` = A + 1 ký tự |

---

### Điều kiện so sánh

Viết trong dấu nháy kép: `">5"` · `"<=10"` · `"<>0"`

**Kết hợp ô tham chiếu:** `">"&C1`

⚠️ SUMIFS: sum_range ở đầu · SUMIF: sum_range ở cuối — dễ nhầm thứ tự
"""),

8: (
"Sắp Xếp Dữ Liệu và Vẽ Biểu Đồ",
"""### Sắp xếp dữ liệu (Sort)

1. Đặt con trỏ vào ô bất kỳ trong bảng → `Ctrl + A`
2. `Data → Sort`
3. Tích **My data has headers** (dòng đầu là tiêu đề, không sắp)
4. **Sort By** → chọn cột sắp xếp chính
5. **Order** → Smallest to Largest (tăng dần) / Largest to Smallest (giảm dần)
6. Nếu trùng → **Add Level** → chọn cột sắp xếp phụ → OK

> **Nhớ nhanh:** Sort By = tiêu chí chính · Then By = tiêu chí phụ (khi trùng)

---

### Vẽ biểu đồ cột (Column Chart)

1. Chọn vùng dữ liệu cần vẽ (Ctrl + kéo nếu 2 vùng không liền kề)
2. `Insert → Charts → Column → chọn kiểu → OK`
3. Thêm nhãn số: nhấp dấu `+` bên phải đồ thị → **Data Labels**
4. Đặt tiêu đề: nhấp vào **Chart Title** → gõ tiêu đề
5. Đổi kiểu: `Chart Design → Change Chart Type`

---

### Vẽ biểu đồ tròn (Pie Chart)

- Chỉ chọn **vùng dữ liệu** — **không chọn** dòng/cột tiêu đề
- `Insert → Charts → Pie → chọn kiểu → OK`

---

### So sánh Column vs Pie

| | Column | Pie |
|-|--------|-----|
| Chọn dữ liệu | Có thể gồm tiêu đề | Chỉ chọn số liệu thuần |
| Dùng khi | So sánh nhiều đối tượng | Thể hiện tỉ lệ phần trăm |

⚠️ Vẽ biểu đồ Pie mà chọn cả tiêu đề cột sẽ bị sai dữ liệu
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
  - excel
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
