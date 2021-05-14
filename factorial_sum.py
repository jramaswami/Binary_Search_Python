"""
binarysearch.com :: Factorial Sum
jramaswami
"""
from math import factorial
from itertools import combinations, chain


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


class Solution:
    def __init__(self):
        # 13! > 2^31
        factorials = [factorial(n) for n in range(1, 13)]
        self.factorial_sums = set(sum(p) for p in powerset(factorials))
        
    def solve(self, n):
        return n in self.factorial_sums


def test_1():
    assert Solution().solve(31) == True


def test_2():
    assert Solution().solve(4) == False


def test_3():
    assert Solution().solve(6) == True


def test_4():
    assert Solution().solve(29) == False
