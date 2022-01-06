"""
binarysearch.com :: Nearest Bus Stop From a House
jramaswami
"""


import enum
import math
import collections


class CellType(enum.IntEnum):
    EMPTY = 0
    WALL = 1
    HOUSE = 2
    BUS_STOP = 3


class Solution:

    def solve(self, matrix):

        OFFSETS = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def inbounds(r, c):
            "Return True if matrix[r][c] is inside matrix."
            return r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[r])

        def neighbors(r, c):
            "Return the neighbors of matrix[r][c]"
            for dr, dc in OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        def navigable(r, c):
            "Return True if you can walk through matrix[r][c]."
            if matrix[r][c] == CellType.WALL or matrix[r][c] == CellType.HOUSE:
                return False
            return True

        # Gather bus stops.
        dist = [[math.inf for _ in row] for row in matrix]
        queue = collections.deque()
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == CellType.HOUSE:
                    queue.append((r, c))
                    dist[r][c] = 0

        # BFS
        while queue:
            r, c = queue.popleft()
            if matrix[r][c] == CellType.BUS_STOP:
                return matrix[r][c]
            for r0, c0 in neighbors(r, c):
                if navigable(r0, c0) and dist[r][c] + 1 < dist[r0][c0]:
                    dist[r0][c0] = dist[r][c] + 1
                    queue.append((r0, c0))
        return -1


def test_1():
    matrix = [
        [2, 1, 3, 0],
        [1, 1, 1, 1],
        [0, 3, 0, 0],
        [0, 0, 0, 2]
    ]
    assert Solution().solve(matrix) == 3


def test_2():
    "WA.  Endless loop because I didn't keep track of visited cells."
    matrix = [
        [0, 2, 0],
        [1, 2, 0],
        [3, 1, 0]
    ]
    assert Solution().solve(matrix) == -1



def test_3():
    "WA"
    matrix = [[2, 3]]
    assert Solution().solve(matrix) == 1
