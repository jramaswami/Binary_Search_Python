"""
binarysearch.com :: Equal Piles
jramaswami
"""


import collections


class Solution:

    def solve(self, nums):
        ctr = collections.Counter(nums)
        curr = 0
        soln = 0
        keys = list(sorted(ctr, reverse=True))
        for k in keys[:-1]:
            curr += ctr[k]
            soln += curr
        return soln


def test_1():
    nums = [4, 8, 2]
    expected = 3
    assert Solution().solve(nums) == expected


def test_2():
    nums = [4, 4, 4, 4]
    expected = 0
    assert Solution().solve(nums) == expected


def test_3():
    nums = []
    expected = 0
    assert Solution().solve(nums) == expected


def test_4():
    nums = [1, 2, 2, 2, 3, 4, 5]
    expected = 12
    assert Solution().solve(nums) == expected
