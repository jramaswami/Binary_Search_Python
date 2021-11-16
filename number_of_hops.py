"""
binarysearch.com :: Number of Hops
jramaswami
"""


import math


class Solution:
    def solve(self, nums):
        if nums:
            dp = [math.inf for _ in nums]
            dp[0] = 0
            for i, n in enumerate(nums):
                for j in range(1, n+1):
                    if i+j < len(dp):
                        dp[i+j] = min(dp[i+j], dp[i] + 1)
            return dp[-1]
        return 0


def test_1():
    nums = [3, 3, 2, 0, 1]
    expected = 2
    assert Solution().solve(nums) == expected