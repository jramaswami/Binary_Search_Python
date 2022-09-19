"""
binarysearch.com :: In-Place Move Zeros to End of List
jramaswami
"""


class Solution:
    def solve(self, nums):
        curr_zeros = 0
        for i, n in enumerate(nums):
            if n == 0:
                curr_zeros += 1
            else:
                nums[i - curr_zeros] = n
        for i in range(len(nums) - curr_zeros, len(nums)):
            nums[i] = 0
        return nums



def test_1():
    nums = [0, 1, 0, 2, 3]
    expected = [1, 2, 3, 0, 0]
    assert Solution().solve(nums) == expected