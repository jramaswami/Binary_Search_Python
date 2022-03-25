"""
binarysearch.com :: Making Change Sequel
jramaswami
"""


import math
import heapq


class Solution:
    def solve(self, denominations, amount):
        dp = dict()
        for d in denominations:
            dp[d] = 1
        Q = list(denominations)
        heapq.heapify(Q)
        while Q:
            k = heapq.heappop(Q)
            for d in denominations:
                if k + d <= amount:
                    if k + d not in dp:
                        dp[k+d] = dp[k] + 1
                        heapq.heappush(Q, k+d)
                    else:
                        dp[k+d] = min(dp[k+d], dp[k]+1)
        if amount in dp:
            return dp[amount]
        return -1


def test_1():
    denominations = [1, 5, 10, 25]
    amount = 60
    expected = 3
    assert Solution().solve(denominations, amount) == expected


def test_2():
    denominations = [3, 7, 10]
    amount = 8
    expected = -1
    assert Solution().solve(denominations, amount) == expected


def test_3():
    denominations = [1, 5, 10, 25]
    amount = 500000
    expected = 20000
    assert Solution().solve(denominations, amount) == expected
