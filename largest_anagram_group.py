"""
binarysearch.com :: Largest Anagram Group
jramaswami
"""


import collections


class Solution:

    def solve(self, words):
        return max(collections.Counter("".join(sorted(w)) for w in words).values())


def test_1():
    words = ["ab", "ba", "abc", "cba", "bca", "ddddd"]
    expected = 3
    assert Solution().solve(words) == expected
