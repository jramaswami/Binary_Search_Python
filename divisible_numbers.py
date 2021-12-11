"""
binarysearch.com :: Divisible Numbers
jramaswami
"""


import math


class Solution:

    def solve(self, n, a, b, c):
        a, b, c = sorted((a, b, c))
        lo = 0
        hi = a * n
        l1 = a * b // math.gcd(a, b)
        l2 = a * c // math.gcd(a, c)
        l3 = b * c // math.gcd(b, c)
        l4 = a * b * c // math.gcd(a, b, c)
        soln = hi
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            # a + b + c - a&b - a&c - b&c + a&b&c
            ts = (
                mid // a +
                mid // b +
                mid // c -
                mid // l1 -
                mid // l2 -
                mid // l3 +
                mid // l4
            )
            if ts > n:
                hi = mid - 1
            elif ts < n:
                lo = mid + 1
            else:
                if mid % a == 0 or mid % b == 0 or mid % c == 0:
                    soln = min(soln, mid)
                hi = mid - 1

        return soln



def test_1():
    n = 8
    a = 2
    b = 5
    c = 7
    expected = 12
    assert Solution().solve(n, a, b, c) == expected
