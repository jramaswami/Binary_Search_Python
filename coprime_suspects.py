"""
binarysearch.com :: Coprime Suspects
jramaswami
"""


import math


class Solution:

    def solve(self, a, b):
        if math.gcd(a, b) > 1:
            return 0
        if math.gcd(a, b+1) > 1:
            return 1
        if math.gcd(a, b-1) > 1:
            return 1
        if math.gcd(a+1, b) > 1:
            return 1
        if math.gcd(a-1, b) > 1:
            return 1
        return 2


def test_1():
    a, b, expected = 5, 10, 0
    assert Solution().solve(a, b) == expected


def test_2():
    a, b, expected = 3, 7, 1
    assert Solution().solve(a, b) == expected


def test_3():
    a, b, expected = 7, 23, 2
    assert Solution().solve(a, b) == expected