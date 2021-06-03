"""
binarysearch.com :: Largest Square Submatrix
jramaswami
"""


class Solution:
    def solve(self, matrix):
        row_dp = [list(row) for row in matrix]
        col_dp = [list(row) for row in matrix]

        for r, row in enumerate(row_dp):
            curr = 0
            for c, val in enumerate(row):
                curr = (curr + val) * val
                row_dp[r][c] = curr


        for c in range(len(matrix[0])):
            curr = 0
            for r in range(len(matrix)):
                val = matrix[r][c]
                curr = (curr + val) * val
                col_dp[r][c] = curr

        square = [list(row) for row in matrix]
        soln = 1
        for r, row in enumerate(row_dp):
            for c, _ in enumerate(row):
                if r == 0 or c == 0:
                    continue
                prev_square = square[r-1][c-1]
                min_square = min(prev_square + 1, row_dp[r][c], col_dp[r][c])
                square[r][c] = min_square
                soln = max(soln, square[r][c] ** 2)

        # print('matrix')
        # for row in matrix:
        #     print(row)
        # print('row dp')
        # for row in row_dp:
        #     print(row)
        # print('col dp')
        # for row in col_dp:
        #     print(row)
        # print('square')
        # for row in square:
        #     print(row)

        return soln


#
# Previous TLE Solution: used for random testing on new solution.
#


from itertools import accumulate


class SubmatrixSums:
    def __init__(self, matrix):
        self.sums = [list(accumulate(row)) for row in matrix]
        for r, row in enumerate(self.sums):
            for c, _ in enumerate(row):
                if r - 1 >= 0:
                    self.sums[r][c] += self.sums[r-1][c]

    def query(self, row, col):
        """Return sum of submatrix from 0, 0 to row, col (inclusive)."""
        if row < 0 or col < 0:
            return 0
        return self.sums[row][col]

    def max_square(self, row, col, best_so_far):
        """Return the max square with top left corner at (row, col)"""
        delta = best_so_far - 1
        soln = best_so_far
        while row + delta < len(self.sums) and col + delta < len(self.sums[0]):
            # Find the submatrix sum from (row, col) to (row0, col0) exclusive
            row0 = row + delta
            col0 = col + delta
            sqrt = delta + 1

            A = self.query(row0, col0) 
            B = self.query(row0, col - 1) 
            C = self.query(row - 1, col0) 
            D = self.query(row - 1, col - 1)
            s = (A - B - C + D)

            if s == sqrt * sqrt:
                soln = max(soln, sqrt * sqrt)
            delta += 1
        return soln

    def __str__(self):
        return "\n".join(str(row) for row in self.sums)


def solve_with_submatrix_sums(matrix):
    """TLE solution."""
    submatrix_sums = SubmatrixSums(matrix)
    soln = 0
    for r, row in enumerate(matrix):
        for c, _ in enumerate(row):
            soln = max(soln, submatrix_sums.max_square(r, c, 0))
    return soln


#
# Testing
#


import random


def test_1():
    matrix = [
        [0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == 16


def test_2():
    matrix = [
        [0, 1, 1, 1, 0, 1, 0, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 0, 1, 1, 1, 1, 1, 0, 0],
        [1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
    ]
    assert Solution().solve(matrix) == 9


def test_3():
    matrix = [[0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1],
              [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1],
              [0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
              [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1],
              [1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
              [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
              [0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1],
              [0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0],
              [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
              [1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
              [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
              [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0]]
    assert Solution().solve(matrix) == 9


def test_4():
    matrix = [[1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1], 
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1], 
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1], 
              [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
              [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1], 
              [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
              [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1], 
              [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1], 
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1], 
              [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
              [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1], 
              [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1], 
              [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1], 
              [1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1], 
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1], 
              [1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1], 
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 
              [1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0]]

    solve_with_submatrix_sums(matrix)
    assert Solution().solve(matrix) == 25


def test_5():
    matrix = [[1, 1, 1, 0, 1], 
              [1, 1, 1, 1, 1], 
              [1, 1, 1, 1, 1], 
              [1, 1, 1, 1, 1], 
              [0, 1, 1, 1, 1]]
    assert Solution().solve(matrix) == 16


def test_6():
    """WA"""
    matrix = [[0]]
    assert Solution().solve(matrix) == 0


def generate_random_matrix(size):
    """Genrate a random matrix."""
    return [[random.choice([0,1,1,1,1,1,1]) for _ in range(size)] for _ in range(size)]


def test_random():
    N = 200
    T = 2
    for _ in range(T):
        matrix = generate_random_matrix(N)
        expected = solve_with_submatrix_sums(matrix) 
        result = Solution().solve(matrix)
        if result != expected:
            print(f"{expected=} {result=}")
            print(matrix)

        assert result == expected



#
# Main method to get a handle on how fast solution runs against maximal
# conditions
#


from timeit import default_timer as timer


def main():
    """For timing against a large matrix."""
    matrix = generate_random_matrix(200)
    start = timer()
    Solution().solve(matrix)
    stop = timer()
    print(f"{stop - start} seconds.")



if __name__ == '__main__':
    main()


