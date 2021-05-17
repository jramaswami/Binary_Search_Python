"""
binarysearch.com :: Prime Factorization
jramaswami
"""
from math import sqrt


class Solution:
    def solve(self, n):
        # Sieve of Eratosthenes
        sqrt_n = 1 + int(sqrt(n))
        sieve = [True for _ in range(sqrt_n + 1)]
        sieve[0] = sieve[1] = False
        soln = []
        p = 2
        if sieve[p]:
            # If p is prime, then add it as many times as it divides n.
            while n % p == 0:
                n //= p
                soln.append(p)
            # Mark multiples of p as not prime.
            for k in range(p + p, sqrt_n + 1, p):
                sieve[k] = False

        for p in range(3, sqrt_n, 2):
            if sieve[p]:
                # If p is prime, then add it as many times as it divides n.
                while n % p == 0:
                    n //= p
                    soln.append(p)
                # Mark multiples of p as not prime.
                for k in range(p + p, sqrt_n + 1, p):
                    sieve[k] = False

        if n > 1:
            soln.append(n)
        return soln


#
# Testing
#
from random import randint
from functools import reduce
from operator import mul

def test_1():
    assert Solution().solve(12) == [2, 2, 3]


def test_2():
    """TLE"""
    assert Solution().solve(4423) == [4423]


def test_3():
    """TLE"""
    assert Solution().solve(6040) == [2, 2, 2, 5, 151]


def test_4():
    """TLE"""
    assert Solution().solve(81983948) == [2, 2, 20495987]


def test_random():
    for _ in range(100):
        n = randint(1, pow(10, 8))
        pf = Solution().solve(n)
        assert reduce(mul, pf, 1) == n

