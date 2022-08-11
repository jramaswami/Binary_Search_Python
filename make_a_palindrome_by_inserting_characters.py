"""
binarysearch.com :: Make a Palindrome by Inserting Characters
jramaswami
"""


import functools


class Solution:

    def solve(self, s):
        t = s[::-1]

        @functools.cache
        def lcs(i, j):
            if i >= len(s):
                return 0
            if j >= len(t):
                return 0

            if s[i] == t[j]:
                return 1 + lcs(i+1, j+1)
            return max(lcs(i+1, j), lcs(i, j+1))

        return len(s) - lcs(0, 0)


def test_1():
    s = "radr"
    expected = 1
    assert Solution().solve(s) == expected
