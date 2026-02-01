import yfinance as yf
import pandas as pd
from datetime import datetime

def get_data():
    ticker_symbol = "GOOGL"
    ticker = yf.Ticker(ticker_symbol)
    
    # 1. Price History
    # Fetch recent history to get the latest price
    hist = ticker.history(period="5d")
    if not hist.empty:
        latest_price = hist['Close'].iloc[-1]
        latest_date = hist.index[-1].strftime('%Y-%m-%d')
    else:
        latest_price = "N/A"
        latest_date = "N/A"
        
    # 2. Key Stats
    info = ticker.info
    shares = info.get('sharesOutstanding', 'N/A')
    market_cap = info.get('marketCap', 'N/A')
    beta = info.get('beta', 'N/A')
    
    if isinstance(shares, (int, float)):
        shares_b = f"{shares / 1e9:.2f}"
    else:
        shares_b = shares

    if isinstance(market_cap, (int, float)):
        market_cap_b = f"{market_cap / 1e9:.2f}"
    else:
        market_cap_b = market_cap

    # 3. Financials (LTM)
    # yfinance often returns annual in .financials, need to check if quarterly is better for LTM
    # For simplicity, we'll take the latest available annual or try to sum quarterly if needed.
    # Actually ticker.info often has 'totalRevenue' which is LTM or latest annual.
    # Let's try to get specific LTM data from info if available, or calc from financials.
    
    revenue_ltm = info.get('totalRevenue', 'N/A')
    if isinstance(revenue_ltm, (int, float)):
        revenue_ltm_b = f"{revenue_ltm / 1e9:.2f}"
    else:
        revenue_ltm_b = revenue_ltm

    ebitda = info.get('ebitda', 'N/A')
    if isinstance(ebitda, (int, float)):
        ebitda_b = f"{ebitda / 1e9:.2f}"
    else:
        ebitda_b = ebitda

    # 4. Risk Free Rate
    tnx = yf.Ticker("^TNX")
    tnx_hist = tnx.history(period="5d")
    if not tnx_hist.empty:
        rf_rate = tnx_hist['Close'].iloc[-1] / 100.0 # TNX is in index points (e.g. 4.0 = 4%)
        rf_rate_disp = f"{tnx_hist['Close'].iloc[-1]:.2f}%"
    else:
        rf_rate = 0.04
        rf_rate_disp = "4.00% (Est)"

    print(f"### Data Dictionary: {ticker_symbol}")
    print("| Metric | Value | Unit | Source | Date |")
    print("| :--- | :--- | :--- | :--- | :--- |")
    print(f"| Price | {latest_price:.2f} | USD | yfinance | {latest_date} |")
    print(f"| Shares | {shares_b} | B | yfinance | {latest_date} |")
    print(f"| Market Cap | {market_cap_b} | B USD | yfinance | {latest_date} |")
    print(f"| Revenue (LTM) | {revenue_ltm_b} | B USD | yfinance | {latest_date} |")
    print(f"| EBITDA (LTM) | {ebitda_b} | B USD | yfinance | {latest_date} |")
    print(f"| Beta | {beta} | - | yfinance | {latest_date} |")
    print(f"| Risk-Free Rate | {rf_rate_disp} | - | ^TNX | {latest_date} |")
    
    # Also print PE and Forward PE if available
    pe = info.get('trailingPE', 'N/A')
    fwd_pe = info.get('forwardPE', 'N/A')
    print(f"| P/E (Trailing) | {pe} | x | yfinance | {latest_date} |")
    print(f"| P/E (Forward) | {fwd_pe} | x | yfinance | {latest_date} |")

if __name__ == "__main__":
    try:
        get_data()
    except Exception as e:
        print(f"Error: {e}")
