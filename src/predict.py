import numpy as np
import joblib
import os
import pandas as pd

def load_ai_model(model_path='models/xgb_classifier.pkl'):
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None

def generate_trading_signal(current_features, model=None):
    if model is not None:
        features = ['RSI', 'Stoch', 'SMA_20', 'SMA_50', 'EMA_20', 'MACD', 'MACD_Signal', 'BB_High', 'BB_Low', 'ATR']
        x_input = pd.DataFrame([current_features])[features]
        
        pred = model.predict(x_input)[0]
        proba = np.max(model.predict_proba(x_input)[0]) * 100
        
        if pred == 1: signal = 1
        elif pred == 2: signal = -1
        else: signal = 0
        
        return signal, proba, "Machine Learning"
    else:
        rsi = current_features.get('RSI', 50)
        macd = current_features.get('MACD', 0)
        macd_signal = current_features.get('MACD_Signal', 0)
        close_price = current_features.get('Close', 0)
        sma_20 = current_features.get('SMA_20', 0)
        
        if rsi < 40 and macd > macd_signal and close_price > sma_20: signal = 1
        elif rsi > 60 and macd < macd_signal and close_price < sma_20: signal = -1
        else: signal = 0
            
        return signal, 75.0, "Rule-base"

def generate_explanation(current_features, signal):
    """Tạo lời giải thích sử dụng ngôn ngữ phổ thông, văn phong chuyên nghiệp"""
    rsi = current_features.get('RSI', 50)
    macd = current_features.get('MACD', 0)
    macd_signal = current_features.get('MACD_Signal', 0)
    close_price = current_features.get('Close', 0)
    sma_20 = current_features.get('SMA_20', 0)
    
    reasons = []
    if signal == 1:
        reasons.append("<b>Xu hướng:</b> Giá hiện tại đang duy trì mức cao hơn trung bình 20 ngày, cho thấy thị trường đang có đà tăng trưởng tốt.")
        if rsi < 50:
            reasons.append("<b>Rủi ro:</b> Áp lực bán ra đã giảm bớt. Đây là mức giá tương đối an toàn để xem xét mua vào.")
        if macd > macd_signal:
            reasons.append("<b>Dòng tiền:</b> Khối lượng mua đang có dấu hiệu tăng lên rõ rệt.")
    elif signal == -1:
        reasons.append("<b>Xu hướng:</b> Giá đang thấp hơn mức trung bình 20 ngày, cho thấy thị trường đang suy yếu.")
        if rsi > 50:
            reasons.append("<b>Rủi ro:</b> Giá đã tăng khá nóng trong thời gian qua, khả năng những người mua trước đó sẽ bắt đầu chốt lời.")
        if macd < macd_signal:
            reasons.append("<b>Dòng tiền:</b> Lượng người bán đang chiếm ưu thế.")
    else:
        reasons.append("Thị trường hiện tại đang đi ngang và chưa hình thành xu hướng tăng/giảm rõ rệt.")
        reasons.append("Rủi ro dao động thất thường đang ở mức cao. Hệ thống khuyến nghị bạn nên giữ nguyên nguồn vốn và tiếp tục theo dõi thêm trước khi ra quyết định.")
        
    return "<br><br>".join(reasons)

def get_trading_plan(current_features, signal, lots=1):
    close_price = current_features.get('Close', 0)
    atr = current_features.get('ATR', 0)
    
    if atr == 0 or signal == 0:
        return {
            "signal": "CHỜ (Đứng ngoài quan sát)",
            "action_code": 0,
            "entry": 0,
            "tp": 0,
            "sl": 0
        }
        
    entry = close_price
    if signal == 1:
        action = "MUA VÀO (Long)"
        sl = entry - (1.5 * atr)
        tp = entry + (3.0 * atr)
    else:
        action = "BÁN RA (Short)"
        sl = entry + (1.5 * atr)
        tp = entry - (3.0 * atr)
        
    return {
        "signal": action,
        "action_code": signal,
        "entry": round(entry, 0),
        "tp": round(tp, 0),
        "sl": round(sl, 0)
    }
