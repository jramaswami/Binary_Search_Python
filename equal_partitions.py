"""
binarysearch.com :: Equal Partitions
jramaswami
"""


import functools


class Solution:
    def solve(self, nums):

        @functools.cache
        def is_partitionable(index, target_sum):
            # Base case: we have reached zero.
            if target_sum == 0:
                return True
            # Base case: we have gone below zero.
            if target_sum < 0:
                return False
            # Base case: we have reached the end without reaching zero.
            if index >= len(nums):
                return False

            # Either add current number or don't ...
            return (
                is_partitionable(index + 1, target_sum) or
                is_partitionable(index + 1, target_sum - nums[index])
            )

        S = sum(nums)
        # In order to evenly paritition the numbers, the sum
        # must be even.
        if S % 2:
            return False
        # Partitioning intot two equal sum subsets means that
        # both subsets will equal S / 2.  We can, therefore,
        # find any set equal to S / 2.
        T = S // 2
        return is_partitionable(0, T)


def test_1():
    nums = [1,5,11,5]
    expected = True
    assert Solution().solve(nums) == expected


def test_2():
    nums = [1,2,3,5]
    expected = False
    assert Solution().solve(nums) == expected


def test_3():
    nums = [1] * 200
    expected = True
    assert Solution().solve(nums) == expected
