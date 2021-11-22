"""
binarysearch.com :: Edit Distance
jramaswami

REF: https://www.youtube.com/watch?v=We3YDTzNXEk&t=321s
"""


class Solution:

    def solve(self, S, T):
        dp = [[0 for _ in range(len(T) + 1)] for _ in range(len(S) + 1)]
        # Initialize first row.
        dp[0] = list(range(len(T) + 1))
        for r, row in enumerate(dp):
            row[0] = r

        for r, s in enumerate(S, start=1):
            for c, t in enumerate(T, start=1):
                if s == t:
                    # Take the left diagonal.
                    dp[r][c] = dp[r-1][c-1]
                else:
                    # Take the one added to minimum of left, up, and
                    # diagonal left.
                    dp[r][c] = 1 + min(dp[r][c-1], dp[r-1][c], dp[r-1][c-1])

        return dp[-1][-1]



def test_1():
    a = "zhello"
    b = "helli"
    expected = 2
    assert Solution().solve(a, b) == expected


def test_2():
    a = "dycare"
    b = "daycare"
    expected = 1
    assert Solution().solve(a, b) == expected