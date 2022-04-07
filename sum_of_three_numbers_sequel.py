"""
binarysearch.com :: Sum of Three Numbers Sequel
jramaswami
"""


import math


class Solution:
    def solve(self, nums, target):
        nums.sort()
        soln = math.inf
        for i, _ in enumerate(nums[:-2]):
            j = i+1
            k = len(nums) - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                soln = min(abs(target - curr), soln)
                if curr <= target:
                    j += 1
                else:
                    k -= 1
        return soln


def test_1():
    nums = [2, 4, 25, 7]
    k = 15
    expected = 2
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [2, 4, 25, 7]
    k = 0
    expected = 13
    assert Solution().solve(nums, k) == expected


def test_3():
    "WA"
    nums = [1,-1,0,-2]
    k = 0
    expected = 0
    assert Solution().solve(nums, k) == expected


def test_4():
    "WA"
    nums = [1,-1,1,-2]
    k = 0
    expected = 0
    assert Solution().solve(nums, k) == expected


def test_5():
    "WA"
    nums = [1,-2,-2,1]
    k = -1
    expected = 1
    assert Solution().solve(nums, k) == expected
