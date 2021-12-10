"""
binarysearch.com :: Tromino Theory
jramaswami

REF: https://www.youtube.com/watch?v=7cijrfUkQzc
"""


class Solution:
    def solve(self, n):
        # Corner cases:
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2

        MOD = pow(10, 9) + 7
        dp = [0 for _ in range(n+1)]
        dp[1], dp[2], dp[3] = 1, 2, 5
        for i in range(4, n+1):
            a = (2 * dp[i-1]) % MOD
            b = dp[i-3]
            dp[i] = (a + b) % MOD
        return dp[n]


def test_1():
    assert Solution().numTilings(3) == 5


def test_2():
    assert Solution().numTilings(1) == 1
