"""
Binary Search :: Weekly Contest 31 :: Walled Off
"""
from collections import deque
from math import inf


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


def moore_neighborhood(row_index, col_index, matrix):
    """Return list of neighbors in Moore (8) neighborhood."""
    neighbors = []
    offsets =[(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1)]
    for row_off, col_off in offsets:
        row_index0 = row_index + row_off
        col_index0 = col_index + col_off
        if (col_index0 >= 0 and col_index0 < len(matrix[0]) and row_index0 >= 0 and row_index0 < len(matrix)):
            neighbors.append((row_index0, col_index0))
    return neighbors


def wall_to_wall(init_row_index, init_col_index, matrix):
    """BFS to get distance from initial point to every wall."""
    # If row index == 0 then we are looking to see if we get to the bottom
    # or the left edges with only 1 added cell.
    dist = [[inf for _ in row] for row in matrix]
    queue = deque([(init_row_index, init_col_index)])
    if matrix[init_row_index][init_col_index] == 1:
        dist[init_row_index][init_col_index] = 0
    else:
        dist[init_row_index][init_col_index] = 1
    soln = inf
    while queue:
        row_index, col_index = queue.popleft()

        # Bottom to right
        if init_row_index == len(matrix) - 1 and col_index == len(matrix[0]) - 1:
            soln = min(soln, dist[row_index][col_index])
        # Bottom to top
        if init_row_index == len(matrix) - 1 and row_index == 0:
            soln = min(soln, dist[row_index][col_index])
        # Left to top
        if init_col_index == 0 and row_index == 0:
            soln = min(soln, dist[row_index][col_index])
        # Left to right
        if init_col_index == 0 and col_index == len(matrix[0]) - 1:
            soln = min(soln, dist[row_index][col_index])

        for row_index0, col_index0 in moore_neighborhood(row_index, col_index, matrix):
            # Do not consider source and sink.
            if row_index0 == 0 and col_index0 == 0:
                pass
            elif row_index0 == len(matrix) - 1 and col_index0 == len(matrix[0]) - 1:
                pass
            elif matrix[row_index0][col_index0] == 1 and dist[row_index0][col_index0] > dist[row_index][col_index]:
                dist[row_index0][col_index0] = dist[row_index][col_index]
                if dist[row_index0][col_index0] <= 2:
                    queue.append((row_index0, col_index0))
            elif matrix[row_index0][col_index0] == 0 and dist[row_index0][col_index0] > dist[row_index][col_index] + 1:
                dist[row_index0][col_index0] = dist[row_index][col_index] + 1
                if dist[row_index0][col_index0] <= 2:
                    queue.append((row_index0, col_index0))

    return soln

def source_to_sink(matrix):
    """See if you can go from top left to bottom right."""
    visited = [[False for _ in row] for row in matrix]
    visited[0][0] = True
    queue = deque()
    queue.append((0, 0))
    while queue:
        row_index, col_index = queue.popleft()
        for row_index0, col_index0 in vn_neighborhood(row_index, col_index, matrix):
            if matrix[row_index0][col_index0] == 1:
                continue
            if not visited[row_index0][col_index0]:
                queue.append((row_index0, col_index0))
                visited[row_index0][col_index0] = True
    return visited[-1][-1]


class Solution:
    def solve(self, matrix):
        soln = 2
        if not source_to_sink(matrix):
            return 0

        # Bottom row
        for init_col_index in range(0, len(matrix[0]) - 1):
            soln = min(soln, wall_to_wall(len(matrix) - 1, init_col_index, matrix))
            if soln == 1:
                return 1
        # Left col
        for init_row_index in range(1, len(matrix)):
            soln = min(soln, wall_to_wall(init_row_index, 0, matrix))
            if soln == 1:
                return 1
        return soln


def test_1():
    solver = Solution()
    matrix = [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
    assert solver.solve(matrix) == 1

def test_2():
    solver = Solution()
    matrix = [
        [0, 1],
        [0, 0]
    ]
    assert solver.solve(matrix) == 1

def test_3():
    solver = Solution()
    matrix = [
        [0, 1],
        [1, 0]
    ]
    assert solver.solve(matrix) == 0

def test_4():
    solver = Solution()
    matrix = [
        [0, 0, 0],
        [1, 0, 0],
        [0, 0, 0]
    ]
    assert solver.solve(matrix) == 1

def test_5():
    solver = Solution()
    matrix = [
        [0, 0, 1],
        [0, 0, 0],
        [1, 0, 0]
    ]
    assert solver.solve(matrix) == 1

def test_6():
    solver = Solution()
    matrix = [
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [0, 1, 0, 0]
    ]
    assert solver.solve(matrix) == 1

def test_6():
    solver = Solution()
    matrix = [
        [0, 0, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]
    assert solver.solve(matrix) == 1

def test_7():
    solver = Solution()
    matrix = [
        [0, 0],
        [0, 0],
        [0, 0]
    ]
    assert solver.solve(matrix) == 2

def test_8():
    solver = Solution()
    matrix = [
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert solver.solve(matrix) == 2

def test_9():
    solver = Solution()
    matrix = [
        [0, 1, 0],
        [0, 1, 0]
    ]
    assert solver.solve(matrix) == 0

def test_9():
    solver = Solution()
    matrix = [
        [0, 0, 0],
        [0, 1, 1],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert solver.solve(matrix) == 1

def test_10():
    matrix = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 2

def test_11():
    matrix = [
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0]
    ]
    solver = Solution()
    assert solver.solve(matrix) == 1
