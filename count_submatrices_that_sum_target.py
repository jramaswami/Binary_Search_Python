"""
binarysearch.com :: Count Submatrices That Sum Target
jramaswami
"""


import math


class Solution:

    def solve(self, matrix, target):

        # Prefix sums for matrix.
        prefix = [[0 for _ in row] for row in matrix]

        def get_prefix(r, c):
            "Helper function to return prefix sum or 0 if out of bounds."
            if r < 0 or c < 0:
                return 0
            return prefix[r][c]

        # Compute prefix sums
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                prefix[r][c] = (
                    get_prefix(r-1, c) +
                    get_prefix(r, c-1) -
                    get_prefix(r-1, c-1) +
                    val
                )

        def get_sum(r1, c1, r2, c2):
            """
            Compute the sum for the matrix from top left (r1, c1)
            to bottom right (r2, c2).
            """
            return (
                get_prefix(r2, c2) -
                get_prefix(r1-1, c2) -
                get_prefix(r2, c1-1) +
                get_prefix(r1-1, c1-1)
            )

        # Compute number of submatrices that sum to target.
        soln = 0
        height, width = len(matrix), len(matrix[0])
        for r1 in range(height):
            for r2 in range(r1, height):
                for c1 in range(width):
                    for c2 in range(c1, width):
                        if get_sum(r1, c1, r2, c2) == target:
                            soln += 1
        return soln


def test_1():
    matrix = [ [0, -1], [0, 0] ]
    target = 0
    expected = 5
    assert Solution().solve(matrix, target) == expected
