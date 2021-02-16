"""
binarysearch.com :: Remove One Letter
jramaswami
"""
from collections import Counter
from string import ascii_lowercase


class Solution:
    def solve(self, s0, s1):
        """
        Given two strings s0 and s1, return whether you can obtain s1 by 
        removing 1 letter from s0.
        """
        ctr0 = Counter(s0)
        ctr1 = Counter(s1)
        delta = 0
        for c in ascii_lowercase:
            freq0 = ctr0.get(c, 0)
            freq1 = ctr1.get(c, 0)

            # We will remove a letter from s0 so there can be no letters
            # in s1 that have a greater frequency.
            if freq0 < freq1:
                return False

            delta += freq0 - freq1

        # There can be only one extra letter in s1.
        return delta == 1


def test_1():
    s0 = "hello"
    s1 = "hello"
    assert Solution().solve(s0, s1) == False


def test_2():
    s0 = "hello"
    s1 = "helo"
    assert Solution().solve(s0, s1) == True


def test_3():
    s0 = "hello"
    s1 = "heloz"
    assert Solution().solve(s0, s1) == False


def test_4():
    s0 = "hello"
    s1 = "hel"
    assert Solution().solve(s0, s1) == False


def test_5():
    s0 = "h"
    s1 = ""
    assert Solution().solve(s0, s1) == True

def test_6():
    s0 = "nnx"
    s1 = "xn"
    assert Solution().solve(s0, s1) == False
