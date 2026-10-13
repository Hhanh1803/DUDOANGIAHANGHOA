"""
Module chứa các thành phần giao diện người dùng (UI Components).
Bao gồm: Thanh điều hướng, Thẻ báo giá, Khối AI Hero, Bảng tài chính, Khối XAI và Footer chuẩn Webgia.
"""

import streamlit as st

try:
    from src.predict import generate_trading_signal, get_trading_plan
    from src.config import QUICK_ITEMS
except ImportError:
    from predict import generate_trading_signal, get_trading_plan
    from config import QUICK_ITEMS

INDICATOR_BAR_HTML = """
<div class="indicator-legend-bar">
    <div class="legend-hint-label">💡 <b>CHÚ GIẢI CHỈ BÁO</b> <span style="color:#64748B; font-weight:normal;">(Rê chuột để xem giải nghĩa):</span></div>
    <div class="legend-badges-group">
        <div class="legend-badge-item" title="📊 Biểu đồ Nến Nhật: Biểu diễn 4 mức giá trong phiên (Mở, Đóng, Cao, Thấp). Nến xanh là TĂNG, Nến đỏ là GIẢM.">
            <span class="candle-icon-sym"></span>
            <span class="badge-name">Giá (VNĐ)</span>
            <div class="legend-tooltip-pop">
                <div class="pop-title">📊 Biểu đồ Nến Nhật (Candlestick)</div>
                <div class="pop-desc">
                    Biểu diễn 4 mức giá quan trọng trong mỗi phiên:<br>
                    • <b>Mở cửa & Đóng cửa:</b> Thân nến thể hiện khoảng dao động chính.<br>
                    • <b>Cao nhất & Thấp nhất:</b> Râu nến trên và dưới.<br>
                    • <span style="color:#00E676; font-weight:bold;">🟢 Nến Xanh:</span> Giá đóng cửa cao hơn mở cửa (Thị trường TĂNG).<br>
                    • <span style="color:#FF5252; font-weight:bold;">🔴 Nến Đỏ:</span> Giá đóng cửa thấp hơn mở cửa (Thị trường GIẢM).
                </div>
            </div>
        </div>
        <div class="legend-badge-item" title="📈 Đường SMA 20: Trung bình giá 20 phiên. Giá nằm TRÊN SMA 20 là xu hướng TĂNG, dưới là GIẢM.">
            <span class="line-sma-sym"></span>
            <span class="badge-name">SMA 20</span>
            <div class="legend-tooltip-pop">
                <div class="pop-title">📈 Đường Trung Bình Động 20 Phiên (SMA 20)</div>
                <div class="pop-desc">
                    Đường màu xanh tính giá đóng cửa trung bình của 20 phiên gần nhất:<br>
                    • <b>Giá nằm TRÊN SMA 20:</b> Xu hướng thị trường đang <b>TĂNG TRƯỞNG</b> tích cực.<br>
                    • <b>Giá nằm DƯỚI SMA 20:</b> Xu hướng thị trường đang <b>SUY YẾU / ĐIỀU CHỈNH</b>.<br>
                    • Đóng vai trò là mức cản hỗ trợ/kháng cự động quan trọng.
                </div>
            </div>
        </div>
        <div class="legend-badge-item" title="🛡️ Dải BB High: Dải Bollinger trên (Kháng cự động / Quá mua). Báo hiệu giá tăng quá nóng, dễ điều chỉnh giảm.">
            <span class="line-bb-sym"></span>
            <span class="badge-name">BB High</span>
            <div class="legend-tooltip-pop">
                <div class="pop-title">🛡️ Dải Bollinger Band Trên (BB High)</div>
                <div class="pop-desc">
                    Đường nét đứt phía trên đo lường độ lệch chuẩn +2 của biên độ dao động:<br>
                    • Là <b>Ngưỡng Kháng Cự động</b> của thị trường.<br>
                    • Khi giá tiệm cận hoặc đâm thủng BB High: Báo hiệu vùng <b>QUÁ MUA (Overbought)</b>, lực mua bắt đầu suy kiệt và có xác suất cao xuất hiện nhịp giảm chốt lời.
                </div>
            </div>
        </div>
        <div class="legend-badge-item" title="🛡️ Dải BB Low: Dải Bollinger dưới (Hỗ trợ động / Quá bán). Báo hiệu lực bán cạn kiệt, dễ phục hồi bật tăng.">
            <span class="line-bb-sym"></span>
            <span class="badge-name">BB Low</span>
            <div class="legend-tooltip-pop">
                <div class="pop-title">🛡️ Dải Bollinger Band Dưới (BB Low)</div>
                <div class="pop-desc">
                    Đường nét đứt phía dưới đo lường độ lệch chuẩn -2 của biên độ dao động:<br>
                    • Là <b>Ngưỡng Hỗ Trợ động</b> quan trọng.<br>
                    • Khi giá chạm hoặc thủng qua BB Low: Báo hiệu vùng <b>QUÁ BÁN (Oversold)</b>, lực bán tháo đã cạn kiệt và thường kích hoạt lực cầu bắt đáy giúp giá phục hồi bật tăng.
                </div>
            </div>
        </div>
        <div class="legend-badge-item" title="🎯 Kế hoạch AI: Đường nét đứt dự báo giá chốt lời (TP - Xanh) và cắt lỗ an toàn (SL - Đỏ) tính toán tự động từ mô hình Machine Learning.">
            <span class="line-ai-sym"></span>
            <span class="badge-name">Kế hoạch AI</span>
            <div class="legend-tooltip-pop">
                <div class="pop-title">🤖 Kế Hoạch Dự Báo Từ Mô Hình AI</div>
                <div class="pop-desc">
                    Hệ thống Machine Learning (XGBoost) phân tích hơn 14 chỉ báo kỹ thuật & vĩ mô để dự phóng:<br>
                    • <span style="color:#00E676; font-weight:bold;">🎯 Đường Nét Đứt Xanh (AI TP):</span> Mức giá mục tiêu dự kiến đạt tới để <b>Chốt lời tối ưu</b>.<br>
                    • <span style="color:#FF5252; font-weight:bold;">⛔ Đường Nét Đứt Đỏ (AI SL):</span> Ngưỡng phòng thủ bắt buộc để <b>Cắt lỗ & bảo vệ an toàn vốn</b>.
                </div>
            </div>
        </div>
        <div class="legend-badge-item" title="📊 Khối lượng (Volume): Tổng số hợp đồng giao dịch trong phiên. Cột xanh là Mua, Cột đỏ là Bán, Đường vàng là Vol MA 20.">
            <span class="bar-vol-sym"><span></span><span></span><span></span></span>
            <span class="badge-name">Volume</span>
            <div class="legend-tooltip-pop">
                <div class="pop-title">📊 Khối Lượng Giao Dịch (Volume) & Dòng Tiền</div>
                <div class="pop-desc">
                    Tổng số hợp đồng tương lai khớp lệnh trong phiên:<br>
                    • <span style="color:#00E676; font-weight:bold;">🟢 Cột Xanh:</span> Phiên TĂNG giá — Lực Mua chủ động áp đảo.<br>
                    • <span style="color:#FF5252; font-weight:bold;">🔴 Cột Đỏ:</span> Phiên GIẢM giá — Lực Bán chủ động chiếm ưu thế.<br>
                    • <span style="color:#FFB300; font-weight:bold;">📈 Đường Vàng Vol MA 20:</span> Thanh khoản bình quân 20 phiên. Khi cột Volume cao đột biến vượt qua đường này: Xác nhận <b>DÒNG TIỀN LỚN (Cá Mập/Tổ chức)</b> nhập cuộc, củng cố xu hướng bứt phá (Breakout) tin cậy cao!
                </div>
            </div>
        </div>
    </div>
</div>
"""


