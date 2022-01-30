"""
binarysearch.com :: Rotate List Left by K
jramaswami
"""


class Solution:
    def solve(self, nums, k):
        # Special case: empty array.
        if not nums:
            return nums
        # rotating k times brings us back to the same array.
        k = k % len(nums)
        if k:
            nums[:k] = reversed(nums[:k])
            nums[k:] = reversed(nums[k:])
            nums = nums[:][::-1]
        return nums
