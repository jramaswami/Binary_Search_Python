"""
binarysearch.com :: Longest Common Substring
jramaswami
"""


class Solution:

    def solve(self, s0, s1):
        dp = [[0 for _ in s1] for _ in s0]

        def get(r, c):
            "Helper method for retrieving value from dp matrix."
            if r < 0 or c < 0:
                return 0
            return dp[r][c]

        soln = 0
        for i, a in enumerate(s0):
            for j, b in enumerate(s1):
                if a == b:
                    dp[i][j] = 1 + get(i-1, j-1)
                    soln = max(soln, dp[i][j])

        return soln


def test_1():
    s0 = "helloworld"
    s1 = "worldpine"
    expected = 5
    assert Solution().solve(s0, s1) == expected


def test_2():
    s0 = ""
    s1 = "worldpine"
    expected = 0
    assert Solution().solve(s0, s1) == expected


def test_3():
    s0 = "worldpine"
    s1 = ""
    expected = 0
    assert Solution().solve(s0, s1) == expected


def test_4():
    s0 = ""
    s1 = ""
    expected = 0
    assert Solution().solve(s0, s1) == expected
