"""
binarysearch.com :: Longest Palindrome From Concatenating Two Subsequences
jramaswami
"""


import functools


class Solution:

    def solve(self, a, b):
        t = a + b[::-1]

        @functools.cache
        def rec(i, j):
            if i == j:
                return 1
            if i + 1 == j:
                return 2 if t[i] == t[j] else 0
            if t[i] == t[j]:
                return 2 + rec(i+1, j-1)
            return max(rec(i+1, j), rec(i, j-1))

        return rec(0, len(t)-1)


def test_1():
    a = "abac"
    b = "accb"
    expected = 5
    assert Solution().solve(a, b) == expected


def test_2():
    "WA"
    a = "c"
    b = "aa"
    expected = 0
    assert Solution().solve(a, b) == expected