"""
binarysearch.com :: Pythagorean Triplets
jramaswami
"""


import itertools


class Solution:
    def solve(self, nums):
        nums0 = set(n * n for n in nums)
        for a, b in itertools.combinations(nums, 2):
            if ((a * a) + (b * b)) in nums0:
                return True
        return False