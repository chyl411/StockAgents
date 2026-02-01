import pandas as pd
import numpy as np

# Inputs
ticker = "AVGO"
current_price = 331.30
shares_outstanding = 4.74e9 # 4.74B
net_debt = 49.0e9 # $49B
last_revenue = 63.9e9 # FY25

# WACC Calculation
rf_rate = 0.0424 # 4.24%
beta = 1.22
erp = 0.05
cost_of_equity = rf_rate + beta * erp # ~10.34%
cost_of_debt_pre_tax = 0.05
tax_rate = 0.21
cost_of_debt = cost_of_debt_pre_tax * (1 - tax_rate) # ~3.95%

# Capital Structure (Market Value)
equity_val = current_price * shares_outstanding
total_cap = equity_val + net_debt
weight_e = equity_val / total_cap
weight_d = net_debt / total_cap

wacc = weight_e * cost_of_equity + weight_d * cost_of_debt
# wacc is likely close to 10%

# Projections (Bull Case / Market Implied)
years = 5
growth_rates = [0.55, 0.25, 0.20, 0.15, 0.10] # Matching Consensus + Sustained AI
target_ebit_margin = 0.58 # Higher margins from software mix
net_reinvestment_rate = 0.02 # Asset light

# DCF Logic
projections = []
revenue = last_revenue
for g in growth_rates:
    revenue = revenue * (1 + g)
    ebit = revenue * target_ebit_margin
    nopat = ebit * (1 - tax_rate)
    reinvestment = revenue * net_reinvestment_rate
    fcff = nopat - reinvestment
    projections.append({
        'Revenue': revenue,
        'EBIT': ebit,
        'NOPAT': nopat,
        'FCFF': fcff
    })

df = pd.DataFrame(projections)
df.index = range(1, years + 1)

# Discounting
discount_factors = [1 / ((1 + wacc) ** t) for t in range(1, years + 1)]
pv_explicit = sum(df['FCFF'] * discount_factors)

# Terminal Value (Gordon Growth)
terminal_g = 0.03
terminal_fcff = df['FCFF'].iloc[-1] * (1 + terminal_g)
terminal_value = terminal_fcff / (wacc - terminal_g)
pv_tv = terminal_value * discount_factors[-1]

enterprise_value = pv_explicit + pv_tv
equity_value_calc = enterprise_value - net_debt
implied_price = equity_value_calc / shares_outstanding

# Sensitivity Matrix (WACC vs Terminal Growth)
wacc_range = np.arange(wacc - 0.01, wacc + 0.015, 0.005) # +/- 1%
g_range = np.arange(terminal_g - 0.01, terminal_g + 0.015, 0.005) # +/- 1%

sensitivity = pd.DataFrame(index=wacc_range, columns=g_range)

for w in wacc_range:
    for g_term in g_range:
        # Recalculate PV Explicit (technically minimal change if WACC changes for discount, doing full recalc)
        dfs = [1 / ((1 + w) ** t) for t in range(1, years + 1)]
        pv_ex = sum(df['FCFF'] * dfs)
        
        tv = (df['FCFF'].iloc[-1] * (1 + g_term)) / (w - g_term)
        pv_t = tv * dfs[-1]
        
        eq_val = (pv_ex + pv_t) - net_debt
        price = eq_val / shares_outstanding
        sensitivity.loc[w, g_term] = price

print(f"WACC: {wacc:.2%}")
print(f"Implied Price (Base): ${implied_price:.2f}")
print(f"Current Price: ${current_price:.2f}")
print(f"Upside: {(implied_price/current_price - 1):.1%}")
print("\nSensitivity Matrix (Rows=WACC, Cols=TermGrowth):")
print(sensitivity)
print("\nProjections:")
print(df[['Revenue', 'FCFF']])
