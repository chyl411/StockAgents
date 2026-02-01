---
name: financial-statement-analysis
description: Performs financial statement analysis including three-statement review, ratio and trend analysis, working capital and cash conversion, quality of earnings, and accounting red flags. Use when the user mentions financial statements, 10-K/10-Q, annual report, ratio analysis, cash flow quality, or accounting review.
---

# Financial Statement Analysis

## Instructions

**CRITICAL RULE**: Use Python for all ratio calculations and consistency checks.

### 1. Data Ingestion & Integrity Check (Python)
*   Get the last 3 years of Income Statement, Balance Sheet, Cash Flow.
*   **Run "The Accountant's Check" script**:
    *   `Check 1`: Does `Assets = Liabilities + Equity`?
    *   `Check 2`: Does `Net Income` in IS match `Net Income` in CFS?
    *   `Check 3`: Does `Cash at End of Period` in CFS match BS Cash?
    *   *Action*: If any verify fails, STOP and warn the user of data inconsistency.

### 2. Ratio Analysis (Python)
*   Calculate:
    *   **Growth**: Revenue CAGR, EBITDA CAGR.
    *   **Margins**: Gross, EBITDA, Net.
    *   **Returns**: ROE, ROIC.
    *   **Liquidity/Solvency**: Current Ratio, Net Debt/EBITDA.
    *   **Efficiency**: Days Sales Outstanding (DSO), Inventory Days (DIO).

### 3. Quality of Earnings & Red Flags (Institutional Grade)
*   **GAAP vs. Non-GAAP Gap:**
    *   Calculate the difference between GAAP EPS and Non-GAAP EPS.
    *   **SBC Check:** Calculate Stock-Based Compensation (SBC) as a % of Revenue and % of Operating Cash Flow. *High SBC = Shareholder Dilution.*
*   **Cash Flow Quality:**
    *   Calculate `FCF / Net Income` conversion ratio.
    *   *Flag*: If NI is growing but CFO is flat/declining -> "Low Quality Earnings".
    *   *Flag*: If EBITDA is high but FCF is low -> "Capital Intensive" or "Working Capital Trap".
*   **One-Time Items:**
    *   Identify large "Restructuring Charges" or "Asset Impairments" that appear recurringly.

### 4. Unit Economics & Monetization Trend (For Fintech/SaaS)
*   **Take Rate / Monetization Rate Analysis (Crucial):**
    *   If TPV (Total Payment Volume) or GMV (Gross Merchandise Value) is available, Calculate: `Take Rate = Revenue / TPV`.
    *   **Trend Check**: Is the Take Rate declining?
        *   *Falling Take Rate + Rising Volume* = **Commoditization Risk** (Pricing power loss).
        *   *Stable/Rising Take Rate* = **Moat** (Pricing power intact).
*   **Transaction Margin:**
    *   Calculate `(Revenue - Transaction Expense) / Revenue`. This is the "Gross Profit" of the payment utility itself.

## Output Template
### 1. Integrity Report
*   ✅ Balance Sheet Balanced
*   ✅ Cash Flow Reconciled

### 2. Key Ratios Dashboard
(Table with T-2, T-1, Current, vs Industry Avg)

### 3. Monetization & Unit Economics
*   **Take Rate Trend**: [Rising/Flat/Declining] (e.g., 2.0% -> 1.9% -> 1.8%)
*   **Interpretation**: [Is the company being commoditized?]

### 4. "Red Flag" & Quality Scanner
*   **Earnings Quality**: [High/Low] (Explain CFO vs NI gap)
*   **SBC Burden**: [X]% of Revenue. (Is this dilutive?)
*   **Working Capital**: [Comment on swelling inventory or receivables]
