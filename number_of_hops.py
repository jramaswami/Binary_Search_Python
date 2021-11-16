"""
binarysearch.com :: Number of Hops
jramaswami

REF: https://www.youtube.com/watch?v=vBdo7wtwlXs
"""


class Solution:
    def solve(self, nums):
        if len(nums) > 1:
            current_ladder = nums[0]
            next_ladder = current_ladder
            hops = 1
            for i, n in enumerate(nums[1:], start=1):
                # See if this ladder should be our next ladder
                if i > current_ladder:
                    # You must switch ladders
                    hops += 1
                    current_ladder = next_ladder
                    assert i <= current_ladder
                next_ladder = max(next_ladder, i + n)

            return hops

        return 0


#
# Testing
#


import random


def solve_dp(nums):
    if nums:
        dp = [math.inf for _ in nums]
        dp[0] = 0
        for i, n in enumerate(nums):
            for j in range(1, n+1):
                if i+j < len(dp):
                    dp[i+j] = min(dp[i+j], dp[i] + 1)
        return dp[-1]
    return 0


def test_1():
    nums = [3, 3, 2, 0, 1]
    expected = 2
    assert Solution().solve(nums) == expected


def test_2():
    N = 100
    nums = [3] * N
    expected = N // 3
    assert Solution().solve(nums) == expected


def test_3():
    nums = [100001]
    for _ in range(1, 100000):
        nums.append(random.randint(1, 100000))
    assert Solution().solve(nums) == 1


def test_4():
    """WA"""
    nums = [0]
    assert Solution().solve(nums) == 0