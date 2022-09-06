"""
binarysearch.com :: Intersection of Two Maps
jramaswami
"""


class Solution:
    def solve(self, a, b):
        visited = [[False for _ in row] for row in a]

        def inbounds(r, c):
            return r >= 0 and r < len(a) and c >= 0 and c < len(a[r])

        OFFSETS = ((0, 1), (0, -1), (1, 0), (-1, 0))
        def neighbors(r, c):
            for dr, dc in OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        def same_island(r, c):
            visited[r][c] = True
            # Does this cell have the same neighhbors in b?
            result = a[r][c] == b[r][c]
            for r0, c0 in neighbors(r, c):
                if a[r0][c0] != b[r0][c0]:
                    result = False
            # Recurse
            for r0, c0 in neighbors(r, c):
                if a[r][c] == 1 and not visited[r0][c0]:
                    result = result and same_island(r0, c0)

            return result

        soln = 0
        for r, row in enumerate(a):
            for c, val in enumerate(row):
                if not visited[r][c] and val == 1:
                    if same_island(r, c):
                        soln += 1
        return soln


def test_1():
    a = [
        [1, 0, 1],
        [1, 0, 0],
        [1, 0, 0]
    ]
    b = [
        [1, 0, 0],
        [1, 0, 1],
        [1, 0, 0]
    ]
    expected = 1
    assert Solution().solve(a, b) == expected


def test_2():
    a = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    b = [
        [1, 1, 0],
        [1, 0, 1],
        [1, 0, 0]
    ]
    expected = 0
    assert Solution().solve(a, b) == expected


def test_3():
    "WA"
    a = [[1,1]]
    b = [[0,1]]
    expected = 0
    assert Solution().solve(a, b) == expected


def test_4():
    "WA"
    a = [[1]]
    b = [[0]]
    expected = 0
    assert Solution().solve(a, b) == expected


def test_5():
    "WA"
    a = [[1,0,1]]
    b = [[1,0,0]]
    expected = 1
    assert Solution().solve(a, b) == expected