"""
binarysearch.com :: Diagonal Sort
jramaswami
"""

class Solution:
    def solve(self, matrix):
        # Corner cases:
        if matrix == [] or matrix[0] == []:
            return [list(row) for row in matrix]

        def inbounds(r, c):
            return r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[r])

        def diagonal_generator(r, c):
            while inbounds(r, c):
                yield r, c
                r, c = r + 1, c + 1

        def collect_diagonal(r, c):
            return [matrix[r0][c0] for r0, c0 in diagonal_generator(r, c)]

        matrix0 = [list(row) for row in matrix]
        for r, _ in enumerate(matrix):
            values = collect_diagonal(r, 0)
            values.sort()
            for (r0, c0), value in zip(diagonal_generator(r, 0), values):
                matrix0[r0][c0] = value
        for c, _ in enumerate(matrix[0][1:], start=1):
            values = collect_diagonal(0, c)
            values.sort()
            for (r0, c0), value in zip(diagonal_generator(0, c), values):
                matrix0[r0][c0] = value
        return matrix0


def test_1():
    matrix = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    expected = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    assert Solution().solve(matrix) == expected


def test_2():
    matrix = []
    expected = []
    assert Solution().solve(matrix) == expected


def test_3():
    matrix = [[], [], []]
    expected = [[], [], []]
    assert Solution().solve(matrix) == expected
