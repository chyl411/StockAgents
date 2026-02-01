import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def get_google_data():
    ticker = yf.Ticker("GOOGL")
    
    # 1. Price History (1 Year for Support/Resistance)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    hist = ticker.history(start=start_date, end=end_date)
    
    # 2. Key Stats
    info = ticker.info
    
    # 3. Financials (just to check health)
    financials = ticker.financials
    
    print("--- PRICE DATA (Last 5 days) ---")
    print(hist.tail())
    
    print("\n--- KEY STATS ---")
    keys_to_print = ['currentPrice', 'targetMeanPrice', 'recommendationKey', 'numberOfAnalystOpinions', 'beta', 'fiftyTwoWeekHigh', 'fiftyTwoWeekLow', 'trailingPE', 'forwardPE']
    for k in keys_to_print:
        if k in info:
            print(f"{k}: {info[k]}")
            
    print("\n--- SUPPORT LEVELS CALCULATION ---")
    # Simple Moving Averages
    hist['SMA_50'] = hist['Close'].rolling(window=50).mean()
    hist['SMA_200'] = hist['Close'].rolling(window=200).mean()
    
    print(f"Current SMA_50: {hist['SMA_50'].iloc[-1]}")
    print(f"Current SMA_200: {hist['SMA_200'].iloc[-1]}")
    
    # Recent Lows (Swing Lows)
    # Find local minimums in the last 90 days
    last_90 = hist.tail(90)
    min_90 = last_90['Low'].min()
    print(f"90-Day Low: {min_90}")

if __name__ == "__main__":
    get_google_data()
