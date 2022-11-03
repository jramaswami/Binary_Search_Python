"""
binarysearch.com :: Longest Palindrome From Concatenating Two Subsequences
jramaswami
"""


import functools


class Solution:

    def solve(self, a, b):
        t = a + b

        @functools.cache
        def rec(i, j):
            "Return the longest palindromic substring between i and j."
            result = 0
            if i > j:
                result = 0
            elif i == j:
                result = 1
            elif i + 1 == j:
                if t[i] == t[j]:
                    result = 2
                else:
                    # Pick one or the other.
                    result = 1
            elif t[i] == t[j]:
                result = 2 + rec(i+1, j-1)
            else:
                result = max(rec(i+1, j), rec(i, j-1))
            return result

        soln = 0
        for i in range(len(a)):
            for j in range(len(a), len(a)+len(b)):
                # We must pick a start in a and an end in b.
                if t[i] == t[j]:
                    x = rec(i+1, j-1)
                    soln = max(soln , 2 + x)
        return soln


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


def test_3():
    "WA"
    a = "b"
    b = "bc"
    expected = 2
    assert Solution().solve(a, b) == expected


def test_4():
    "WA"
    a = "a"
    b = "aba"
    expected = 3
    assert Solution().solve(a, b) == expected