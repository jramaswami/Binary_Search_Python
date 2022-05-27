"""
binarysearch.com :: Distance Sums
jramaswami
"""


import collections


class Solution:

    def solve(self, nums):
        indexes = collections.defaultdict(list)
        for i, n in enumerate(nums):
            indexes[n].append(i)
        soln = [0 for _ in nums]
        for n in indexes:
            for i, a in enumerate(indexes[n]):
                for j, b in enumerate(indexes[n]):
                    if i != j:
                        soln[a] += abs(b - a)
        return soln



def test_1():
    nums = [3, 0, 1, 3, 3]
    expected = [7, 0, 0, 4, 5]
    assert Solution().solve(nums) == expected

