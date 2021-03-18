"""
binarysearch.com :: Group Integers
jramaswami
"""
from collections import Counter
from math import gcd
from functools import reduce


class Solution:
    def solve(self, nums):
        if nums == []:
            return False
        ctr = Counter(nums)
        freqs = list(ctr.values())
        g = reduce(gcd, freqs)
        return g >= 2


def test_1():
    nums = [2, 3, 5, 8, 3, 2, 5, 8]
    assert Solution().solve(nums) == True

def test_2():
    nums = [3, 0, 0, 3, 3, 3]
    assert Solution().solve(nums) == True

def test_3():
    nums = [3, 0, 0, 3, 3, 3, 0]
    assert Solution().solve(nums) == False

def test_4():
    nums = []
    assert Solution().solve(nums) == False
