"""
binarysearch.com :: Subsequence Sum
jramaswami
"""


class Solution:
    def solve(self, nums):
        dp = list(nums)
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i+1:], start=i+1):
                if m - n == j - i:
                    dp[j] = max(dp[j], dp[i] + m)
        return max(dp)


def test_1():
    nums = [5, 6, 8, 8, 7, 4]
    assert Solution().solve(nums) == 19


# def test_2():
#     "TLE"
#     nums = list(range(100000))
#     assert Solution().solve(nums) == sum(nums)
