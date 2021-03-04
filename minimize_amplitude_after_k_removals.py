"""
binarysearch.com :: Minimize Amplitude After K Removals
jramaswami
"""
from math import inf


class Solution:
    def solve(self, nums, k):
        # Corner case where you remove all but one number.
        if k == len(nums) - 1:
            return 0

        nums0 = list(nums)
        nums0.sort()

        # len(nums) - k numbers will remain.  Use a sliding window.
        window_length = len(nums0) - k
        i = 0
        soln = inf
        while i + window_length <= len(nums0):
            soln = min(soln, abs(nums0[i] - nums0[i + window_length - 1]))
            i += 1
        return soln


def test_1():
    nums = [2, 10, 14, 12, 30]
    k = 2
    assert Solution().solve(nums, k) == 4

def test_2():
    nums = [1, 1, 0]
    k = 1
    assert Solution().solve(nums, k) == 0
