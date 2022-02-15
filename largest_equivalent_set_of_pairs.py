"""
binarysearch.com :: Largest Equivalent Set of Pairs
jramaswami
"""


import collections


class Solution:

    def solve(self, nums):
        # double knapsack
        max_sum = sum(nums) // 2

        # O(1500 * 1500 * 30)

        # dp[index][w1][w2]
        dp = [collections.defaultdict(lambda: collections.defaultdict(lambda: False)) for _ in nums]
        dp[0][nums[0]][0] = True
        dp[0][0][nums[0]] = True
        dp[0][0][0] = True
        for i, n in enumerate(nums[1:], start=1):
            for w1 in dp[i-1]:
                for w2 in dp[i-1][w1]:
                    if dp[i-1][w1][w2]:
                        # Can I add it to w1?
                        if w1 + n <= max_sum:
                            dp[i][w1+n][w2] = True
                        # Can I add it to w2?
                        if w2 + n <= max_sum:
                            dp[i][w1][w2+n] = True
                        # I can always chuck n!
                        dp[i][w1][w2] = True

        return max(w for w in range(max_sum+1) if dp[-1][w][w])


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
