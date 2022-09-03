"""
binarysearch.com :: Seat Arrangement
jramaswami
"""


import functools


class Solution:
    def solve(self, n, seats):

        @functools.cache
        def rec(i, x, p):
            if x == 0:
                return True

            if i >= len(seats):
                return False

            if seats[i] == 1:
                # This seat is occupied, we cannot sit here.
                return rec(i+1, x, True)
            elif p:
                # Previous seat is occupied, we cannot sit here.
                return rec(i+1, x, not p)
            elif i + 1 == len(seats) or seats[i+1] == 0:
                # Someone can sit here or not.
                return rec(i+1, x-1, True) or rec(i+1, x, False)
            else:
                # Next seat is occupied, we cannot sit here.
                return rec(i+1, x, False)

        return rec(0, n, False)