"""
binarysearch.com :: Randomized Binary Search
jramaswami
"""


import itertools
import math


class Solution:

    def solve(self, nums):
        # In order for the pseudo binary search to work,
        # any given number must be more than all numbers to its
        # left and less than all numbers to its right.
        prefix_max = list(itertools.accumulate(nums, max))
        suffix_min = list(reversed(list(itertools.accumulate(reversed(nums), min))))
        prefix_max.append(-math.inf)
        suffix_min.append(math.inf)
        soln = 0
        for i, n in enumerate(nums):
            if prefix_max[i-1] < n < suffix_min[i+1]:
                soln += 1
        return soln



def test_1():
    nums = [1, 10, 5, 20]
    expected = 2
    assert Solution().solve(nums) == expected


def test_2():
    nums = [0, 0]
    expected = 0
    assert Solution().solve(nums) == expected
