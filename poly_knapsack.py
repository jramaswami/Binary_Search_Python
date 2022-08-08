"""
binarysearch.com :: Poly Knapsack
jramaswami
"""


import math


class Solution:

    def solve(self, weights, values, capacity):
        dp = [[-math.inf for _ in range(capacity+1)] for _ in range(len(weights)+1)]
        dp[0][0] = 0
        soln = -math.inf
        for i, _ in enumerate(weights):
            w = weights[i]
            v = values[i]
            for pw in range(capacity+1):
                cw = 0
                cv = 0
                while pw + cw <= capacity:
                    dp[i+1][pw+cw] = max(
                        dp[i+1][pw+cw],
                        dp[i][pw] + cv
                    )
                    cw += w
                    cv += v
        return max(max(row) for row in dp)


def test_1():
    weights = [1, 2, 3]
    values = [1, 5, 3]
    capacity = 5
    expected = 11
    assert Solution().solve(weights, values, capacity) == expected
