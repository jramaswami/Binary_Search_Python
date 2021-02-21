"""
binarysearch.com :: Enclosed Islands
jramaswami
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
        visited = [[False for _ in row] for row in matrix]
        queue = deque()
        queue.extend((0, i) for i, c in enumerate(matrix[0]) if c == 1)
        queue.extend((len(matrix) - 1, i) for i, c in enumerate(matrix[-1]) if c == 1)
        queue.extend((i, 0) for i, row in enumerate(matrix[1:-1], start=1) if row[0] == 1)
        queue.extend((i, len(row) - 1) for i, row in enumerate(matrix[1:-1], start=1) if row[-1] == 1)
        for r, c in queue:
            visited[r][c] = True
        while queue:
            r, c = queue.popleft()
            matrix[r][c] = 0
            for r0, c0 in adjacent_land(r, c, matrix):
                if not visited[r0][c0]:
                    queue.append((r0, c0))
                    visited[r0][c0] = True

        return sum(sum(row) for row in matrix)


def test_1():
    matrix = [
        [0, 0, 0, 1],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == 4

def test_2():
    matrix = [
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == 4

def test_3():
    matrix = [
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 1, 1],
        [0, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == 0

def test_4():
    matrix = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == 1
