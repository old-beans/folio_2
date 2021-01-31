import pandas as pd

bal_vinix = 200000
bal_fzrox = 40000
bal_fspsx = 70000
bal_fbtix = 10000

portfolio = {'VINIX': {'asset class': 'domestic stock', 'value': bal_vinix},
             'FZROX': {'asset class': 'domestic stock', 'value': bal_fzrox},
             'FSPSX': {'asset class': 'international stock', 'value': bal_fspsx},
             'FBTIX': {'asset class': 'bond', 'value': bal_fbtix}}

df_portfolio = pd.DataFrame(portfolio).swapaxes(0, 1)
df_portfolio.loc["Total"] = df_portfolio.sum(numeric_only=True)
# asset_class_sum = df_portfolio.groupby(['asset class']).sum()


print(df_portfolio)
# print(asset_class_sum)
