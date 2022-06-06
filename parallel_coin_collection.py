"""
binarysearch.com :: Parallel Coin Collection
jramaswami
"""


import math
import functools


class Solution:

    OFFSETS = (-1, 0, 1)

    def solve(self, matrix):
        def inbounds(c):
            return c >= 0 and c < len(matrix[r])

        def neighbors(c):
            for dc in Solution.OFFSETS:
                c0 = c + dc
                if inbounds(c0):
                    yield c0

        @functools.cache
        def dfs(r, xc, yc):
            if r == len(matrix) - 1:
                return 0

            result = -math.inf
            r0 = r + 1
            for xc0 in neighbors(xc):
                for yc0 in neighbors(yc):
                    px = matrix[r0][xc0]
                    matrix[r0][xc0] = 0
                    py = matrix[r0][yc0]
                    matrix[r0][yc0] = 0
                    result = max(result, px + py + dfs(r0, xc0, yc0))
                    matrix[r0][yc0] = py
                    matrix[r0][xc0] = px
            return result

        r, xc, yc = 0, 0, len(matrix[0]) - 1
        return dfs(r, xc, yc)


def test_1():
    matrix = [ [0, 0, 0, 0], [2, 1, 0, 1], [1, 0, 3, 3], [0, 2, 0, 0] ]
    expected = 10
    assert Solution().solve(matrix) == expected


def test_2():
    "WA"
    matrix = [[2,3,2]]
    expected = 4
    assert Solution().solve(matrix) == expected
