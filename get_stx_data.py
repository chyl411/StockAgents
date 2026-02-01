import yfinance as yf
import json
import sys

def get_stx_data():
    try:
        ticker = yf.Ticker("STX")
        info = ticker.info
        hist = ticker.history(period="5d")
        current_price = hist['Close'].iloc[-1] if not hist.empty else None
        
        data = {
            "ticker": "STX",
            "price": current_price,
            "market_cap": info.get("marketCap"),
            "forward_pe": info.get("forwardPE"),
            "trailing_pe": info.get("trailingPE"),
            "peg_ratio": info.get("pegRatio"),
            "price_to_book": info.get("priceToBook"),
            "ev_to_ebitda": info.get("enterpriseToEbitda"),
            "profit_margins": info.get("profitMargins"),
            "revenue_growth": info.get("revenueGrowth")
        }
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_stx_data()
