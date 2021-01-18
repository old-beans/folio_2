
bal_vinix = 200000
bal_fspsx = 70000
bal_fbtix = 9080
bal_fzrox = 40000

portfolio = [bal_vinix, bal_fspsx, bal_fbtix, bal_fzrox]

portfolio_sum = sum(portfolio)
print("sum = ", portfolio_sum)

for fund in portfolio:
    fund_weight = int(fund/portfolio_sum * 100)
    print(fund_weight)







