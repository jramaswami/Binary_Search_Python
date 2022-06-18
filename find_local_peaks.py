"""
binarysearch.com :: Find Local Peaks
jramaswami
"""


class Solution:

    def solve(self, nums):
        if len(nums) < 2:
            return []

        peaks = []

        # Check index 0
        if nums[0] > nums[1]:
            peaks.append(0)

        if len(nums) > 2:
            for i, _ in enumerate(nums[1:-1], start=1):
                if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                    peaks.append(i)

        # Check last index
        if nums[-2] < nums[-1]:
            peaks.append(len(nums)-1)

        return peaks


def test_1():
    nums = [1, 2, 3, 2, 4]
    expected = [2, 4]
    assert Solution().solve(nums) == expected


def test_2():
    nums = [1, 1, 1, 1]
    expected = []
    assert Solution().solve(nums) == expected


def test_3():
    nums = [5]
    expected = []
    assert Solution().solve(nums) == expected


def test_4():
    nums = [3, 4]
    expected = [1]
    assert Solution().solve(nums) == expected
