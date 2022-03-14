"""
binarysearch.com :: Ways to Sum Consecutive Numbers to N
jramaswami

Searching for the sequence on OEIS shows that it is A001227,
number of odd divisors of N.
"""


class Solution():
    def solve(self, N):
        # Boundary case:
        if N == 0:
            return 1

        soln = 0
        k = 1
        N0 = N
        while N0 % 2 == 0:
            N0 //= 2

        while k * k <= N0:
            if N0 % k == 0:
                if k * k == N0:
                    soln += 1
                else:
                    soln += 2
            k += 2
        return soln


def test_1():
    n = 9
    expected = 3
    assert Solution().solve(n) == expected


def test_2():
    n = 2147483647
    expected = 2
    assert Solution().solve(n) == expected
