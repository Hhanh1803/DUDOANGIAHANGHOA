"""
Module vẽ biểu đồ kỹ thuật chuyên sâu (Plotly Candlestick & Technical Indicators).
Hỗ trợ Candlestick, SMA 20, Bollinger Bands, Volume, Vol MA 20 và các mốc TP/SL dự phóng từ AI.
"""

import streamlit as st
import plotly.graph_objects as go
from plotly.subplots import make_subplots

try:
    from src.predict import generate_trading_signal, get_trading_plan
except ImportError:
    from predict import generate_trading_signal, get_trading_plan


def render_chart(df_sub, asset_name="", ai_model=None, is_replay=False, target_hour="", show_volume=False):
    """
    Vẽ biểu đồ nến kỹ thuật chuyên nghiệp.
    Dùng chung cho cả chế độ xem trực tiếp và chế độ mô phỏng chuyển động từng giờ (Market Replay).
    """
    x_data = df_sub['Date'] if 'Date' in df_sub else df_sub.index
    
    if is_replay:
        # Trong chế độ chạy từng giờ: Hiển thị 35 nến gần nhất để nến to rõ, dễ quan sát chuyển động
        df_plot = df_sub.tail(35)
        x_plot = df_plot['Date'] if 'Date' in df_plot else df_plot.index
        init_start_x = x_plot.iloc[0]
        init_end_x = x_plot.iloc[-1]
    else:
        df_plot = df_sub
        x_plot = x_data
        init_view_idx = max(0, len(x_plot) - 75)
        init_start_x = x_plot.iloc[init_view_idx]
        init_end_x = x_plot.iloc[-1]
        
    time_buttons = [
        dict(count=1, label="1T", step="month", stepmode="backward"),
        dict(count=3, label="3T", step="month", stepmode="backward"),
        dict(count=6, label="6T", step="month", stepmode="backward"),
        dict(count=1, label="1N", step="year", stepmode="backward"),
        dict(count=3, label="3N", step="year", stepmode="backward"),
        dict(count=5, label="5N", step="year", stepmode="backward"),
        dict(count=10, label="10N", step="year", stepmode="backward"),
        dict(step="all", label="Tất cả (25N+)")
    ]
    
    range_selector_cfg = dict(
        buttons=time_buttons,
        bgcolor="#EEF4FC",
        activecolor="#FFCC00",
        bordercolor="#D6E4F8",
        borderwidth=1,
        x=0,
        y=1.05,
        xanchor="left",
        yanchor="bottom",
        font=dict(size=11, color="#002B80")
    )
    
    if show_volume:
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                            vertical_spacing=0.04, row_width=[0.28, 0.72])
        fig.add_trace(go.Candlestick(
            x=x_plot, open=df_plot['Open'], high=df_plot['High'],
            low=df_plot['Low'], close=df_plot['Close'], 
            name='Giá (VNĐ)',
            increasing_line_color='#00B06F', decreasing_line_color='#F23645',
            hovertemplate="<b>Nến Giá</b> (%{x})<br>Đóng: %{close:,.0f} VNĐ<br>Mở: %{open:,.0f} VNĐ<br>Cao: %{high:,.0f} VNĐ<br>Thấp: %{low:,.0f} VNĐ<extra>Giá thực tế</extra>"
        ), row=1, col=1)
        fig.add_trace(go.Scatter(
            x=x_plot, y=df_plot['SMA_20'], 
            line=dict(color='#2962FF', width=1.5), 
            name='SMA 20',
            hovertemplate="<b>SMA 20 (Đường trung bình 20 phiên)</b><br>Mức giá: %{y:,.0f} VNĐ<br><i>Giá trên SMA 20 là xu hướng TĂNG</i><extra>Xu hướng</extra>"
        ), row=1, col=1)
        fig.add_trace(go.Scatter(
            x=x_plot, y=df_plot['BB_High'], 
            line=dict(color='rgba(100, 116, 139, 0.5)', width=1, dash='dot'), 
            name='BB High',
            hovertemplate="<b>BB High (Bollinger Band Trên)</b><br>Kháng cự: %{y:,.0f} VNĐ<br><i>Vùng Quá Mua - Dễ đảo chiều giảm</i><extra>Kháng cự</extra>"
        ), row=1, col=1)
        fig.add_trace(go.Scatter(
            x=x_plot, y=df_plot['BB_Low'], 
            line=dict(color='rgba(100, 116, 139, 0.5)', width=1, dash='dot'), 
            name='BB Low', fill='tonexty', fillcolor='rgba(41,98,255,0.03)',
            hovertemplate="<b>BB Low (Bollinger Band Dưới)</b><br>Hỗ trợ: %{y:,.0f} VNĐ<br><i>Vùng Quá Bán - Dễ bật tăng lại</i><extra>Hỗ trợ</extra>"
        ), row=1, col=1)
        
        vol_colors = ['#00B06F' if row['Close'] >= row['Open'] else '#F23645' for _, row in df_plot.iterrows()]
        vol_type_text = [
            'Phiên TĂNG (Phe Mua áp đảo)' if row['Close'] >= row['Open'] else 'Phiên GIẢM (Phe Bán áp đảo)'
            for _, row in df_plot.iterrows()
        ]
        fig.add_trace(go.Bar(
            x=x_plot, y=df_plot['Volume'], 
            marker=dict(color=vol_colors, line=dict(color=vol_colors, width=0.8), opacity=1.0),
            name='Khối lượng (Volume)',
            customdata=vol_type_text,
            hovertemplate="<b>Khối lượng (%{x}):</b> %{y:,.0f} HĐ<br><b>Tính chất:</b> %{customdata}<extra>Volume</extra>"
        ), row=2, col=1)
        
        vol_ma = df_plot['Volume'].rolling(20, min_periods=1).mean()
        fig.add_trace(go.Scatter(
            x=x_plot, y=vol_ma,
            line=dict(color='#F59E0B', width=1.5),
            name='Vol MA 20',
            hovertemplate="<b>Vol MA 20 (%{x}):</b> %{y:,.0f} HĐ<br><i>Đường trung bình khối lượng 20 phiên</i><extra>Vol MA 20</extra>"
        ), row=2, col=1)
        
        fig.update_xaxes(
            range=[init_start_x, init_end_x],
            rangeselector=range_selector_cfg if not is_replay else None,
            rangeslider_visible=False,
            row=1, col=1
        )
        fig.update_xaxes(rangeslider_visible=False, row=2, col=1)
        fig.update_yaxes(
            row=2, col=1,
            side="right",
            showgrid=True, gridcolor="#F1F5F9",
            tickformat="~s",
            title=dict(text="Khối lượng (HĐ)", font=dict(size=11, color="#64748B"))
        )
    else:
        fig = go.Figure()
        fig.add_trace(go.Candlestick(
            x=x_plot, open=df_plot['Open'], high=df_plot['High'],
            low=df_plot['Low'], close=df_plot['Close'], 
            name='Giá (VNĐ)',
            increasing_line_color='#00B06F', decreasing_line_color='#F23645',
            hovertemplate="<b>Nến Giá</b> (%{x})<br>Đóng: %{close:,.0f} VNĐ<br>Mở: %{open:,.0f} VNĐ<br>Cao: %{high:,.0f} VNĐ<br>Thấp: %{low:,.0f} VNĐ<extra>Giá thực tế</extra>"
        ))
        fig.add_trace(go.Scatter(
            x=x_plot, y=df_plot['SMA_20'], 
            line=dict(color='#2962FF', width=1.5), 
            name='SMA 20',
            hovertemplate="<b>SMA 20 (Đường trung bình 20 phiên)</b><br>Mức giá: %{y:,.0f} VNĐ<br><i>Giá trên SMA 20 là xu hướng TĂNG</i><extra>Xu hướng</extra>"
        ))
        fig.add_trace(go.Scatter(
            x=x_plot, y=df_plot['BB_High'], 
            line=dict(color='rgba(100, 116, 139, 0.5)', width=1, dash='dot'), 
            name='BB High',
            hovertemplate="<b>BB High (Bollinger Band Trên)</b><br>Kháng cự: %{y:,.0f} VNĐ<br><i>Vùng Quá Mua - Dễ đảo chiều giảm</i><extra>Kháng cự</extra>"
        ))
        fig.add_trace(go.Scatter(
            x=x_plot, y=df_plot['BB_Low'], 
            line=dict(color='rgba(100, 116, 139, 0.5)', width=1, dash='dot'), 
            name='BB Low', fill='tonexty', fillcolor='rgba(41,98,255,0.03)',
            hovertemplate="<b>BB Low (Bollinger Band Dưới)</b><br>Hỗ trợ: %{y:,.0f} VNĐ<br><i>Vùng Quá Bán - Dễ bật tăng lại</i><extra>Hỗ trợ</extra>"
        ))
        fig.update_xaxes(
            range=[init_start_x, init_end_x],
            rangeselector=range_selector_cfg if not is_replay else None,
            rangeslider_visible=False
        )

    # Vẽ các mốc dự báo mục tiêu từ Mô hình AI (Take Profit & Stop Loss) trực tiếp lên biểu đồ
    try:
        curr_feat = df_sub.iloc[-1].to_dict()
        ai_sig, _, _ = generate_trading_signal(curr_feat, ai_model)
        ai_pl = get_trading_plan(curr_feat, ai_sig)
        if ai_pl['action_code'] != 0:
            hl_kwargs = dict(row=1, col=1) if show_volume else {}
            tp_val = ai_pl['tp']
            sl_val = ai_pl['sl']
            fig.add_hline(
                y=tp_val, line_dash="dash", line_color="#00B06F", line_width=1.5,
                annotation_text=f"🎯 AI TP (Mục tiêu): {tp_val:,.0f} VNĐ",
                annotation_position="top left",
                annotation_font=dict(size=10.5, color="#00875A", family="Arial"),
                annotation_bgcolor="rgba(240, 253, 244, 0.85)",
                **hl_kwargs
            )
            fig.add_hline(
                y=sl_val, line_dash="dash", line_color="#F23645", line_width=1.5,
                annotation_text=f"⛔ AI SL (Ngưỡng an toàn): {sl_val:,.0f} VNĐ",
                annotation_position="bottom left",
                annotation_font=dict(size=10.5, color="#D32F2F", family="Arial"),
                annotation_bgcolor="rgba(254, 242, 242, 0.85)",
                **hl_kwargs
            )
    except Exception:
        pass

    layout_update = dict(
        template="plotly_white",
        plot_bgcolor="#FFFFFF", paper_bgcolor="#FFFFFF",
        height=680 if show_volume else 640, margin=dict(l=0, r=40, t=35, b=10),
        yaxis=dict(side="right", showgrid=True, gridcolor="#F1F5F9", tickformat=",.0f"),
        xaxis=dict(showgrid=True, gridcolor="#F1F5F9"),
        showlegend=False,
        dragmode="pan"
    )
    if is_replay and target_hour and asset_name:
        layout_update["title"] = dict(text=f"Biểu đồ {asset_name} - Diễn biến lúc {target_hour}", font=dict(size=14, color="#002B80"), x=0.5, xanchor="center")
    
    fig.update_layout(**layout_update)
    st.plotly_chart(fig, use_container_width=True, config=dict(scrollZoom=True, displayModeBar=False))
