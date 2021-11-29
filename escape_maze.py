"""
binarysearch.com :: Escape Maze
jramaswami
"""


import math
import collections


class Solution:

    def solve(self, maze):

        OFFSETS = ((1, 0), (-1, 0), (0, 1), (-1, 0))

        def inbounds(r, c):
            return r >= 0 and c >= 0 and r < len(maze) and c < len(maze[r])

        def neighbors(r, c):
            for dr, dc in OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0


        dist = [[math.inf for _ in row] for row in maze]
        queue = collections.deque()
        if maze[0][0] == 0:
            dist[0][0] = 1
            queue.append((0, 0))
        while queue:
            r, c = queue.popleft()
            for r0, c0 in neighbors(r, c):
                if maze[r0][c0] == 0 and dist[r0][c0] > dist[r][c] + 1:
                    dist[r0][c0] = dist[r][c] + 1
                    queue.append((r0, c0))

        return -1 if dist[-1][-1] == math.inf else dist[-1][-1]


def test_1():
    matrix = [
        [0, 1, 0],
        [0, 0, 1],
        [0, 0, 0]
    ]
    expected = 5
    assert Solution().solve(matrix) == expected


def test_2():
    matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    expected = -1
    assert Solution().solve(matrix) == expected


def test_3():
    "WA"
    matrix = [[1]]
    expected = -1
    assert Solution().solve(matrix) == expected


def test_4():
    "WA"
    matrix = [ [0, 0, 0, 1], [1, 1, 0, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 0, 0] ]
    expected = 10
    assert Solution().solve(matrix) == expected
