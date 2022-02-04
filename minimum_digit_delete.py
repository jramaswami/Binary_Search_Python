"""
binarysearch.com :: Minimum Digit Delete
jramaswami
"""


import math
import functools


class Solution:

    def solve(self, a, b):
        digits_a = [int(c) for c in a]
        digits_b = [int(c) for c in b]

        @functools.cache
        def solve0(i, j):
            "Return the maximum value common subtring."
            soln = 0
            if i < len(digits_a):
                soln = max(soln, solve0(i + 1, j))
            if j < len(digits_b):
                soln = max(soln, solve0(i, j + 1))
            if i < len(digits_a) and j < len(digits_b) and digits_a[i] == digits_b[j]:
                # If the digits are the same, remove them and count them toward
                # the total.
                soln = max(soln, digits_a[i] + solve0(i + 1, j + 1))
            return soln

        # Solution is total value of both strings - the maximum value common
        # substring (twice).
        return sum(digits_a) + sum(digits_b) - (2 * solve0(0, 0))


def test_1():
    a = "01291"
    b = "191"
    expected = 2
    assert Solution().solve(a, b) == expected


def test_2():
    a = "111"
    b = "222"
    expected = 9
    assert Solution().solve(a, b) == expected
