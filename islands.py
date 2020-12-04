"""
binarysearch.com :: Number of Islands
https://binarysearch.com/problems/Number-of-Islands
"""
from collections import deque

def adjacent_land(row, col, matrix):
    """Return any of the four neighbors that are land."""
    offsets = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for row_off, col_off in offsets:
        row0 = row + row_off
        col0 = col + col_off
        if col0 < 0 or col0 >= len(matrix[0]):
            continue
        if row0 < 0 or row0 >= len(matrix):
            continue
        if matrix[row0][col0] == 1:
            yield (row0, col0)

class Solution:
    def solve(self, matrix):
        visited = [[0 for _ in row] for row in matrix]
        soln = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 1 and visited[row][col] == 0:
                    visited[row][col] = 1
                    soln += 1
                    # BFS
                    queue = deque([(row, col)])
                    while queue:
                        row0, col0 = queue.popleft()
                        for row1, col1 in adjacent_land(row0, col0, matrix):
                            if not visited[row1][col1]:
                                visited[row1][col1] = 1
                                queue.append((row1, col1))
        return soln

def test_1():
    matrix = [
        [1, 1],
        [1, 0]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 1

def test_2():
    matrix = [
        [1, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 4

def test_3():
    matrix = [
        [0, 1],
        [1, 0]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 2