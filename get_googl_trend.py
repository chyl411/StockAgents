import yfinance as yf

def get_trend():
    t = yf.Ticker("GOOGL")
    hist = t.history(period="1y")
    low = hist['Close'].min()
    high = hist['Close'].max()
    current = hist['Close'].iloc[-1]
    
    print(f"52-Week Range: {low:.2f} - {high:.2f}")
    print(f"Current: {current:.2f}")
    
    # Simple Moving Averages
    ma50 = hist['Close'].rolling(window=50).mean().iloc[-1]
    ma200 = hist['Close'].rolling(window=200).mean().iloc[-1]
    print(f"MA50: {ma50:.2f}")
    print(f"MA200: {ma200:.2f}")

if __name__ == "__main__":
    get_trend()
