"""
binarysearch.com :: Vertical Word Arrangement
jramaswami
"""


import itertools


class Solution:

    def solve(self, s):
        return [''.join(t).rstrip() for t in itertools.zip_longest(*s.split(), fillvalue=' ')]


def test_1():
    s = "abc def ghij"
    expected = ["adg", "beh", "cfi", "  j"]
    assert Solution().solve(s) == expected


def test_2():
    "WA"
    s = "ab c"
    expected = ["ac", "b"]
    assert Solution().solve(s) == expected
