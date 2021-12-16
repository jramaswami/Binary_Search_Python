"""
binarysearch.com :: Bomber Man
jramaswami
"""


class Solution:

    def solve(self, matrix):
        def column(c):
            "Generator yielding values in column c."
            for row in matrix:
                yield row[c]

        row_sums = [sum(row) for row in matrix]
        col_sums = [sum(column(c)) for c, _ in enumerate(matrix[0])]

        soln = 0
        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                if row_sums[r] == 0 and col_sums[c] == 0:
                    soln += 1
        return soln


def test_1():
    matrix = [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert Solution().solve(matrix) == 1


def test_2():
    matrix = [[]]
    assert Solution().solve(matrix) == 0


def test_3():
    matrix = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == 2
