"""
binarysearch.com :: Intersection of Two Maps
jramaswami
"""


import collections


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

        def get_islands(grid):
            islands = []
            visited = [[False for _ in row] for row in grid]
            for r0, row in enumerate(grid):
                for c0, _ in enumerate(row):
                    if not visited[r0][c0] and grid[r0][c0] == 1:
                        island = []
                        queue = collections.deque()
                        queue.append((r0, c0))
                        visited[r0][c0] = True
                        while queue:
                            r1, c1 = queue.popleft()
                            island.append((r1, c1))
                            for r2, c2 in neighbors(r1, c1):
                                if not visited[r2][c2] and grid[r2][c2] == 1:
                                    visited[r2][c2] = True
                                    queue.append((r2, c2))
                        islands.append(tuple(sorted(island)))
            return islands

        soln = 0
        for a_island in get_islands(a):
            for b_island in get_islands(b):
                if a_island == b_island:
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

def test_5():
    "WA"
    a = [[1,0,1]]
    b = [[1,0,0]]
    expected = 1
    assert Solution().solve(a, b) == expected


def test_6():
    "WA"
    a = [[0,1,1]]
    b = [[1,1,1]]
    expected = 0
    assert Solution().solve(a, b) == expected