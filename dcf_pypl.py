import numpy as np
import pandas as pd

# Inputs
current_price = 52.69
shares_outstanding = 935.65  # Million
cash = 10755.00  # Million
debt = 12167.00  # Million
revenue_ltm = 32862.00  # Million
ebitda_ltm = 6619.00 # Million

# Assumptions
revenue_growth_rate = 0.08  # 8% growth
ebit_margin = 0.18  # Conservative 18% (EBITDA is ~20%, so EBIT slightly lower)
tax_rate = 0.21
wacc = 0.100  # 10.0%
terminal_growth_rate = 0.025 # 2.5%

# Projection (5 Years)
years = 5
revenues = []
ebits = []
fcf = []

current_rev = revenue_ltm

# Simplified FCF Proxy: EBIT * (1-t) (Assuming Capex = D&A roughly, and NWC change is minimal/offset)
# For a more detailed model, we'd project D&A, Capex, NWC separately. 
# Given PYPL is asset-light software, Free Cash Flow Conversion from EBITDA is usually high.
# Let's align with LTM FCF ($3125M) vs Net Income/EBITDA.
# LTM FCF ($3.1B) is ~9.5% of Revenue ($32.9B). 
# This is lower than historical (15-20%). Let's assume some recovery to 12% FCF Margin.

fcf_margin = 0.12 

for i in range(1, years + 1):
    rev = current_rev * ((1 + revenue_growth_rate) ** i)
    revenues.append(rev)
    # Project FCF directly as % of Revenue
    projected_fcf = rev * fcf_margin
    fcf.append(projected_fcf)

# Terminal Value
terminal_value = fcf[-1] * (1 + terminal_growth_rate) / (wacc - terminal_growth_rate)

# Discounting
discount_factors = [(1 + wacc) ** i for i in range(1, years + 1)]
pv_explicit = sum([f / d for f, d in zip(fcf, discount_factors)])
pv_terminal = terminal_value / ((1 + wacc) ** years)

enterprise_value = pv_explicit + pv_terminal
equity_value = enterprise_value + cash - debt
implied_share_price = equity_value / shares_outstanding

print(f"Base Case Price: ${implied_share_price:.2f}")

# Sensitivity Matrix
print("\nSensitivity Matrix (Share Price):")
wacc_range = [wacc - 0.01, wacc - 0.005, wacc, wacc + 0.005, wacc + 0.01]
g_range = [terminal_growth_rate - 0.005, terminal_growth_rate, terminal_growth_rate + 0.005]

header = ["WACC / g", "2.0%", "2.5%", "3.0%"]
print(f"{header[0]:<10} | {header[1]:<8} | {header[2]:<8} | {header[3]:<8}")
print("-" * 45)

for w in wacc_range:
    row_vals = []
    for g in g_range:
        tv = fcf[-1] * (1 + g) / (w - g)
        pv_tv = tv / ((1 + w) ** years)
        df_local = [(1 + w) ** i for i in range(1, years + 1)]
        pv_exp = sum([f / d for f, d in zip(fcf, df_local)])
        ev = pv_exp + pv_tv
        eq = ev + cash - debt
        price = eq / shares_outstanding
        row_vals.append(price)
    
    print(f"{w:.1%}      | ${row_vals[0]:.2f}   | ${row_vals[1]:.2f}   | ${row_vals[2]:.2f}")
