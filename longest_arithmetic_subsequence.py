"""
binarysearch.com :: Longest Arithmetic Subsequence
jramaswami
"""


from collections import defaultdict


class Solution:

    def solve(self, nums):

        # Corner case
        if len(nums) == 0:
            return 0

        cache = [defaultdict(lambda: 1) for _ in nums]

        soln = 1
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:], start=i+1):
                delta = b - a
                cache[j][delta] = max(cache[j][delta], 1 + cache[i][delta])
                soln = max(soln, cache[j][delta])

        return soln


def test_1():
    nums = [1, 3, 5, 7, 9]
    expected = 5
    assert Solution().solve(nums) == expected


def test_2():
    nums = [1, 3, 6, 7, 5, 8, 9]
    expected = 4
    assert Solution().solve(nums) == expected
