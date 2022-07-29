"""
binarysearch.com :: K Unique String
jramaswami
"""


import collections


class Solution:

    def solve(self, s, k):
        ctr = collections.Counter(s)
        freqs = sorted((v, k) for k, v in ctr.items())
        return sum(v for v, _ in freqs[:-k])


def test_1():
    s = "daabbccaa"
    k = 3
    expected = 1
    assert Solution().solve(s, k) == expected


def test_2():
    s = "daabbccaad"
    k = 3
    expected = 2
    assert Solution().solve(s, k) == expected