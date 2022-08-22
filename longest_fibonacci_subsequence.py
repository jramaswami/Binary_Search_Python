"""
binarysearch.com :: Longest Fibonacci Subsequence
jramaswami
"""


class Solution:

    def solve(self, nums):
        nums0 = set(nums)
        soln = 0
        for i, a in enumerate(nums):
            for _, b in enumerate(nums[i+1:], start=i+1):
                x, y = a, b
                curr = 2
                while x + y in nums0:
                    curr += 1
                    x, y = y, x + y
                if curr >= 3:
                    soln = max(soln, curr)
        return soln


def test_1():
    nums = [1, 2, 3, 4, 5]
    expected = 4
    assert Solution().solve(nums) == expected