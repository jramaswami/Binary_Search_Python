"""
binarysearch.com :: Condo Developers
jramaswami
"""
class Solution:
    def solve(self, matrix):
        row_maxes = [max(row) for row in matrix]
        col_maxes = [max(row[i] for row in matrix) for i, _ in enumerate(matrix[0])]
        soln = [list(row) for row in matrix]
        for r, row in enumerate(soln):
            for c, _ in enumerate(row):
                soln[r][c] = min(row_maxes[r], col_maxes[c])
        return soln


def test_1():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected = [
        [3, 3, 3],
        [6, 6, 6],
        [7, 8, 9]
    ]
    assert Solution().solve(matrix) == expected

def test_2():
    matrix = [
        [4, 4, 3],
        [5, 5, 3],
        [7, 8, 3]
    ]
    expected = [
        [4, 4, 3],
        [5, 5, 3],
        [7, 8, 3]
    ]
    assert Solution().solve(matrix) == expected
