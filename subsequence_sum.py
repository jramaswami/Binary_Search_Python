"""
binarysearch.com :: Subsequence Sum
jramaswami
"""


import collections


class Solution:
    def solve(self, nums):
        dp = collections.defaultdict(int)
        for i, n in enumerate(nums):
            dp[n - i] += n
        return max(dp.values())


def test_1():
    nums = [5, 6, 8, 8, 7, 4]
    assert Solution().solve(nums) == 19


def test_2():
    "TLE"
    nums = list(range(100000))
    assert Solution().solve(nums) == sum(nums)
