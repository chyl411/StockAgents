
import numpy as np
import pandas as pd

def calculate_dcf(
    current_revenue_bn=11.6,  # Based on Q1/Q2 FY26 run rate
    growth_rates=[0.25, 0.20, 0.15, 0.10, 0.05], # AGGRESSIVE AI Growth to test $250 valuation
    ebit_margin=0.35,         # Optimistic Margin expansion
    tax_rate=0.21,
    wacc=0.09,                # Lower WACC due to market enthusiasm
    terminal_growth=0.03,
    shares_outstanding_mn=348,
    net_debt_bn=2.0           
):
    
    # Project Free Cash Flows
    years = range(1, 6)
    revenues = []
    ebits = []
    nopat = [] # Net Operating Profit After Tax
    fcff = []  # Free Cash Flow to Firm (proxy: NOPAT * conversion, assuming capex ~ dep for mature HDD)
               # Actually, HDD requires capex. Let's assume FCF conversion is 80% of NOPAT
    
    current_rev = current_revenue_bn
    
    print(f"{'Year':<5} | {'Revenue ($B)':<12} | {'EBIT ($B)':<10} | {'FCF ($B)':<10}")
    print("-" * 50)

    for g in growth_rates:
        current_rev = current_rev * (1 + g)
        revenues.append(current_rev)
        
        ebit = current_rev * ebit_margin
        ebits.append(ebit)
        
        _nopat = ebit * (1 - tax_rate)
        nopat.append(_nopat)
        
        # Assumption: FCF is ~80% of NOPAT (Capex > Depreciation for capacity expansion)
        _fcf = _nopat * 0.80 
        fcff.append(_fcf)
        
        print(f"{len(revenues):<5} | {current_rev:<12.2f} | {ebit:<10.2f} | {_fcf:<10.2f}")

    # Terminal Value
    terminal_fcf = fcff[-1] * (1 + terminal_growth)
    terminal_value = terminal_fcf / (wacc - terminal_growth)
    
    # Discounting
    discount_factors = [(1 + wacc) ** i for i in years]
    pv_fcff = sum([f / d for f, d in zip(fcff, discount_factors)])
    pv_terminal = terminal_value / ((1 + wacc) ** 5)
    
    enterprise_value = pv_fcff + pv_terminal
    equity_value = enterprise_value - net_debt_bn
    share_price = (equity_value * 1000) / shares_outstanding_mn
    
    print("-" * 50)
    print(f"Terminal Value ($B): {terminal_value:.2f}")
    print(f"PV of FCF ($B): {pv_fcff:.2f}")
    print(f"PV of TV ($B): {pv_terminal:.2f}")
    print(f"Enterprise Value ($B): {enterprise_value:.2f}")
    print(f"Equity Value ($B): {equity_value:.2f}")
    print(f"Implied Share Price ($): {share_price:.2f}")
    
    return share_price

if __name__ == "__main__":
    calculate_dcf()
