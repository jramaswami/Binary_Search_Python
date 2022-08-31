"""
binarysearch.com :: Bear of Wall Street
jramaswami
"""


import functools


class Solution:

    def solve(self, prices):

        @functools.cache
        def sell(i):
            # Base case.
            if i >= len(prices):
                return 0

            return max(
                prices[i] + buy(i+2),   # I can sell now, but I have wait a day,
                sell(i+1)               # or wait and sell later.
            )

        @functools.cache
        def buy(i):
            # Base case.
            if i >= len(prices):
                return 0

            return max(
                -prices[i] + sell(i+1),    # I can buy now,
                buy(i+1)                   # Or wait and buy later.
            )

        return buy(0)


def test_1():
    prices = [1, 5, 8, 3, 10]
    expected = 11
    assert Solution().solve(prices) == expected
