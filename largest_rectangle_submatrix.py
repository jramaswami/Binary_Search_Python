"""
binarysearch.com :: Largest Rectangle Submatrix
jramaswami
"""


from collections import namedtuple


Item = namedtuple('Item', ['height', 'index'])


class Solution:
    def solve(self, matrix):
        # Corner case:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        # The "height" of the column at (r, c).
        height = [[0 for _ in row] for row in matrix]

        for c, _ in enumerate(matrix[0]):
            for r, _ in enumerate(matrix):
                if r == 0:
                    height[r][c] = matrix[r][c]
                else:
                    if matrix[r][c]:
                        height[r][c] = matrix[r][c] + height[r-1][c]

        soln = 0

        # Left to right
        for r, row in enumerate(height):
            stack = []
            for c, ht in enumerate(row):
                # Add current index to stack.
                stack.append(Item(ht, c))

                # Fix the stack by "cutting off the tops."
                stack = [Item(min(ht, s.height), s.index) for s in stack]

                soln = max(soln,
                        max(
                            s.height * (1 + c - s.index) for s in stack
                        )
                )

        return soln


def test_1():
    matrix = [ [1, 0, 0, 0], [1, 0, 1, 1], [1, 0, 1, 1], [0, 1, 0, 0] ]
    expected = 4
    assert Solution().solve(matrix) == expected


def test_2():
    matrix = [ [1, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 1, 1, 0, 0], [0, 0, 0, 0, 0], [1, 1, 0, 0, 1], [1, 1, 0, 0, 1] ]
    expected = 4
    assert Solution().solve(matrix) == expected


def test_3():
    matrix = [ [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0] ]
    expected = 12
    assert Solution().solve(matrix) == expected


def test_4():
    matrix = [ [1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 1, 1], [1, 1, 1, 1] ]
    expected = 8
    assert Solution().solve(matrix) == expected
