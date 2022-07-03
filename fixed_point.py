"""
binarysearch.com :: Fixed Point
jramaswami
"""


class Solution:

    def solve(self, nums):
        lo = 0
        hi = len(nums) - 1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if nums[mid] == mid:
                return mid
            elif nums[mid] < mid:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1


def test_1():
    nums = [-5, -2, 0, 3, 4]
    expected = 3
    assert Solution().solve(nums) == expected


def test_2():
    nums = [-5, -4, 0]
    expected = -1
    assert Solution().solve(nums) == expected


def test_3():
    nums = [0, 1, 2]
    expected = -1
    assert Solution().solve(nums) == expected
