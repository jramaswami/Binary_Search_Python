"""
Binary Search :: Weekly Contest 31 :: Peak Heights 
"""
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
        queue = []
        visited = [[False for _ in row] for row in matrix]
        for row_index, row in enumerate(matrix):
            for col_index, val in enumerate(row):
                if val == 0:
                    queue.append((row_index, col_index))
                    visited[row_index][col_index] = True

        new_queue = []
        while queue:
            for row_index, col_index in queue:
                for row_index0, col_index0 in vn_neighborhood(row_index, col_index, matrix):
                    if not visited[row_index0][col_index0]:
                        matrix[row_index0][col_index0] = matrix[row_index][col_index] + 1
                        visited[row_index0][col_index0] = True
                        new_queue.append((row_index0, col_index0))
            queue, new_queue = new_queue, []

        return matrix


def test_1():
    solver = Solution()
    matrix = [[0, 1, 0], [1, 1, 1], [1, 1, 1]]
    assert solver.solve(matrix) == [[0, 1, 0], [1, 2, 1], [2, 3, 2]]
