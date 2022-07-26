"""
binarysearch.com :: Dominos
jramaswami


Three possible states:

 A   B   C
### ##  ###
### ### ###
### ### ##

(1) transition from A to B or C by adding one tile.
(2) transition from B or C to a by adding two tiles.

B & C are symmetrical.
"""

import functools


class Solution:

    MOD = pow(10, 9) + 7

    def solve(self, n):

        @functools.cache
        def A(x):
            if x == 0:
                return 1
            if x == 1:
                return 0
            return (A(x-2) + (2 * B(x-1))) % Solution.MOD

        @functools.cache
        def B(x):
            if x == 0:
                return 0
            if x == 1:
                return 1
            return (A(x-1) + B(x-2)) % Solution.MOD

        # There must be at least two tiles in order to cover properly.
        if n < 2:
            return 0
        # There is only three ways to cover 2x3:
        # -- || --
        # -- || ||
        # -- -- ||
        if n == 3:
            return 3

        return A(n)

def test_1():
    n = 2
    expected = 3
    assert Solution().solve(n) == expected


def test_2():
    n = 1
    expected = 0
    assert Solution().solve(n) == expected

def test_3():
    n = 8
    expected = 153
    assert Solution().solve(n) == expected


def test_4():
    n = 30
    expected = 299303201
    assert Solution().solve(n) == expected