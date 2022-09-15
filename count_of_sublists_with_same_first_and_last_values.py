"""
binarysearch.com :: Count of Sublists with Same First and Last Values
jramaswami
"""


import collections


class Solution:
    def solve(self, nums):
        # n Choose 2 = (n * (n-1)) / 2
        def nC2(n):
            return (n * (n - 1)) // 2

        freqs = collections.Counter(nums)
        soln = 0
        for k, f in freqs.items():
            soln += f
            soln += nC2(f)
        return soln