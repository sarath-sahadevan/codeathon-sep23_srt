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
    

import unittest

class TestMaxProfit(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_profit([]), -1)
    
    def test_single_price(self):
        self.assertEqual(max_profit([5]), -1)
    
    def test_no_profit(self):
        self.assertEqual(max_profit([7, 6, 5, 4, 3, 2, 1]), -1)
    
    def test_max_profit(self):
        self.assertEqual(max_profit([7, 1, 5, 3, 6, 4]), 5)
    
    def test_duplicate_prices(self):
        self.assertEqual(max_profit([7, 1, 5, 5, 3, 6, 4]), 5)
    
if __name__ == '__main__':
    unittest.main()