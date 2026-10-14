# Thư mục Dữ liệu (Data Directory)

Thư mục này chứa các tệp dữ liệu của dự án:

1. **`all_commodities/`**: Chứa 23 file CSV dữ liệu lịch sử giá và chỉ báo kỹ thuật của từng mặt hàng riêng lẻ (Đậu tương, Cà phê, Vàng, Dầu thô...).
2. **`tat_ca_hang_hoa_tong_hop.csv`**: File tổng hợp gộp tất cả 23 mặt hàng vào một bảng duy nhất (hơn 4.600 dòng).
3. **`agricultural_prices.csv`**: Dữ liệu lịch sử giá nông sản thế giới (hơn 260.000 dòng).

---
### Cách cập nhật dữ liệu mới nhất:
Chạy lệnh sau tại thư mục gốc:
```bash
python3 export_all_data.py
```
