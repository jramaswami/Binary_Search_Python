"""
binarysearch.com :: Arrange Symbols to Create Sum
jramaswami
"""


import collections


class Solution:
    def solve(self, nums, target):
        # Corner case:
        if nums == []:
            if target == 0:
                return 1
            return 0
        # sum of nums <= 1000
        # len(nums) <= 20
        # Account for positive and negative numbers.
        # -1000 + 1000 = 0, so add 1000 to all sums.
        offset = sum(nums)
        dp = [[0 for _ in range((2 * offset) + 5)] for _ in nums]
        dp[0][offset + nums[0]] = 1
        dp[0][offset - nums[0]] = 1
        for r, n in enumerate(nums[1:], start=1):
            for c, _ in enumerate(dp[r]):
                if dp[r-1][c]:
                    dp[r][c+n] += dp[r-1][c]
                if dp[r-1][c]:
                    dp[r][c-n] += dp[r-1][c]

        return dp[-1][target + offset]



def test_1():
    nums = [1, 2, 2, 2, 1]
    target = 6
    expected = 2
    assert Solution().solve(nums, target) == expected


def test_2():
    nums = [2, 4, 3, 0, 3, 5, 1, 2, 2, 5, 6, 4, 9, 8, 2, 0, 4, 7, 0, 2]
    target = 69
    expected = 8
    assert Solution().solve(nums, target) == expected


def test_3():
    """TLE"""
    nums = [38, 16, 11, 33, 15, 15, 40, 28, 29, 27, 10, 19, 42, 50, 34, 36, 48, 20, 32, 35]
    target = 82
    expected = 5007
    assert Solution().solve(nums, target) == expected


def test_4():
    """RTE"""
    nums = []
    target = 0
    expected = 0
    assert Solution().solve(nums, target) == expected


def test_5():
    """WA"""
    nums = [0]
    target = 0
    expected = 2
    assert Solution().solve(nums, target) == expected

