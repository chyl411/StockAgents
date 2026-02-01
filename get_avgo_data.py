import yfinance as yf
import pandas as pd
import json

def get_avgo_data():
    ticker = yf.Ticker("AVGO")
    
    # 1. Price History (for Beta/Volatility and ATH check)
    hist = ticker.history(period="1y")
    current_price = hist['Close'].iloc[-1]
    high_52w = hist['High'].max()
    low_52w = hist['Low'].min()
    ath_check = (current_price / high_52w) * 100
    
    # 2. Financials
    # Get LTM data if available, else latest annual
    financials = ticker.financials
    balance_sheet = ticker.balance_sheet
    cashflow = ticker.cashflow
    
    # Key Metrics
    info = ticker.info
    
    data = {
        "price": current_price,
        "52w_high": high_52w,
        "52w_low": low_52w,
        "ath_pct": ath_check,
        "market_cap": info.get('marketCap'),
        "pe_ratio": info.get('trailingPE'),
        "forward_pe": info.get('forwardPE'),
        "beta": info.get('beta'),
        "dividend_yield": info.get('dividendYield'),
        "revenue_growth": info.get('revenueGrowth'),
        "profit_margins": info.get('profitMargins'),
        "debt_to_equity": info.get('debtToEquity'),
        "free_cash_flow": info.get('freeCashflow')
    }
    
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    get_avgo_data()
