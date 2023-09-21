def max_profit(prices):
    if len(prices) < 2:
        return -1
    
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    
    if max_profit == 0:
        return -1
    else:
        return max_profit