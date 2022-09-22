"""
binarysearch.com :: Equivalent Value and Frequency
jramaswami
"""


import collections


class Solution:

    def solve(self, nums):
        freqs = collections.Counter(nums)
        return any(f == v for f, v in freqs.items())


def test_1():
    nums = [7, 9, 3, 3, 3]
    assert Solution().solve(nums) == True


def test_2():
    nums = [7, 9, 3, 3]
    assert Solution().solve(nums) == False


def test_3():
    nums = []
    assert Solution().solve(nums) == False