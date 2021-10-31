"""
binarysearch.com :: Making Change
jramaswami
"""


import math


class Solution:

    def solve(self, n):
        COINS = (1, 5, 10, 25)
        dp = [math.inf for _ in range(n + 1)]
        dp[0] = 0
        for i in range(n + 1):
            if dp[i] == math.inf:
                continue
            for coin in COINS:
                if i + coin <= n:
                    dp[i + coin] = min(dp[i + coin], dp[i] + 1)
        return dp[-1]


def test_1():
    assert Solution().solve(3) == 3


def test_2():
    assert Solution().solve(5) == 1


def test_3():
    assert Solution().solve(6) == 2


def test_4():
    assert Solution().solve(294624) == 11790


def test_5():
    """TLE"""
    assert Solution().solve(69733939) == 2789362