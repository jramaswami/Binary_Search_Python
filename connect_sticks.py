"""
binarysearch.com :: Connect Sticks
jramaswami


Problem statement not really clear!!!
"""


class Solution:

    def solve(self, sticks):
        used = [False for _ in sticks]

        def dfs(a, b):
            result = 0
            for i, (x, y) in enumerate(sticks):
                if not used[i]:
                    used[i] = True
                    if a == x:
                        result = max(result, 1 + dfs(b, y))
                    if b == x:
                        result = max(result, 1 + dfs(a, y))
                    if a == y:
                        result = max(result, 1 + dfs(b, x))
                    if b == y:
                        result = max(result, 1 + dfs(a, x))
                    used[i] = False
            return result

        soln = 0
        for i, (a, b) in enumerate(sticks):
            used[i] = True
            soln = max(soln, 1 + dfs(a, b))
            used[i] = False
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
    expected = 3
    assert Solution().solve(sticks) == expected