---
title: "Excel lecture - Bài 4: Các Hàm Cơ Bản"
tags:
  - excel
  - cntt-co-ban
  - exam-note
---

# Bài 4: Các Hàm Cơ Bản

← [[3 - Các Loại Địa Chỉ Ô|Bài 3]]  |  [[Excel lecture|📋 Mục lục]]  |  [[5 - Hàm IF, AND, OR|Bài 5]] →

---

### Hàm xử lý chuỗi

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

---

## Ghi Chú Cá Nhân

> [!question] Chưa hiểu
> -

> [!check] Đã nắm
> -

---

← [[3 - Các Loại Địa Chỉ Ô|Bài 3]]  |  [[Excel lecture|📋 Mục lục]]  |  [[5 - Hàm IF, AND, OR|Bài 5]] →
