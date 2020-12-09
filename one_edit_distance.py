"""
binarysearch.com :: One Edit Distance
https://binarysearch.com/problems/One-Edit-Distance
"""
class Solution:
    def solve(self, s0, s1):
        dp = [[0 for _ in range(len(s1)+1)] for _ in range(len(s0)+1)]
        # Initialize dp array
        for i in range(len(dp)):
            dp[i][0] = i
        for i in range(len(dp[0])):
            dp[0][i] = i

        for i, a in enumerate(s0):
            for j, b in enumerate(s1):
                if a == b:
                    # Since two characters are equal, the edit distance is the
                    # same as that for the the string without the two characters.
                    dp[i+1][j+1] = dp[i][j]
                else:
                    # The edit distance is 1 + the minimum of the three up and
                    # to the left of this cell.
                    dp[i+1][j+1] = 1 + min(dp[i][j], dp[i][j+1], dp[i+1][j])

        return dp[-1][-1] <= 1

def test_1():
    s0 = "quicksort"
    s1 = "quicksort"
    solver = Solution()
    assert solver.solve(s0, s1) == True

def test_2():
    s0 = "mergesort"
    s1 = "mergesorts"
    solver = Solution()
    assert solver.solve(s0, s1) == True

def test_3():
    s0 = "mergeport"
    s1 = "mergesorts"
    solver = Solution()
    assert solver.solve(s0, s1) == False

def test_4():
    s0 = ""
    s1 = "mergesorts"
    solver = Solution()
    assert solver.solve(s0, s1) == False

def test_5():
    s0 = ""
    s1 = ""
    solver = Solution()
    assert solver.solve(s0, s1) == True