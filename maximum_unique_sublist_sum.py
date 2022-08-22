"""
binarysearch.com :: Maximum Unique Sublist Sum
https://binarysearch.com/problems/Maximum-Unique-Sublist-Sum
jramaswami
"""


from collections import defaultdict
from itertools import accumulate


class Solution:
    def solve(self, nums):
        # Corner case.
        if nums == []:
            return 0

        # DP to find longest unique sublist ending at i with prefix sums
        # to find the maximum sum at i.
        soln = nums[0]
        prefix = list(accumulate(nums))
        dp = [0 for _ in nums]
        dp[0] = 1
        prev = defaultdict(int)
        prev[nums[0]] = 0
        for i in range(1, len(nums)):
            if nums[i] in prev:
                dp[i] = min(dp[i-1] + 1, i - prev[nums[i]])
            else:
                dp[i] = dp[i-1] + 1
            prev[nums[i]] = i
            j = i - dp[i]
            if j == -1:
                soln = max(soln, prefix[i])
            else:
                soln = max(soln, prefix[i] - prefix[j])

        return soln


def test_1():
    nums = [1, 2, 2, 3, 4, 4]
    assert Solution().solve(nums) == 9


def test_2():
    nums = [9, 9, 9, 9, 9]
    assert Solution().solve(nums) == 9


def test_3():
    nums = [1, 2, 3, 4, 5]
    assert Solution().solve(nums) == 15


def test_4():
    nums = []
    assert Solution().solve(nums) == 0