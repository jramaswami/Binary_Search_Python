"""
binarysearch.com :: Shortest Bridge
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


def bfs(row_index, col_index, island_id, matrix, islands):
    queue = deque([(row_index, col_index)])
    islands[row_index][col_index] = island_id
    cells = [(island_id, row_index, col_index, 0)]
    while queue:
        row_index0, col_index0 = queue.popleft()
        for row_index1, col_index1 in vn_neighborhood(row_index0, col_index0, matrix):
            if matrix[row_index1][col_index1] == 1 and islands[row_index1][col_index1] == 0:
                queue.append((row_index1, col_index1))
                cells.append((island_id, row_index1, col_index1, 0))
                islands[row_index1][col_index1] = island_id
    return cells


class Solution:
    def solve(self, matrix):
        island_id = 0
        islands = [[0 for _ in row] for row in matrix]
        # This will be queue for bfs to find shortest bridge
        queue = deque()
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == 1 and islands[r][c] == 0:
                    island_id += 1
                    cells = bfs(r, c, island_id, matrix, islands)
                    queue.extend(cells)

        visited = [[[False for _ in row] for row in islands] for _ in range(island_id + 1)]

        while queue:
            island_id, r, c, d = queue.popleft()
            for r0, c0 in vn_neighborhood(r, c, islands):
                if visited[island_id][r0][c0]:
                    continue

                if islands[r0][c0] == 0:
                    queue.append((island_id, r0, c0, d + 1))
                elif islands[r0][c0] == island_id:
                    queue.append((island_id, r0, c0, d))
                else:
                    return d


def test_1():
    matrix = [
        [0, 1],
        [1, 0]
    ]
    assert Solution().solve(matrix) == 1


def test_2():
    matrix = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    assert Solution().solve(matrix) == 3


def test_3():
    matrix = [
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == 5


def test_4():
    matrix = [
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == 2


def test_5():
    matrix = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    assert Solution().solve(matrix) == 1