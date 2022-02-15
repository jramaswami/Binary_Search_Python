"""
binarysearch.com :: Largest Equivalent Set of Pairs
jramaswami
"""


import math
import functools


class Solution:

    def solve(self, nums):

        LIMIT = sum(nums) / 2

        @functools.cache
        def solve0(index, ss, ps):
            # Shortcut: the positive sum cannot exceed half the sum of nums.
            if ps > LIMIT:
                return -math.inf

            if index >= len(nums):
                if ss == 0:
                    return ps
                else:
                    return -math.inf

            n = nums[index]
            return max(
                solve0(index + 1, ss + n, ps + n),
                solve0(index + 1, ss - n, ps),
                solve0(index + 1, ss, ps)
            )

        return solve0(0, 0, 0)


def test_1():
    nums = [1, 4, 3, 5]
    expected = 5
    assert Solution().solve(nums) == expected


def test_2():
    nums = list(range(1, 31))
    expected = 232
    assert Solution().solve(nums) == expected


def test_3():
    "Would be TLE"
    nums = [21, 64, 99, 36, 45, 40, 34, 78, 57, 19, 85, 92, 54, 94, 41, 59, 25, 70, 61, 69, 67, 41, 25, 29, 63, 38, 80, 87, 91, 63]
    expected = 854
    assert Solution().solve(nums) == expected
