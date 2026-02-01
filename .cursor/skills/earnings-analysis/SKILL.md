---
name: earnings-analysis
description: Analyzes earnings results versus expectations, decomposes drivers, extracts guidance changes, and summarizes key takeaways and risks with citations. Use when the user mentions earnings, quarterly results, beats/misses, guidance, call transcript, or QoQ/YoY performance.
---

# Earnings Analysis

## Instructions

### 1. The Numbers (Headline vs Consensus)
*   **Table**: Revenue, EPS, Gross Margin.
*   **Comparison**: Actual vs Consensus Estimate (use `market-data-retrieval` to find consensus).
*   **Guidance**: Next Quarter (Q+1) Guide vs Street expectations.

### 2. Operational & Engagement Metrics (The "Pulse" of the Business)
*   **Beyond the P&L**: Look for the *leading indicators* of business health.
*   **Engagement Metrics (Crucial for Tech/Fintech)**:
    *   **TPA (Transactions Per Account)**: Is user activity intensifying or fading?
    *   **Churn / Retention**: Are they losing users?
    *   **Active Accounts**: Growth vs. Stall.
    *   **CAC (Customer Acquisition Cost)**: Efficiency check.
*   **Interpretation**:
    *   *High Account Growth + Low TPA* = Low quality growth (Marketing driven).
    *   *Flat Account Growth + High TPA* = High quality, loyal core (Pricing power).

### 3. The Narrative (Press Release)
*   What drove the beat/miss? (Volume? Price? FX? One-offs?)
*   Identify the "Pivot": Did the company change its strategic focus?

### 4. The Q&A Session (Crucial Alpha)
*   **Analyze the Transcript**: Focus on the Analyst Q&A session.
*   **Sentiment Check**: Is Management confident or evasive?
*   **Top 3 Questions**: What did analysts keep asking about? (e.g., "3 separate analysts asked about AI margin impact").
*   **"Read-Through"**: What does this say about the competitor/industry?

## Output Template
### Flash Note: [Ticker] Q[X] Earnings

**1. Scorecard**
| Metric | Actual | Consensus | Delta | Guide (Next Q) |
| :--- | :--- | :--- | :--- | :--- |
| Rev | ... | ... | ... | ... |

**2. Engagement & Unit Economics**
*   **Active Accounts**: [Value] (Trend)
*   **TPA (Engagement)**: [Value] (Trend) -> *Verdict: [Sticky/Churning]*

**3. Key Takeaways**
*   **Bullish**: [Point 1]
*   **Bearish**: [Point 2]

**4. Q&A & Sentiment Analysis**
*   **Tone**: [Confident/Cautious/Defensive]
*   **Key Debate**: [What was the most heated topic?]
*   **Mgmt Quote**: "[Insert key quote]"
