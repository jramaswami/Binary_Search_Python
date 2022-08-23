"""
binarysearch.com :: Connect Sticks
jramaswami


Problem statement not really clear!!!
"""


import collections


Stick = collections.namedtuple('Stick', ['left', 'right', 'length'])


class Solution:

    def solve(self, sticks):
        visited = [[True for _ in range(7)] for _ in range(7)]
        for a, b in sticks:
            visited[a][b] = False

        def dfs(a, b):
            result = 0
            for x, y in sticks:
                if not visited[x][y]:
                    visited[x][y] = True
                    if a == x:
                        result = max(result, 1 + dfs(b, y))
                    if b == x:
                        result = max(result, 1 + dfs(a, y))
                    if a == y:
                        result = max(result, 1 + dfs(b, x))
                    if b == y:
                        result = max(result, 1 + dfs(a, x))
                    visited[x][y] = False
            return result

        soln = 0
        for a, b in sticks:
            visited[a][b] = True
            soln = max(soln, 1 + dfs(a, b))
            visited[a][b] = False
        return soln


def test_1():
    sticks = [ [1, 2], [1, 3], [2, 4], [6, 6] ]
    expected = 3
    assert Solution().solve(sticks) == expected


def test_2():
    sticks = []
    expected = 0
    assert Solution().solve(sticks) == expected


def test_3():
    sticks = [ [1, 2] ]
    expected = 1
    assert Solution().solve(sticks) == expected


def test_4():
    "WA"
    sticks = [[2,1],[4,1],[6,4]]
    expected = 3
    assert Solution().solve(sticks) == expected


def test_5():
    "WA"
    sticks = [[2, 1], [4, 1], [6, 4]]
    expected = 2
    assert Solution().solve(sticks) == expected