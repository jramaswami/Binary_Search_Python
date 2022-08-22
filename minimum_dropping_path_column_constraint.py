"""
binarysearch.com :: Minimum Dropping Path Sum With Column Distance Constraint
jramaswami
"""


from math import inf


class Solution:
    def solve(self, matrix):
        dp = [[inf for _ in row] for row in matrix]
        dp[0] = list(matrix[0])
        for r, row in enumerate(dp):
            if r < len(matrix) - 1:
                for c, val in enumerate(row):
                    if c - 1 >= 0:
                        k = matrix[r+1][c-1] + val
                        dp[r+1][c-1] = min(k, dp[r+1][c-1])
                    if c + 1 < len(row):
                        k = matrix[r+1][c+1] + val
                        dp[r+1][c+1] = min(k, dp[r+1][c+1])
                    k = matrix[r+1][c] + val
                    dp[r+1][c] = min(k, dp[r+1][c])

        return min(dp[-1])


def test_1():
    matrix = [
        [3, 0, 3],
        [1, 4, 3],
        [-2, 3, -3]
    ]
    assert Solution().solve(matrix) == -1


def test_2():
    matrix = [
        [-2, 1],
        [2, -3],
        [-1, 0]
    ]
    assert Solution().solve(matrix) == -6