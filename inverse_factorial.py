"""
binarysearch.com :: Inverse Factorial
jramaswami
"""
class Solution:
    def solve(self, a):
        soln = 0
        k = 1
        f = 1
        a0 = a
        while a0 > 1:
            f = f * k
            soln += 1
            a0 = a0 // k
            k += 1
        
        return -1 if (a != f) else soln


#
# Testing
#
import math


def test_1():
    assert Solution().solve(6) == 3

def test_2():
    assert Solution().solve(10) == -1

def test_3():
    assert Solution().solve(math.factorial(12)) == 12

def test_4():
    assert Solution().solve(math.factorial(12) + 4) == -1

