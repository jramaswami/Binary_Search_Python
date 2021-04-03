"""
binarysearch.com :: Matrix Nearest Zero
jramaswami
"""
from math import inf
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


class Solution:
    def solve(self, matrix):
        dist = [[inf for _ in row] for row in matrix]
        queue = deque()
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == 0:
                    dist[r][c] = 0
                    queue.append((r, c))
        
        while queue:
            r, c = queue.popleft()
            for r0, c0 in vn_neighborhood(r, c, matrix):
                if dist[r][c] + 1 < dist[r0][c0]:
                    dist[r0][c0] = dist[r][c] + 1
                    queue.append((r0, c0))

        return dist


def test_1():
    matrix = [[1, 1, 1], [1, 0, 1], [0, 0, 0]]
    assert Solution().solve(matrix) == [[2, 1, 2], [1, 0, 1], [0, 0, 0]]
