"""
binarysearch.com :: Sublist Sum
jramaswami
"""
from math import inf


def kadanes(arr):
    """Kadane's algorithm to return maximum subarray sum."""
    max_sum = -inf
    curr_sum = 0
    for a in arr:
        curr_sum = max(0, curr_sum + a)
        max_sum = max(max_sum, curr_sum)
    return max_sum


class Solution:
    def solve(self, nums):
        max_sum = kadanes(nums)
        arr_sum = sum(nums)
        return max_sum > arr_sum


def test_1():
    nums = [1, -2, 3, 4]
    assert Solution().solve(nums) == True

def test_2():
    nums = [-2]
    assert Solution().solve(nums) == True


