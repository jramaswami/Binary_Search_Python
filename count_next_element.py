"""
binarysearch.com :: Count Next Element
jramaswami
"""


class Solution:

    def solve(self, nums):
        existing_nums = set(nums)
        return sum(1 if n + 1 in existing_nums else 0 for n in nums)


def test_1():
    nums = [3, 1, 2, 2, 7]
    expected = 3
    assert Solution().solve(nums) == expected
