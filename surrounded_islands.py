"""
binarysearch.com :: Surrounded Islands
jramaswami
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


def bfs(r, c, matrix, visited):
    """BFS to determine if this island is surrounded by water."""
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    result = True
    while queue:
        r, c = queue.popleft()
        neighbors = vn_neighborhood(r, c, matrix)
        if len(neighbors) != 4:
            # This island is adjacent to a border, so is not surrounded by water.
            result = False
        for r0, c0 in neighbors:
            if matrix[r0][c0] == 1 and not visited[r0][c0]:
                queue.append((r0, c0))
                visited[r0][c0] = True
    return result


class Solution:
    def solve(self, matrix):
        soln = 0
        visited = [[False for _ in row] for row in matrix]
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == 1 and not visited[r][c]:
                    if bfs(r, c, matrix, visited):
                        soln += 1
        return soln


def test_1():
    matrix = [
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == 1


def test_2():
    matrix = [
        [1, 1, 1],
        [0, 1, 0],
        [1, 0, 0]
    ]
    assert Solution().solve(matrix) == 0


def test_3():
    matrix = [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ]
    assert Solution().solve(matrix) == 0


def test_4():
    matrix = [
        [1, 0, 1],
        [0, 1, 0],
        [0, 0, 0]
    ]
    assert Solution().solve(matrix) == 1
