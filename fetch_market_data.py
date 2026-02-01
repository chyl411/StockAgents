import yfinance as yf
import pandas as pd

def fetch_data():
    tickers = ['AVGO', 'NVDA', 'AMD', 'MRVL']
    info_list = []
    
    print("Fetching data...")
    for t in tickers:
        try:
            ticker = yf.Ticker(t)
            # Force fetch to ensure data is retrieved
            hist = ticker.history(period="1d")
            info = ticker.info
            
            # Extract key metrics with fallbacks
            data = {
                'Ticker': t,
                'Price': info.get('currentPrice', info.get('regularMarketPrice')),
                'Market Cap (B)': info.get('marketCap', 0) / 1e9 if info.get('marketCap') else None,
                'Forward PE': info.get('forwardPE'),
                'Trailing PE': info.get('trailingPE'),
                'PEG Ratio': info.get('pegRatio'),
                'PriceToSales': info.get('priceToSalesTrailing12Months'),
                'Beta': info.get('beta'),
                '52W High': info.get('fiftyTwoWeekHigh'),
                '52W Low': info.get('fiftyTwoWeekLow'),
                'Recommendation': info.get('recommendationKey')
            }
            info_list.append(data)
        except Exception as e:
            print(f"Error fetching {t}: {e}")

    df = pd.DataFrame(info_list)
    # Format for better readability
    print("\n### Market Data Snapshot (Jan 2026)")
    print(df.to_markdown(index=False))

if __name__ == "__main__":
    fetch_data()
