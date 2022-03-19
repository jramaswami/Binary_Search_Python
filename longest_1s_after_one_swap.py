"""
binarysearch.com :: Longest 1s After One Swap
jramaswami
"""


class Solution:

    def solve(self, S):
        dp = [0 for _ in S]
        curr_sum = 0
        total = 0
        for i, c in enumerate(S):
            if c == '1':
                curr_sum += 1
                total += 1
            else:
                curr_sum = 0
            dp[i] = curr_sum

        curr_sum = 0
        soln = 0
        for i in range(len(dp)-1, -1, -1):
            if dp[i] > 0:
                curr_sum = max(curr_sum, dp[i])
            else:
                curr_sum = 0
            dp[i] = curr_sum
            soln = max(soln, curr_sum + 1)

        for i, v in enumerate(dp[1:-1], start=1):
            if dp[i-1] > 0 and dp[i] == 0 and dp[i+1] > 0:
                soln = max(soln, dp[i-1] + dp[i+1] + 1)
        soln = min(total, soln)
        return soln


def test_1():
    s = "0111011101"
    assert Solution().solve(s) == 7


def test_2():
    s = "000100010"
    assert Solution().solve(s) == 2
