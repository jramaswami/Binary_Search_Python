"""
binarysearch.com :: Bomber Man Sequel
jramaswami
"""


EMPTY = 0
WALL = 1
ENEMY = 2


class Solution:

    def solve(self, matrix):
        # Corner case: empty matrix.
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        soln = 0
        dp = [[1 if v == ENEMY else 0 for v in row] for row in matrix]

        # Left to right
        for r, row in enumerate(matrix):
            curr_enemies = 0
            for c, val in enumerate(row):
                if val == WALL:
                    curr_enemies = 0
                else:
                    dp[r][c] += curr_enemies
                    if val == ENEMY:
                        curr_enemies += 1

        # Right to left
        for dr, row in enumerate(matrix):
            curr_enemies = 0
            r = len(matrix) - 1 - dr
            for dc, _ in enumerate(row):
                c = len(row) - 1 - dc
                val = matrix[r][c]
                if val == WALL:
                    curr_enemies = 0
                else:
                    dp[r][c] += curr_enemies
                    if val == ENEMY:
                        curr_enemies += 1

        # Up to down
        for c, _ in enumerate(matrix[0]):
            curr_enemies = 0
            for r, _ in enumerate(matrix):
                val = matrix[r][c]
                if val == WALL:
                    curr_enemies = 0
                else:
                    dp[r][c] += curr_enemies
                    if val == ENEMY:
                        curr_enemies += 1

        # Down to up
        for dc, _ in enumerate(matrix[0]):
            curr_enemies = 0
            c = len(matrix[0]) - 1 - dc
            for dr, _ in enumerate(matrix):
                r = len(matrix) - 1 - dr
                val = matrix[r][c]
                if val == WALL:
                    curr_enemies = 0
                else:
                    dp[r][c] += curr_enemies
                    if val == ENEMY:
                        curr_enemies += 1

                if val == EMPTY:
                    # You can only place a bomb in an empty cell.
                    soln = max(soln, dp[r][c])

        return soln



def test_1():
    matrix = [
        [0, 2, 2, 0],
        [0, 2, 0, 2],
        [0, 1, 1, 0],
        [0, 0, 2, 0]
    ]
    expected = 3
    assert Solution().solve(matrix) == expected


def test_2():
    matrix = [[2, 2, 0, 1, 0], [2, 2, 0, 0, 0], [2, 1, 2, 0, 2], [0, 0, 0, 0, 0], [1, 0, 0, 0, 1]]
    expected = 3
    assert Solution().solve(matrix) == expected


def test_3():
    matrix = []
    expected = 0
    assert Solution().solve(matrix) == expected


def test_4():
    matrix = [[2, 2, 0, 1, 0]]
    expected = 2
    assert Solution().solve(matrix) == expected


def test_5():
    matrix = [[2, 2, 1, 1, 0]]
    expected = 0
    assert Solution().solve(matrix) == expected


def test_6():
    matrix = [[2], [2], [0], [1], [0]]
    expected = 2
    assert Solution().solve(matrix) == expected


def test_7():
    matrix = [[2], [2], [1], [1], [0]]
    expected = 0
    assert Solution().solve(matrix) == expected
