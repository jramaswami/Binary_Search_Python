"""
binarysearch.com :: Conway's Game of Life
jramaswami
"""
def moore_neighborhood(row_index, col_index, matrix):
    """Return list of neighbors in Moore (8) neighborhood."""
    neighbors = []
    offsets =[(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for row_off, col_off in offsets:
        row_index0 = row_index + row_off
        col_index0 = col_index + col_off
        if (col_index0 >= 0 and col_index0 < len(matrix[0]) and row_index0 >= 0 and row_index0 < len(matrix)):
            neighbors.append((row_index0, col_index0))
    return neighbors


class Solution:
    def solve(self, matrix):
        next_state = [[0 for _ in row] for row in matrix]
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                living_neighbors = sum(matrix[r0][c0] for r0, c0 in moore_neighborhood(r, c, matrix))
                if val == 1 and (living_neighbors == 2 or living_neighbors == 3):
                    next_state[r][c] = 1
                if val == 0 and living_neighbors == 3:
                    next_state[r][c] = 1
        return next_state
                

def test_1():
    matrix = [
        [1, 1, 1, 0],
        [0, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 0, 1]
    ]
    expected = [
        [1, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 0],
        [1, 1, 1, 0]
    ]
    assert Solution().solve(matrix) == expected
