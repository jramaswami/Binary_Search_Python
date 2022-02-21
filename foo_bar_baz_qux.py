"""
binarysearch.com :: Foo Bar Qaz Qux
jramaswami

REF: https://www.geeksforgeeks.org/find-minimum-elements-considering-possible-transformations/
"""


import collections


class Solution:

    def solve(self, quxes):
        colors = 'RGB'
        freqs = collections.Counter(quxes)
        if any(freqs[c] == len(quxes) for c in colors):
            return len(quxes)
        elif all(freqs[c] % 2 == 0 for c in colors):
            return 2
        elif all(freqs[c] % 2 == 1 for c in colors):
            return 2
        return 1


def test_1():
    quxes = ["R", "G", "B", "G", "B"]
    expected = 1
    assert Solution().solve(quxes) == expected


def test_2():
    quxes = []
    expected = 0
    assert Solution().solve(quxes) == expected

def test_3():
    quxes = ["R", "R", "R","G"]
    expected = 1
    assert Solution().solve(quxes) == expected
