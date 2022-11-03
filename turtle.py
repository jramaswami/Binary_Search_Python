"""
binarysearch.com :: Weekly Contest 32 :: Turtle of Wall Street
https://binarysearch.com/room/Weekly-Contest-32-oSuVsQ17Hc
"""
class Solution:
    def solve(self, nums):
        profit = 0
        if nums:
            N = len(nums)
            dp = [0 for _ in nums]
            max_sell = nums[-1]
            for i in range(N-1, -1, -1):
                max_sell = max(nums[i], max_sell)
                dp[i] = max_sell

            profit = sum(sell - buy for buy, sell in zip(nums, dp))
        return profit


def test_1():
    solver = Solution()
    nums = [1, 2, 5, 1, 3]
    assert solver.solve(nums) == 9


def test_2():
    solver = Solution()
    nums = [5, 2]
    assert solver.solve(nums) == 0


def test_3():
    solver = Solution()
    nums = []
    assert solver.solve(nums) == 0

