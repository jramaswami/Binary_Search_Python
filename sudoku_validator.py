"""
binarysearch.com :: Sudoku Validator
jramaswami
"""


class Solution:

    def solve(self, matrix):

        # Generator for rows.
        def row_gen(r):
            """Return values from the row indexed with r."""
            for n in matrix[r]:
                yield n

        # Generator for cols.
        def col_gen(c):
            """Return values from the column indexed c."""
            for row in matrix:
                yield row[c]

        # Generator for box.
        def box_gen(r, c):
            """Return values for box with top left of (r, c)."""
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    yield matrix[i][j]

        # Validate a section.
        def valid_section(g):
            """Return True if section is valid."""
            valid_numbers = set()
            for n in g:
                if 1 <= n <= 9:
                    valid_numbers.add(n)
                else:
                    # Invalid number.
                    return False
            return len(valid_numbers) == 9


        # Functions to validate rows, cols, and boxes.
        def all_rows_valid():
            """Return True if all rows are valid."""
            return all(valid_section(row_gen(r))
                       for r, _ in enumerate(matrix))

        def all_cols_valid():
            """Return True if all columns are valid."""
            return all(valid_section(col_gen(c))
                       for c, _ in enumerate(matrix[0]))

        def all_boxes_valid():
            """Return True if all boxes are valid."""
            return all(valid_section(box_gen(r, c))
                       for r in range(0, len(matrix), 3)
                       for c in range(0, len(matrix[0]), 3))

        return all_rows_valid() and all_cols_valid() and all_boxes_valid()


def test_1():
    matrix = [
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
    assert Solution().solve(matrix) == True


def test_2():
    matrix = [
        [4, 2, 6, 5, 7, 1, 3, 9, 8],
        [8, 5, 7, 2, 9, 3, 1, 4, 6],
        [1, 3, 9, 4, 6, 8, 2, 7, 5],
        [9, 7, 1, 3, 8, 5, 6, 2, 4],
        [5, 4, 3, 7, 2, 6, 8, 1, 9],
        [6, 8, 2, 1, 4, 9, 7, 5, 3],
        [7, 9, 4, 2, 3, 2, 5, 8, 1],
        [2, 6, 5, 8, 1, 4, 9, 3, 7],
        [3, 1, 8, 9, 5, 7, 4, 6, 2]
    ]
    assert Solution().solve(matrix) == False


def test_3():
    """
    WA.
    Since it wasn't specified, I assumed that the numbers would only be 1-9.
    """
    matrix = [
        [4, 2, 6, 5, 7, 1, 3, 20, 8],
        [8, 5, 7, 2, 9, 3, 1, 4, 6],
        [1, 3, 9, 4, 6, 8, 2, 7, 5],
        [9, 7, 1, 3, 8, 5, 6, 2, 4],
        [5, 4, 3, 7, 2, 6, 8, 1, 9],
        [6, 8, 2, 1, 4, 9, 7, 5, 3],
        [7, 9, 4, 6, 3, 2, 5, 8, 1],
        [2, 6, 5, 8, 1, 4, 9, 3, 7],
        [3, 1, 8, 9, 5, 7, 4, 6, 2]]
    assert Solution().solve(matrix) == False
