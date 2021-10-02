"""
binarysearch.com :: Insertion Index in Sorted List
jramaswami

One could use bisect.bisect_right to answer this question, but it feels like
cheating.
"""


class Solution:

    def solve(self, nums, target):
        lo = 0
        hi = len(nums) - 1
        soln = len(nums)
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if nums[mid] <= target:
                # Move right.
                lo = mid + 1
            else:
                # Move left, recording the possible solution.
                hi = mid - 1
                soln = min(soln, mid)
        return soln


def test_1():
    nums = [1, 2, 4, 5]
    target = 3
    expected = 2
    assert Solution().solve(nums, target) == expected


def test_2():
    nums = [1, 1, 1, 2, 4, 5]
    target = 1
    expected = 3
    assert Solution().solve(nums, target) == expected


def test_3():
    nums = [1]
    target = 0
    expected = 0
    assert Solution().solve(nums, target) == expected


def test_4():
    nums = []
    target = 1
    expected = 0
    assert Solution().solve(nums, target) == expected


def test_5():
    nums = [1, 1, 1, 2, 4, 5]
    target = 5
    expected = 6
    assert Solution().solve(nums, target) == expected
