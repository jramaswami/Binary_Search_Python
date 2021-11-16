"""
binarysearch.com :: Number of Hops
jramaswami
"""


import math
import functools


class Solution:
    def solve(self, nums):

        @functools.cache
        def solve0(i):
            if i >= len(nums) - 1:
                return 0
            if nums[i]:
                return 1 + min(solve0(i+k) for k in range(1, nums[i]+1))
            return math.inf

        return solve0(0)


def test_1():
    nums = [3, 3, 2, 0, 1]
    expected = 2
    assert Solution().solve(nums) == expected