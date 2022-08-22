"""
binarysearch.com :: Direct Closure
jramaswami
"""


class UnionFind:

    def __init__(self, N):
        self.parent = list(range(N))
        self.size = [0 for _ in self.parent]

    def find_set(self, u):
        if self.parent[u] == u:
            return u
        p = self.find_set(self.parent[u])
        self.parent[u] = p
        return p

    def union_set(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            if self.size[b] > self.size[a]:
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]

    def path_between(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a == b:
            return 1
        return 0


class Solution:
    def solve(self, graph):

        N = len(graph)
        uf = UnionFind(N)

        for u, _ in enumerate(graph):
            for v in graph[u]:
                uf.union_set(u, v)

        return [[uf.path_between(u, v) for v in range(N)] for u in range(N)]


def test_1():
    graph = [ [1], [0, 2], [1] ]
    expected = [ [1, 1, 1], [1, 1, 1], [1, 1, 1] ]
    assert Solution().solve(graph) == expected


def test_2():
    graph = [ [1], [0], [3], [2] ]
    expected = [ [1, 1, 0, 0], [1, 1, 0, 0], [0, 0, 1, 1], [0, 0, 1, 1] ]
    assert Solution().solve(graph) == expected