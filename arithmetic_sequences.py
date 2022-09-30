"""
binarysearch.com :: Arithmetic Subsequences
jramaswami
"""


import collections
import math


class Solution:

    def solve(self, nums):
        def summation(n):
            return (n * (n + 1)) // 2
        soln = 0
        dp = [collections.defaultdict(list) for _ in nums]
        curr_delta = math.inf
        curr_length = 0
        for i, left in enumerate(nums[:-1]):
            right = nums[i+1]
            delta = right - left
            if curr_delta == delta:
                curr_length += 1
            else:
                # Previous sequence is has ended.  How many could we have.
                if curr_length >= 3:
                    soln += (summation(curr_length) - curr_length - (curr_length - 1))
                curr_length = 2
            curr_delta = delta
        # What is left at the end.
        if curr_length >= 3:
            soln += (summation(curr_length) - curr_length - (curr_length - 1))
        return soln


def test_1():
    nums =  [5, 7, 9, 11, 12, 13]
    assert Solution().solve(nums) == 4