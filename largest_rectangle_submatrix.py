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
            # Stack holds the leftmost index for a given height.
            # Stack invariant: heights are in ascending order.
            stack = []
            for c, ht in enumerate(row):
                # Add current index to stack.
                stack.append(Item(ht, c))

                # Fix the stack.  Find the leftmost item with a height greater
                # than ht.  Replace that item with an item at the same index
                # but with a height of ht.
                leftmost_index = c
                while stack and stack[-1].height >= ht:
                    leftmost_index = min(c, stack[-1].index)
                    stack.pop()
                stack.append(Item(ht, leftmost_index))

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


def test_5():
    matrix = [[1 for _ in range(250)] for _ in range(250)]
    expected = 250 * 250
    assert Solution().solve(matrix) == expected
