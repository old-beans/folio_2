
bal_vinix = 200000
bal_fzrox = 40000
bal_fspsx = 70000
bal_fbtix = 9080

portfolio = [
    {'symbol': 'VINIX', 'type': 'domestic stock', 'value': bal_vinix},
    {'symbol': 'FZROX', 'type': 'domestic stock', 'value': bal_fzrox},
    {'symbol': 'FSPSX', 'type': 'international_stock', 'value': bal_fspsx},
    {'symbol': 'FBTIX', 'type': 'bond', 'value': bal_fbtix}
    ]


def sum_portfolio():
    portfolio_total = sum(fund['value'] for fund in portfolio)
    print("Total ->", portfolio_total)
    return portfolio_total


def fund_weights(portfolio_total):
    total_weight = 0
    for fund in portfolio:
        fund_weight = fund['value']/total_value * 100
        print(fund['symbol'], " -> {:.2f} %".format(fund_weight), "%")
        total_weight += fund_weight

    print("Total Weight ->", total_weight)
    return


total_value = sum_portfolio()
fund_weights(total_value)








