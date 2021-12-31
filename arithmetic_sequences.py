"""
binarysearch.com :: Arithmetic Subsequences
jramaswami
"""


import collections


class Solution:

    def solve(self, nums):

        # DP[end][delta] = list of lengths
        soln = 0
        dp = [collections.defaultdict(list) for _ in nums]
        for i, left in enumerate(nums):
            for j, right in enumerate(nums[i+1:], start=i+1):
                delta = right - left
                if delta in dp[i]:
                    for t in dp[i][delta]:
                        t0 = 1 + t
                        dp[j][delta].append(t0)
                        if t0 >= 3:
                            soln += (t0 - 3 + 1)
                else:
                    # The first one.
                    dp[j][delta].append(2)
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
    """
    WA: problem was that there was more than one way to arrive at a given
    index with the given delta.
    """
    nums = [1,1,2,3]
    assert Solution().solve(nums) == 2
