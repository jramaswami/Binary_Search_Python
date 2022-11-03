"""
binarysearch.com :: Weekly Contest 40 :: Minimum Dropping Path Sum With Column Distance Cost
jramaswami
"""
from math import inf


class Solution:
    def solve(self, matrix):
        dp = [[-inf for _ in row] for row in matrix]
        soln = [0 for _ in matrix[0]]
        for r, row in enumerate(matrix):
            max_value = -inf
            for c, value in enumerate(row):
                max_value = max(max_value - 1, value)
                dp[r][c] = max(dp[r][c], max_value)

            max_value = -inf
            for c in range(len(row) -1, -1, -1):
                value = row[c]
                max_value = max(max_value - 1, value)
                dp[r][c] = max(dp[r][c], max_value)

            for c, _ in enumerate(row):
                if r+1 < len(matrix):
                    matrix[r+1][c] += dp[r][c]

        return max(matrix[-1])


def test_1():
    matrix = [
        [3, 2, 1, 6],
        [4, 1, 2, 0],
        [1, 5, 2, -2]
    ]
    assert Solution().solve(matrix) == 11

def test_2():
    matrix = [
        [7, 6, 5, 6],
        [6, 4, 5, 8]
    ]
    assert Solution().solve(matrix) == 14

def test_3():
    matrix = [
        [2, 1, 3]
    ]
    assert Solution().solve(matrix) == 3
