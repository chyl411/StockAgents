import yfinance as yf
import pandas as pd
import datetime

def get_data():
    ticker = yf.Ticker("VZ")
    
    # 1. Price History & Current Price
    try:
        history = ticker.history(period="1y")
        current_price = history['Close'].iloc[-1]
        prev_price = history['Close'].iloc[-2]
        price_change = (current_price - prev_price) / prev_price
    except:
        current_price = "N/A"
        price_change = "N/A"

    # 2. Key Stats
    info = ticker.info
    stats = {
        "Price": current_price,
        "Market Cap": info.get("marketCap"),
        "PE Ratio (Trailing)": info.get("trailingPE"),
        "PE Ratio (Forward)": info.get("forwardPE"),
        "Dividend Yield": info.get("dividendYield"),
        "Beta": info.get("beta"),
        "52 Week High": info.get("fiftyTwoWeekHigh"),
        "52 Week Low": info.get("fiftyTwoWeekLow"),
        "Debt to Equity": info.get("debtToEquity"),
        "Free Cash Flow": info.get("freeCashflow"),
        "Operating Margins": info.get("operatingMargins"),
    }
    
    # 3. Financials (Most recent year)
    try:
        financials = ticker.financials.iloc[:, 0] # Most recent year
        stats["Total Revenue"] = financials.get("Total Revenue")
        stats["Net Income"] = financials.get("Net Income")
    except:
        pass

    # 4. Treasury Yield (Risk Free Rate)
    try:
        tnx = yf.Ticker("^TNX")
        rf_rate = tnx.history(period="5d")['Close'].iloc[-1]
    except:
        rf_rate = 4.0 # Fallback

    print("### Data Dictionary: VZ")
    print("| Metric | Value | Unit | Source | Date |")
    print("| :--- | :--- | :--- | :--- | :--- |")
    print(f"| Price | {stats['Price']} | USD | yfinance | {datetime.date.today()} |")
    print(f"| Market Cap | {stats['Market Cap']} | USD | yfinance | {datetime.date.today()} |")
    print(f"| PE (Fwd) | {stats['PE Ratio (Forward)']} | x | yfinance | {datetime.date.today()} |")
    print(f"| Div Yield | {stats['Dividend Yield']} | % | yfinance | {datetime.date.today()} |")
    print(f"| Beta | {stats['Beta']} | x | yfinance | {datetime.date.today()} |")
    print(f"| 10y Treasury | {rf_rate} | % | yfinance | {datetime.date.today()} |")
    print(f"| Debt/Equity | {stats['Debt to Equity']} | % | yfinance | {datetime.date.today()} |")
    
    return stats

if __name__ == "__main__":
    get_data()
