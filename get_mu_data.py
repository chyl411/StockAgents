import yfinance as yf
import json
from datetime import datetime

def get_market_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol)
    
    # 1. Price & History
    try:
        hist = ticker.history(period="1mo")
        current_price = hist['Close'].iloc[-1] if not hist.empty else None
    except Exception:
        current_price = None

    # 2. Financials (LTM)
    try:
        financials = ticker.financials
        revenue_ttm = financials.loc['Total Revenue'].sum() if 'Total Revenue' in financials.index else None
        net_income_ttm = financials.loc['Net Income'].sum() if 'Net Income' in financials.index else None
    except Exception:
        revenue_ttm = None
        net_income_ttm = None

    # 3. Key Stats
    try:
        info = ticker.info
        market_cap = info.get('marketCap')
        forward_pe = info.get('forwardPE')
        beta = info.get('beta')
        fifty_two_week_high = info.get('fiftyTwoWeekHigh')
        fifty_two_week_low = info.get('fiftyTwoWeekLow')
    except Exception:
        market_cap = None
        forward_pe = None
        beta = None
        fifty_two_week_high = None
        fifty_two_week_low = None

    data = {
        "ticker": ticker_symbol,
        "price": current_price,
        "market_cap": market_cap,
        "revenue_ttm": revenue_ttm,
        "net_income_ttm": net_income_ttm,
        "forward_pe": forward_pe,
        "beta": beta,
        "52w_high": fifty_two_week_high,
        "52w_low": fifty_two_week_low,
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    get_market_data("MU")
