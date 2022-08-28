"""
binarysearch.com :: Flipped Matrix
jramawami
"""


class Solution:
    def solve(self, matrix):
        # First flip all rows so that the first row is 1.
        for r, row in enumerate(matrix):
            if row[0] == 0:
                for c, _ in enumerate(row):
                    matrix[r][c] = (1 if matrix[r][c] == 0 else 0)
        # Determine the number of one bits in each column.
        colbits = [0 for _ in matrix[0]]
        for r, row in enumerate(matrix):
            for c, x in enumerate(row):
                colbits[c] += x

        soln = 0
        val = 1
        for x in reversed(colbits):
            soln += (val * max(x, len(matrix) - x))
            val *= 2
        return soln



def test_1():
    matrix = [ [0, 0, 1], [0, 0, 0] ]
    expected = 13
    assert Solution().solve(matrix) == expected
