"""
binarysearch.com :: Distance Pair
jramaswami
"""


import math


class Solution:

    def solve(self, nums):
        curr_max = -math.inf
        soln = -math.inf
        for i, n in enumerate(nums):
            curr_max -= 1
            soln = max(soln, n + curr_max)
            curr_max = max(curr_max, n)
        return soln


def test_1():
    nums = [5, 5, 1, 1, 1, 7]
    expected = 9
    assert Solution().solve(nums) == expected