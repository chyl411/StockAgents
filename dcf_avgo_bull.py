import pandas as pd
import numpy as np

# Inputs
ticker = "AVGO"
current_price = 331.30
shares_outstanding = 4.74e9
net_debt = 49.0e9
last_revenue = 63.9e9

# WACC
wacc = 0.10 # Fixed at 10% for simplicity

# Bull Case Assumptions
years = 5
growth_rates = [0.55, 0.25, 0.20, 0.15, 0.10] # Aggressive Consensus
target_ebitda_margin = 0.60 # Mgmt Target
target_ebit_margin = 0.58 
tax_rate = 0.21
net_reinvestment_rate = 0.02 # Asset Light

# DCF
projections = []
revenue = last_revenue
for g in growth_rates:
    revenue = revenue * (1 + g)
    ebitda = revenue * target_ebitda_margin
    ebit = revenue * target_ebit_margin
    nopat = ebit * (1 - tax_rate)
    reinvestment = revenue * net_reinvestment_rate
    fcff = nopat - reinvestment
    projections.append({
        'Revenue': revenue,
        'EBITDA': ebitda,
        'FCFF': fcff
    })

df = pd.DataFrame(projections)
df.index = range(1, years + 1)

discount_factors = [1 / ((1 + wacc) ** t) for t in range(1, years + 1)]
pv_explicit = sum(df['FCFF'] * discount_factors)

# Method 1: Perpetuity Growth (3.5%)
g_term = 0.035
tv_perp = df['FCFF'].iloc[-1] * (1 + g_term) / (wacc - g_term)
pv_tv_perp = tv_perp * discount_factors[-1]
ev_perp = pv_explicit + pv_tv_perp
price_perp = (ev_perp - net_debt) / shares_outstanding

# Method 2: Exit Multiple (20x EBITDA)
exit_multiple = 20.0
tv_mult = df['EBITDA'].iloc[-1] * exit_multiple
pv_tv_mult = tv_mult * discount_factors[-1]
ev_mult = pv_explicit + pv_tv_mult
price_mult = (ev_mult - net_debt) / shares_outstanding

print(f"Price (Perpetuity 3.5%): ${price_perp:.2f}")
print(f"Price (Exit Multiple 20x): ${price_mult:.2f}")
print(f"Current Price: ${current_price:.2f}")

print("\nProjections:")
print(df[['Revenue', 'EBITDA', 'FCFF']])
