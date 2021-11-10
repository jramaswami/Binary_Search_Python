"""
binarysearch.com :: Largest K-Divisible Subsequence
jramaswami
"""


class Solution:
    def solve(self, nums, k):
        # dp will hold the maximum sum % k for each index.
        dp = [[0 for _ in range(k)] for _ in nums]
        dp[0][nums[0] % k] = nums[0]

        for i, n in enumerate(nums[1:], start=1):
            for remainder, max_sum in enumerate(dp[i-1]):
                # For each maximum sum per remainder, add n and then
                # store if it is the maximum for the new remainder.
                new_sum = max_sum + n
                new_remainder = new_sum % k
                dp[i][new_remainder] = max(dp[i][new_remainder], new_sum)
        return dp[-1][0]


def test_1():
    nums = [2, 6, 4, 1]
    k = 1
    expected = 13
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [5]
    k = 2
    expected = 0
    assert Solution().solve(nums, k) == expected


def test_3():
    """TLE"""
    nums = [1] * 200
    k = 10
    expected = 200
    assert Solution().solve(nums, k) == expected


def test_4():
    """RTE"""
    nums = []
    k = 4
    expected = 0
    assert Solution().solve(nums, k) == expected
