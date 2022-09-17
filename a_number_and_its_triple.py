"""
binarysearch.com :: A Number and Its Triple
jramaswami
"""


import collections


class Solution:
    def solve(self, nums):
        freqs = collections.Counter(nums)
        for n in nums:
            if n == 0:
                if freqs[0] > 1:
                    return True
            elif freqs[n*3] > 0:
                return True
        return False


def test_1():
    nums = [2, 3, 10, 7, 6]
    assert Solution().solve(nums) == True


def test_2():
    nums = [3, 4, 5]
    assert Solution().solve(nums) == False


def test_3():
    nums = [0, 2, 0]
    assert Solution().solve(nums) == True


def test_4():
    "WA"
    nums = [0]
    assert Solution().solve(nums) == False