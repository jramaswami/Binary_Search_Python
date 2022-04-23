"""
binarysearch.com :: Even Frequency
jramaswami
"""


class Solution:
    def solve(self, nums):
        nums.sort()
        i = 0
        j = 0
        while i < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if (j - i) % 2:
                return False
            i = j
        return True
