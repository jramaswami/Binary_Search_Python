"""
binarysearch.com :: Broker of Wall Street
jramaswami
"""


import functools


class Solution:

    def solve(self, prices, fee):

        @functools.cache
        def buy(i):
            # Base Case.
            if i >= len(prices):
                return 0

            # Buy here or stay.
            return max(
                sell(i+1) - prices[i],
                buy(i+1)
            )

        @functools.cache
        def sell(i):
            # Base case.
            if i >= len(prices):
                return 0

            # Sell here or hold.
            return max(
                buy(i+1) - fee + prices[i],
                sell(i+1)
            )

        return buy(0)


def test_1():
    prices = [1, 9, 3, 7]
    fee = 3
    expected = 6
    assert Solution().solve(prices, fee) == expected