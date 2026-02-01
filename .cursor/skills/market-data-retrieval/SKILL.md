---
name: market-data-retrieval
description: Fetches historical price data, financial statements, and real-time market metrics using Python (yfinance) or web search. Use when the user asks for stock prices, historical data, financial metrics, beta, or Treasury rates.
---

# Market Data Retrieval

## Instructions

**Goal**: Obtain accurate, sourced financial data to feed into analysis models. **Never hallucinate numbers.** **Data freshness is paramount.**

1.  **Method 1: Python API (Primary)**
    *   Attempt to use the `yfinance` library in a Python script first. This is the most accurate and structured method.
    *   **Script Pattern**:
        ```python
        import yfinance as yf
        ticker = yf.Ticker("AAPL")
        
        # 1. Price History (for Beta/Volatility)
        hist = ticker.history(period="5y")
        
        # 2. Financials (Income Stmt, BS, Cash Flow)
        # ticker.financials, ticker.balance_sheet, ticker.cashflow
        
        # 3. Key Stats (Shares, Beta, Book Value)
        # ticker.info['sharesOutstanding'], ticker.info['beta']
        ```
    *   *Note*: If the library is missing or fails, gracefully fall back to Method 2.

2.  **Method 2: Precise Web Search (Fallback)**
    *   Use `web_search` tool with specific queries.
    *   **Queries**: "AAPL outstanding shares 2024 10-K", "US 10 year treasury yield current", "Damodaran equity risk premium 2024".
    *   **Citation**: You MUST record the source URL for every data point retrieved via search.

3.  **Data Verification Protocol (MANDATORY)**
    *   **Time-Stamp Check (CRITICAL):**
        *   For **Price/PE/VIX**: Data MUST be from the **current trading session** or **previous close**.
        *   **FAIL CONDITION:** Do NOT accept search snippets that are > 3 days old (e.g., finding a price from May when it is January).
        *   **Action:** If search results are stale, refine query to include current month/year (e.g., "WDC stock price January 2026").
    *   **Triangulation Rule:**
        *   If the price/valuation seems "too cheap" (e.g., PE < 10 for a growth stock) or "too expensive", **verify with a second source**.
        *   Check for recent **Stock Splits** or **Spin-offs** that might distort the price per share.
    *   **Currency & Scale:**
        *   Check currency (USD vs local).
        *   Check scale (Millions vs Billions).
        *   Check period (LTM vs FY).

## Output Format (for downstream agents)
Return data in a structured Markdown table or JSON block that other agents can parse:

```markdown
### Data Dictionary: [TICKER]
| Metric | Value | Unit | Source | Date |
| :--- | :--- | :--- | :--- | :--- |
| Price | 150.00 | USD | yfinance | 2023-10-27 |
| Shares | 15.2 | B | 10-Q | 2023-09-30 |
| Revenue (LTM)| 385.0 | B | yfinance | 2023-09-30 |
```
