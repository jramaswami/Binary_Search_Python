"""
binarysearch.com :: Square of a List
jramaswami
"""
class Solution:
    def solve(self, nums):
        return sorted(x * x for x in nums)
