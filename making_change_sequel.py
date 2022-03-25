"""
binarysearch.com :: Making Change Sequel
jramaswami
"""


import math
import functools
import sys


sys.setrecursionlimit(pow(10, 9))


class Solution:
    def solve(self, denominations, amount):

        @functools.cache
        def solve0(amt):
            if amt < 0:
                return math.inf
            if amt == 0:
                return 0
            return 1 + min(solve0(amt - d) for d in denominations)

        soln = solve0(amount)
        return -1 if soln == math.inf else soln


def test_1():
    denominations = [1, 5, 10, 25]
    amount = 60
    expected = 3
    assert Solution().solve(denominations, amount) == expected


def test_2():
    denominations = [3, 7, 10]
    amount = 8
    expected = -1
    assert Solution().solve(denominations, amount) == expected


def test_3():
    denominations = [1, 5, 10, 25]
    amount = 500000
    expected = 250
    assert Solution().solve(denominations, amount) == expected

