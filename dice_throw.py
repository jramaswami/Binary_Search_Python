"""
binarysearch.com :: Dice Throw
jramaswami
"""


class Solution:
    def solve(self, n, faces, total):
        MOD = pow(10, 9) + 7
        dp = [[0 for _ in range(total+1)] for _ in range(n+1)]
        dp[0][0] = 1
        for i, row in enumerate(dp[:-1]):
            for k, _ in enumerate(row):
                if dp[i][k]:
                    for f in range(1, faces+1):
                        if k+f <= total:
                            dp[i+1][k+f] = (dp[i+1][k+f] + dp[i][k]) % MOD
        return dp[-1][-1]


def test_1():
    n = 2
    faces = 6
    total = 7
    expected = 6
    assert Solution().solve(n, faces, total) == expected
