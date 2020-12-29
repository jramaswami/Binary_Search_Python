"""
binarysearch.com :: Complete an Arithmetic Sequence
"""
from collections import defaultdict


class Solution:
    def solve(self, nums):

        if len(nums) == 2:
            return nums[0] + ((nums[1] - nums[0]) // 2)

        if len(nums) == 3:
            # delta1 assumes the missing number is between nums[1] and nums[2]
            delta1 = nums[1] - nums[0]
            # delta2 assumes the missing number is between nums[0] and nums[1]
            delta2 = nums[2] - nums[1]
            if nums[1] + delta1 + delta1 == nums[2]:
                return nums[1] + delta1
            else:
                return nums[0] + delta2

        deltas = [b - a for a, b in zip(nums[:-1], nums[1:])]
        freqs = defaultdict(int)
        for d in deltas:
            freqs[d] += 1

        good_delta = 0
        bad_delta = 0
        for k, v in freqs.items():
            if v == 1:
                bad_delta = k
            else:
                good_delta = k

        if good_delta == 0:
            return nums[0]

        acc = nums[0]
        for n in nums[1:]:
            acc += good_delta
            if acc != n:
                return acc


def test_1():
    nums = [1, 3, 5, 9]
    assert Solution().solve(nums) == 7

def test_2():
    nums = [10, 7, 1, -2]
    assert Solution().solve(nums) == 4

def test_3():
    nums = [-10, -6, -2, 6, 10]
    assert Solution().solve(nums) == 2

def test_4():
    nums= [0, 0]
    assert Solution().solve(nums) == 0

def test_5():
    nums = [4, 12]
    assert Solution().solve(nums) == 8

def test_6():
    nums = [6, 2, 0]
    assert Solution().solve(nums) == 4

def test_7():
    nums = [0, 0, 0, 0]
    assert Solution().solve(nums) == 0
