"""
binarysearch.com :: Cut Matrix
jramaswami
"""


class MatrixSums:

    def __init__(self, matrix):
        self.prefix = [[0 for _ in row] for row in matrix]
        self.is_empty = True

        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                if matrix[r][c] == 1:
                    self.is_empty = False
                self.prefix[r][c] = (
                    matrix[r][c] +
                    self.get_prefix(r-1, c) +
                    self.get_prefix(r, c-1) -
                    self.get_prefix(r-1, c-1)
                )

    def get_prefix(self, r, c):
        if r < 0 or r >= len(self.prefix) or c < 0 or c >= len(self.prefix[r]):
            return 0
        return self.prefix[r][c]

    def get_sum(self, r1, c1, r2, c2):
        return (
            self.get_prefix(r2, c2) -
            self.get_prefix(r1-1, c2) -
            self.get_prefix(r2, c1-1) +
            self.get_prefix(r1-1, c1-1)
        )


class Solution:

    def solve(self, matrix, k):
        MOD = pow(10, 9) +7

        # Use prefix sum on matrices to get submatrix sums.
        matrix_sums = MatrixSums(matrix)

        # Boundary case: matrix has no ones in it.
        if matrix_sums.is_empty:
            return 0

        max_row, max_col = len(matrix) - 1, len(matrix[0]) - 1
        # dp[number of cuts][top left row][top left col]
        # There are k - 1 cuts to make k pieces.
        dp = [[[0 for _ in row] for row in matrix] for _ in range(k)]
        # There is 1 way to get a matrix with some ones with 0 cuts.
        dp[0][0][0] = 1
        for cut in range(0, k-1):
            for r, row in enumerate(matrix):
                for c, _ in enumerate(row):
                    # If the state dp[cut][r][c] is reachable ...
                    if dp[cut][r][c] > 0:
                        # We can try to cut on any row [r+1, max_row).
                        # The column will remain the same.
                        for r_cut, _ in enumerate(matrix[r+1:], start=r+1):
                            # If we are going to make this cut, both of the
                            # resulting submatrices must have a sum > 0.
                            x = matrix_sums.get_sum(r, c, r_cut-1, max_col)
                            y = matrix_sums.get_sum(r_cut, c, max_row, max_col)
                            if x > 0 and y > 0:
                                dp[cut+1][r_cut][c] = (dp[cut+1][r_cut][c] + dp[cut][r][c]) % MOD
                        # We can try to cut on any column [c+1, max_col).
                        # The row will remain the same.
                        for c_cut, _ in enumerate(matrix[0][c+1:], start=c+1):
                            x = matrix_sums.get_sum(r, c, max_row, c_cut-1)
                            y = matrix_sums.get_sum(r, c_cut, max_row, max_col)
                            if x > 0 and y > 0:
                                dp[cut+1][r][c_cut] = (dp[cut+1][r][c_cut] + dp[cut][r][c]) % MOD

        # Solution is the number of ways we can reach k-1 cuts.
        soln = 0
        for row in dp[k-1]:
            for x in row:
                soln = (soln + x) % MOD
        return soln



def test_1():
    matrix = [ [1, 1], [1, 1] ]
    k = 2
    expected = 2
    assert Solution().solve(matrix, k) == expected


def test_2():
    matrix = [ [0, 0], [1, 1] ]
    k = 2
    expected = 1
    assert Solution().solve(matrix, k) == expected
