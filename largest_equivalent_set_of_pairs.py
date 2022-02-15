"""
binarysearch.com :: Largest Equivalent Set of Pairs
jramaswami
"""


import math
import collections


class Solution:

    def solve(self, nums):
        soln = -math.inf
        dp = [collections.defaultdict(set) for _ in nums]
        for i, n in enumerate(nums):
            if i == 0:
                dp[i][-n] = [0]
                dp[i][n] = [n]
                dp[i][0] = [0]
            else:
                for ss in dp[i-1]:
                    for t in dp[i-1][ss]:
                        # Add to ss
                        dp[i][ss+n].add(t + n)
                        # Sub from ss
                        dp[i][ss-n].add(t)
                        # Zero
                        dp[i][ss].add(t)

        return max(dp[-1][0])


def test_1():
    nums = [1, 4, 3, 5]
    expected = 5
    assert Solution().solve(nums) == expected


def test_2():
    nums = list(range(1, 31))
    expected = 232
    assert Solution().solve(nums) == expected


def test_3():
    "Would be TLE"
    nums = [21, 64, 99, 36, 45, 40, 34, 78, 57, 19, 85, 92, 54, 94, 41, 59, 25, 70, 61, 69, 67, 41, 25, 29, 63, 38, 80, 87, 91, 63]
    expected = 854
    assert Solution().solve(nums) == expected
