"""
binarysearch.com :: Symmetric Blocks
jramaswami
"""


class Solution:
    def solve(self, nums):
        right_index = len(nums) - 1
        for left_index, _ in enumerate(nums):
            while nums[right_index] - 1 < left_index:
                right_index -= 1
            up_height = nums[left_index] - left_index
            rt_length = right_index - left_index + 1
            if up_height != rt_length:
                return False
        return True


def test_1():
    nums = [5, 3, 2, 1, 1]
    expected = True
    assert Solution().solve(nums) == expected
