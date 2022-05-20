"""
binarysearch.com :: A Flight of Stairs Sequel
jramaswami
"""


class Solution:

    def solve(self, n, k):
        # dp[three jumps][stair]
        dp = [[0 for _ in range(n+1)] for _ in range(k+1)]
        dp[0][0] = 1

        for stair, _ in enumerate(dp[0]):
            for three_jumps, _ in enumerate(dp):
                # From here you can step 1 or 2 steps with no cost.
                if stair + 1 <= n:
                    dp[three_jumps][stair+1] += dp[three_jumps][stair]
                if stair + 2 <= n:
                    dp[three_jumps][stair+2] += dp[three_jumps][stair]
                # You can jump 3 steps if you haven't exceeded the max yet.
                if stair + 3 <= n and three_jumps + 1 <= k:
                    dp[three_jumps+1][stair+3] += dp[three_jumps][stair]

        return sum(row[-1] for row in dp)


def test_1():
    n = 4
    k = 1
    expected = 7
    assert Solution().solve(n, k) == expected


def test_2():
    n = 3
    k = 0
    expected = 3
    assert Solution().solve(n, k) == expected
