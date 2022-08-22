"""
binarysearch.com :: Longest Increasing Subsequence
jramaswami
"""


class Solution():
    def solve(self, nums):
        # O(N^2) Solution
        if nums:
            dp = [1 for _ in nums]
            for i, n in enumerate(nums):
                for j, m in enumerate(nums[:i]):
                    if m < n:
                        dp[i] = max(dp[i], 1 + dp[j])
            return max(dp)
        return 0


def test_1():
    nums = [6, 1, 7, 2, 8, 3, 4, 5]
    assert Solution().solve(nums) == 5


def test_2():
    nums = []
    assert Solution().solve(nums) == 0