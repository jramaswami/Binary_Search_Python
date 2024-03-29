"""
binarysearch.com :: Largest Island After Land Cell Addition
jramaswami
"""


class UnionFind:

    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [1 for _ in self.parent]

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def are_connected(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.size[a] += self.size[b]
            self.parent[b] = a


class Solution:

    OFFSETS = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def solve(self, matrix):

        def inbounds(r, c):
            return r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[r])

        def neighbors(r, c):
            for dr, dc in Solution.OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        def rc_to_index(r, c):
            return r * len(matrix[0]) + c

        uf = UnionFind(len(matrix) * len(matrix[0]))
        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                if matrix[r][c] == 1:
                    i = rc_to_index(r, c)
                    for r0, c0 in neighbors(r, c):
                        if matrix[r0][c0] == 1:
                            j = rc_to_index(r0, c0)
                            uf.union(i, j)

        soln = max(1, max(uf.size))
        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                if matrix[r][c] == 0:
                    connected_islands = set()
                    for r0, c0 in neighbors(r, c):
                        if matrix[r0][c0] == 1:
                            i = rc_to_index(r0, c0)
                            a = uf.find(i)
                            connected_islands.add(a)
                            soln = max(soln, 1 + sum(uf.size[k] for k in connected_islands))
        return soln



def test_1():
    matrix = [ [1, 1, 1], [0, 0, 0], [1, 1, 1] ]
    expected = 7
    assert Solution().solve(matrix) == expected


def test_2():
    matrix = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
    expected = 1
    assert Solution().solve(matrix) == expected


def rest_3():
    matrix = [ [1, 1, 1], [0, 0, 0], [0, 0, 0] ]
    expected = 4
    assert Solution().solve(matrix) == expected


def test_4():
    matrix = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]
    expected = 2
    assert Solution().solve(matrix) == expected


def test_5():
    "WA"
    matrix = [[1, 1]]
    expected = 2
    assert Solution().solve(matrix) == expected


def test_6():
    "RTE"
    matrix = [[1], [1]]
    expected = 2
    assert Solution().solve(matrix) == expected


def test_7():
    "WA"
    matrix = [[1,0,1],[0,1,0]]
    expected = 4
    assert Solution().solve(matrix) == expected
