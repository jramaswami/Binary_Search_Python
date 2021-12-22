"""
binarysearch.com :: Triangle Triplets
jramaswami
"""

from bisect import bisect_right


def count_lte(a, x):
    i = bisect_right(a, x)
    if i:
        return i-1
    return -1


class Solution:

    def solve(self, nums):
        soln = 0
        nums.sort()
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:], start=i+1):
                soln += 1 + count_lte(nums[j+1:], a + b)
        return soln


def test_1():
    nums = [7, 8, 8, 9, 100]
    assert Solution().solve(nums) == 4


def test_2():
    "WA"
    nums = [1, 1, 0]
    assert Solution().solve(nums) == 0
