"""
CSS Stylesheet cho Giao diện Dự Báo Giá Hàng Hóa MXV.
Chuẩn phong cách tài chính trực quan, sạch đẹp, chuyên nghiệp.
"""

CUSTOM_CSS = """
<style>
    /* Reset & Nền tổng thể sáng sạch */
    .stApp {
        background-color: #F4F6F9;
        color: #212529;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    }
    
    /* Tối ưu khoảng cách phía trên */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 2rem !important;
        max-width: 1400px !important;
    }
    
    /* Ẩn hoàn toàn header và sidebar mặc định */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    [data-testid="stSidebar"] {
        display: none !important;
    }
    [data-testid="collapsedControl"] {
        display: none !important;
    }
    
    /* 1. TOP HEADER & BẢNG ĐIỀU KHIỂN NẰM TRỌN TRONG KHỐI XANH ROYAL BLUE */
    .webgia-header {
        background-color: #002B80;
        color: #FFFFFF;
        padding: 12px 20px 8px 20px;
        border-radius: 6px 6px 0 0;
        margin-top: 5px;
        margin-bottom: 0px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .webgia-brand {
        font-size: 24px;
        font-weight: 800;
        letter-spacing: -0.5px;
        white-space: nowrap;
    }
    .webgia-brand span {
        color: #FFCC00;
    }

    /* TÍCH HỢP TOÀN BỘ BẢNG ĐIỀU KHIỂN VÀO KHỐI XANH */
    div[data-testid="stVerticalBlock"] > div:has(.blue-controls-marker) {
        background-color: #002B80 !important;
        border-radius: 0 0 6px 6px !important;
        padding: 0px 20px 14px 20px !important;
        margin-top: 0px !important;
        margin-bottom: 14px !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.15) !important;
    }

    /* Chữ nhãn màu trắng tinh trên nền xanh */
    div:has(.blue-controls-marker) label p,
    div:has(.blue-controls-marker) label {
        color: #FFFFFF !important;
        font-size: 12.5px !important;
        font-weight: 600 !important;
        margin-bottom: 2px !important;
    }

    /* Biến tất cả các ô nhập liệu màu đen thành ô trắng sang trọng */
    div:has(.blue-controls-marker) div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 4px !important;
        height: 38px !important;
        min-height: 38px !important;
    }
    div:has(.blue-controls-marker) div[data-baseweb="select"] span,
    div:has(.blue-controls-marker) div[data-baseweb="select"] div,
    div:has(.blue-controls-marker) div[data-baseweb="select"] svg {
        color: #0F172A !important;
        fill: #0F172A !important;
        font-weight: 500 !important;
    }

    div:has(.blue-controls-marker) div[data-baseweb="input"] {
        background-color: #FFFFFF !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 4px !important;
        height: 38px !important;
    }
    div:has(.blue-controls-marker) input {
        color: #0F172A !important;
        background-color: #FFFFFF !important;
        font-weight: 600 !important;
    }
    div:has(.blue-controls-marker) button[data-testid^="stNumberInputStep"] {
        background-color: #F1F5F9 !important;
        color: #002B80 !important;
        border: none !important;
    }

    /* Nút Chạy mô hình màu vàng nổi bật trên nền xanh */
    div:has(.blue-controls-marker) div[data-testid="stButton"] > button {
        background-color: #FFCC00 !important;
        color: #002B80 !important;
        font-weight: 800 !important;
        border: none !important;
        border-radius: 4px !important;
        height: 38px !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.15) !important;
    }
    div:has(.blue-controls-marker) div[data-testid="stButton"] > button:hover {
        background-color: #FFB800 !important;
        color: #001F5C !important;
    }

    /* 3. SUB-NAVBAR TRẮNG CÓ TAB MẶT HÀNG NỔI BẬT */
    .webgia-subnav {
        background-color: #FFFFFF;
        border: 1px solid #E5E7EB;
        border-radius: 4px;
        padding: 6px 14px;
        display: flex;
        gap: 8px;
        align-items: center;
        overflow-x: auto;
        white-space: nowrap;
        margin-bottom: 14px;
    }
    .subnav-item {
        color: #374151;
        font-size: 13px;
        padding: 5px 10px;
        border-radius: 4px;
        text-decoration: none;
        font-weight: 500;
    }
    .subnav-active {
        background-color: #FFF3CD;
        color: #856404 !important;
        font-weight: 700;
        border-bottom: 2px solid #FFC107;
    }


    /* 5. TIÊU ĐỀ TRANG */
    .page-title {
        color: #002B80;
        font-size: 23px;
        font-weight: 700;
        margin-top: 0px;
        margin-bottom: 2px;
    }
    .page-subtitle {
        color: #64748B;
        font-size: 13.5px;
        margin-bottom: 14px;
    }

    /* 6. KHUNG BÁO GIÁ BÊN PHẢI (TRADINGVIEW QUOTE CARD) */
    .quote-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 16px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        margin-bottom: 16px;
    }
    .quote-ticker {
        font-size: 18px;
        font-weight: 800;
        color: #0F172A;
        margin-bottom: 2px;
    }
    .quote-sub {
        font-size: 12.5px;
        color: #64748B;
        margin-bottom: 10px;
    }
    .quote-price {
        font-size: 30px;
        font-weight: 800;
        color: #0F172A;
        line-height: 1.1;
    }
    .quote-price span.unit {
        font-size: 13.5px;
        font-weight: 500;
        color: #64748B;
    }
    .quote-change {
        font-size: 14.5px;
        font-weight: 700;
        margin-top: 4px;
        margin-bottom: 10px;
    }
    .change-green { color: #00B06F; }
    .change-red { color: #F23645; }
    
    .market-status {
        font-size: 12px;
        color: #00B06F;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 5px;
        margin-bottom: 12px;
    }

    /* Phạm vi ngày */
    .day-range-box {
        border-top: 1px solid #F1F5F9;
        padding-top: 10px;
        margin-top: 6px;
    }
    .range-labels {
        display: flex;
        justify-content: space-between;
        font-size: 12px;
        color: #64748B;
        margin-bottom: 4px;
    }
    .range-bar-bg {
        width: 100%;
        height: 6px;
        background-color: #E2E8F0;
        border-radius: 3px;
        position: relative;
    }
    .range-bar-fill {
        height: 100%;
        background-color: #002B80;
        border-radius: 3px;
    }

    /* 7. SIGNAL BADGE */
    .signal-badge {
        padding: 12px 14px;
        border-radius: 6px;
        text-align: center;
        font-size: 14.5px;
        font-weight: 700;
        margin-bottom: 14px;
        border: 1px solid;
    }
    .badge-buy { background-color: #E6F9F0; border-color: #00B06F; color: #008754; }
    .badge-sell { background-color: #FDE8E8; border-color: #F23645; color: #D32F2F; }
    .badge-wait { background-color: #F1F5F9; border-color: #CBD5E1; color: #475569; }

    /* 8. BẢNG THÔNG TIN TÀI CHÍNH (GIỮ NGUYÊN NỘI DUNG CHỮ) */
    .custom-table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 12px;
        font-size: 13.5px;
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 6px;
        overflow: hidden;
    }
    .custom-table th {
        background-color: #F8FAFC;
        color: #002B80;
        text-align: left;
        padding: 8px 12px;
        border-bottom: 1px solid #E2E8F0;
        font-size: 12px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.3px;
    }
    .custom-table td {
        padding: 8px 12px;
        border-bottom: 1px solid #F1F5F9;
        color: #334155;
    }
    .custom-table td:nth-child(2) {
        text-align: right;
        font-weight: 600;
        color: #0F172A;
    }
    .text-green { color: #00B06F !important; }
    .text-red { color: #F23645 !important; }

    /* 9. FOOTER CHUẨN WEBGIA */
    .webgia-footer {
        background-color: #001F5C;
        color: #CBD5E1;
        padding: 26px 24px 18px 24px;
        margin-top: 35px;
        border-radius: 6px;
        font-size: 13.5px;
        line-height: 1.6;
    }
    .footer-heading {
        color: #FFFFFF;
        font-size: 15.5px;
        font-weight: 700;
        margin-bottom: 10px;
        border-bottom: 2px solid #FFCC00;
        display: inline-block;
        padding-bottom: 3px;
    }
    .footer-bottom {
        border-top: 1px solid rgba(255,255,255,0.1);
        margin-top: 20px;
        padding-top: 14px;
        text-align: center;
        font-size: 12px;
        color: #94A3B8;
    }

    /* Style button Streamlit */
    div[data-testid="stButton"] > button {
        background-color: #002B80;
        color: white;
        border: none;
        border-radius: 4px;
        font-weight: 600;
        padding: 8px 12px;
        height: 38px;
    }
    div[data-testid="stButton"] > button:hover {
        background-color: #001F5C;
        color: white;
    }

    /* 10. REPLAY TOOLBAR CONTAINER */
    div[data-testid="stVerticalBlock"]:has(> div > div > .replay-container-marker) {
        background-color: #FFFFFF !important;
        border: 1px solid #C7D9F5 !important;
        border-radius: 8px !important;
        padding: 14px 18px !important;
        margin-top: 10px !important;
        margin-bottom: 16px !important;
        box-shadow: 0 2px 8px rgba(0, 43, 128, 0.05) !important;
    }
    div[data-testid="stVerticalBlock"]:has(> div > div > .replay-container-marker) [data-testid="stWidgetLabel"] p {
        color: #002B80 !important;
        font-weight: 600 !important;
        font-size: 13px !important;
    }
    .replay-title {
        font-size: 14.5px;
        font-weight: 700;
        color: #002B80;
    }
    .replay-badge {
        background-color: #E6F0FF;
        color: #0044CC;
        padding: 2px 8px;
        border-radius: 12px;
        font-size: 11.5px;
        font-weight: 600;
        margin-left: 8px;
    }

    /* 11. THANH CHÚ GIẢI CHỈ BÁO & HOVER TOOLTIP */
    div[data-testid="stMarkdownContainer"]:has(.indicator-legend-bar),
    div[data-testid="column"]:has(.indicator-legend-bar) {
        overflow: visible !important;
    }
    .indicator-legend-bar {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: #F8FAFC;
        border: 1px solid #CBD5E1;
        border-radius: 6px;
        padding: 6px 12px;
        margin-bottom: 6px;
        flex-wrap: wrap;
        gap: 8px;
        overflow: visible !important;
        min-height: 42px;
        box-sizing: border-box;
    }
    .legend-hint-label {
        font-size: 12px;
        color: #475569;
        display: flex;
        align-items: center;
        gap: 4px;
        font-weight: 500;
    }
    .legend-badges-group {
        display: flex;
        align-items: center;
        gap: 8px;
        flex-wrap: wrap;
        overflow: visible !important;
    }
    .legend-badge-item {
        position: relative;
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background-color: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 4px;
        padding: 5px 10px;
        cursor: pointer;
        transition: all 0.2s ease;
        user-select: none;
    }
    .legend-badge-item:hover {
        background-color: #EEF4FC;
        border-color: #002B80;
        box-shadow: 0 2px 6px rgba(0, 43, 128, 0.15);
    }
    .badge-name {
        font-size: 12px;
        font-weight: 700;
        color: #0F172A;
    }
    .candle-icon-sym {
        display: inline-block;
        width: 13px;
        height: 13px;
        border: 1.5px solid #00B06F;
        background: #00B06F;
        border-radius: 2px;
        box-shadow: 0 0 0 1px #F23645 inset;
    }
    .line-sma-sym {
        display: inline-block;
        width: 15px;
        height: 3px;
        background-color: #2962FF;
        border-radius: 2px;
    }
    .line-bb-sym {
        display: inline-block;
        width: 15px;
        height: 0;
        border-top: 2px dashed #64748B;
    }
    .bar-vol-sym {
        display: inline-flex;
        align-items: flex-end;
        gap: 1.5px;
        height: 12px;
        width: 13px;
    }
    .bar-vol-sym span:nth-child(1) {
        width: 3px;
        height: 6px;
        background-color: #00B06F;
        border-radius: 1px;
    }
    .bar-vol-sym span:nth-child(2) {
        width: 3px;
        height: 12px;
        background-color: #00B06F;
        border-radius: 1px;
    }
    .bar-vol-sym span:nth-child(3) {
        width: 3px;
        height: 8px;
        background-color: #F23645;
        border-radius: 1px;
    }
    .line-ai-sym {
        display: inline-block;
        width: 15px;
        height: 4px;
        border-top: 2px dashed #00B06F;
        border-bottom: 2px dashed #F23645;
    }
    .legend-tooltip-pop {
        position: absolute;
        top: calc(100% + 6px);
        right: 0;
        width: 310px;
        background-color: #0F172A;
        color: #FFFFFF;
        border-radius: 8px;
        padding: 12px 14px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.45);
        font-size: 12px;
        line-height: 1.55;
        z-index: 9999999;
        display: none;
        pointer-events: none;
        text-align: left;
    }
    .legend-badge-item:hover .legend-tooltip-pop {
        display: block !important;
    }
    .legend-tooltip-pop::after {
        content: "";
        position: absolute;
        bottom: 100%;
        right: 18px;
        border-width: 6px;
        border-style: solid;
        border-color: transparent transparent #0F172A transparent;
    }
    .pop-title {
        font-weight: 800;
        color: #FFCC00;
        font-size: 13px;
        margin-bottom: 6px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.15);
        padding-bottom: 4px;
    }
    .pop-desc {
        color: #E2E8F0;
        font-size: 12px;
    }

    /* 12. NÚT HIỆN VOLUME TRONG KHUNG BIỂU ĐỒ */
    div[data-testid="stCheckbox"] {
        background-color: #F8FAFC !important;
        border: 1px solid #CBD5E1 !important;
        border-radius: 6px !important;
        padding: 0 12px !important;
        height: 42px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin-bottom: 6px !important;
        box-sizing: border-box !important;
        transition: all 0.2s ease !important;
        cursor: pointer !important;
    }
    div[data-testid="stCheckbox"]:hover {
        background-color: #EEF4FC !important;
        border-color: #002B80 !important;
        box-shadow: 0 2px 6px rgba(0, 43, 128, 0.12) !important;
    }
    div[data-testid="stCheckbox"]:has(input:checked) {
        background-color: #EEF4FC !important;
        border-color: #002B80 !important;
        box-shadow: 0 0 0 1px #002B80 inset, 0 2px 6px rgba(0, 43, 128, 0.15) !important;
    }
    div[data-testid="stCheckbox"] label {
        margin: 0 !important;
        padding: 0 !important;
        cursor: pointer !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        width: 100% !important;
        height: 100% !important;
        gap: 6px !important;
    }
    div[data-testid="stCheckbox"] label span,
    div[data-testid="stCheckbox"] label p,
    div[data-testid="stCheckbox"] [data-testid="stWidgetLabel"] p,
    div[data-testid="stCheckbox"] p {
        color: #002B80 !important;
        font-weight: 700 !important;
        font-size: 13px !important;
        margin: 0 !important;
        white-space: nowrap !important;
    }

    /* 13. AI BRANDING & HERO CARDS */
    .ai-badge-hdr {
        background: linear-gradient(135deg, rgba(255, 204, 0, 0.25), rgba(255, 170, 0, 0.35));
        border: 1px solid #FFCC00;
        color: #FFCC00;
        padding: 3px 9px;
        border-radius: 4px;
        font-size: 11px;
        font-weight: 800;
        letter-spacing: 0.5px;
        margin-left: 8px;
        display: inline-block;
        vertical-align: middle;
    }
    .ai-status-tag {
        background: rgba(0, 230, 118, 0.15);
        border: 1px solid #00E676;
        color: #00E676;
        padding: 2px 8px;
        border-radius: 3px;
        font-size: 11px;
        font-weight: 700;
        display: inline-block;
    }
    .ai-title-chip {
        background: #EEF4FC;
        border: 1px solid #002B80;
        color: #002B80;
        padding: 3px 9px;
        border-radius: 4px;
        font-size: 12px;
        font-weight: 800;
        margin-left: 8px;
        display: inline-block;
        vertical-align: middle;
    }
    .ai-hero-card {
        background: #FFFFFF;
        border: 1px solid #CBD5E1;
        border-radius: 6px;
        overflow: hidden;
        margin-bottom: 12px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
    }
    .ai-hero-header {
        background: #0F172A;
        color: #FFFFFF;
        padding: 8px 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 11.5px;
    }
    .ai-chip-live {
        display: flex;
        align-items: center;
        gap: 6px;
        color: #FFCC00;
        font-weight: 700;
    }
    .ai-chip-dot {
        width: 8px;
        height: 8px;
        background-color: #00E676;
        border-radius: 50%;
        display: inline-block;
        box-shadow: 0 0 6px #00E676;
        animation: aiPulse 1.5s infinite;
    }
    @keyframes aiPulse {
        0% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.4; transform: scale(0.85); }
        100% { opacity: 1; transform: scale(1); }
    }
    .ai-chip-tech {
        color: #94A3B8;
        font-size: 11px;
        font-weight: 500;
    }
    .ai-hero-body {
        padding: 12px 14px;
    }
    .ai-hero-body.body-buy {
        background: linear-gradient(180deg, #F0FDF4 0%, #FFFFFF 100%);
        border-bottom: 3px solid #00B06F;
    }
    .ai-hero-body.body-sell {
        background: linear-gradient(180deg, #FEF2F2 0%, #FFFFFF 100%);
        border-bottom: 3px solid #F23645;
    }
    .ai-hero-body.body-wait {
        background: linear-gradient(180deg, #F8FAFC 0%, #FFFFFF 100%);
        border-bottom: 3px solid #64748B;
    }
    .ai-hero-signal {
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 10px;
    }
    .ai-signal-icon {
        font-size: 26px;
    }
    .ai-signal-action {
        font-size: 15px;
        font-weight: 800;
        line-height: 1.2;
    }
    .body-buy .ai-signal-action { color: #00875A; }
    .body-sell .ai-signal-action { color: #D32F2F; }
    .body-wait .ai-signal-action { color: #475569; }
    .ai-signal-sub {
        font-size: 11.5px;
        color: #64748B;
        font-weight: 500;
        margin-top: 2px;
    }
    .ai-confidence-box {
        background: rgba(255, 255, 255, 0.85);
        border: 1px solid #E2E8F0;
        border-radius: 4px;
        padding: 6px 10px;
    }
    .ai-conf-row {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 12px;
        color: #334155;
        margin-bottom: 4px;
    }
    .ai-conf-row b {
        color: #002B80;
        font-size: 13px;
    }
    .ai-conf-progress-bg {
        height: 6px;
        background-color: #E2E8F0;
        border-radius: 3px;
        overflow: hidden;
    }
    .body-buy .ai-conf-progress-bar {
        height: 100%;
        background: linear-gradient(90deg, #00B06F, #00E676);
    }
    .body-sell .ai-conf-progress-bar {
        height: 100%;
        background: linear-gradient(90deg, #F23645, #FF5252);
    }
    .body-wait .ai-conf-progress-bar {
        height: 100%;
        background: #94A3B8;
    }
    /* 13. KHỐI XAI NẰM DƯỚI BIỂU ĐỒ */
    .xai-dashboard-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 14px 18px;
        margin-top: 10px;
        margin-bottom: 20px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
    }
    .xai-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 12px;
        padding-bottom: 8px;
        border-bottom: 1px solid #E2E8F0;
        flex-wrap: wrap;
        gap: 6px;
    }
    .xai-header-title {
        font-weight: 700;
        font-size: 13.5px;
        color: #002B80;
        letter-spacing: 0.2px;
    }
    .xai-header-sub {
        font-size: 11.5px;
        color: #64748B;
        font-weight: 500;
    }
    .xai-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 12px;
    }
    @media (max-width: 900px) {
        .xai-grid {
            grid-template-columns: 1fr;
        }
    }
    .xai-box {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 6px;
        padding: 12px 14px;
    }
    .xai-box-title {
        font-weight: 700;
        font-size: 12.5px;
        color: #1E293B;
        margin-bottom: 6px;
    }
    .xai-box-desc {
        font-size: 12px;
        color: #475569;
        line-height: 1.55;
    }
    .xai-box-desc code {
        background-color: #0F172A;
        color: #00E676;
        padding: 1px 5px;
        border-radius: 3px;
        font-size: 11px;
    }
</style>
"""
