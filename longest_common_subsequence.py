"""
binarysearch.com :: Longest Common Subsequence
REF: https://www.youtube.com/watch?v=NnD96abizww
"""
class Solution:
    def solve(self, a, b):
        if a == "" or b == "":
            return 0

        dp = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]
        for i in range(1, len(a)+1):
            for j in range(1, len(b)+1):
                if a[i-1] == b[j-1]:
                    # If the characters are the same, then the LCS including
                    # b[j-1] is 1 + the LCS that included a[i-2] and b[j-2],
                    # the previous chars in a and b.
                    dp[j][i] = 1 + dp[j-1][i-1]
                else:
                    # If the characters are not the same, then the LCS
                    # including b[j-1] is the longest that included b[i-2] or
                    # the one that includes b[i-2] or the one that included
                    # a[i-2].
                    dp[j][i] = max(dp[j][i-1], dp[j-1][i])

        return dp[-1][-1]


def test_1():
    a = "abcvc"
    b = "bv"
    solver = Solution()
    assert solver.solve(a, b) == 2

def test_2():
    a = "abc"
    b = "abc"
    solver = Solution()
    assert solver.solve(a, b) == 3

def test_3():
    a = "abc"
    b = "def"
    solver = Solution()
    assert solver.solve(a, b) == 0

def test_4():
    a = "binarysearch"
    b = "searchbinary"
    solver = Solution()
    assert solver.solve(a, b) == 6

def test_5():
    a = ""
    b = "searchbinary"
    solver = Solution()
    assert solver.solve(a, b) == 0

def test_6():
    a = "searchbinary"
    b = ""
    solver = Solution()
    assert solver.solve(a, b) == 0
