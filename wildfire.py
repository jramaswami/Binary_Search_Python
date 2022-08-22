"""
binarysearch.com :: Wildfire
jramaswami
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
        trees_not_on_fire = 0
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == 2:
                    queue.append((r, c))
                elif val == 1:
                    trees_not_on_fire += 1

        # BFS to count the number of days.
        days = 0
        new_queue = []
        while queue and trees_not_on_fire:
            days += 1
            for r, c in queue:
                for r0, c0 in vn_neighborhood(r, c, matrix):
                    if matrix[r0][c0] == 1:
                        # This tree is now on fire.
                        matrix[r0][c0] = 2
                        trees_not_on_fire -= 1
                        new_queue.append((r0, c0))
            queue, new_queue = new_queue, []

        # Did all the trees catch fire?
        if trees_not_on_fire:
            return -1
        else:
            return days


def test_1():
    matrix = [
        [1, 1, 1],
        [1, 2, 1],
        [1, 1, 1]
    ]
    assert Solution().solve(matrix) == 2


def test_2():
    matrix = [
        [1, 1, 1],
        [0, 0, 0],
        [1, 2, 1]
    ]
    assert Solution().solve(matrix) == -1