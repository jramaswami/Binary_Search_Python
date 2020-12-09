"""
binarysearch.com :: Collecting Coins
https://binarysearch.com/problems/Collecting-Coins
"""
class Solution:
    def solve(self, matrix):
        dp = [[0 for _ in row] for row in matrix]
        dp[0][0] = matrix[0][0]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                # Down
                if i+1 < len(matrix):
                    dp[i+1][j] = max(dp[i+1][j], dp[i][j] + matrix[i+1][j])
                # Left
                if j+1 < len(matrix[i]):
                    dp[i][j+1] = max(dp[i][j+1], dp[i][j] + matrix[i][j+1])
        return dp[-1][-1]


def test_1():
    matrix = [
        [0, 3, 1, 1],
        [2, 0, 0, 4]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 9

def test_2():
    matrix = [
        [0, 3, 1, 1],
        [2, 0, 0, 4],
        [1, 5, 3, 1]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 12

def test_3():
    matrix = [
        [0, 2, 1],
        [2, 5, 0],
        [4, 1, 3]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 11
