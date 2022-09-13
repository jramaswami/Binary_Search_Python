"""
binarysearch.com :: Making Change Trequel
jramaswami
"""


class Solution:

    def solve(self, denominations, amount):
        MOD = pow(10, 9) + 7
        # dp[amount] = number of ways to reach it.
        dp = [0 for _ in range(amount+1)]
        # There is one way to reach 0.
        dp[0] = 1
        for i, _ in enumerate(dp):
            for d in denominations:
                if i+d <= amount:
                    dp[i+d] += dp[i]
                    dp[i+d] %= MOD
                else:
                    break
        return dp[-1] % MOD


def test_1():
    denominations = [2, 3]
    amount = 6
    expected = 2
    assert Solution().solve(denominations, amount) == expected


def test_2():
    denominations = [1,57]
    amount = 1001
    expected = 18
    assert Solution().solve(denominations, amount) == expected