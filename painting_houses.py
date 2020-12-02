"""
binarysearch.com :: Painting Houses
https://binarysearch.com/problems/Painting-Houses
"""
from math import inf


class Solution:
    def solve(self, matrix):
        dp = [[inf for _ in row] for row in matrix]
        dp[0] = list(matrix[0])
        for i in range(len(matrix)-1):
            for j in range(len(matrix[i])):
                for k in range(len(matrix[i])):
                    if j == k:
                        continue
                    dp[i+1][k] = min(dp[i+1][k], dp[i][j] + matrix[i+1][k])

        for row in dp:
            print(row)
        return min(dp[-1])


def test_1():
    matrix = [
        [5, 3, 4],
        [2, 1, 6],
        [2, 3, 4],
        [4, 3, 3]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 10

def test_2():
    matrix = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 5

def test_3():
    matrix = [
        [1, 5, 1],
        [1, 5, 1],
        [1, 5, 1],
        [1, 5, 1],
        [1, 5, 1]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 5

def test_4():
    matrix = [
        [1, 2, 3],
        [4, 1, 8],
        [2, 3, 4],
        [3, 3, 1],
        [4, 2, 3]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 7
