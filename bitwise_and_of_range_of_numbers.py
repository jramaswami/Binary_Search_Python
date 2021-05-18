"""
binarysearch.com :: Bitwise AND of Range of Numbers
jramaswami
"""
class Solution:
    def solve(self, start, end):
        soln = 0

        # Scan from MSB -> LSB
        for bit in range(32, -1, -1):
            mask = 1 << bit
            
            start_set = start & mask
            end_set = end & mask

            # If both are set then set the bit in the soln.
            if start_set and end_set:
                soln |= mask
                continue

            # If both are not set it is ok.
            if not start_set and not end_set:
                continue

            # If one is and the other is not then stop.
            break

        return soln


#
# Testing
#
from functools import reduce
from operator import __and__
from random import randint

def test_1():
    start = 5
    end = 7
    assert Solution().solve(start, end) == 4


def test_2():
    start = 1
    end = 2147483648
    assert Solution().solve(start, end) == 0


def test_3():
    start = 5
    end = 19
    assert Solution().solve(start, end) == reduce(__and__, range(start, end), end)


def test_random():
    for _ in range(100):
        start = randint(0, 1000)
        end = randint(start + 1, 10000)
        assert Solution().solve(start, end) == reduce(__and__, range(start, end), end)

