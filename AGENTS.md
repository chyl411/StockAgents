# Financial Services Agents Architecture

This document defines the multi-agent architecture for financial analysis, modeling, and reporting.

## 1. Core Orchestrator

**Agent: `finance-orchestrator`**
- **Role:** Central router and task manager. Receives high-level user requests and delegates to specialized agents.
- **Trigger Keywords:** "analyze", "model", "valuation", "report", "DD", "due diligence", "earnings".
- **Workflow:**
 1. Parse request (Ticker, Period, Output Type).
 2. **[CRITICAL] Macro-Risk Check**: Route to `risk-timing-agent` FIRST. Check global war/macro risks independently of the ticker.
 3. **Data-First**: Route to `market-data-retrieval` to fetch raw data.
 4. **[NEW] Consensus Check**: Route to `consensus-check` to compare Agent view vs Wall St.
 5. **Python-Calc & Modeling**: Route to specialized agents (`dcf-model`, `financial-statement-analysis`) which MUST use Python.
 6. **[NEW] Red Team Attack**: Route to `bear-case-analysis` to find idiosyncratic risks.
 7. Aggregate outputs.
 8. Final verdict & Execution Trace.

## 2. Specialized Agents & Skills Map

| Agent Role | Responsibility | Primary Skill / Tool |
| :--- | :--- | :--- |
| **`market-data-retrieval`** | Fetch Prices, Financials, Beta via Python/Web. | `market-data-retrieval` |
| **`consensus-check`** | **[NEW]** Compare Analysis vs Wall St Estimates (Alpha). | `consensus-check` |
| **`industry-research-agent`** | Strategy, **Product Execution Check**, Management, Moat, AI impact. | `strategic-market-analysis` |
| **`filing-ingestion-agent`** | Fetch and index filings, transcripts, presentations. | (Built-in WebFetch / Glob) |
| **`statement-extraction-agent`** | Extract financial tables from PDFs/Docs. | `financial-statement-analysis` |
| **`financial-normalization-agent`** | **Take Rate & Unit Econ**, SBC Check, Standardization. | `financial-statement-analysis` |
| **`comps-valuation-agent`** | Relative valuation (Multiples) with Justification. | `comparable-company-analysis` |
| **`dcf-valuation-agent`** | Absolute valuation (DCF) with **Sensitivity Matrix**. | `dcf-model` |
| **`bear-case-analysis`** | **[NEW]** "Red Team" / Short Seller Analysis. | `bear-case-analysis` |
| **`earnings-analysis-agent`** | Quarterly results + **TPA & Engagement** + Q&A Sentiment. | `earnings-analysis` |
| **`due-diligence-pack-agent`** | DD checklists, data room analysis. | `due-diligence-data-packs` |
| **`coverage-report-agent`** | Write full initiation/update reports (Modular). | `initiating-coverage-reports` |
| **`excel-model-operator-agent`** | Generate/Fill Excel files. | (Excel Tools / Python Pandas) |
| **`risk-timing-agent`** | Assess Geopolitics, Macro Risks, and Entry Timing. | `investment-risk-timing` |
| **`reviewer-agent`** | QA, logic checks, narrative consistency. | (General LLM QA) |

## 3. Workflow Examples

### A. Full Initiation Report (Institutional Grade)
**User:** "Write an initiation report for AVGO."
**Orchestrator Flow:**
1. **`risk-timing-agent`**: Macro/Geopolitics check.
2. **`market-data-retrieval`**: Get Price, Financials.
3. **`consensus-check`**: "Street expects 15% growth; what do we think?"
4. **`industry-research-agent`**: Analyze Product Strategy & **Execution Score** (Fastlane/AI).
5. **`financial-normalization-agent`**: Check **Take Rate Trends** & SBC impact.
6. **`dcf-valuation-agent`**: Run DCF with Sensitivity Analysis.
7. **`bear-case-analysis`**: "Find the Customer Concentration risk."
8. **`coverage-report-agent`**: Synthesize and write report.

### B. Earnings Review
**User:** "Analyze TSLA Q3 earnings."
**Orchestrator Flow:**
1. `filing-ingestion-agent`: Get Q3 release & transcript.
2. `earnings-analysis-agent`: Run `earnings-analysis` (Check **TPA/Engagement**).
3. `consensus-check`: Did they beat expectations?

## 4. Skills Directory
All specialized skills are located in `.cursor/skills/`:
- `market-data-retrieval/`
- `consensus-check/`
- `strategic-market-analysis/`
- `investment-risk-timing/`
- `comparable-company-analysis/`
- `dcf-model/`
- `bear-case-analysis/`
- `due-diligence-data-packs/`
- `earnings-analysis/`
- `financial-statement-analysis/`
- `initiating-coverage-reports/`

## 5. Transparency Protocol
**GOAL:** The user must never feel the analysis is a "Black Box".
**REQUIREMENT:** Every final response MUST include an "Execution Trace" or "Process Review" section (at the end or in a collapsible section) that explicitly lists:
1. **Skills Activated:** Which specific `.cursor/skills/` files were read and followed?
 - *Example:* "✅ Activated `consensus-check` to find variance."
2. **Key Actions Taken:** What did the agent actually do?
 - *Example:* "🔍 Compared Street estimate (12%) vs Our Model (15%)."
 - *Example:* "📉 Analyzed Take Rate trend (2.0% -> 1.8%)."
3. **Skills Skipped (If relevant):** Why were certain standard models NOT used?
