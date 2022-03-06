"""
binarysearch.com :: Wolf of Wall Street
jramaswami
"""

class Solution:

    def solve(self, prices):
        # Boundary case: empty prices
        if not prices:
            return 0

        mins = list(prices)
        maxs = list(prices)

        for i, _ in enumerate(prices[1:], start=1):
            mins[i] = min(mins[i], mins[i-1])

        for i in range(len(maxs)-2, -1, -1):
            maxs[i] = max(maxs[i], maxs[i+1])

        return max(mx-mn for mn,mx in zip(mins, maxs))


def test_1():
    prices = [9, 11, 8, 5, 7, 10]
    expected = 5
    assert Solution().solve(prices) == expected


def test_2():
    prices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = 8
    assert Solution().solve(prices) == expected


def test_3():
    prices = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected = 0
    assert Solution().solve(prices) == expected
