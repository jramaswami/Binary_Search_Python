"""
binarysearch.com :: Kth Pair Distance
jramaswami
"""


class Solution:

    def solve(self, nums, k):
        nums.sort()

        def check(x):
            total = 0
            j = 1
            for i, y in enumerate(nums):
                while j < len(nums) and nums[j] - nums[i] <= x:
                    j += 1
                total += (j - i - 1)
            return total >= k

        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            mid = lo + ((hi - lo) // 2)
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo



def test_1():
    nums = [1, 5, 3, 2]
    k = 3
    expected = 2
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [1, 3, 1]
    k = 1
    expected = 0
    assert Solution().solve(nums, k) == expected


def test_3():
    nums = [1, 1, 1]
    k = 2
    expected = 0
    assert Solution().solve(nums, k) == expected


def test_4():
    nums = [1, 6, 1]
    k = 3
    expected = 5
    assert Solution().solve(nums, k) == expected


def test_5():
    nums = [0, 1]
    k = 0
    expected = 1
    assert Solution().solve(nums, k) == expected
