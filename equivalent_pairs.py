"""
binarysearch.com :: Equivalent Pairs
jramaswami
"""


from collections import Counter
from math import factorial


def nCk(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


class Solution:
    def solve(self, nums):
        ctr = Counter(nums)
        soln = 0
        for num, freq in ctr.items():
            if freq > 1:
                soln += nCk(freq, 2)
        return soln


def test_1():
    nums = [3, 2, 3, 2, 2]
    assert Solution().solve(nums) == 4


def test_2():
    nums = [0]
    assert Solution().solve(nums) == 0