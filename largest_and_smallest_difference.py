"""
binarysearch.com :: Largest and Smallest Difference
jramaswami
"""
from math import inf


class Solution:
    def solve(self, nums, k):
        if k == 1:
            return 0

        nums.sort()
        delta = inf
        for start, minval in enumerate(nums):
            if start + k > len(nums):
                break
            maxval = nums[start+k-1]
            delta = min(delta, (maxval - minval))
        return delta


def test_1():
    nums = [2, 10, 5, 1, 8]
    k = 3
    assert Solution().solve(nums, k) == 4

def test_2():
    nums = [0]
    k = 1
    assert Solution().solve(nums, k) == 0

def test_3():
    nums = [1, 0]
    k = 2
    assert Solution().solve(nums, k) == 1
