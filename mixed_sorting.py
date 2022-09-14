"""
binarysearch.com :: Mixed Sorting
jramaswami
"""


class Solution:
    def solve(self, nums):
        evens = sorted(k for k in nums if k % 2 == 0)
        odds = sorted((k for k in nums if k % 2 == 1), reverse=True)
        e = 0
        o = 0
        nums0 = list(nums)
        for i, n in enumerate(nums):
            if n % 2 == 0:
                nums0[i] = evens[e]
                e += 1
            else:
                nums0[i] = odds[o]
                o += 1
        return nums0