"""
binarysearch.com :: Count Square Submatrices
jramaswami
"""

class Solution:

    def solve(self, matrix):
        dp = [list(row) for row in matrix]
        for r, row in enumerate(dp[1:], start=1):
            for c, _ in enumerate(row[1:], start=1):
                if matrix[r][c]:
                    dp[r][c] = 1 + min(dp[r-1][c], dp[r][c-1], dp[r-1][c-1])

        return sum(sum(row) for row in dp)



def test_1():
    matrix = [[1,1,0],[1,1,0]]
    expected = 5
    assert Solution().solve(matrix) == expected

