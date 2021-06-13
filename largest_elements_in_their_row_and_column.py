"""
binarysearch.com :: Largest Elements in Their Row and Column
jramaswami
"""


class Solution:
    def solve(self, matrix):
        if not matrix:
            return 0

        sums_by_row = [sum(row) for row in matrix]
        sums_by_col = [0 for _ in matrix[0]]
        for c, _ in enumerate(matrix[0]):
            for row in matrix:
                sums_by_col[c] += row[c]

        soln = 0
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == 1 and sums_by_row[r] == 1 and sums_by_col[c] == 1:
                    soln += 1
        return soln


def test_1():
    matrix = [
        [0, 0, 1],
        [1, 0, 0],
        [0, 1, 0]
    ]
    assert Solution().solve(matrix) == 3


def test_2():
    matrix = [
        [0, 0, 1],
        [1, 0, 0],
        [1, 0, 0]
    ]
    assert Solution().solve(matrix) == 1


def test_3():
    matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert Solution().solve(matrix) == 0


def test_4():
    matrix = []
    assert Solution().solve(matrix) == 0


def test_5():
    matrix = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    assert Solution().solve(matrix) == 0
