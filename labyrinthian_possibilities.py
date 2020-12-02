"""
binarysearch.com :: Labyrinthian Possibilities
https://binarysearch.com/problems/Labyrinthian-Possibilities
"""
MOD = pow(10, 9) + 7


class Solution:
    def solve(self, matrix):
        dp = [[0 for _ in row] for row in matrix]
        if matrix[0][0] == 0:
            dp[0][0] = 1
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row + 1 < len(matrix) and matrix[row + 1][col] == 0:
                    dp[row + 1][col] = (dp[row + 1][col] + dp[row][col]) % MOD
                if col + 1 < len(matrix[0]) and matrix[row][col+1] == 0:
                    dp[row][col+1] = (dp[row][col+1] + dp[row][col]) % MOD
        return dp[-1][-1]


def test_1():
    matrix = [
        [0, 0, 1],
        [0, 0, 1],
        [1, 0, 0]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 2

def test_2():
    matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 6

def test_3():
    matrix = [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 0

def test_4():
    matrix = [
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 1

def test_5():
    matrix = [
        [0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 3
