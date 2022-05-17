"""
binarysearch.com :: Big Numbers
jramaswami
"""


import math


class Solution:

    def solve(self, matrix):
        soln = 0
        if matrix:
            row_maxes = [max(r) for r in matrix]
            col_maxes = [-math.inf for _ in matrix[0]]
            for c, _ in enumerate(matrix[0]):
                for row in matrix:
                    col_maxes[c] = max(row[c], col_maxes[c])
            for r, row in enumerate(matrix):
                for c, val in enumerate(row):
                    if val == row_maxes[r] and val == col_maxes[c]:
                        soln += 1
        return soln


def test_1():
    matrix = [
        [1, 3, 2],
        [6, 6, 5],
        [1, 5, 7]
    ]
    expected = 3
    assert Solution().solve(matrix) == expected
