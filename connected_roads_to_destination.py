"""
binarysearch.com :: Connected Road to Destination
jramaswami
"""


class UnionFind:

    def __init__(self):
        self.id = dict()
        self.size = dict()

    def add(self, x, y):
        if (x, y) not in self.id:
            self.id[(x, y)] = (x, y)
            self.size[(x, y)] = 1

    def find(self, u):
        p = self.id[u]
        if p != u:
            self.id[u] = self.find(self.find(p))
        return self.id[u]

    def union(self, u, v):
        if u not in self.id or v not in self.id:
            return
        u = self.find(u)
        v = self.find(v)
        if u != v:
            if self.size[u] < self.size[v]:
                u, v, = v, u
            self.id[v] = u
            self.size[u] += self.size[v]

    def is_connected(self, u, v):
        return self.find(u) == self.find(v)


class Solution:

    def solve(self, sx, sy, ex, ey, roads):
        # Boundary case: (sx, sy) and (ex, ey) are equal or adjacent.
        dist = pow(sx - ex, 2) + pow(sy - ey, 2)
        if dist <= 1:
            return 0

        uf = UnionFind()
        uf.add(sx, sy)
        uf.add(ex, ey)

        source = (sx, sy)
        dest = (ex, ey)
        offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        soln = 0
        for x, y in roads:
            uf.add(x, y)
            soln += 1
            for dx, dy in offsets:
                uf.union((x, y), (x+dx, y+dy))
            if uf.is_connected(source, dest):
                return soln

        return -1


def test_1():
    sx = 0
    sy = 0
    ex = 1
    ey = 2
    roads = [ [9, 9], [0, 1], [0, 2], [0, 3], [3, 3] ]
    expected = 3
    assert Solution().solve(sx, sy, ex, ey, roads) == expected


def test_2():
    sx = 1
    sy = 2
    ex = 1
    ey = 2
    roads = [ [9, 9], [0, 1], [0, 2], [0, 3], [3, 3] ]
    expected = 0
    assert Solution().solve(sx, sy, ex, ey, roads) == expected


def test_3():
    sx = 1
    sy = 2
    ex = 0
    ey = 2
    roads = [ [9, 9], [0, 1], [0, 2], [0, 3], [3, 3] ]
    expected = 0
    assert Solution().solve(sx, sy, ex, ey, roads) == expected

def test_3():
    sx = 1
    sy = 2
    ex = 5
    ey = 5
    roads = [ [9, 9], [0, 1], [0, 2], [0, 3], [3, 3] ]
    expected = -1
    assert Solution().solve(sx, sy, ex, ey, roads) == expected
