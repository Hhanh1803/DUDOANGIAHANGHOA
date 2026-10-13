import yfinance as yf
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os
import numpy as np
from data_preprocessing import fetch_data, add_technical_indicators

def create_target_labels(df, look_forward=3):
    """
    Tạo nhãn phân loại: 
    1: Giá tăng > 1% sau look_forward ngày
    -1: Giá giảm > 1% sau look_forward ngày
    0: Đi ngang
    """
    df = df.copy()
    future_returns = df['Close'].shift(-look_forward) / df['Close'] - 1
    
    conditions = [
        (future_returns > 0.01),
        (future_returns < -0.01)
    ]
    choices = [1, -1]
    df['Target'] = np.select(conditions, choices, default=0)
    
    df.dropna(subset=['Target'], inplace=True)
    return df

def train_trading_model(ticker, model_save_path):
    print(f"Fetching data for {ticker}...")
    df = fetch_data(ticker, period='5y')
    if df is None:
        print("Lỗi lấy dữ liệu.")
        return
        
    df = add_technical_indicators(df)
    df = create_target_labels(df)
    
    features = ['RSI', 'Stoch', 'SMA_20', 'SMA_50', 'EMA_20', 'MACD', 'MACD_Signal', 'BB_High', 'BB_Low', 'ATR']
    
    X = df[features]
    y = df['Target']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    
    print("Training XGBoost Classifier...")
    model = XGBClassifier(n_estimators=100, max_depth=5, random_state=42)
    
    y_train_mapped = y_train.map({-1: 2, 0: 0, 1: 1})
    y_test_mapped = y_test.map({-1: 2, 0: 0, 1: 1})
    
    model.fit(X_train, y_train_mapped)
    
    predictions = model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test_mapped, predictions))
    
    os.makedirs(os.path.dirname(model_save_path), exist_ok=True)
    joblib.dump(model, model_save_path)
    print(f"Model saved to {model_save_path}")

if __name__ == "__main__":
    train_trading_model('CL=F', 'models/xgb_classifier.pkl')
