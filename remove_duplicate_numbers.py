"""
binarysearch.com :: Remove Duplicate Numbers
jramaswami
"""

import collections


class Solution:
    def solve(self, nums):
        ctr = Counter(nums)
        return [n for n in nums if ctr[n] == 1]