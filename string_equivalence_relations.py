"""
binarysearch.com :: String Equivalence Relations
jramaswami
"""


from itertools import chain


class Solution:
    def solve(self, a, b, target):
        """
        Use a Disjoint Set augmented with the minimum character in the set
        to solve the problem.
        """
        parent = {}
        minlex = {}

        def make_set(ltr):
            parent[ltr] = ltr
            minlex[ltr] = ltr

        def find_set(ltr):
            if (ltr == parent[ltr]):
                return ltr
            return find_set(parent[ltr])

        def union_sets(s, t):
            s = find_set(s)
            t = find_set(t)
            if (s != t):
                parent[t] = s
                minlex[t] = minlex[s] = min(minlex[s], minlex[t])

        # Initialize DSU
        for c in chain(a, b, target):
            make_set(c)

        # Unite sets
        for s, t in zip(a, b):
            union_sets(s, t)

        return "".join(minlex[find_set(c)] for c in target)


def test_1():
    a = "axc"
    b = "xdz"
    target = "ddxz"
    expected = "aaac"
    assert Solution().solve(a, b, target) == expected


def test_2():
    a = "abc"
    b = "def"
    target = "xyz"
    expected = "xyz"
    assert Solution().solve(a, b, target) == expected


def test_3():
    """WA"""
    a = "cac"
    b = "bbc"
    target = "bb"
    expected = "aa"
    assert Solution().solve(a, b, target) == expected