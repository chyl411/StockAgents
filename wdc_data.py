import yfinance as yf
import json
import sys

def get_wdc_data():
    ticker = yf.Ticker("WDC")
    
    try:
        # 1. Price History (last 5 days for recent context)
        hist = ticker.history(period="5d")
        current_price = hist['Close'].iloc[-1] if not hist.empty else None
        
        # 2. Key Stats
        info = ticker.info
        
        # 3. Financials (get latest available)
        income_stmt = ticker.financials
        balance_sheet = ticker.balance_sheet
        cash_flow = ticker.cashflow
        
        data = {
            "price": current_price,
            "currency": info.get("currency", "USD"),
            "market_cap": info.get("marketCap"),
            "beta": info.get("beta"),
            "trailing_pe": info.get("trailingPE"),
            "forward_pe": info.get("forwardPE"),
            "peg_ratio": info.get("pegRatio"),
            "price_to_book": info.get("priceToBook"),
            "enterprise_value": info.get("enterpriseValue"),
            "shares_outstanding": info.get("sharesOutstanding"),
            "52_week_high": info.get("fiftyTwoWeekHigh"),
            "52_week_low": info.get("fiftyTwoWeekLow"),
            "dividend_yield": info.get("dividendYield"),
            "sector": info.get("sector"),
            "industry": info.get("industry"),
            "recommendation_mean": info.get("recommendationMean"), # 1 is Strong Buy, 5 is Sell
            "target_mean_price": info.get("targetMeanPrice"),
            "revenue_ltm": info.get("totalRevenue"), # This might be trailing
            "ebitda": info.get("ebitda"),
            "debt_to_equity": info.get("debtToEquity"),
            "free_cash_flow": info.get("freeCashflow"),
            "operating_margins": info.get("operatingMargins"),
            "gross_margins": info.get("grossMargins")
        }
        
        print(json.dumps(data, indent=2))
        
    except Exception as e:
        print(f"Error fetching data: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    get_wdc_data()
