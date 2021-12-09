"""
binarysearch.com :: Largest Sublist Sum
jramaswami
"""


import math


class Solution:

    def solve(self, nums):
        curr_max = -math.inf
        curr_sum = 0
        for n in nums:
            curr_max = max(curr_max, curr_sum + n)
            curr_sum = max(0, curr_sum + n)
        return curr_max


def test_1():
    nums = [10, -5, 12, -100, 3, -1, 20]
    expected = 22
    assert Solution().solve(nums) == expected


def test_2():
    nums = [-10, -5, -12, -100, -3, -1, -20]
    expected = -1
    assert Solution().solve(nums) == expected
