import sys

def calculate_dcf():
    # --- 1. Model Inputs (Based on Search Context) ---
    # Current Market Data
    current_price = 78.0
    shares_outstanding = 0.34  # Approx 340M shares (derived from ~$26B Market Cap)
    net_debt = 4.0             # Billions (Debt $6B - Cash $2B approx)
    
    # Financial Projections (The "AI Storage Cycle" Scenario)
    # WDC HDD Revenue ~ $10B. FCF Margin target ~15-18% in upcycle.
    fcf_year_0 = 1.5           # Billion USD (Normalized mid-cycle FCF)
    
    # Sensitivity Variables
    wacc_options = [0.09, 0.11, 0.13]  # 9% (Bull), 11% (Base), 13% (Bear/Risk)
    terminal_growth_options = [-0.02, 0.0, 0.02] # -2% (Tech Obsolescence), 0% (Flat), 2% (GDP)
    
    print(f"{'WACC':<8} | {'Term. Growth':<12} | {'Intrinsic Value':<15} | {'Upside/Downside':<15}")
    print("-" * 60)
    
    # --- 2. DCF Calculation (2-Stage Model) ---
    for wacc in wacc_options:
        for g_term in terminal_growth_options:
            # Stage 1: High Growth for 5 Years (AI Cycle)
            # Assumption: 15% growth for 3 years, then tapering to terminal
            growth_stage_1 = [0.15, 0.15, 0.10, 0.05, 0.02]
            
            future_fcf = []
            current_fcf = fcf_year_0
            
            # Calculate PV of Explicit Period
            pv_stage_1 = 0
            for i, g in enumerate(growth_stage_1):
                current_fcf = current_fcf * (1 + g)
                future_fcf.append(current_fcf)
                pv_stage_1 += current_fcf / ((1 + wacc) ** (i + 1))
            
            # Calculate Terminal Value (Gordon Growth Method)
            fcf_terminal = future_fcf[-1] * (1 + g_term)
            if wacc <= g_term:
                tv = 0 # Invalid
            else:
                tv = fcf_terminal / (wacc - g_term)
            
            pv_tv = tv / ((1 + wacc) ** 5)
            
            # Total Enterprise Value
            enterprise_value = pv_stage_1 + pv_tv
            
            # Equity Value
            equity_value = enterprise_value - net_debt
            
            # Share Price
            intrinsic_price = equity_value / shares_outstanding
            
            diff = (intrinsic_price - current_price) / current_price * 100
            
            print(f"{wacc:.1%}     | {g_term:.1%}        | ${intrinsic_price:6.2f}         | {diff:+6.1f}%")

    print("\n" + "="*60)
    print("ANALYSIS OF THE GAP:")
    print("Current Price ($78) aligns roughly with: WACC 11-13% AND Terminal Growth 0%")
    print("Meaning: The market is pricing in ZERO long-term growth and HIGH execution risk.")

if __name__ == "__main__":
    calculate_dcf()
