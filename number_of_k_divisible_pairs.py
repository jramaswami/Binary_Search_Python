"""
binarysearch.com :: Number of K-Divisible Pairs
jramaswami
"""
class Solution:
    def solve(self, nums, k):
        # Observation (a + b) % k == (a % k) + (b % k)
        # Observation k <= 100
        soln = 0
        dp = [0 for _ in range(100)]
        for a in reversed(nums):
            a0 = a % k
            for b in range(100):
                if (a0 + b) % k == 0:
                    soln += dp[b]
            dp[a0] += 1
        return soln


def test_1():
    nums = [2, 4, 5, 1, 2]
    k = 6
    assert Solution().solve(nums, k) == 3

def test_2():
    nums = []
    k = 6
    assert Solution().solve(nums, k) == 0

def test_3():
    nums = [0, 0]
    k = 1
    assert Solution().solve(nums, k) == 1

def test_4():
    nums = [2, 2, 2]
    k = 4
    assert Solution().solve(nums, k) == 3

def test_5():
    nums = [1, 1]
    k = 1
    assert Solution().solve(nums, k) == 1

def test_6():
    nums = [0, 2, 2]
    k = 2
    assert Solution().solve(nums, k) == 3
