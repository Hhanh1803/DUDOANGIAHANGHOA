# 📈 HỆ THỐNG DỰ BÁO GIÁ & CỐ VẤN GIAO DỊCH HÀNG HÓA MXV (COMMODITY PREDICTOR)

Hệ thống hỗ trợ phân tích kỹ thuật, dự báo xu hướng giá và lập kế hoạch giao dịch tự động cho các mặt hàng phái sinh niêm yết tại **Sở Giao dịch Hàng hóa Việt Nam (MXV)** liên thông quốc tế (CBOT, ICE, NYMEX, COMEX), ứng dụng mô hình Trí tuệ nhân tạo **XGBoost**.

---

## 📋 Yêu cầu hệ thống
* **Hệ điều hành:** macOS, Windows hoặc Linux.
* **Python:** Phiên bản `Python 3.9` trở lên.
* **Kết nối Internet:** Để tự động tải dữ liệu trực tiếp từ Yahoo Finance.

---

## 🛠️ Hướng dẫn Cài đặt (Setup)

### Bước 1: Mở Terminal / Command Prompt
Mở Terminal và di chuyển đến thư mục dự án:
```bash


### Bước 2: (Khuyến nghị) Tạo và kích hoạt môi trường ảo
* **Trên macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
* **Trên Windows:**
  ```cmd
  python -m venv venv
  venv\Scripts\activate
  ```

### Bước 3: Cài đặt các thư viện phụ thuộc
Cài đặt tất cả các thư viện cần thiết thông qua file `requirements.txt`:
```bash
pip install -r requirements.txt
```
*(Nếu dùng macOS mà chưa kích hoạt venv, có thể dùng: `pip3 install -r requirements.txt`)*

---

## 🚀 Hướng dẫn Chạy dự án (How to Run)

### 1. Khởi chạy Giao diện Web (Streamlit App)
Để mở giao diện bảng điều khiển dự báo giá trên trình duyệt:
```bash
python3 -m streamlit run app.py
```
*(Hoặc: `streamlit run app.py`)*

👉 Sau khi chạy lệnh, trình duyệt web sẽ tự động mở tại địa chỉ: **`http://localhost:8501`**

---

### 2. Tải và Xuất dữ liệu toàn bộ 23 mặt hàng ra Excel/CSV
Để tải dữ liệu lịch sử giá mới nhất và các chỉ báo kỹ thuật của toàn bộ 23 mặt hàng nông sản, kim loại, năng lượng:
```bash
python3 export_all_data.py
```
* **Kết quả:**
  * File tổng hợp gộp tất cả: `data/tat_ca_hang_hoa_tong_hop.csv` (hơn 4.600 dòng).
  * 23 file CSV riêng lẻ từng mặt hàng tại: `data/all_commodities/`.

---

### 3. Huấn luyện lại mô hình AI (Train Model)
Nếu muốn huấn luyện lại mô hình Machine Learning XGBoost với dữ liệu mới:
```bash
python3 src/train.py
```
* Mô hình sau khi huấn luyện sẽ tự động được lưu vào: `models/xgb_classifier.pkl`.

---

## 📂 Cấu trúc thư mục dự án

```text
Dubaogianongsan/
├── app.py                      # File giao diện chính chạy ứng dụng Streamlit
├── export_all_data.py          # Script tải & xuất toàn bộ 23 mặt hàng ra CSV
├── requirements.txt            # Danh sách các thư viện Python cần cài đặt
├── README.md                   # Hướng dẫn chi tiết cài đặt và sử dụng
│
├── src/                        # Thư mục mã nguồn chính
│   ├── config.py               # Danh mục mã hàng hóa, tỷ giá và quy chuẩn MXV
│   ├── data_preprocessing.py   # Lấy dữ liệu từ Yahoo Finance và tính 10 chỉ báo kỹ thuật
│   ├── train.py                # Huấn luyện mô hình XGBoost và lưu file .pkl
│   ├── predict.py              # Động cơ dự báo tín hiệu (Mua/Bán/Chờ), XAI và quản trị rủi ro
│   ├── charts.py               # Vẽ biểu đồ nến tương tác Plotly chuẩn tài chính
│   ├── styles.py               # Bộ mã CSS giao diện WebGia chuyên nghiệp
│   └── ui_components.py        # Các khối giao diện, bảng báo giá và thẻ tín hiệu AI
│
├── data/                       # Thư mục chứa dữ liệu
│   ├── all_commodities/        # 23 file CSV riêng biệt của từng mặt hàng
│   ├── tat_ca_hang_hoa_tong_hop.csv # Bảng dữ liệu tổng hợp toàn bộ mặt hàng
│   └── agricultural_prices.csv # Bộ dữ liệu lịch sử giá nông sản thế giới
│
└── models/                     # Thư mục lưu trữ mô hình AI
    └── xgb_classifier.pkl      # File mô hình XGBoost đã được huấn luyện sẵn
```

---

## 💡 Các tính năng chính của hệ thống
1. **Quy đổi giá chuẩn VNĐ:** Tự động quy đổi giá từ Cent/USD trên sàn CBOT, ICE, NYMEX sang VNĐ theo đúng quy định sàn MXV.
2. **Biểu đồ nến kỹ thuật tương tác:** Tích hợp nến Nhật, khối lượng Volume, dải Bollinger Bands, EMA, SMA, RSI, MACD.
3. **Động cơ AI (XGBoost):** Dự báo xu hướng tương lai và sinh tín hiệu **MUA VÀO**, **BÁN RA** hoặc **CHỜ** kèm xác suất tin cậy (%).
4. **Quản trị rủi ro tự động (ATR):** Tự động tính điểm vào lệnh (Entry), cắt lỗ (Stop Loss) và chốt lời (Take Profit) theo tỷ lệ chuẩn $1:2$.
5. **Trí tuệ nhân tạo có thể giải thích (Explainable AI - XAI):** Diễn giải lý do thị trường bằng văn phong tiếng Việt chuyên nghiệp.
6. **Chế độ tua lại (Replay):** Mô phỏng chuyển động từng giờ trong phiên giao dịch.
