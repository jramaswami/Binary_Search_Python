"""
binarysearch.com :: Count Exact Sum
jramaswami
"""


class Solution:

    def solve(self, nums, k):
        MOD = pow(10, 9) + 7
        # dp[nums][sum] = number of ways
        dp = [[0 for _ in range(k+1)] for _ in range(len(nums)+1)]
        dp[0][0] = 1 # You can have no numbers 1 way.
        for i, n in enumerate(nums, start=1):
            for j in range(k+1):
                # Do not choose n
                dp[i][j] += dp[i-1][j]
                dp[i][j] %= MOD
                # Choose n
                if j + n <= k:
                    dp[i][j+n] += dp[i-1][j]
                    dp[i][j+n] %= MOD
        return dp[-1][-1] % MOD


def test_1():
    nums = [1, 2, 3, 4, 5]
    k = 5
    expected = 3
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [1, 2, 3, 4, 5]
    k = 10
    expected = 3
    assert Solution().solve(nums, k) == expected