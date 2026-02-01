import yfinance as yf
import json
import sys

def get_peer_data():
    tickers = ["STX"]
    results = {}
    
    for t in tickers:
        try:
            ticker = yf.Ticker(t)
            info = ticker.info
            hist = ticker.history(period="5d")
            current_price = hist['Close'].iloc[-1] if not hist.empty else None
            
            results[t] = {
                "price": current_price,
                "market_cap": info.get("marketCap"),
                "trailing_pe": info.get("trailingPE"),
                "forward_pe": info.get("forwardPE"),
                "ev_to_ebitda": info.get("enterpriseToEbitda"),
                "price_to_book": info.get("priceToBook"),
                "revenue_growth": info.get("revenueGrowth"),
                "gross_margins": info.get("grossMargins"),
                "operating_margins": info.get("operatingMargins"),
                "free_cash_flow": info.get("freeCashflow")
            }
        except Exception as e:
            results[t] = {"error": str(e)}
            
    print(json.dumps(results, indent=2))

if __name__ == "__main__":
    get_peer_data()
