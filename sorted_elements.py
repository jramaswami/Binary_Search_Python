"""
binarysearch.com :: Sorted Elements
jramaswami
"""


class Solution:
    def solve(self, nums):
        return sum(a == b for a, b in zip(nums, sorted(nums)))



def test_1():
    nums = [1, 7, 3, 4, 10]
    expected = 2
    assert Solution().solve(nums) == expected