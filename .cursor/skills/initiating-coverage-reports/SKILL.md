---
name: initiating-coverage-reports
description: Writes initiating coverage reports with investment thesis, industry overview, business model, competitive positioning, valuation (DCF + comps), catalysts, risks, and compliance-ready disclaimers. Use when the user mentions initiation, initiating coverage, equity research report, coverage report, or investment thesis write-up.
---

# Initiating Coverage Reports

## Instructions

**Strategy**: Do not attempt to write the whole report in one pass. Use a **Modular Approach**.

### Phase 1: Structure & Thesis (The Skeleton)
1.  **Define the Rating & Target**: Buy/Hold/Sell? Target Price (based on Valuation skills).
2.  **Draft the "Variant View"**: What is your thesis that differs from the market consensus? (e.g., "Market underestimates AI revenue tail, we model 50% growth vs 30% consensus").
3.  **Generate Outline**: List the sections.

### Phase 2: Research Modules (The Meat)
*   **Module A (Industry)**: Use `market-data-retrieval` to get TAM size and growth rates.
*   **Module B (Financials)**: Use `financial-statement-analysis` to get historical trends.
*   **Module C (Valuation)**: Use `dcf-model` and `comparable-company-analysis` to get the numbers. **Do not make up numbers.**

### Phase 3: Drafting (The Skin)
*   Write the report section by section using the data from Phase 2.
*   **Chart Placeholder**: Whenever you mention a trend, insert `[CHART: Revenue Growth 2020-2025E]` to indicate where a visual should go.

## Output Structure
1.  **Investment Summary** (The "Elevator Pitch")
2.  **Valuation** (Summary of DCF/Comps)
3.  **Key Risks** (Bear Case)
4.  **Industry Overview**
5.  **Company Analysis**
6.  **Financial Model Summary**
7.  **Disclaimers**

## Quick Checks
- [ ] Does the Investment Thesis have a "Why Now?" component?
- [ ] Are all valuation numbers sourced from the specific valuation agents?
