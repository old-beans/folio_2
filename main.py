import pandas as pd

bal_vinix = 167162
bal_fzrox = 28748
bal_fspsx = 68372
bal_fbtix = 9431

portfolio = {'VINIX': {'asset class': 'domestic stock', 'value': bal_vinix},
             'FZROX': {'asset class': 'domestic stock', 'value': bal_fzrox},
             'FSPSX': {'asset class': 'international stock', 'value': bal_fspsx},
             'FBTIX': {'asset class': 'bond', 'value': bal_fbtix}}

df_portfolio = pd.DataFrame.from_dict(portfolio, orient='index')
df_portfolio.loc["total"] = df_portfolio.sum(numeric_only=True)
total_value = df_portfolio.loc['total', 'value']
df_portfolio['weight %'] = df_portfolio['value'] / total_value * 100

print(df_portfolio)

asset_class_sum = df_portfolio.groupby(['asset class']).sum()
print(asset_class_sum)
