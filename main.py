import pandas as pd

bal_vinix = 200000
bal_fzrox = 40000
bal_fspsx = 70000
bal_fbtix = 9080

portfolio = [
    {'symbol': 'VINIX', 'type': 'domestic stock', 'value': bal_vinix},
    {'symbol': 'FZROX', 'type': 'domestic stock', 'value': bal_fzrox},
    {'symbol': 'FSPSX', 'type': 'international stock', 'value': bal_fspsx},
    {'symbol': 'FBTIX', 'type': 'bond', 'value': bal_fbtix}]


df_portfolio = pd.DataFrame(portfolio)
df_portfolio['weighting'] = (df_portfolio['value']/sum(fund['value'] for fund in portfolio)*100)
print(df_portfolio)








