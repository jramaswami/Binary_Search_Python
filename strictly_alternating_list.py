"""
binarysearch.com :: Strictly Alternating List
jramaswami
"""


class Solution:
    def solve(self, nums):
        # To be strictly increasing there must be more than one element
        if len(nums) < 2:
            return False
        # The array must start off increasing.
        if nums[0] >= nums[1]:
            return False
        # After than, there must be no consecutive elements that are the same.
        return all(a != b for a, b in zip(nums[:-1], nums[1:]))


def test_1():
    nums = [1, 2, 5, 7, 4, 1, 6, 8, 3, 2]
    expected = True
    assert Solution().solve(nums) == expected


def test_2():
    nums = [1, 1, 2, 3, 2, 1]
    expected = False
    assert Solution().solve(nums) == expected


def test_3():
    nums = [1, 3, 5, 7]
    expected = True
    assert Solution().solve(nums) == expected


def test_4():
    nums = [5, 3, 1, 5, 7]
    expected = False
    assert Solution().solve(nums) == expected