def maxProfit(prices = [3,2, 6,4,4, 7]):
	buy = prices[0]
	sell = prices[0]
	profit = (0, )
	for p in prices:
		if p < buy:
			if sell - buy > profit[0]:
				profit = (sell - buy, buy, sell)
			buy = p
			sell = p		
		if p > sell:
			sell = p
	if sell - buy > profit[0]:
		return (buy, sell)
	return	profit[1:]
print(maxProfit())



