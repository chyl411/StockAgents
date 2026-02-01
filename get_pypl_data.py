import yfinance as yf
import json
import sys

def get_data():
    ticker = yf.Ticker("PYPL")
    
    try:
        # 1. Price History (for Beta/Volatility)
        hist = ticker.history(period="1y")
        if hist.empty:
            current_price = "N/A"
            prev_close = "N/A"
        else:
            current_price = hist['Close'].iloc[-1]
            prev_close = hist['Close'].iloc[-2] if len(hist) > 1 else hist['Open'].iloc[-1]
            
        # 2. Key Stats
        info = ticker.info
        
        # 3. Financials (Get latest available)
        financials = ticker.financials
        balance_sheet = ticker.balance_sheet
        cashflow = ticker.cashflow
        
        data = {
            "price": current_price,
            "prev_close": prev_close,
            "market_cap": info.get('marketCap'),
            "beta": info.get('beta'),
            "pe_ratio": info.get('trailingPE'),
            "forward_pe": info.get('forwardPE'),
            "price_to_sales": info.get('priceToSalesTrailing12Months'),
            "revenue_ltm": info.get('totalRevenue'),
            "ebitda": info.get('ebitda'),
            "cash": info.get('totalCash'),
            "debt": info.get('totalDebt'),
            "free_cash_flow": info.get('freeCashflow'),
            "shares_outstanding": info.get('sharesOutstanding')
        }
        
        print(json.dumps(data, indent=2))
        
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    get_data()
