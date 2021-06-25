"""
binarysearch.com :: Buying Cars
jramaswami
"""


class Solution:
    def solve(self, prices, k):
        # O(n log n)
        prices0 = sorted(prices)
        soln = 0
        # O(n)
        for p in prices0:
            if p <= k:
                k -= p
                soln += 1
        return soln


def test_1():
    prices = [90, 30, 20, 40, 90]
    k = 95
    expected = 3
    assert Solution().solve(prices, k) == expected


def test_2():
    prices = [60, 90, 55, 75]
    k = 50
    expected = 0
    assert Solution().solve(prices, k) == expected
