"""
binarysearch.com :: Anagram Substrings
jramaswami
"""


import collections


class Solution:

    def solve(self, s0, s1):
        target = collections.Counter(s0)
        curr = collections.Counter(s1[:len(s0)])
        soln = 0
        for i, c in enumerate(s1[len(s0):], start=len(s0)):
            if target == curr:
                soln += 1
            r = s1[i - len(s0)]
            curr[c] += 1
            curr[r] -= 1
            if curr[r] == 0:
                del curr[r]
        if target == curr:
            soln += 1
        return soln


def test_1():
    s0 = "abc"
    s1 = "bcabxabc"
    expected = 3
    assert Solution().solve(s0, s1) == expected
