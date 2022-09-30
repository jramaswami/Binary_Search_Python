"""
binarysearch.com :: Arithmetic Subsequences
jramaswami
"""


import collections


class Solution:

    def solve(self, nums):
        soln = 0
        dp = [collections.defaultdict(list) for _ in nums]
        for i, left in enumerate(nums[:-1]):
            j, right = i + 1, nums[i+1]
            delta = right - left
            # Extend previous
            if delta in dp[i]:
                for t in dp[i][delta]:
                    dp[j][delta].append(t + 1)
                    if t + 1 >= 3:
                        soln += 1
            # Start from here.
            dp[j][delta].append(2)
        return soln


def test_1():
    nums =  [5, 7, 9, 11, 12, 13]
    assert Solution().solve(nums) == 4