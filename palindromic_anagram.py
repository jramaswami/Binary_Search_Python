"""
binarysearch.com :: Palindromic Anagram
jramaswami

A palindrome has one of two forms:
(1) abccba
(2) abcdcba

In case:
(1) each letter has an even frequency.
(2) a single letter has an odd frequency and the rest have an even frequency.

A string will be a palindrome if it satifies either case (1) or case (2).
"""


import collections


class Solution:
    def solve(self, S):
        ctr = collections.Counter(S)
        odd_freqs = sum(v % 2 for v in ctr.values())
        return odd_freqs <= 1


def test_1():
    S = "carrace"
    assert Solution().solve(S) == True


def test_2():
    S = "carracer"
    assert Solution().solve(S) == False


def test_3():
    S = ""
    assert Solution().solve(S) == True
