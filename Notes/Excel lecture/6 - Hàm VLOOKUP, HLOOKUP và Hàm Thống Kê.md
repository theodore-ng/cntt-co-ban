---
title: "Excel lecture - Bài 6: Hàm VLOOKUP, HLOOKUP và Hàm Thống Kê"
tags:
  - excel
  - cntt-co-ban
  - exam-note
---

# Bài 6: Hàm VLOOKUP, HLOOKUP và Hàm Thống Kê

← [[5 - Hàm IF, AND, OR|Bài 5]]  |  [[Excel lecture|📋 Mục lục]]  |  [[7 - Hàm Thống Kê theo Điều Kiện|Bài 7]] →

---

### VLOOKUP — Tìm theo cột

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

---

## Ghi Chú Cá Nhân

> [!question] Chưa hiểu
> -

> [!check] Đã nắm
> -

---

← [[5 - Hàm IF, AND, OR|Bài 5]]  |  [[Excel lecture|📋 Mục lục]]  |  [[7 - Hàm Thống Kê theo Điều Kiện|Bài 7]] →
