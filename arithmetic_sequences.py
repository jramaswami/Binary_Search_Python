"""
binarysearch.com :: Arithmetic Subsequences
jramaswami
"""


class Solution:

    def solve(self, nums):

        # DP[end][delta]
        soln = 0
        dp = [dict() for _ in nums]
        for i, left in enumerate(nums):
            for j, right in enumerate(nums[i+1:], start=i+1):
                delta = right - left
                if delta in dp[i]:
                    dp[j][delta] = 1 + dp[i][delta]
                else:
                    dp[j][delta] = 2
                if dp[j][delta] >= 3:
                    soln += (dp[j][delta] - 3 + 1)
        return soln



def test_1():
    nums = [5, 11, 12, 7, 9, 13]
    assert Solution().solve(nums) == 3


def test_2():
    nums = []
    assert Solution().solve(nums) == 0


def test_3():
    nums = [1,2,3,4,5,6,7,8,9]
    assert Solution().solve(nums) == 41


def test_4():
    nums = list(range(1000))
    assert Solution().solve(nums) == 2781846


def test_5():
    "WA"
    nums = [1,1,2,3]
    assert Solution().solve(nums) == 2

