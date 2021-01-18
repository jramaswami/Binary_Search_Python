"""
binarysearch.com :: Largest Gap
jramaswami
"""
class Solution:
    def solve(self, nums):
        nums.sort()
        return max(b - a for a, b in zip(nums[:-1], nums[1:]))

def test_1():
    nums = [4, 1, 2, 8, 9, 10]
    assert Solution().solve(nums) == 4
