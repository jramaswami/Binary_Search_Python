"""
binarysearch.com :: The Meeting Place Sequel
jramaswami
"""


import collections
import itertools


class Solution:

    def solve(self, matrix):
        OFFSETS = ((1, 0), (-1, 0), (0, 1), (0, -1))
        WALL = 1
        PERSON = 2

        def inbounds(r, c):
            return r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[r])

        def neighbors(r, c):
            for dr, dc in OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0) and matrix[r0][c0] != WALL:
                    yield r0, c0

        visited = [[set() for _ in row] for row in matrix]
        counter = itertools.count(0)
        queue = collections.deque()
        for r, row in enumerate(matrix):
            for c, x in enumerate(row):
                if x == PERSON:
                    pid = next(counter)
                    queue.append((r, c, pid, 0))
                    visited[r][c].add(pid)
        people_count = len(queue)

        def multibfs():
            while queue:
                r, c, pid, t = queue.popleft()
                if len(visited[r][c]) == people_count:
                    return t
                for r0, c0 in neighbors(r, c):
                    if pid not in visited[r0][c0]:
                        visited[r0][c0].add(pid)
                        if len(visited[r0][c0]) == people_count:
                            return t + 1
                        queue.append((r0, c0, pid, t+1))
            return 0

        soln = multibfs()
        return soln



def test_1():
    matrix = [ [2, 0, 1, 0], [1, 0, 1, 2], [0, 0, 2, 2] ]
    expected = 3
    assert Solution().solve(matrix) == expected


def test_2():
    "WA"
    matrix = [[0]]
    expected = 0
    assert Solution().solve(matrix) == expected
