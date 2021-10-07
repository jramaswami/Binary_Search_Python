"""
binarysearch.com :: Binary Sublist with Target Sum
jramaswami
"""


from collections import defaultdict


class Solution:

    def solve(self, nums, target_sum):
        soln = 0
        curr_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] += 1
        for n in nums:
            curr_sum += n
            # For a sublist from [i, j] to be the target sum, then
            # there must exists a sublist [0, i-1] that has the sum
            # of curr_sum - target_sum.
            delta = curr_sum - target_sum
            soln += prefix_sums[delta]
            prefix_sums[curr_sum] += 1
        return soln



def test_1():
    nums = [1, 0, 1, 1]
    target = 2
    expected = 3
    assert Solution().solve(nums, target) == expected


def test_2():
    """RTE"""
    nums = [1]
    target = 0
    expected = 0
    assert Solution().solve(nums, target) == expected


def test_3():
    nums = [0, 0, 0, 1, 0]
    target = 0
    expected = 7
    assert Solution().solve(nums, target) == expected


def test_4():
    nums = [0, 0, 0, 0, 0]
    target = 0
    expected = 15
    assert Solution().solve(nums, target) == expected


def test_5():
    nums = []
    target = 0
    expected = 0
    assert Solution().solve(nums, target) == expected


def test_6():
    """WA"""
    nums = [1, 0]
    target = 1
    expected = 2
    assert Solution().solve(nums, target) == expected


def test_7():
    """WA"""
    nums = [0, 1, 0]
    target = 1
    expected = 4
    assert Solution().solve(nums, target) == expected
