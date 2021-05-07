"""
binarysearch.com :: Wolves of Wall Street
jramaswami
"""
class Solution:
    def solve(self, prices):
        soln = 0
        for left, right in zip(prices[:-1], prices[1:]):
            if left < right:
                soln += right - left
        return soln


def test_1():
    prices = [1, 5, 3, 4, 6]
    assert Solution().solve(prices) == 7


def test_2():
    prices = [5, 4, 3, 2, 1]
    assert Solution().solve(prices) == 0


def test_3():
    prices = [4, 1, 5, 1, 4, 2, 5, 8, 1, 8, 3, 1, 6, 6, 2, 4, 4, 5, 2, 7]
    assert Solution().solve(prices) == 33


def test_4():
    prices = [1, 5, 4, 10, 1, 3, 3, 1, 5, 5, 2, 3, 10, 2, 2, 5, 5, 4, 1, 5]
    assert Solution().solve(prices) == 31