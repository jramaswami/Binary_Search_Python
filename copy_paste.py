"""
binarysearch.com :: Copy Paste
jramaswami
"""


class Solution:

    def solve(self, n):
        # dp[i] = max chars at this operation.
        dp = [0 for _ in range(n+1)]
        for i, _ in enumerate(dp[:-1]):
            # At this point you can insert a single char and be done.
            dp[i+1] = max(dp[i+1],dp[i] + 1)
            # Or You can copy the buffer an paste as many times as possible.
            clip = dp[i] * 2
            for j, _ in enumerate(dp[i+2:], start=i+2):
                dp[j] = max(dp[j], clip)
                clip += dp[i]
        return dp[-1]


def test_1():
    n = 6
    expected = 9
    assert Solution().solve(n) == expected


def test_2():
    "TLE"
    n = 40
    expected = 2125764
    assert Solution().solve(n) == expected


def test_3():
    n = 100
    expected = 7412080755407364
    assert Solution().solve(n) == expected