"""
binarysearch.com :: Swap Characters to Equalize Strings
jramaswami
"""


import collections


class Solution:

    def solve(self, S, T):
        freqs = collections.Counter(S)
        freqs.update(T)
        return all(freq % 2 == 0 for freq in freqs.values())


def test_1():
    s = "ab"
    t = "ba"
    assert Solution().solve(s, t) == True


def test_2():
    s = "aa"
    t = "aa"
    assert Solution().solve(s, t) == True


def test_3():
    s = "aaa"
    t = "bbb"
    assert Solution().solve(s, t) == False