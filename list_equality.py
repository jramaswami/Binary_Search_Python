"""
binarysearch.com :: List Equality with Increments
https://binarysearch.com/problems/List-Equality-with-Increments
"""


class Solution:
    def solve(self, nums):
        # Increasing all but one element is equivalent to decreasing that element.
        # So we must decrease each element until it is equal to the smallest
        # element.
        smallest_element = min(nums)
        return sum(a - smallest_element for a in nums)


def test_1():
    assert Solution().solve([1, 3, 4]) == 5