"""
binarysearch.com :: Number of Palindromic Substrings
jramaswami
"""


import functools
import sys


sys.setrecursionlimit(pow(10, 9))


class Solution:

    def solve(self, S):

        @functools.cache
        def is_palindrome(left, right):
            # Base case.
            if left >= right:
                return True
            if S[left] == S[right]:
                return is_palindrome(left+1, right-1)
            return False

        soln = 0
        for left in range(len(S)):
            for right in range(len(S) - 1, left - 1, -1):
                if is_palindrome(left, right):
                    soln += 1
        return soln


def test_1():
    s = "tacocat"
    expected = 10
    assert Solution().solve(s) == expected


def test_2():
    s = ""
    expected = 0
    assert Solution().solve(s) == expected


def test_3():
    s = "a" * 1000
    expected = 500500
    assert Solution().solve(s) == expected
