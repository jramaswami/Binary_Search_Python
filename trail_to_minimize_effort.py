"""
binarysearch.com :: Trail to Minimize Effort
jramaswami
"""

import heapq
from collections import defaultdict, namedtuple
from math import inf


class Solution:
    def solve(self, matrix):

        def inbounds(r, c):
            """Return True if (r, c) is inside the matrix."""
            return r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[r])

        def neighbors(r, c):
            """Return the 4 neighbors of (r, c)."""
            offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in offsets:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield (r0, c0)

        def cost(r, c, r0, c0):
            """Return cost to go from (r, c) to (r0, c0)."""
            return abs(matrix[r][c] - matrix[r0][c0])

        #Dijkstra's algorithm to find shortest path.
        dist = defaultdict(lambda: inf)
        dist[(0, 0)] = 0
        # Q --> (dist, row, col)
        Q = [(0, 0, 0)]

        while Q:
            d, r, c = heapq.heappop(Q)

            if d > dist[(r, c)]:
                continue

            if r == len(matrix) - 1 and c == len(matrix[r]) - 1:
                return d

            for r0, c0 in neighbors(r, c):
                # dist of the path is the largest cost in the path.
                d0 = max(d, cost(r, c, r0, c0))
                if d0 < dist[(r0, c0)]:
                    dist[(r0, c0)] = d0
                    heapq.heappush(Q, (d0, r0, c0))


def test_1():
    matrix = [
        [1, 5, 3],
        [2, 4, 3],
        [3, 5, 3]
    ]
    expected = 2
    assert Solution().solve(matrix) == expected
