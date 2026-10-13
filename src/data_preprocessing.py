import pandas as pd
import yfinance as yf
import ta

def fetch_data(ticker, period='2y', interval='1d', multiplier=1.0):
    """Lấy dữ liệu từ yfinance và chuyển đổi sang VNĐ"""
    try:
        if interval == '1h' and period in ['2y', '5y', 'max']:
            period = '730d' # yfinance limit for intraday
            
        df = yf.download(ticker, period=period, interval=interval, progress=False)
        if df.empty:
            return None
        
        df.reset_index(inplace=True)
        # Rename "Datetime" to "Date" for 1h interval consistency
        if 'Datetime' in df.columns:
            df.rename(columns={'Datetime': 'Date'}, inplace=True)
            
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [col[0] for col in df.columns]
            
        # Đổi giá sang VNĐ theo định lượng riêng
        for col in ['Open', 'High', 'Low', 'Close']:
            if col in df.columns:
                df[col] = df[col] * multiplier
                
        return df
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

def add_technical_indicators(df):
    """Tính toán các chỉ báo kỹ thuật trên nền giá VNĐ"""
    df = df.copy()
    
    df = df.dropna(subset=['Close'])
    
    df['RSI'] = ta.momentum.RSIIndicator(close=df['Close'], window=14).rsi()
    df['Stoch'] = ta.momentum.StochasticOscillator(high=df['High'], low=df['Low'], close=df['Close']).stoch()
    
    df['SMA_20'] = ta.trend.sma_indicator(close=df['Close'], window=20)
    df['SMA_50'] = ta.trend.sma_indicator(close=df['Close'], window=50)
    df['EMA_20'] = ta.trend.ema_indicator(close=df['Close'], window=20)
    macd = ta.trend.MACD(close=df['Close'])
    df['MACD'] = macd.macd()
    df['MACD_Signal'] = macd.macd_signal()
    
    bb = ta.volatility.BollingerBands(close=df['Close'], window=20, window_dev=2)
    df['BB_High'] = bb.bollinger_hband()
    df['BB_Low'] = bb.bollinger_lband()
    df['ATR'] = ta.volatility.AverageTrueRange(high=df['High'], low=df['Low'], close=df['Close'], window=14).average_true_range()
    
    df.dropna(inplace=True)
    
    return df
