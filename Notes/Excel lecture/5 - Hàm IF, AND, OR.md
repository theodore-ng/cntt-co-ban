---
title: "Excel lecture - Bài 5: Hàm IF, AND, OR"
tags:
  - excel
  - cntt-co-ban
  - exam-note
---

# Bài 5: Hàm IF, AND, OR

← [[4 - Các Hàm Cơ Bản|Bài 4]]  |  [[Excel lecture|📋 Mục lục]]  |  [[6 - Hàm VLOOKUP, HLOOKUP và Hàm Thống Kê|Bài 6]] →

---

### Hàm IF

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

---

## Ghi Chú Cá Nhân

> [!question] Chưa hiểu
> -

> [!check] Đã nắm
> -

---

← [[4 - Các Hàm Cơ Bản|Bài 4]]  |  [[Excel lecture|📋 Mục lục]]  |  [[6 - Hàm VLOOKUP, HLOOKUP và Hàm Thống Kê|Bài 6]] →
