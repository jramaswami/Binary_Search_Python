"""
binarysearch.com :: Largest K-Divisible Subsequence
jramaswami
"""


import functools


class Solution:
    def solve(self, nums, k):

        @functools.cache
        def solve0(i, acc):
            # Base case.
            if i >= len(nums):
                if acc % k:
                    return 0
                else:
                    return acc

            # With the value at nums[i].
            max_with = solve0(i + 1, acc + nums[i])
            # Without the value at nums[i]
            max_without = solve0(i + 1, acc)
            return max(max_with, max_without)

        return solve0(0, 0)


def test_1():
    nums = [2, 6, 4, 1]
    k = 1
    expected = 13
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [5]
    k = 2
    expected = 0
    assert Solution().solve(nums, k) == expected


def test_3():
    """TLE"""
    nums = [1] * 200
    k = 10
    expected = 200
    assert Solution().solve(nums, k) == expected
