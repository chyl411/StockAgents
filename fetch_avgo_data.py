import yfinance as yf
import json
import pandas as pd

def get_data():
    ticker = yf.Ticker("AVGO")
    
    # 1. Price & History (1y for recent trend, 5y for context)
    try:
        hist = ticker.history(period="1y")
        current_price = hist['Close'].iloc[-1] if not hist.empty else None
    except Exception as e:
        print(f"Error fetching history: {e}")
        current_price = None
        hist = pd.DataFrame()

    # 2. Key Stats
    try:
        info = ticker.info
    except Exception as e:
        print(f"Error fetching info: {e}")
        info = {}

    # 3. Financials
    try:
        financials = ticker.financials
        balance_sheet = ticker.balance_sheet
        cashflow = ticker.cashflow
        
        # Get LTM Revenue and EBITDA if possible, or use latest annual
        # yfinance often provides annual in 'financials'. Quarterly is 'quarterly_financials'
        q_financials = ticker.quarterly_financials
        
    except Exception as e:
        print(f"Error fetching financials: {e}")
        financials = pd.DataFrame()
        q_financials = pd.DataFrame()

    data = {
        "current_price": current_price,
        "market_cap": info.get("marketCap"),
        "trailingPE": info.get("trailingPE"),
        "forwardPE": info.get("forwardPE"),
        "beta": info.get("beta"),
        "dividendYield": info.get("dividendYield"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "recommendationMean": info.get("recommendationMean"),
        "targetMeanPrice": info.get("targetMeanPrice"),
        "sharesOutstanding": info.get("sharesOutstanding"),
    }
    
    # Calculate some LTM figures if quarterly data exists
    if not q_financials.empty:
        # Sum last 4 quarters for LTM
        ltm_rev = q_financials.loc['Total Revenue'].iloc[:4].sum() if 'Total Revenue' in q_financials.index else None
        data['LTM_Revenue'] = ltm_rev
    
    print(json.dumps(data, indent=2))

if __name__ == "__main__":
    get_data()
