"""
binarysearch.com :: Odd Longest Increasing Subsequence
jramaswami
"""

import collections


class Solution:
    def solve(self, nums, k):
        dp = [collections.defaultdict(int) for _ in nums]
        soln = 0
        for i, n in enumerate(nums):
            odd = n % 2
            # You can always have this as our subsequence.
            dp[i][odd] = max(dp[i][odd], 1)
            if odd >= k:
                soln = max(soln, dp[i][odd])
            for j, m in enumerate(nums[:i]):
                if m < n:
                    for p in dp[j]:
                        dp[i][p+odd] = max(dp[i][p+odd], dp[j][p] + 1)
                        if p+odd >= k:
                            soln =  max(soln, dp[i][p+odd])
        return soln


def test_1():
    nums = [10, 12, 14, 3, 5, 6]
    k = 2
    expected = 3
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = []
    k = 7
    expected = 0
    assert Solution().solve(nums, k) == expected


def test_3():
    """WA"""
    nums = [0]
    k = 0
    expected = 1
    assert Solution().solve(nums, k) == expected


def test_4():
    nums = [0, 2, 4, 6, 8, 10]
    k = 0
    expected = len(nums)
    assert Solution().solve(nums, k) == expected
