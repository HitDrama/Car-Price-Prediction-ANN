
# Used Car Price Prediction


## 🔗 Giới thiệu
Dự án này dự đoán giá xe ô tô đã qua sử dụng dựa trên dữ liệu thực tế được thu thập từ website [Bonbanh.com](https://bonbanh.com/), bao gồm khoảng **800 chiếc xe** được crawl từ page 1 - 40.

Dự án sử dụng mô hình **Artificial Neural Network (ANN)** để huấn luyện trên các đặc trưng của xe, giá để dự đoán giá bán lại có độ chính xác cao.

---

## 🔢 Dataset

### ✨ Nguồn dữ liệu
- Website: [https://bonbanh.com/](https://bonbanh.com)
- Số lượng: ~800 xe

### 📂 Các trường dữ liệu:
- **hang**: Hãng xe (Toyota, Ford, etc)
- **mau**: Phiên bản/Đời mẫu
- **nam**: Năm sản xuất
- **so_km**: Số km đã đi
- **dong_co**: Thông tin động cơ
- **so_cho**: Số chỗ ngồi
- **mau_xe**: Màu sắc
- **tinh_trang**: Tình trạng (xe mới / cũ)
- **loai_dong_co**: Loại nhiên liệu (Xăng / Dầu)
- **gia_vnd**: Giá bán (VNĐ)

### 📈 Tiền xử lý dữ liệu:
- NaN được xử lý bằng trung vị, mode hoặc thay = `không xác định`.
- Đã chuẩn hóa số km, năm, giá, số chỗ về dạng numeric.

---

## 🛠 Kiến trúc Mô hình

- **Mô hình**: ANN Sequential Model
- **Tầng (Layers)**:
  - Dense(64 units, relu) + L2 regularization + Dropout 40%
  - Dense(32 units, relu) + Dropout 20%
  - Dense(16 units, relu)
  - Dense(1 unit, linear) (Output)

- **Trình biên dịch**:
```python
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse', metrics=['mae'])
```
## 🔢 Dự đoán giá xe thực tế

<img src="https://github.com/HitDrama/Car-Price-Prediction-ANN/blob/main/static/training/Screenshot%202025-04-29%20103150.png" alt="Model Architecture" width="700"/>

---
## 🚀 Tác giả

**Đặng Tô Nhân - Developer**
