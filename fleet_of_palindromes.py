"""
binarysearch.com :: Fleet of Palindromes
jramaswami
"""


import collections


class Solution:
    def solve(self, s, k):
        freqs = collections.Counter(s)
        return len(s) >= k and sum(f % 2 for f in freqs.values()) <= k


def test_1():
    s = "racelevelcar"
    k = 2
    expected = True
    assert Solution().solve(s, k) == expected


def test_2():
    s = "dog"
    k = 2
    expected = False
    assert Solution().solve(s, k) == expected


def test_3():
    s = "dog"
    k = 3
    expected = True
    assert Solution().solve(s, k) == expected