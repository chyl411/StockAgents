---
name: dcf-model
description: Builds a DCF model with explicit drivers, WACC, terminal value, scenarios, sensitivities, and audit checks. Use when the user mentions DCF, intrinsic value, WACC, discount rate, terminal value, FCF forecast, valuation model, or absolute valuation.
---

# Discounted Cash Flow (DCF) Model

## Instructions

**CRITICAL RULE**: Do **NOT** perform arithmetic manually. You **MUST** write and execute a Python script for the DCF projection and WACC calculation to ensure precision.

### Phase 1: Data & Assumptions Proposal (Interactive)
1.  **Fetch Data**: Use `market-data-retrieval` to get historicals, beta, risk-free rate, and share count.
2.  **Draft Assumptions**: Based on historicals, propose the following drivers:
    *   Revenue Growth (Next 5 years)
    *   EBIT margins (Target margin)
    *   Tax Rate
    *   WACC inputs (Rf, ERP, Beta, Cost of Debt)
    *   Terminal Growth Rate (g)
3.  **STOP & ASK**: Present a summary table of these assumptions to the user. Ask: *"Do these assumptions look reasonable, or should I adjust the growth/margin profile?"*

### Phase 2: Model Execution (Python)
Once assumptions are confirmed (or if user says "proceed with defaults"):
1.  **Write Python Script**:
    *   Define the projection years (Year 1 to Year 5 + Terminal Year).
    *   Calculate FCFF: `EBIT * (1-Tax) + D&A - Capex - Change_in_NWC`.
    *   Calculate Discount Factors: `1 / (1+WACC)^t`.
    *   Calculate Terminal Value (Gordon Growth Method).
    *   Calculate Enterprise Value (PV of Explicit + PV of TV).
    *   **Sum-of-the-Parts (SOTP) Check:** If the company is a conglomerate (e.g., AVGO, AMZN), explicitly mention if we are valuing the whole or if an SOTP approach would be better. *For this skill, standard DCF is default, but acknowledge SOTP.*
    *   Bridge to Equity Value: `EV + Cash - Debt - Minority Interest`.
    *   Calculate Share Price: `Equity Value / Diluted Shares`.
2.  **Sensitivity Analysis (in Python) - MANDATORY**:
    *   Create a data frame/matrix for **WACC (±0.5%)** vs. **Terminal Growth (±0.5%)**.
    *   This generates a *Range of Values* rather than a single point estimate.

### Phase 3: Reporting
Output the final model including:
*   **Executive Summary**: Implied share price vs current price (Upside/Downside).
*   **Key Drivers**: Narrative explaining *why* you chose these growth rates.
*   **The Model**: A clean Markdown table of the DCF (copied from Python output).
*   **Sensitivity Table**: Matrix of share prices showing the valuation range.

## Quick Checks
- [ ] Did I use Python for math? (Yes/No)
- [ ] Is Terminal Value < 70% of total EV? (If >70%, flag as "TV heavy")
- [ ] Did I provide a sensitivity matrix? (Single price targets are forbidden).
