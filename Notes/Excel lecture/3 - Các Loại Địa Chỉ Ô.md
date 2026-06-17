---
title: "Excel lecture - Bài 3: Các Loại Địa Chỉ Ô"
tags:
  - excel
  - cntt-co-ban
  - exam-note
---

# Bài 3: Các Loại Địa Chỉ Ô

← [[2 - Các Kiểu Dữ Liệu trong Excel|Bài 2]]  |  [[Excel lecture|📋 Mục lục]]  |  [[4 - Các Hàm Cơ Bản|Bài 4]] →

---

### 3 loại địa chỉ

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

---

## Ghi Chú Cá Nhân

> [!question] Chưa hiểu
> -

> [!check] Đã nắm
> -

---

← [[2 - Các Kiểu Dữ Liệu trong Excel|Bài 2]]  |  [[Excel lecture|📋 Mục lục]]  |  [[4 - Các Hàm Cơ Bản|Bài 4]] →
