"""
binarysearch.com :: Split List Into Strictly Increasing Chunks
jramaswami
"""


import collections


class Solution:
    def solve(self, nums, k):
        freqs = collections.Counter(nums)
        min_length = max(2, max(freqs.values()))
        return len(nums) // min_length >= k