def render_header():
    """Hiển thị Top Header khối xanh hoàng gia chuẩn Webgia Hàng Hóa"""
    st.markdown("""
<div class="webgia-header">
    <div style="display: flex; justify-content: space-between; align-items: center; width: 100%; flex-wrap: wrap; gap: 8px;">
        <div style="display: flex; align-items: center; gap: 10px;">
            <div class="webgia-brand">Dự Báo Giá <span>Hàng Hóa</span> <span style="font-size:14px; font-weight:500; color:#E0E7FF; margin-left:8px;">| SÀN HÀNG HÓA MXV</span></div>
            <span class="ai-badge-hdr">🤖 AI QUANT ENGINE</span>
        </div>
        <div style="font-size:12.5px; color:#E0E7FF; font-weight:500; display: flex; align-items: center; gap: 8px;">
            <span class="ai-status-tag">⚡ AI MODEL: ONLINE (XGBOOST)</span>
            <span>CBOT</span> • <span>NYMEX</span> • <span>ICE</span> • <span style="color:#00E676; font-weight:700;">🟢 DỮ LIỆU THỜI GIAN THỰC</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


def render_subnav(asset_name, quick_items=None):
    """Hiển thị Sub-navbar với các thẻ mặt hàng nổi bật, tự động highlight mặt hàng đang chọn"""
    if quick_items is None:
        quick_items = QUICK_ITEMS
    subnav_html = '<div class="webgia-subnav">'
    for item in quick_items:
        if item == asset_name:
            subnav_html += f'<span class="subnav-item subnav-active">Giá {item}</span>'
        else:
            subnav_html += f'<span class="subnav-item">Giá {item}</span>'
    subnav_html += '</div>'
    st.markdown(subnav_html, unsafe_allow_html=True)


def render_page_title(asset_name, ticker):
    """Hiển thị tiêu đề và phụ đề trang"""
    st.markdown(f"""
<div class="page-title">
    Biểu đồ giá {asset_name} thế giới hôm nay - {ticker}
    <span class="ai-title-chip">🤖 AI DỰ BÁO XU HƯỚNG</span>
</div>
<div class="page-subtitle">Biểu đồ kỹ thuật trực tiếp & Tín hiệu giao dịch tự động hóa bằng Trí tuệ nhân tạo (Machine Learning XGBoost)</div>
""", unsafe_allow_html=True)


def render_quote_and_ai(df_sub, asset_name, ticker, unit, margin_req, lot_size, capital, risk_pct, ai_model=None, is_replay=False, target_hour=""):
    """
    Hiển thị cột phải gồm:
    1. Thẻ báo giá (Quote Card) kèm thanh phạm vi ngày
    2. Thẻ khuyến nghị AI Hero Card (XGBoost v2.4 & Độ tin cậy)
    3. 3 bảng chi tiết tài chính (Kế hoạch hành động, Dự báo mục tiêu giá, Quản trị rủi ro & phân bổ vốn)
    """
    current_features = df_sub.iloc[-1].to_dict()
    signal, confidence, ai_status = generate_trading_signal(current_features, ai_model)
    plan = get_trading_plan(current_features, signal)
    
    current_price = df_sub['Close'].iloc[-1]
    prev_price = df_sub['Close'].iloc[-2] if len(df_sub) > 1 else current_price
    change_val = current_price - prev_price
    change_pct = (change_val / prev_price) * 100 if prev_price > 0 else 0
    day_high = df_sub['High'].iloc[-1]
    day_low = df_sub['Low'].iloc[-1]
    day_span = day_high - day_low if day_high > day_low else 1
    slider_pct = min(max(((current_price - day_low) / day_span) * 100, 0), 100)
    
    change_class = "change-green" if change_val >= 0 else "change-red"
    change_prefix = "+" if change_val >= 0 else ""
    status_label = f"⏱️ Diễn biến tại: {target_hour}" if is_replay and target_hour else "🟢 Thị trường mở cửa"
    sub_desc = f"{asset_name} • Hàng hóa • Nến lúc {target_hour}" if is_replay and target_hour else f"{asset_name} • Hàng hóa • Kỳ hạn MXV"
    
    st.markdown(f"""
    <div class="quote-card">
        <div class="quote-ticker">{ticker}</div>
        <div class="quote-sub">{sub_desc}</div>
        <div class="quote-price">{current_price:,.0f} <span class="unit">VNĐ / {unit}</span></div>
        <div class="quote-change {change_class}">{change_prefix}{change_val:,.0f} ({change_prefix}{change_pct:.2f}%)</div>
        <div class="market-status">{status_label}</div>
        <div class="day-range-box">
            <div class="range-labels">
                <span>Thấp: {day_low:,.0f}</span>
                <span style="font-weight:600; color:#002B80;">PHẠM VI NGÀY</span>
                <span>Cao: {day_high:,.0f}</span>
            </div>
            <div class="range-bar-bg">
                <div class="range-bar-fill" style="width: {slider_pct:.1f}%;"></div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # 2. TÍN HIỆU KHUYẾN NGHỊ TỪ TRÍ TUỆ NHÂN TẠO (AI QUANT CO-PILOT CARD)
    if plan['action_code'] == 1:
        sig_icon = "🟢"
        sig_action = "MUA VÀO (LONG)"
        sig_sub = "Xác suất tăng giá cao • Tối ưu lợi nhuận"
        sig_cls = "body-buy"
    elif plan['action_code'] == -1:
        sig_icon = "🔴"
        sig_action = "BÁN RA (SHORT)"
        sig_sub = "Xác suất giảm giá cao • Bảo toàn vốn"
        sig_cls = "body-sell"
    else:
        sig_icon = "⚪"
        sig_action = "THEO DÕI (QUAN SÁT)"
        sig_sub = "Thị trường giằng co • Rủi ro biến động cao"
        sig_cls = "body-wait"

    ai_hero_html = f"""
    <div class="ai-hero-card">
        <div class="ai-hero-header">
            <div class="ai-chip-live">
                <span class="ai-chip-dot"></span>
                <span>AI QUANT CO-PILOT</span>
            </div>
            <div class="ai-chip-tech">XGBoost ML v2.4</div>
        </div>
        <div class="ai-hero-body {sig_cls}">
            <div class="ai-hero-signal">
                <div class="ai-signal-icon">{sig_icon}</div>
                <div>
                    <div class="ai-signal-action">{sig_action}</div>
                    <div class="ai-signal-sub">{sig_sub}</div>
                </div>
            </div>
            <div class="ai-confidence-box">
                <div class="ai-conf-row">
                    <span>Độ tin cậy mô hình AI:</span>
                    <b>{confidence:.1f}%</b>
                </div>
                <div class="ai-conf-progress-bg">
                    <div class="ai-conf-progress-bar" style="width: {min(max(confidence, 0), 100):.1f}%;"></div>
                </div>
            </div>
        </div>
    </div>
    """
    st.markdown(ai_hero_html, unsafe_allow_html=True)
    
    # 3. BẢNG CHI TIẾT TÀI CHÍNH TÍCH HỢP TỪ MÔ HÌNH AI
    if plan['action_code'] != 0:
        risk_per_unit = abs(plan['entry'] - plan['sl'])
        max_loss = capital * (risk_pct / 100)
        safe_volume = max_loss / risk_per_unit if risk_per_unit > 0 else 0
        reward_per_unit = abs(plan['tp'] - plan['entry'])
        rr_ratio = reward_per_unit / risk_per_unit if risk_per_unit > 0 else 0
        
        target_color = "text-green" if plan['action_code'] == 1 else "text-red"
        action_text = "🟢 MUA VÀO / NHẬP HÀNG" if plan['action_code'] == 1 else "🔴 BÁN RA / XUẤT HÀNG"
        
        required_lots = safe_volume / lot_size
        total_margin = required_lots * margin_req
        
        html_tables = f"""
        <table class="custom-table">
            <tr><th colspan="2">1. KẾ HOẠCH HÀNH ĐỘNG TỪ AI</th></tr>
            <tr><td>Lệnh hành động ngay lúc này:</td><td class="{target_color}">{action_text}</td></tr>
            <tr><td>Vùng giá ký hợp đồng (Entry):</td><td>{plan['entry']:,.0f} VNĐ / {unit}</td></tr>
        </table>
        
        <table class="custom-table">
            <tr><th colspan="2">2. DỰ BÁO MỤC TIÊU GIÁ CỦA AI</th></tr>
            <tr><td>Mức giá dự kiến sẽ đạt (Chốt lời):</td><td class="text-green">{plan['tp']:,.0f} VNĐ / {unit}</td></tr>
            <tr><td>Tỷ lệ Lợi nhuận / Rủi ro (R:R):</td><td>1 : {rr_ratio:.1f}</td></tr>
        </table>
        
        <table class="custom-table">
            <tr><th colspan="2">3. QUẢN TRỊ RỦI RO & PHÂN BỔ VỐN AI</th></tr>
            <tr><td>Ngưỡng giá nguy hiểm (Cắt lỗ):</td><td class="text-red">{plan['sl']:,.0f} VNĐ / {unit}</td></tr>
            <tr><td>Khối lượng đầu tư an toàn tuyệt đối:</td><td>{safe_volume:,.0f} {unit}</td></tr>
            <tr><td>Ký quỹ MXV (mỗi {lot_size:,.0f} {unit}):</td><td>{margin_req:,.0f} VNĐ</td></tr>
        </table>
        """
        st.markdown(html_tables, unsafe_allow_html=True)
    else:
        st.info("Thị trường hiện đang đi ngang, phe mua và phe bán giằng co. AI chưa tìm thấy xu hướng rõ ràng. Khuyến nghị: Đứng ngoài quan sát.")


def render_xai_analysis(df_sub, ai_model=None):
    """
    Hiển thị Khối Giải trình AI (Explainable AI - XAI) dạng 3 cột ngang đặt ngay dưới biểu đồ nến giá.
    Bao gồm 3 trụ cột: Kỹ thuật (Technicals), Vĩ mô (Macro DXY), Dòng tiền Order Flow.
    """
    current_features = df_sub.iloc[-1].to_dict()
    signal, confidence, ai_status = generate_trading_signal(current_features, ai_model)
    plan = get_trading_plan(current_features, signal)
    
    if plan['action_code'] != 0:
        rsi_val = current_features.get('RSI', 50)
        macd_val = current_features.get('MACD', 0)
        macd_sig = current_features.get('MACD_Signal', 0)
        action_name = "MUA VÀO (LONG)" if plan['action_code'] == 1 else "BÁN RA (SHORT)"
        order_side = "MUA (Bulls)" if plan['action_code'] == 1 else "BÁN (Bears)"
        macd_dir = "cắt lên trên đường Signal" if macd_val > macd_sig else "cắt xuống dưới đường Signal"
        
        xai_html = f"""
        <div class="xai-dashboard-card">
            <div class="xai-header">
                <span class="xai-header-title">🧠 4. ĐỘNG CƠ PHÂN TÍCH CỦA AI (EXPLAINABLE AI - XAI)</span>
                <span class="xai-header-sub">Hệ thống phân tích đa nhân tố: Kỹ thuật • Vĩ mô (DXY) • Dòng tiền liên thị trường</span>
            </div>
            <div class="xai-grid">
                <div class="xai-box">
                    <div class="xai-box-title">📊 1. Chỉ Báo Kỹ Thuật (Technicals)</div>
                    <div class="xai-box-desc">
                        Chỉ số RSI đạt <code>{rsi_val:.1f}</code>; MACD đang <b>{macd_dir}</b>. Cấu trúc giá và dải Bollinger Bands ủng hộ mạnh mẽ tín hiệu <b>{action_name}</b>.
                    </div>
                </div>
                <div class="xai-box">
                    <div class="xai-box-title">🌐 2. Tác Động Vĩ Mô (Macro DXY)</div>
                    <div class="xai-box-desc">
                        Chỉ số Dollar Index (DXY) biến động tương quan nghịch với giá hàng hóa. Môi trường tỷ giá USD/VND tạo động lực trợ giá cho hợp đồng.
                    </div>
                </div>
                <div class="xai-box">
                    <div class="xai-box-title">⚡ 3. Dòng Tiền & Order Flow</div>
                    <div class="xai-box-desc">
                        Phân tích thanh khoản Order Flow xác nhận phe <b>{order_side}</b> đang chủ động kiểm soát và bảo vệ các ngưỡng then chốt của thị trường.
                    </div>
                </div>
            </div>
        </div>
        """
        st.markdown(xai_html, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="xai-dashboard-card" style="padding: 12px 16px;">
            <span style="font-size: 13px; color: #64748B;">
                🧠 <b>4. ĐỘNG CƠ PHÂN TÍCH AI (XAI):</b> Thị trường hiện đang đi ngang (Sideway), phe mua và phe bán giằng co. Mô hình khuyến nghị đứng ngoài quan sát để bảo toàn vốn.
            </span>
        </div>
        """, unsafe_allow_html=True)


def render_footer():
    """Hiển thị Footer toàn trang chuẩn Webgia Hàng Hóa"""
    st.markdown("""
<div class="webgia-footer">
    <div style="display: flex; gap: 40px; flex-wrap: wrap;">
        <div style="flex: 1.2; min-width: 280px;">
            <div class="footer-heading">Giới thiệu - Dự Báo Giá Hàng Hóa</div>
            <p>
                Hệ thống Dự Báo Giá Hàng Hóa (Commodity Predictor) là giải pháp ứng dụng Machine Learning hỗ trợ phân tích xu hướng thị trường và đưa ra khuyến nghị thời điểm giao dịch tối ưu cho các doanh nghiệp xuất nhập khẩu, nông dân và nhà đầu tư phái sinh hàng hóa (MXV).
            </p>
        </div>
        <div style="flex: 1.8; min-width: 320px;">
            <div class="footer-heading">Thông tin thị trường hàng hóa</div>
            <p style="margin-bottom: 6px;">
                <b>Nông sản & Nguyên liệu:</b> Giá Cà phê Robusta/Arabica, Đậu tương, Khô đậu tương, Dầu đậu tương, Ngô, Lúa mì Chicago/Kansas, Gạo thô, Đường 11, Ca cao, Bông sợi.
            </p>
            <p style="margin-bottom: 6px;">
                <b>Năng lượng & Kim loại:</b> Giá Vàng, Bạc, Đồng, Bạch kim, Palađi, Dầu thô WTI, Dầu Brent, Khí tự nhiên, Xăng pha chế, Dầu sưởi (DO).
            </p>
            <p style="margin-bottom: 6px;">
                <b>Công nghệ Phân tích:</b> Mô hình dự báo giá Machine Learning (XGBoost), Tín hiệu khuyến nghị điểm vào lệnh MXV, Quản trị vốn & tính toán mức ký quỹ an toàn.
            </p>
            <p style="margin-bottom: 0;">
                <b>Liên kết hữu ích:</b> Sở Giao dịch Hàng hóa Việt Nam (MXV), Báo cáo cung cầu nông sản thế giới (USDA), Lịch mùa vụ nông sản Việt Nam.
            </p>
        </div>
    </div>
    <div class="footer-bottom">
        <div style="margin-bottom: 8px;">
            <a href="#" style="color:#94A3B8; text-decoration:none; margin: 0 10px;">Giới thiệu</a> | 
            <a href="#" style="color:#94A3B8; text-decoration:none; margin: 0 10px;">Chính sách bảo mật</a> | 
            <a href="#" style="color:#94A3B8; text-decoration:none; margin: 0 10px;">Điều khoản sử dụng</a> | 
            <a href="#" style="color:#94A3B8; text-decoration:none; margin: 0 10px;">Từ chối trách nhiệm</a> | 
            <a href="#" style="color:#94A3B8; text-decoration:none; margin: 0 10px;">Liên hệ</a>
        </div>
        <div>© 2026, Dự Báo Giá Hàng Hóa (Commodity Predictor) - Hệ thống AI phân tích & Dự báo thị trường hàng hóa MXV.</div>
    </div>
</div>
""", unsafe_allow_html=True)
