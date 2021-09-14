"""
binarysearch.com :: Maximum Product Path in Matrix
jramaswami
"""


from math import inf


class Solution:

    def solve(self, matrix):
        MOD = pow(10, 9) + 7

        # Init dp matrices.  You need to keep track the min values because
        # two negative values produce a positive value.
        dp_max = [[-inf for _ in row] for row in matrix]
        dp_max[0][0] = matrix[0][0]
        dp_min = [[inf for _ in row] for row in matrix]
        dp_min[0][0] = matrix[0][0]

        for r, row in enumerate(matrix):
                for c, val in enumerate(row):
                    # You can arrive at dp[r][c] from above or from the left
                    if r > 0:
                        x = val * dp_max[r-1][c]
                        y = val * dp_min[r-1][c]
                        dp_max[r][c] = max(dp_max[r][c], max(x, y))
                        dp_min[r][c] = min(dp_min[r][c], min(x, y))
                    if c > 0:
                        x = val * dp_max[r][c-1]
                        y = val * dp_min[r][c-1]
                        dp_max[r][c] = max(dp_max[r][c], max(x, y))
                        dp_min[r][c] = min(dp_min[r][c], min(x, y))

        for row in dp_max:
            print(row)
        soln = dp_max[-1][-1]
        if soln < 0:
            return -1
        return soln % (pow(10, 9) + 7)


def test_1():
    matrix = [
        [2, 1, -2],
        [-1, -1, -2],
        [1, 1, 1]
    ]
    assert Solution().solve(matrix) == 8


def test_2():
    """WA: forgot to return -1 if answer is negative."""
    matrix = [[2], [-2]]
    assert Solution().solve(matrix) == -1


def test_3():
    """
    WA: misunderstood problem.  We are going from top-left to bottom-right,
    not anywhere on bottom row.
    """
    matrix = [[2, -2, 0]]
    assert Solution().solve(matrix) == 0


def test_4():
    """Still WA"""
    matrix = [[2, -1, 1]]
    assert Solution().solve(matrix) == -1
