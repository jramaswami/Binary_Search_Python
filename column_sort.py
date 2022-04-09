"""
binarysearch.com :: Column Sort
jramaswami
"""


class Solution:
    def solve(self, matrix):
        for c, _ in enumerate(matrix[0]):
            values = sorted(matrix[r][c] for r, _ in enumerate(matrix))
            for r, _ in enumerate(matrix):
                matrix[r][c] = values[r]
        return matrix


def test_1():
    matrix = [ [10, 20, 30], [5, 5, 3], [0, 10, 7] ]
    expected = [ [0, 5, 3], [5, 10, 7], [10, 20, 30] ]
    assert Solution().solve(matrix) == expected
