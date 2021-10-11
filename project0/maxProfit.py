def maxProfit(prices = [7,1,5,3,6,4]):
	buy = prices[0]
	sell = prices[0]
	for p in prices:
		if p < buy:
			buy = p
			sell = p
		if p > sell:
			sell = p
	return sell - buy
print(maxProfit())



