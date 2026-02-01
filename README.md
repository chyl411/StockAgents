# Agent Analysis - Financial Services Architecture

An AI-powered multi-agent system designed for institutional-grade financial analysis, modeling, and reporting. This project leverages a specialized orchestrator and a suite of domain-specific agents to perform deep-dive equity research.

## 🚀 Overview

This repository houses the **Financial Services Agents Architecture**, a structured framework where AI agents collaborate to answer complex investment questions. From parsing user requests to running DCF models and stress-testing investment theses, the system acts as a virtual hedge fund analyst team.

**Core Philosophy:**
- **Data-First:** Grounded in real-time market data and financial filings.
- **Variant View:** Always compares internal analysis vs. Wall Street consensus.
- **Transparency:** Every output includes an "Execution Trace" showing exactly what tools and logic were used.

## 📂 Project Structure

- **`.cursor/skills/`**: The brain of the agents. Contains prompt-engineered "Skill" files that define specific capabilities (e.g., DCF modeling, Bear Case analysis).
- **`AGENTS.md`**: The master architecture document defining agent roles, workflows, and routing logic.
- **`*.py`**: Python utility scripts for data retrieval (yfinance) and financial modeling.

## 🤖 Agent Roles & Capabilities

The system is controlled by a **Core Orchestrator** (`finance-orchestrator`) that delegates tasks to:

| Agent | Responsibility |
| :--- | :--- |
| **`risk-timing-agent`** | Assesses macro/geopolitical risks and entry timing. |
| **`market-data-retrieval`** | Fetches prices, financials, and beta. |
| **`consensus-check`** | Compares our view vs. Wall Street estimates. |
| **`strategic-market-analysis`** | Analyzes industry trends, moats, and management execution. |
| **`dcf-valuation-agent`** | Builds absolute valuation models with sensitivity analysis. |
| **`bear-case-analysis`** | "Red Team" that attacks the bullish thesis. |
| **`earnings-analysis-agent`** | Reviews quarterly results and guidance. |

*(See `AGENTS.md` for the full skills map)*

## 🛠️ Usage

This project is optimized for use within **Cursor** or similar AI-integrated IDEs.

1.  **Ask a Question:**
    > "Analyze PYPL and tell me if it's a buy."
    > "Run a bear case analysis on NVDA."

2.  **Orchestration:**
    The AI follows the protocol in `AGENTS.md`, sequentially activating skills:
    1.  Checks Macro Risk
    2.  Fetches Data
    3.  Checks Consensus
    4.  Runs Valuation Models
    5.  Performs Strategic & Bear Case Analysis

3.  **Output:**
    Receives a comprehensive report with a specific recommendation (Buy/Hold/Sell) and an Execution Trace.

## 📄 Documentation

For detailed architecture, workflow examples, and transparency protocols, please refer to:
👉 **[AGENTS.md](./AGENTS.md)**

## ⚠️ Disclaimer

This tool is for informational and research purposes only. It does not constitute financial advice. Always conduct your own due diligence before making investment decisions.
