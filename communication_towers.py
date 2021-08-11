"""
binarysearch.com :: Communication Towers
jramaswami
"""

import collections


class UnionFind:

    def __init__(self):
        self.parent = dict()
        self.size = dict()
        self.count = 0

    def make_set(self, v):
        if v not in self.parent:
            self.parent[v] = v
            self.size[v] = v
            self.count += 1

    def find_set(self, v):
        if self.parent[v] == v:
            return v
        p = self.find_set(self.parent[v])
        self.parent[v] = p
        return p

    def union_set(self, a, b):
        a = self.find_set(a)
        b = self.find_set(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.parent[b] = a
            self.size[a] += self.size[b]
            self.count -= 1

    def __len__(self):
        return self.count


class Solution:
    def solve(self, matrix):
        uf = UnionFind()
        towers = []
        W = len(matrix[0])
        for r, row in enumerate(matrix):
            for c, tower in enumerate(row):
                if tower:
                    uf.make_set(r)
                    uf.make_set(W + c)
                    uf.union_set(r, W + c)
        return len(uf)


def test_1():
    matrix = [
        [1, 1, 0],
        [0, 0, 1],
        [0, 0, 1]
    ]
    assert Solution().solve(matrix) == 2


def test_2():
    matrix = [
        [1, 0, 0],
        [0, 0, 1],
        [0, 1, 0]
    ]
    assert Solution().solve(matrix) == 3


def test_3():
    """WA"""
    matrix = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [1, 1, 1, 0, 0, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    expected = 2
    assert Solution().solve(matrix) == expected
