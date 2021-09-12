"""
binarysearch.com :: Sort by Frequency and Value
jramaswami
"""


from collections import Counter
from itertools import repeat


class Solution:

    def solve(self, nums):
        ctr = Counter(nums)
        soln = []
        for v, k in sorted(((v, k) for k, v in ctr.items()), reverse=True):
            soln.extend(repeat(k, v))
        return soln


def test_1():
    nums = [1, 1, 5, 5, 5, 2, 2, 2, 1, 1]
    assert Solution().solve(nums) == [1, 1, 1, 1, 5, 5, 5, 2, 2, 2]
