"""
binarysearch.com :: List Consecutive Split
jramaswami
"""


import collections


class Solution:

    def solve(self, nums, k):
        if len(nums) % k:
            return False
        freqs = collections.Counter(nums)
        return max(freqs.values()) <= (len(nums) // k)


def test_1():
    nums = [3, 2, 3, 4, 5, 1]
    k = 3
    assert Solution().solve(nums, k) == True


def test_2():
    "WA"
    nums = [0, 0]
    k = 1
    assert Solution().solve(nums, k) == True


def test_3():
    "WA"
    nums = [0, 1, 1, 3]
    k = 2
    assert Solution().solve(nums, k) == False