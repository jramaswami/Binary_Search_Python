"""
binarysearch.com :: Ambigram Detection
jramaswami
"""


import string


class UnionFind:

    def __init__(self):
        self.id = {c: c for c in string.ascii_lowercase}
        self.size = {c: 1 for c in string.ascii_lowercase}

    def find(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.id[b] = a
            self.size[a] += self.size[b]


class Solution:

    def solve(self, S, pairs):
        uf = UnionFind()
        for a, b in pairs:
            uf.union(a, b)

        i = 0
        j = len(S) - 1
        while i <= j:
            if uf.find(S[i]) != uf.find(S[j]):
                return False
            i += 1
            j -= 1
        return True


def test_1():
    s = "acba"
    pairs = [ ["b", "c"] ]
    assert Solution().solve(s, pairs) == True


def test_2():
    s = "zz"
    pairs = []
    assert Solution().solve(s, pairs) == True


def test_3():
    s = "ac"
    pairs = [ ["a", "b"], ["b", "c"] ]
    assert Solution().solve(s, pairs) == True
