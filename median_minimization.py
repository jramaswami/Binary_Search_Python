"""
binarysearch.com :: Median Minimization
jramaswami
"""


class Solution:

    def solve(self, nums):
        # Since len(nums) // 2 is odd we can sort nums.  Pick the
        # two items in the middle. And then just distribute items
        # so that those two are in the middle.  We only want the
        # difference, so we don't have to create the two arrays.
        nums.sort()
        mid = len(nums) // 2
        return nums[mid] - nums[mid-1]


def test_1():
    nums = [1, 9, 7, 4, 3, 6]
    expected = 2
    assert Solution().solve(nums) == expected


def test_2():
    nums = []
