"""
binarysearch.com :: Maximal Sublist Product
jramaswami
"""


import math


class Solution:
    def solve(self, nums):
        # Init
        leftmost_negative = len(nums)
        product = []
        curr_product = 1
        soln = -math.inf

        # Moving from left to right.  At any given index, we can have the
        # product [i, j] where nums[i] is the last non-zero number and nums[j]
        # is the current number.  We want to find the maximum possible product.
        # If the current product is postive then we this is the maximum
        # possible product.  If the product is negative, we want to find
        # nums[i] such that nums[i] < 0.  Then we will take the product at
        # i divided by the nums[i+1] to exclude the last negative number.
        for i, n in enumerate(nums):
            curr_product *= n
            product.append(curr_product)
            if curr_product == 0:
                # No product including this index will be anything but zero.
                # Since we are moving from left to right, start over at the
                # next index.
                leftmost_negative = len(nums)
                curr_product = 1
            elif curr_product < 0 and leftmost_negative < len(nums):
                soln = max(soln, curr_product // product[leftmost_negative])
            else:
                soln = max(soln, curr_product)
            if n < 0:
                leftmost_negative = min(leftmost_negative, i)
        return soln



#
# Testing
#


import functools
import operator
import random


def brute_force(nums):
    soln = -math.inf
    for left, _ in enumerate(nums):
        for right, _ in enumerate(nums[left:], start=left):
            p = functools.reduce(operator.mul, nums[left:right+1], 1)
            soln = max(soln, p)
    return soln


def test_bf():
    nums = [1, 10, 2, 0, 3, 5]
    expected = 20
    assert brute_force(nums) == expected


def test_1():
    nums = [1, 10, 2, 0, 3, 5]
    expected = 20
    assert Solution().solve(nums) == expected


def test_2():
    """RTE"""
    nums = [0]
    expected = 0
    assert Solution().solve(nums) == expected


def test_random():
    for _ in range(100):
        N = random.randint(1, 200)
        nums = [random.randint(-1000, 1000) for _ in range(N)]
        assert Solution().solve(nums) == brute_force(nums)
