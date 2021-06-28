"""
binarysearch.com :: Number of Sublists With Sum of Target
jramaswami
"""


from collections import defaultdict


class Solution:
    def solve(self, nums, target):
        # Keep track of previous sums and the number of times we have seen them.
        prev_sums = defaultdict(int)
        prev_sums[0] = 1
        soln = 0

        curr_sum = 0
        for n in nums:
            curr_sum += n
            # Count the number of sublists ending with end that sum to the
            # target value.  To do this see how many times curr_sum - target
            # has been seen because curr_sum - target_sum is the sum of a
            # sublist ending at the current num.  See below for illustration.
            # [x1, x2, x3, x4, x5, x6, x7, x8, ...]
            # -----------curr sum------------
            # ---prev_sum----
            #                ---target sum---
            soln += prev_sums.get(curr_sum - target, 0)
            prev_sums[curr_sum] += 1
        return soln


def test_1():
    nums = [2, 0, 2]
    target = 2
    expected = 4
    assert Solution().solve(nums, target) == expected


def test_2():
    nums = []
    target = 2
    expected = 0
    assert Solution().solve(nums, target) == expected


def test_3():
    nums = [5, -3, 1, 3, 0, -2, 3, 0, -2, -4, -5, 1, -2, -2, -2, 2, -2, 5, -1, 3, 4, 4, -5, 2, -3, -1, -2, -1, 3, -2]
    target = 2
    expected = 22
    assert Solution().solve(nums, target) == expected
