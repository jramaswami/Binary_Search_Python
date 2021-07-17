"""
binarysearch.com :: Rotate A Box Under Gravity
jramaswami
"""


class Solution:
    def solve(self, matrix):
        N = len(matrix)
        M = len(matrix[0])

        # Compute the lowest point that each box can fall to.
        lowest_point = [[-1 for _ in row] for row in matrix]
        for r, row in enumerate(matrix):
            low = M - 1
            for c in range(M - 1, -1, -1):
                if matrix[r][c] == '#':
                    lowest_point[r][c] = low
                    low -= 1
                elif matrix[r][c] == '*':
                    lowest_point[r][c] = c
                    low = c - 1
        # Create new matrix
        rot_matrix = [['.' for _ in range(N)] for _ in range(M)]

        # Populate new matrix
        for r, row in enumerate(matrix):
            for c, value in enumerate(row):
                if value != '.':
                    r0 = lowest_point[r][c]
                    c0 = len(rot_matrix[0]) - r - 1
                    rot_matrix[r0][c0] = value

        return rot_matrix


def test_1():
    matrix = [
        ["#", "#", ".", ".", ".", ".", "."],
        ["#", "#", "#", ".", ".", ".", "."],
        ["#", "#", "#", ".", ".", "#", "."]
    ]
    expected = [
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."],
        ["#", ".", "."],
        ["#", "#", "."],
        ["#", "#", "#"],
        ["#", "#", "#"]
    ]
    assert Solution().solve(matrix) == expected


def test_2():
    matrix = [
        ["#", "*", "."],
        ["*", ".", "."],
        ["#", "#", "."],
        [".", ".", "."]
    ]
    expected = [
        [".", ".", "*", "#"],
        [".", "#", ".", "*"],
        [".", "#", ".", "."]
    ]
    assert Solution().solve(matrix) == expected
