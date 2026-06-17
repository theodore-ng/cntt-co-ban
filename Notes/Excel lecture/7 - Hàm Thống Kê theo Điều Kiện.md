---
title: "Excel lecture - Bài 7: Hàm Thống Kê theo Điều Kiện"
tags:
  - excel
  - cntt-co-ban
  - exam-note
---

# Bài 7: Hàm Thống Kê theo Điều Kiện

← [[6 - Hàm VLOOKUP, HLOOKUP và Hàm Thống Kê|Bài 6]]  |  [[Excel lecture|📋 Mục lục]]  |  [[8 - Sắp Xếp Dữ Liệu và Vẽ Biểu Đồ|Bài 8]] →

---

### COUNTIF — Đếm 1 điều kiện

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

---

## Ghi Chú Cá Nhân

> [!question] Chưa hiểu
> -

> [!check] Đã nắm
> -

---

← [[6 - Hàm VLOOKUP, HLOOKUP và Hàm Thống Kê|Bài 6]]  |  [[Excel lecture|📋 Mục lục]]  |  [[8 - Sắp Xếp Dữ Liệu và Vẽ Biểu Đồ|Bài 8]] →
