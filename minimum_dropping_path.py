"""
binarysearch.com :: Minimum Dropping Path Sum
jramaswami
"""
from math import inf


class Solution:
    def solve(self, matrix):
        dp = [[inf for _ in row] for row in matrix]
        dp[0] = list(matrix[0])
        for r, row in enumerate(matrix):
            if r == 0:
                continue
            for c0, _ in enumerate(row):
                for c1, _ in enumerate(row):
                    if c0 != c1:
                        dp[r][c0] = min(dp[r][c0], matrix[r][c0] + dp[r-1][c1])
        return min(dp[-1])



def test_1():
    matrix = [
        [4, 5, -2],
        [2, 6, 1],
        [3, 1, 2]
    ]
    assert Solution().solve(matrix) == 1


def test_2():
    matrix = [
        [3, 0, 3],
        [2, 1, 3],
        [-2, 3, 0]
    ]
    assert Solution().solve(matrix) == 1
