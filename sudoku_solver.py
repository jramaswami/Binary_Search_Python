"""
binarysearch.com :: Sudoku Solver
jramaswami
"""


class Solution:

    def solve(self, matrix):

        def box_generator(r, c):
            "For a given row and column, return the values in its box."
            corner_row = 3 * (r // 3)
            corner_col = 3 * (c // 3)

            for dr in range(0, 3):
                for dc in range(0, 3):
                    r0 = corner_row + dr
                    c0 = corner_col + dc
                    yield matrix[r0][c0]

        def row_generator(r):
            "For a given row, return values in the row."
            for c in matrix[r]:
                yield c

        def col_generator(c):
            "For a given column, return values in the column."
            for row in matrix:
                yield row[c]

        def legal_move(r, c, val):
            "Return True if setting matrix[r][c] = val is a legal move."
            return (val not in box_generator(r, c) and
                    val not in row_generator(r) and
                    val not in col_generator(c)
            )

        def dfs(i):
            "DFS search of possible states."
            # Base case: solution found because
            if i >= (len(matrix) * len(matrix)):
                soln = [list(row) for row in matrix]
                return soln

            # Convert 1d index to 2d indices.
            r, c = divmod(i, len(matrix))

            # Base case: if matrix[r][c] is already set, continue to next cell.
            if matrix[r][c] > 0:
                return dfs(i+1)

            for d in range(1, 10):
                if legal_move(r, c, d):
                    matrix[r][c] = d
                    result = dfs(i)
                    if result is not None:
                        return result
                    matrix[r][c] = 0
            return None

        return dfs(0)


def test_1():
    matrix = [
        [0, 2, 0, 5, 0, 1, 0, 9, 0],
        [8, 0, 0, 2, 0, 3, 0, 0, 6],
        [0, 3, 0, 0, 6, 0, 0, 7, 0],
        [0, 0, 1, 0, 0, 0, 6, 0, 0],
        [5, 4, 0, 0, 0, 0, 0, 1, 9],
        [0, 0, 2, 0, 0, 0, 7, 0, 0],
        [0, 9, 0, 0, 3, 0, 0, 8, 0],
        [2, 0, 0, 8, 0, 4, 0, 0, 7],
        [0, 1, 0, 9, 0, 7, 0, 6, 0]
    ]
    expected = [
        [4, 2, 6, 5, 7, 1, 3, 9, 8],
        [8, 5, 7, 2, 9, 3, 1, 4, 6],
        [1, 3, 9, 4, 6, 8, 2, 7, 5],
        [9, 7, 1, 3, 8, 5, 6, 2, 4],
        [5, 4, 3, 7, 2, 6, 8, 1, 9],
        [6, 8, 2, 1, 4, 9, 7, 5, 3],
        [7, 9, 4, 6, 3, 2, 5, 8, 1],
        [2, 6, 5, 8, 1, 4, 9, 3, 7],
        [3, 1, 8, 9, 5, 7, 4, 6, 2]
    ]
    assert Solution().solve(matrix) == expected
