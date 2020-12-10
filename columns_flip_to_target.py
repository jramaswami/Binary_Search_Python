"""
binarysearch.io :: Columns Flip to Target
https://binarysearch.io/problems/Column-Flips-to-Target
"""

class Solution:
    def solve(self, matrix, target):
        """Solve puzzle."""
        soln = 0
        matrix.sort()
        target.sort()
        col = 0
        while col < len(matrix[0]):
            if any(matrix[row][col] != target[row][col] for row, _ in enumerate(matrix)):
                soln += 1
                for row, _ in enumerate(matrix):
                    matrix[row][col] = 1 if matrix[row][col] == 0 else 0
                matrix.sort()
                if any(matrix[row][col] != target[row][col] for row, _ in enumerate(matrix)):
                    return -1
            col += 1
        return soln

def test1():
    matrix = [[0, 0], [1, 0], [1, 1]]
    target = [[0, 1], [1, 0], [1, 1]]
    solver = Solution()
    assert solver.solve(matrix, target) == 1

def test2():
    matrix = [[1, 1]]
    target = [[1, 0]]
    solver = Solution()
    assert solver.solve(matrix, target) == 1

def test3():
    matrix = [[0, 0]]
    target = [[1, 0]]
    solver = Solution()
    assert solver.solve(matrix, target) == 1