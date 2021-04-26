"""
binarysearch.com :: High Frequency
jramaswami
"""
from collections import Counter


class Solution:
    def solve(self, nums):
        if nums:
            ctr = Counter(nums)
            return max(ctr.values())
        return 0


def test_1():
    assert Solution().solve([1, 4, 1, 7, 1, 7, 1, 1]) == 5

def test_2():
    assert Solution().solve([5, 5, 5, 5, 5, 5, 5]) == 7