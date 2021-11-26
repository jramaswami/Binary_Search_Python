"""
binarysearch.com :: A Maniacal Walk
jramaswami
"""


class Solution:

    def solve(self, length, N):
        MOD = pow(10, 9) + 7
        dp = [[0 for _ in range(length)] for _ in range(N+1)]
        dp[0][0] = 1
        for r, _ in enumerate(dp[1:], start=1):
            for c, _ in enumerate(dp[r]):
                # Move right
                if c - 1 >= 0:
                    dp[r][c] = (dp[r][c] + dp[r-1][c-1]) % MOD

                # Stay
                dp[r][c] = (dp[r][c] + dp[r-1][c]) % MOD

                # Move left
                if c + 1 < len(dp[r]):
                    dp[r][c] = (dp[r][c] + dp[r-1][c+1]) % MOD

        return dp[-1][0]


def test_1():
    assert Solution().solve(5, 3) == 4
