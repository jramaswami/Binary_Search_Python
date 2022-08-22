"""
binarysearch.com :: Buy and Sell K Stocks
jramaswami
"""


import functools


class Solution:

    def solve(self, prices, max_stocks):

        @functools.lru_cache(maxsize=None)
        def buy(day, stock_count):
            # Base case, ran out of days.
            if day >= len(prices):
                return 0

            # Base case, ran out of stocks.
            nonlocal max_stocks
            if stock_count >= max_stocks:
                return 0

            # You can buy the stock today.
            max_profit_buying = sell(day + 1, stock_count + 1) - prices[day]
            # You can choose to buy later.
            max_profit_not_buying = buy(day + 1, stock_count)
            return max(max_profit_buying, max_profit_not_buying)


        @functools.lru_cache(maxsize=None)
        def sell(day, stock_count):
            # Base case, ran out of days.
            if day >= len(prices):
                return 0

            # Base case ran out stocks won't happen because we don't buy
            # over the max stocks.

            # You can sell the stock today.
            max_profit_selling = buy(day + 1, stock_count) + prices[day]
            # You can choose to sell later.
            max_profit_not_selling = sell(day + 1, stock_count)
            return max(max_profit_selling, max_profit_not_selling)

        return buy(0, 0)


def test_1():
    prices = [6, 2, 4, 1, 2]
    k = 2
    expected = 3
    assert Solution().solve(prices, k) == expected


def test_2():
    prices = [5, 10, 15, 20, 25, 30, 35, 40, 45]
    k = 4
    expected = 40
    assert Solution().solve(prices, k) == expected


def test_3():
    prices = [5, 10, 15, 20, 25, 30, 35, 40, 45]
    k = 0
    expected = 0
    assert Solution().solve(prices, k) == expected