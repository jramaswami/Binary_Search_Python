"""
binarysearch.com :: Farthest Point From Water
jramaswami
"""


import math


class Solution:

    def solve(self, matrix):
        # Corner case
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return -1

        dist = [[math.inf for _ in row] for row in matrix]

        def inbounds(r, c):
            return r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[0])

        def neighbors(r, c):
            offsets = ((1, 0), (-1, 0), (0, 1), (0, -1))
            for dr, dc in offsets:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        def bfs(r, c, d):
            for r0, c0 in neighbors(r, c):
                if dist[r0][c0] > d + 1:
                    dist[r0][c0] = d + 1
                    bfs(r0, c0, d + 1)

        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if val == 0:
                    dist[r][c] = 0
                    bfs(r, c, 0)

        print(dist)
        soln = 0
        for r, row in enumerate(dist):
            for c, d in enumerate(row):
                soln = max(soln, d)

        if soln == 0:
            # All water
            return -1
        if soln == math.inf:
            # All land
            return -1
        return soln


def test_1():
    matrix = [ [1, 1, 0], [1, 1, 0], [0, 0, 1] ]
    expected = 2
    assert Solution().solve(matrix) == expected


def test_2():
    matrix = [ [1, 1], [1, 1] ]
    expected = -1
    assert Solution().solve(matrix) == expected


def test_3():
    matrix = [ [1, 1, 1, 1], [0, 1, 1, 1], [0, 0, 1, 0] ]
    expected = 3
    assert Solution().solve(matrix) == expected


def test_4():
    matrix = [[]]
    expected = -1
    assert Solution().solve(matrix) == expected


def test_5():
    """WA"""
    matrix = [[0,0,0],[0,0,0],[0,0,0]]
    expected = -1
    assert Solution().solve(matrix) == expected
