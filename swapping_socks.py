"""
binarysearch.com :: Swapping Socks
jramaswami

REF: https://www.youtube.com/watch?v=mJVQL-deD7A
"""


class UnionFind:

    def __init__(self, n):
        self.id = [i for i in range(n)]
        self.size = [1 for _ in self.id]
        self.count = n

    def find(self, a):
        if self.id[a] != a:
            p = self.id[a]
            self.id[a] = self.find(p)
        return self.id[a]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a != b:
            if self.size[a] < self.size[b]:
                a, b = b, a
            self.id[b] = a
            self.size[a] += self.size[b]
            self.count -= 1

    def __len__(self):
        return self.count


class Solution:

    def solve(self, row):
        couples = len(row) // 2
        uf = UnionFind(couples)
        for i in range(0, len(row), 2):
            a = row[i]
            b = row[i+1]
            couple_a = a // 2
            couple_b = b // 2
            uf.union(couple_a, couple_b)
        return couples - len(uf)


def test_1():
    row = [0, 4, 1, 3, 2, 5]
    expected = 2
    assert Solution().solve(row) == expected


def test_2():
    row = [1, 0, 3, 2]
    expected = 0
    assert Solution().solve(row) == expected


def test_3():
    "TLE"
    row = [45, 33, 36, 9, 34, 72, 17, 60, 89, 3, 6, 90, 32, 66, 44, 70, 26, 98, 68, 28, 81, 76, 74, 22, 65, 11, 51, 62, 59, 52, 20, 78, 94, 82, 79, 57, 42, 86, 91, 39, 87, 85, 29, 41, 71, 99, 35, 80, 25, 92, 38, 55, 0, 67, 47, 13, 23, 37, 2, 46, 56, 15, 54, 63, 97, 96, 31, 16, 8, 48, 61, 75, 73, 53, 40, 69, 27, 7, 84, 1, 49, 24, 58, 77, 4, 88, 14, 64, 12, 93, 83, 18, 21, 43, 5, 95, 50, 10, 19, 30]
    expected = 45
    assert Solution().solve(row) == expected
