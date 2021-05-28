"""
binarysearch.com :: Sorted Elements
jramaswami
"""


from collections import defaultdict


class Solution:
    def solve(self, nums):
        # Find the proper position for each element.
        # Be sure to handle the case of duplicates in nums.
        nums0 = sorted(nums)
        positions = defaultdict(set)
        for i, n in enumerate(nums0):
            positions[n].add(i)

        soln = 0
        for i, n in enumerate(nums):
            if i in positions[n]:
                soln += 1

        return soln



def test_1():
    nums = [1, 7, 3, 4, 10]
    expected = 2
    assert Solution().solve(nums) == expected