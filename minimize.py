"""
binarysearch.com :: Minimize Absolute Difference of Three Numbers
https://binarysearch.com/room/Weekly-Contest-38-CNs3hGBp9j?questionsetIndex=2
"""
from math import inf
from bisect import bisect_left

class Solution:
    def solve(self, A, B, C):
        A.sort()
        B.sort()
        C.sort()

        soln = inf
        for j, b in enumerate(B):
            left = inf
            right = inf
            i = bisect_left(A, b)
            if i - 1 >= 0:
                left = min(left, abs(A[i-1] - b))
            if i < len(A):
                left = min(left, abs(A[i] - b))

            k = bisect_left(C, b)
            if k - 1 >= 0:
                right = min(right, abs(C[k-1] - b))
            if k < len(C):
                right = min(right, abs(C[k] - b))
            soln = min(soln, left + right)
        return soln


def test_1():
    a = [1, 8, 5]
    b = [2, 9]
    c = [5, 4]
    assert Solution().solve(a, b, c) == 3

def test_2():
    a = [2]
    b = [0, 2]
    c = [0]
    assert Solution().solve(a, b, c) == 2
