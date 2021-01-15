"""
binarysearch.com :: List Partitioning with Inequality Relation
jramaswami
"""
from math import inf


class Solution:
    def solve(self, nums):
        """
        Parition nums into two non empty sublists, A, B such that for every a
        in A, b in B a < b.
        """
        prefix_max = [-inf for _ in nums]
        suffix_min = [inf for _ in nums]
        for i, _ in enumerate(nums):
            if i == 0:
                prefix_max[i] = nums[i]
                suffix_min[len(nums) - 1] = nums[len(nums) - 1]
            else:
                prefix_max[i] = max(nums[i], prefix_max[i-1])
                suffix_min[len(nums) - 1 - i] = min(suffix_min[len(nums) - i], nums[len(nums) - 1 - i])

        for i, _ in enumerate(prefix_max):
            if i + 1 < len(suffix_min) and prefix_max[i] <= suffix_min[i+1]:
                return i + 1


def test_1():
    assert Solution().solve([2, 0, 1, 4, 3]) == 3

def test_2():
    assert Solution().solve([2, 4, 5, 6]) == 1

def test_3():
    assert Solution().solve([4, 3, 2, 7]) == 3

