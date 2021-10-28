"""
binarysearch.com :: Sum of Three Numbers
jramaswami
"""


import bisect


class Solution:
    def solve(self, nums, k):
        nums.sort()
        for p, a in enumerate(nums):
            for q, b in enumerate(nums[p+1:], start=p+1):
                delta = k - a - b
                r = bisect.bisect_left(nums, delta, q+1)
                if r != len(nums) and nums[r] == delta:
                    return True
        return False
