"""
binarysearch.com :: K Maximum Sums
jramaswami
"""


import itertools


class Solution:

    def solve(self, nums, k):

        prefix = list(itertools.accumulate(nums))

        def get_sum(left, right):
            if left - 1 < 0:
                return prefix[right]
            return prefix[right] - prefix[left-1]


        solns = [get_sum(left, right)
                 for left, _ in enumerate(nums)
                 for right, _ in enumerate(nums[left:], start=left)
        ]
        solns.sort()
        return solns[-k:]


def test_1():
    nums = [1, 3, 4, -100, 10, -30, 5, -3, 5]
    k = 3
    expected = [7, 8, 10]
    assert Solution().solve(nums, k) == expected
