"""
binarysearch.com :: Sum Pairs to Target
jramaswami
"""


import collections


class Solution:

    def solve(self, nums, target):
        soln = 0
        freqs = collections.defaultdict(int)
        for n in nums:
            m = target - n
            if freqs[m]:
                soln += 1
                freqs[m] -= 1
            else:
                freqs[n] += 1
        return soln


def test_1():
    nums = [1, 3, 5, 3, 7]
    target = 6
    assert Solution().solve(nums, target) == 2


def test_2():
    nums = [6]
    target = 6
    assert Solution().solve(nums, target) == 0
