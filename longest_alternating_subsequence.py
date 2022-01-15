"""
binarysearch.com :: Longest Alternating Subsequence
jramaswami
"""


import functools


class Solution:

    def solve(self, nums):

        @functools.cache
        def longest_increasing(i):
            result = 0
            for j, m in enumerate(nums[i+1:], start=i+1):
                if m > nums[i]:
                    result = max(result, 1 + longest_decreasing(j))
            return result


        @functools.cache
        def longest_decreasing(i):
            result = 0
            for j, m in enumerate(nums[i+1:], start=i+1):
                if m < nums[i]:
                    result = max(result, 1 + longest_increasing(j))
            return result

        soln = 0
        for i, _ in enumerate(nums):
            soln = max(soln, 1 + longest_decreasing(i), 1 +  longest_increasing(i))
        return soln


def test_1():
    nums = [5, 9, 3, 1, 2, 8, 3, 6]
    expected = 6
    assert Solution().solve(nums) == expected
