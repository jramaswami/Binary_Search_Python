"""
binarysearch.com :: Swap Consecutive Index Pairs
jramaswami
"""

class Solution:
    def solve(self, nums):
        for i in range(0, len(nums) - 2, 4):
            nums[i], nums[i+2] = nums[i+2], nums[i]
        for i in range(1, len(nums) - 2, 4):
            nums[i], nums[i+2] = nums[i+2], nums[i]
        return nums


def test_1():
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    expected = [2, 3, 0, 1, 6, 7, 4, 5, 8]
    assert Solution().solve(nums) == expected


def test_2():
    nums = []
    expected = []
    assert Solution().solve(nums) == expected
