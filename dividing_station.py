"""
binarysearch.com :: Dividing Station
jramaswami
"""


class Solution:

    def solve(self, nums):
        nums.sort()

        # Build graph of divisible pairs.
        adj = [[] for _ in nums]
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i+1:], start=i+1):
                if m % n == 0:
                    adj[i].append(j)

        # Find longest path using dp.
        soln = 0
        dp = [1 for _ in nums]
        for i, _ in enumerate(nums):
            soln = max(soln, dp[i])
            for j in adj[i]:
                dp[j] = max(dp[j], dp[i] + 1)
        return soln


def test_1():
    nums = [3, 5, 10, 20, 21]
    expected = 3
    assert Solution().solve(nums) == expected


def test_2():
    nums = [1, 3, 6, 24]
    expected = 4
    assert Solution().solve(nums) == expected


def test_3():
    nums = []
    expected = 0
    assert Solution().solve(nums) == expected


def test_4():
    nums = [1]
    expected = 1
    assert Solution().solve(nums) == expected


def test_5():
    nums = [2,3,5,7,11,13]
    expected = 1
    assert Solution().solve(nums) == expected
