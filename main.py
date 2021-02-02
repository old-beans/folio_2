import pandas as pd

bal_vinix = 169842
bal_fzrox = 28748
bal_fspsx = 69176
bal_vbtix = 9352
bal_vfiax = 5876

portfolio = {'VINIX': {'asset class': 'dom stock', 'p_value': bal_vinix, 'returns': 10, 'Net ER': 0.035},
             'FZROX': {'asset class': 'dom stock', 'p_value': bal_fzrox, 'returns': 10, 'Net ER': 0},
             'FSPSX': {'asset class': 'int stock', 'p_value': bal_fspsx, 'returns': 5, 'Net ER': 0.035},
             'VBTIX': {'asset class': 'bond',      'p_value': bal_vbtix, 'returns': 5, 'Net ER': 0.035},
             'VFIAX': {'asset class': 'dom stock', 'p_value': bal_vfiax, 'returns': 5, 'Net ER': 0.04}}

df_portfolio = pd.DataFrame.from_dict(portfolio, orient='index')
df_portfolio = df_portfolio.sort_values('p_value', axis=0, ascending=False)
df_portfolio.loc['total'] = df_portfolio[['p_value']].sum(numeric_only=True)

df_portfolio['weight %'] = df_portfolio['p_value'] / df_portfolio.loc['total', 'p_value'] * 100
df_portfolio['weight %'] = df_portfolio['weight %'].round(decimals=2)

print(df_portfolio)


asset_class_sum = df_portfolio.groupby(['asset class']).sum()
asset_class_sum = asset_class_sum.sort_values('weight %', ascending=False)

print(asset_class_sum)
