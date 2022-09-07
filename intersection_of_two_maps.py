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

        # Mark the islands in a.
        a_islands = [[0 for _ in row] for row in a]
        def mark_island(r, c, curr_id):
            "DFS to mark island."
            a_islands[r][c] = curr_id
            for r0, c0 in neighbors(r, c):
                if a[r0][c0] == 1 and a_islands[r0][c0] == 0:
                    mark_island(r0, c0, curr_id)

        curr_id = 0
        for r, row in enumerate(a):
            for c, _ in enumerate(row):
                if a[r][c] == 1 and a_islands[r][c] == 0:
                    curr_id += 1
                    mark_island(r, c, curr_id)

        # In order for the island to be the same, each neighbor must match.
        same_island = [True for _ in range(curr_id+1)]
        same_island[0] = False
        def same(r, c):
            return a[r][c] == b[r][c]

        def all_neighbors_match(r, c):
            return same(r, c) and all(same(r0, c0) for r0, c0 in neighbors(r, c))

        for r, row in enumerate(a):
            for c, _ in enumerate(row):
                if a_islands[r][c] != 0 and not all_neighbors_match(r, c):
                    same_island[a_islands[r][c]] = False
        return sum(same_island)


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