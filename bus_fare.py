"""
binarysearch.com :: Bus Fare
jramaswami
"""


import math
import functools


class Solution:

    def solve(self, days):

        @functools.cache
        def solve0(i, pass_until):
            # Base Case
            if i >= len(days):
                return 0

            return min(
                25 + solve0(i+1, days[i]+30),
                7 + solve0(i+1, days[i]+7),
                2 + solve0(i+1, days[i]+1),
                math.inf if pass_until <= days[i] else solve0(i+1, pass_until)
            )

        return solve0(0, -1)



def test_1():
    days = [1, 3, 4, 5, 29]
    expected = 9
    assert Solution().solve(days) == expected


def test_2():
    days = [1]
    expected = 2
    assert Solution().solve(days) == expected


def test_3():
    days = []
    expected = 0
    assert Solution().solve(days) == expected
