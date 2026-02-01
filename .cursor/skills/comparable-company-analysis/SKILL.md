---
name: comparable-company-analysis
description: Builds comparable company analysis (Comps) including peer selection, metric normalization, multiple calculation, outlier handling, and valuation range. Use when the user mentions comps, comparable companies, trading multiples, peer benchmarking, EV/EBITDA, P/E, or relative valuation.
---

# Comparable Company Analysis (Comps)

## Instructions

**CRITICAL RULE**: Do **NOT** calculate multiples manually. Use Python to divide Enterprise Value by Metrics.

### 1. Peer Selection & Justification
*   **Universe**: Identify 5-10 potential peers.
*   **Selection Logic**: For each peer, write a **"Justification"** sentence.
    *   *Good*: "Selected because it competes directly in the GPU data center market."
    *   *Bad*: "It is a tech company."
*   **Exclusion**: Explicitly list 1-2 companies you *excluded* and why (e.g., "Excluded AMZN because AWS is only 15% of revs").

### 2. Data Gathering (Python/Tool)
*   Use `market-data-retrieval` to get:
    *   Market Cap, Net Debt (to calculate EV).
    *   LTM Revenue, LTM EBITDA, NTM Revenue (consensus), NTM EBITDA.

### 3. Calculation & Normalization (Python)
*   Write a Python script to:
    *   Calculate `EV = Market Cap + Debt - Cash`.
    *   Calculate Multiples: `EV/Rev`, `EV/EBITDA`, `P/E`.
    *   **Handle Outliers**: logic to filter out negative multiples or results > 2x the median (flag them).
    *   Calculate Statistics: Mean, Median, 25th/75th percentile.

### 4. Valuation Implication
*   Apply the **Median** peer multiple to the Target Company's metrics.
*   Derive Implied Share Price Range.

## Output Template
### Peer Group Rationale
| Ticker | Company | Inclusion Rationale | Business Overlap |
| :--- | :--- | :--- | :--- |
| AMD | Advanced Micro Devices | Direct competitor in CPU/GPU duopoly | High |

### Comparable Table
(Output from Python DataFrame)

### Valuation Summary
*   **Metric Used**: NTM EV/EBITDA (e.g., 25.0x Median)
*   **Implied EV**: [Value]
*   **Implied Share Price**: [Range]
