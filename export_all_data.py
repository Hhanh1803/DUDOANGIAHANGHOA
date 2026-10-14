import os
import re
import pandas as pd
from src.config import MXV_INFO
from src.data_preprocessing import fetch_data, add_technical_indicators

def sanitize_filename(name):
    # Loại bỏ ký tự đặc biệt để làm tên file an toàn
    name = name.replace(" ", "_").replace("(", "").replace(")", "").replace("/", "_")
    return name

def export_all():
    output_dir = "data/all_commodities"
    os.makedirs(output_dir, exist_ok=True)
    
    total_items = len(MXV_INFO)
    print(f"==================================================")
    print(f"🚀 BẮT ĐẦU TẢI & XUẤT DỮ LIỆU TOÀN BỘ {total_items} MẶT HÀNG MXV")
    print(f"📁 Thư mục lưu: {output_dir}/")
    print(f"==================================================\n")
    
    combined_list = []
    success_count = 0
    
    for i, (asset_name, info) in enumerate(MXV_INFO.items(), 1):
        ticker = info["ticker"]
        multiplier = info["multiplier"]
        category = info["category"]
        
        print(f"[{i:02d}/{total_items:02d}] Đang tải: {asset_name} ({ticker}) - Nhóm: {category}...", end=" ", flush=True)
        
        try:
            # Tải dữ liệu 1 năm gần nhất, khung 1 ngày (1d)
            df = fetch_data(ticker, period="1y", interval="1d", multiplier=multiplier)
            
            if df is not None and not df.empty:
                df = add_technical_indicators(df)
                
                # 1. Lưu file CSV riêng cho từng mặt hàng
                file_name = f"{sanitize_filename(asset_name)}.csv"
                file_path = os.path.join(output_dir, file_name)
                df.to_csv(file_path, index=False)
                
                # 2. Thêm thông tin vào bảng tổng hợp chung
                df_combined = df.copy()
                df_combined.insert(0, "Mặt hàng", asset_name)
                df_combined.insert(1, "Nhóm", category)
                df_combined.insert(2, "Mã Ticker", ticker)
                combined_list.append(df_combined)
                
                print(f"✅ Xong ({len(df)} ngày)")
                success_count += 1
            else:
                print("⚠️ Không có dữ liệu")
        except Exception as e:
            print(f"❌ Lỗi: {e}")
            
    # Lưu file tổng hợp tất cả mặt hàng vào 1 file duy nhất
    if combined_list:
        combined_df = pd.concat(combined_list, ignore_index=True)
        combined_file_path = "data/tat_ca_hang_hoa_tong_hop.csv"
        combined_df.to_csv(combined_file_path, index=False)
        print(f"\n==================================================")
        print(f"🎉 HOÀN THÀNH!")
        print(f"✅ Đã xuất thành công: {success_count}/{total_items} mặt hàng.")
        print(f"📁 Từng file riêng lẻ tại: {output_dir}/")
        print(f"📊 File TỔNG HỢP toàn bộ: {combined_file_path} (Tổng cộng: {len(combined_df):,} dòng)")
        print(f"==================================================")

if __name__ == "__main__":
    export_all()
