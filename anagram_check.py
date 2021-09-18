"""
binarysearch.com :: Anagram Check
jramaswami
"""

from collections import Counter


class Solution:

    def solve(self, s0, s1):
        ctr0 = Counter(s0)
        ctr1 = Counter(s1)
        return ctr0 == ctr1


def test_1():
    s0 = "listen"
    s1 = "silent"
    assert Solution().solve(s0, s1) == True


def test_2():
    s0 = "bedroom"
    s1 = "bathroom"
    assert Solution().solve(s0, s1) == False
