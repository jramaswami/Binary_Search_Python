"""
binarysearch.com :: Largest Island Area
"""
from collections import deque


def vn_neighborhood(row_index, col_index, matrix):
    """Return list of neighbors in von Neumann (4) neighborhood."""
    neighbors = []
    offsets =[(1, 0), (-1, 0), (0, 1), (0, -1)]
    for row_off, col_off in offsets:
        row_index0 = row_index + row_off
        col_index0 = col_index + col_off
        if (col_index0 >= 0 and col_index0 < len(matrix[0]) and row_index0 >= 0 and row_index0 < len(matrix)):
            neighbors.append((row_index0, col_index0))
    return neighbors


def bfs(row_index, col_index, matrix, visited):
    soln = 0
    queue = deque([(row_index, col_index)])
    visited[row_index][col_index] = True
    while queue:
        row_index0, col_index0 = queue.popleft()
        soln += 1
        for row_index1, col_index1 in vn_neighborhood(row_index0, col_index0, matrix):
            if matrix[row_index1][col_index1] == 1 and not visited[row_index1][col_index1]:
                queue.append((row_index1, col_index1))
                visited[row_index1][col_index1] = True
    return soln


class Solution:
    def solve(self, matrix):
        soln = 0
        visited = [[False for _ in row] for row in matrix]
        for row_index, row in enumerate(matrix):
            for col_index, val in enumerate(row):
                if matrix[row_index][col_index] == 1 and not visited[row_index][col_index]:
                    soln = max(soln, bfs(row_index, col_index, matrix, visited))
        return soln


def test_1():
    matrix = [
        [0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == 7
