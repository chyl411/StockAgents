import yfinance as yf
import pandas as pd
import json
from datetime import datetime

def get_data():
    ticker = yf.Ticker("IBM")
    
    # 1. Price History & Current Price
    hist = ticker.history(period="1y")
    current_price = hist['Close'].iloc[-1] if not hist.empty else None
    
    # 2. Key Stats
    info = ticker.info
    
    # 3. Financials (LTM)
    # yfinance returns DataFrame, need to handle empty case
    try:
        financials = ticker.financials
        balance_sheet = ticker.balance_sheet
        cashflow = ticker.cashflow
    except Exception as e:
        financials = pd.DataFrame()
        balance_sheet = pd.DataFrame()
        cashflow = pd.DataFrame()

    data = {
        "price": current_price,
        "market_cap": info.get("marketCap"),
        "pe_ratio": info.get("trailingPE"),
        "forward_pe": info.get("forwardPE"),
        "dividend_yield": info.get("dividendYield"),
        "beta": info.get("beta"),
        "target_mean_price": info.get("targetMeanPrice"),
        "recommendation_key": info.get("recommendationKey"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "description": info.get("longBusinessSummary"),
        "revenue_growth": info.get("revenueGrowth"),
        "earnings_growth": info.get("earningsGrowth"),
        "free_cashflow": info.get("freeCashflow"),
        "operating_margins": info.get("operatingMargins"),
        "return_on_equity": info.get("returnOnEquity"),
        "total_cash": info.get("totalCash"),
        "total_debt": info.get("totalDebt"),
        "shares_outstanding": info.get("sharesOutstanding")
    }
    
    # Print as JSON for parsing
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    get_data()
