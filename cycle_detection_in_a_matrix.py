"""
binarysearch.com :: Cycle Detection in a Matrix
jramaswami
"""
from collections import deque


def vn_neighborhood(r, c, matrix):
    """Return 4 neighbors of (r, c)."""
    offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighborhood = []
    for dr, dc in offsets:
        r0 = r + dr
        c0 = c + dc
        if r0 >= 0 and r0 < len(matrix) and c0 >= 0 and c0 < len(matrix[r]):
            neighborhood.append((r0, c0))
    return neighborhood


def bfs(init_row, init_col, matrix, visited, parent):
    """BFS to determine if there is a cycle."""
    comp_id = matrix[init_row][init_col]
    visited.add((init_row, init_col))
    queue = deque()
    queue.append((init_row, init_col))
    while queue:
        r, c = queue.popleft()
        for r0, c0 in vn_neighborhood(r, c, matrix):
            if matrix[r0][c0] == comp_id:
                if (r0, c0) not in visited:
                    visited.add((r0, c0))
                    queue.append((r0, c0))
                    parent[(r0, c0)] = (r, c)
                elif parent[(r, c)] != (r0, c0):
                    return True
    return False


class Solution:
    def solve(self, matrix):
        parent = dict()
        visited = set()

        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                if (r, c) not in visited:
                    if bfs(r, c, matrix, visited, parent):
                        return True
        return False


def test_1():
    matrix = [
        [2, 1, 1, 1],
        [2, 1, 0, 1],
        [2, 1, 1, 1]
    ]
    assert Solution().solve(matrix) == True


def test_2():
    matrix = [[0], [0], [0]]
    assert Solution().solve(matrix) == False