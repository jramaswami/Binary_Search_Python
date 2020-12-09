"""
binarysearch.com :: Longest Palindromic Subsequence
REF: https://www.youtube.com/watch?v=_nCsPn7_OgI
"""
class Solution:
    def solve(self, s):
        if s == "":
            return 0

        dp = [[0 for _ in s] for _ in s]
        for i, _ in enumerate(s):
            dp[i][i] = 1

        for length in range(2, len(s)+1):
            start = 0
            while start < len(s) - length + 1:
                end = start + length - 1
                if length == 2 and s[start] == s[end]:
                    # If the there are only two chars and they are the same,
                    # then the LPS for [start, end] is 2.
                    dp[start][end] = 2
                elif s[start] == s[end]:
                    # If the chars at start and end are the same then the LPS
                    # for [start, end] is 2 + the LPS for [start+1][end-1].
                    dp[start][end] = 2 + dp[start+1][end-1]
                else:
                    # If the chars at start and end are different then the LPS
                    # for [start, end] is the largest LPS for [start][end-1]
                    # or [start+1][end].
                    dp[start][end] = max(dp[start+1][end], dp[start][end-1])
                start += 1

        return dp[0][-1]

def test_1():
    s = "rbaicneacrayr"
    solver = Solution()
    assert solver.solve(s) == 7

def test_2():
    s = "binarysearch"
    solver = Solution()
    assert solver.solve(s) == 3

def test_3():
    s = "bbbbbbbbbb"
    solver = Solution()
    assert solver.solve(s) == 10

def test_4():
    solver = Solution()
    assert solver.solve("") == 0
