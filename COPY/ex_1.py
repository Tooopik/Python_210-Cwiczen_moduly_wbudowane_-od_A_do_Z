import copy


stocks = [['CDR', '11B'], ['PLW'], ['TEN']]
stocks_copied = copy.copy(stocks)
stocks[0][1] = 'CRJ'


print(f'stocks: {stocks}')
print(f'stocks_copied: {stocks_copied}')
