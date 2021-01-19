import pandas as pd

bal_vinix = 200000
bal_fzrox = 40000
bal_fspsx = 70000
bal_fbtix = 10000

portfolio = [
    {'symbol': 'VINIX', 'asset class': 'domestic stock', 'value': bal_vinix},
    {'symbol': 'FZROX', 'asset class': 'domestic stock', 'value': bal_fzrox},
    {'symbol': 'FSPSX', 'asset class': 'international stock', 'value': bal_fspsx},
    {'symbol': 'FBTIX', 'asset class': 'bond', 'value': bal_fbtix}]


df_portfolio = pd.DataFrame(portfolio)
df_portfolio['weighting'] = (df_portfolio['value']/sum(fund['value'] for fund in portfolio)*100)
df_portfolio.loc["Total"] = df_portfolio.sum(numeric_only=True)

print(df_portfolio)




