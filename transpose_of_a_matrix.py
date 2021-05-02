"""
binarysearch.com :: Transpose of a Matrix
jramaswami
"""
class Solution:
    def solve(self, matrix):
        matrix0 = [list(row) for row in matrix]
        for r, row in enumerate(matrix0):
            for c, _ in enumerate(row):
                if c >= r:
                    break
                matrix0[r][c], matrix0[c][r] = matrix0[c][r], matrix0[r][c]
        return matrix0


def test_1():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    assert Solution().solve(matrix) == expected