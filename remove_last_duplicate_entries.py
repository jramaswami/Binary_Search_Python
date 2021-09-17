"""
binarysearch.com :: Remove Last Duplicate Entries
jramaswami
"""

from collections import defaultdict


class Solution:

    def solve(self, nums):
        freqs = defaultdict(int)
        last_index = defaultdict(lambda: -1)
        for i, n in enumerate(nums):
            freqs[n] += 1
            last_index[n] = i

        soln = []
        for i, n in enumerate(nums):
            if freqs[n] > 1 and i == last_index[n]:
                continue
            soln.append(n)
        return soln


def test_1():
    nums = [1, 3, 4, 1, 3, 5]
    expected = [1, 3, 4, 5]
    assert Solution().solve(nums) == expected


def test_2():
    nums = [1, 1, 1, 2, 2, 2, 3, 3, 3]
    expected = [1, 1, 2, 2, 3, 3]
    assert Solution().solve(nums) == expected
