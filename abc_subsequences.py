"""
binarysearch.com :: ABC Subsequences
jramaswami
"""


class Solution:

    def solve(self, S):
        ord_a = ord('a')
        dp = [1, 0, 0, 0]
        for c in S:
            k = ord(c) - ord_a + 1
            dp[k] += (dp[k-1] + dp[k])
        return dp[-1]


def test_1():
    S = "aabc"
    assert Solution().solve(S) == 3
