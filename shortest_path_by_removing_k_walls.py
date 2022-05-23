"""
binarysearch.com :: Shortest Path by Removing K Walls
jramaswami
"""


import collections
import math


class Solution:

    OFFSETS = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def solve(self, matrix, k):

        def inbounds(r, c):
            return (
                r >= 0 and c >= 0 and
                r < len(matrix) and c < len(matrix[r])
            )

        def neighbors(r, c):
            for dr, dc in Solution.OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        cleared_walls = [[math.inf for _ in row] for row in matrix]
        cleared_walls[0][0] = 0
        queue = collections.deque()
        queue.append((0, 0, 0))
        while queue:
            r, c, dist = queue.popleft()

            if r == len(matrix) - 1 and c == len(matrix[-1]) - 1:
                return dist

            cw = cleared_walls[r][c]
            for r0, c0 in neighbors(r, c):
                cw0 = cw + matrix[r0][c0]
                if cw0 <= k and cw0 < cleared_walls[r0][c0]:
                    cleared_walls[r0][c0] = cw0
                    queue.append((r0, c0, dist + 1))

        return -1


def test_1():
    matrix = [ [0, 0, 0], [1, 1, 1], [0, 0, 0] ]
    k = 1
    expected = 4
    result = Solution().solve(matrix, k)
    assert result == expected


def test_2():
    matrix = [ [1, 0, 0], [1, 1, 1], [0, 0, 0] ]
    k = 1
    expected = 4
    result = Solution().solve(matrix, k)
    assert result == expected
