"""
binarysearch.com :: Minimum Tree From Leaves
jramaswami
"""


import math
import functools


class Solution:

    def solve(self, nums):

        @functools.cache
        def rec(left, right):
            # Base Case array of size 1.
            if left == right:
                return nums[left]

            # Compute
            result = math.inf
            for pivot in range(left, right):
                left_max = max(nums[left:pivot+1])
                right_max = max(nums[pivot+1:right+1])
                product = left_max * right_max
                result = min(
                    result,
                    rec(left, pivot) + rec(pivot+1,right) + product
                )
            return result

        return rec(0, len(nums)-1)


def test_1():
    nums = [2, 3, 5]
    expected = 31
    assert Solution().solve(nums) == expected