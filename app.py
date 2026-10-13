import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os
import time

# Thêm thư mục src vào PATH
sys.path.append(os.path.abspath('src'))

from src.config import MXV_INFO, CATEGORIES, QUICK_ITEMS
from src.styles import CUSTOM_CSS
from src.data_preprocessing import fetch_data, add_technical_indicators
from src.predict import load_ai_model
from src.charts import render_chart
from src.ui_components import (
    INDICATOR_BAR_HTML,
    render_header,
    render_subnav,
    render_page_title,
    render_quote_and_ai,
    render_xai_analysis,
    render_footer
)

# --- CONFIG PAGE ---
st.set_page_config(
    page_title="Dự Báo Giá Hàng Hóa MXV (Commodity Predictor)", 
    page_icon="📈", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# --- ÁP DỤNG STYLESHEET CHUẨN GIAO DIỆN ---
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# --- 1. TOP HEADER KHỐI XANH HOÀNG GIA CHUẨN WEBGIA ---
render_header()

# --- 2. BẢNG ĐIỀU KHIỂN TÍCH HỢP TRỌN VẸN VÀO KHỐI XANH ---
with st.container():
    st.markdown("<div class='blue-controls-marker'></div>", unsafe_allow_html=True)
    ctrl_c1, ctrl_c2, ctrl_c3, ctrl_c4, ctrl_c5 = st.columns([1.8, 2.4, 2.0, 2.2, 1.6], gap="small")

    with ctrl_c1:
        category = st.selectbox("Nhóm hàng hóa", CATEGORIES, index=0)
    with ctrl_c2:
        assets_in_category = [name for name, info in MXV_INFO.items() if info["category"] == category]
        asset_name = st.selectbox("Mặt hàng (Hợp đồng)", assets_in_category)
    with ctrl_c3:
        timeframe = st.selectbox("Khung thời gian", [
            "1 Ngày (1D) - Trung hạn", 
            "1 Giờ (1H) - Ngắn hạn", 
            "Theo ngày (Chạy từng giờ ⏱️)"
        ])
        is_replay_mode = "Theo ngày" in timeframe
        interval = "1h" if (is_replay_mode or "1H" in timeframe) else "1d"
    with ctrl_c4:
        capital = st.number_input("Số vốn khả dụng (VNĐ)", min_value=10_000_000, value=500_000_000, step=50_000_000)
    with ctrl_c5:
        risk_pct = st.number_input("Rủi ro (%)", min_value=0.5, max_value=10.0, value=2.0, step=0.5)

ticker = MXV_INFO[asset_name]["ticker"]
unit_full = MXV_INFO[asset_name]["unit_full"]
unit = MXV_INFO[asset_name]["unit"]
multiplier = MXV_INFO[asset_name]["multiplier"]
margin_req = MXV_INFO[asset_name]["margin"]
lot_size = MXV_INFO[asset_name]["lot_size"]

# --- 3. SUB-NAVBAR TỰ ĐỘNG HIGHLIGHT MẶT HÀNG ĐANG CHỌN ---
render_subnav(asset_name, QUICK_ITEMS)

# --- DATA FETCHING & AI ENGINE CACHE ---
if 'df' not in st.session_state or st.session_state.get('ticker') != ticker or st.session_state.get('interval') != interval:
    with st.spinner("Đang tải dữ liệu và chạy mô hình..."):
        period = '60d' if interval == '1h' else 'max'
        df_raw = fetch_data(ticker, period=period, interval=interval, multiplier=multiplier)
        if df_raw is None or df_raw.empty:
            st.warning(f"⚠️ Chưa lấy được dữ liệu hợp đồng '{asset_name}' ({ticker}) từ Sàn quốc tế lúc này. Vui lòng chọn mặt hàng khác hoặc kiểm tra lại sau ít phút.")
            st.stop()
        df = add_technical_indicators(df_raw)
        st.session_state['df'] = df
        st.session_state['asset_name'] = asset_name
        st.session_state['ticker'] = ticker
        st.session_state['interval'] = interval

df = st.session_state['df']
ai_model = load_ai_model('models/xgb_classifier.pkl')

# --- BẢNG ĐIỀU KHIỂN MÔ PHỎNG NẾU Ở CHẾ ĐỘ 'THEO NGÀY (CHẠY TỪNG GIỜ)' ---
play_clicked = False
if is_replay_mode:
    df['Day'] = df['Date'].dt.date
    day_counts = df.groupby('Day').size()
    # Chỉ lấy các ngày có từ 2 nến trở lên để có thể quan sát diễn biến
    valid_days = sorted(day_counts[day_counts > 1].index.tolist())
    day_list = list(reversed(valid_days))
    
    day_map = {}
    today_dt = datetime.now().date()
    for idx, d in enumerate(day_list):
        n_candles = day_counts[d]
        label = d.strftime("%d/%m/%Y")
        if d == today_dt:
            label += f" (Hôm nay - {n_candles} giờ)"
        elif idx == 0:
            label += f" (Phiên gần nhất - {n_candles} giờ)"
        else:
            label += f" ({n_candles} giờ)"
        day_map[label] = d
        
    day_labels = list(day_map.keys())
    
    with st.container():
        st.markdown("<div class='replay-container-marker'></div>", unsafe_allow_html=True)
        st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
            <div class="replay-title">⏱️ MÔ PHỎNG DIỄN BIẾN THEO GIỜ TRONG NGÀY <span class="replay-badge">MARKET REPLAY</span></div>
            <div style="font-size: 12.5px; color: #64748B;">Quan sát nến và tín hiệu AI chuyển động trực tiếp theo từng giờ</div>
        </div>
        """, unsafe_allow_html=True)
        
        rp_col1, rp_col2, rp_col3, rp_col4, rp_col5 = st.columns([2.5, 2.0, 1.8, 1.6, 2.1], gap="small")
        with rp_col1:
            selected_day_label = st.selectbox("Chọn ngày quan sát", day_labels, index=0)
            selected_day = day_map[selected_day_label]
            
        day_hourly_df = df[df['Day'] == selected_day].reset_index(drop=True)
        total_hours = len(day_hourly_df)
        if total_hours == 0:
            day_hourly_df = df.tail(1).reset_index(drop=True)
            total_hours = 1
            
        with rp_col2:
            speed_option = st.selectbox("Tốc độ chuyển động", ["Bình thường (0.6s/giờ)", "Nhanh (0.3s/giờ)", "Chậm rãi (1.2s/giờ)"], index=0)
            speed_sec = 0.3 if "Nhanh" in speed_option else (1.2 if "Chậm rãi" in speed_option else 0.6)
            
        if 'replay_day' not in st.session_state or st.session_state['replay_day'] != selected_day:
            st.session_state['replay_step'] = total_hours
            st.session_state['replay_day'] = selected_day
            
        with rp_col3:
            st.markdown("<div style='height: 27px;'></div>", unsafe_allow_html=True)
            play_clicked = st.button("▶️ TỰ ĐỘNG CHẠY", use_container_width=True, type="primary")
            
        with rp_col4:
            st.markdown("<div style='height: 27px;'></div>", unsafe_allow_html=True)
            if st.button("🔄 Từ 00:00", use_container_width=True):
                st.session_state['replay_step'] = 1
                
        with rp_col5:
            sub_btn1, sub_btn2 = st.columns(2)
            with sub_btn1:
                st.markdown("<div style='height: 27px;'></div>", unsafe_allow_html=True)
                if st.button("⏮️ Lùi 1h", use_container_width=True):
                    st.session_state['replay_step'] = max(1, st.session_state.get('replay_step', total_hours) - 1)
            with sub_btn2:
                st.markdown("<div style='height: 27px;'></div>", unsafe_allow_html=True)
                if st.button("⏭️ Tiến 1h", use_container_width=True):
                    st.session_state['replay_step'] = min(total_hours, st.session_state.get('replay_step', total_hours) + 1)
                    
        curr_step = min(max(1, st.session_state.get('replay_step', total_hours)), total_hours)
        time_label_curr = day_hourly_df['Date'].iloc[curr_step - 1].strftime("%H:%M")
        
        if total_hours > 1:
            slider_step = st.slider(
                f"Kéo thanh trượt để quan sát chuyển động từng giờ bằng mắt: (Nến hiện tại lúc {time_label_curr} - Nến {curr_step}/{total_hours})",
                min_value=1, max_value=total_hours, value=curr_step, step=1
            )
            if slider_step != st.session_state.get('replay_step'):
                st.session_state['replay_step'] = slider_step
        else:
            st.info(f"Thời điểm duy nhất: {time_label_curr}")

# --- TIÊU ĐỀ TRANG ---
render_page_title(asset_name, ticker)

# --- MAIN DASHBOARD LAYOUT (2 CỘT: BIỂU ĐỒ & BÁO GIÁ/AI) ---
col_chart, col_quote = st.columns([6.8, 3.2], gap="medium")
with col_chart:
    tbar_c1, tbar_c2 = st.columns([7.8, 2.2], gap="small")
    with tbar_c1:
        st.markdown(INDICATOR_BAR_HTML, unsafe_allow_html=True)
    with tbar_c2:
        show_volume = st.checkbox(
            "📊 Hiện Volume", 
            value=False, 
            key="chart_volume_checkbox",
            help="📊 Khối lượng giao dịch (Volume): Tổng số hợp đồng khớp lệnh mua/bán tại Sở MXV. Cột xanh = Mua áp đảo; Cột đỏ = Bán áp đảo; Đường vàng = Bình quân 20 phiên (Vol MA 20)."
        )
    chart_ph = st.empty()
quote_ph = col_quote.empty()

if is_replay_mode and play_clicked:
    prog_ph = st.empty()
    for s in range(1, total_hours + 1):
        target_timestamp = day_hourly_df['Date'].iloc[s - 1]
        sub_df = df[df['Date'] <= target_timestamp]
        hour_str = target_timestamp.strftime("%H:%M")
        
        prog_ph.markdown(f"<div style='font-size:13.5px; font-weight:600; color:#002B80; margin-bottom:8px;'>⏱️ Đang phát lại: <b>{hour_str}</b> (Nến {s}/{total_hours}) - Đang quan sát nến & tín hiệu AI chuyển động...</div>", unsafe_allow_html=True)
        with chart_ph.container():
            render_chart(sub_df, asset_name=asset_name, ai_model=ai_model, is_replay=True, target_hour=hour_str, show_volume=show_volume)
            render_xai_analysis(sub_df, ai_model=ai_model)
        with quote_ph.container():
            render_quote_and_ai(sub_df, asset_name, ticker, unit, margin_req, lot_size, capital, risk_pct, ai_model=ai_model, is_replay=True, target_hour=hour_str)
        time.sleep(speed_sec)
    prog_ph.empty()
    st.session_state['replay_step'] = total_hours
else:
    if is_replay_mode:
        step_idx = min(max(1, st.session_state.get('replay_step', total_hours)), total_hours)
        target_timestamp = day_hourly_df['Date'].iloc[step_idx - 1]
        sub_df = df[df['Date'] <= target_timestamp]
        hour_str = target_timestamp.strftime("%H:%M")
    else:
        sub_df = df
        hour_str = ""
        
    with chart_ph.container():
        render_chart(sub_df, asset_name=asset_name, ai_model=ai_model, is_replay=is_replay_mode, target_hour=hour_str, show_volume=show_volume)
        render_xai_analysis(sub_df, ai_model=ai_model)
    with quote_ph.container():
        render_quote_and_ai(sub_df, asset_name, ticker, unit, margin_req, lot_size, capital, risk_pct, ai_model=ai_model, is_replay=is_replay_mode, target_hour=hour_str)

# --- FOOTER CHUẨN WEBGIA HÀNG HÓA ---
render_footer()
