"""
binarysearch.com :: Index with Equal Left and Right Sums
https://binarysearch.com/problems/Index-with-Equal-Left-and-Right-Sums
"""


from itertools import accumulate


class PrefixSums:
    def __init__(self, nums):
        self.prefix = list(accumulate(nums))

    def range_query(self, a, b):
        # sumq(a, b) = sumq(0, b) - sumq(0, a - 1)
        # where sumq(0, -1) == 0
        if a == 0 and b == -1:
            return 0

        if a >= len(self.prefix):
            return 0

        sumb = self.prefix[b]
        suma = 0
        if a > 0:
            suma = self.prefix[a-1]
        return sumb - suma


class Solution:
    def solve(self, nums):
        prefix_sums = PrefixSums(nums)
        for i, _ in enumerate(nums):
            left_sum = prefix_sums.range_query(0, i-1)
            right_sum = prefix_sums.range_query(i+1, len(nums) - 1)
            if left_sum == right_sum:
                return i
        return -1


def test_1():
    nums = [2, 3, 4, 0, 5, 2, 2]
    assert Solution().solve(nums) == 3


def test_2():
    nums = [1, -2, 2]
    assert Solution().solve(nums) == 0


def test_3():
    nums = [-2, -2]
    assert Solution().solve(nums) == -1