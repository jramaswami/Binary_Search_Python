"""
binarysearch.com :: Kth Pair Distance
jramaswami
"""


class Solution:

    def solve(self, nums, k):
        nums.sort()

        lo = min(b - a for a, b in zip(nums[:-1], nums[1:]))
        hi = nums[-1] - nums[0]
        while lo <= hi:
            # Guess a number, x.
            x = lo + ((hi - lo) // 2)
            # How many pair diffs are less than x.
            lt = 0
            # How many pair diffs are less than or equal to x.
            lte = 0
            # What is the largest existing diff <= our guess, x.
            y = 0

            lt_i = 0
            lte_i = 0
            for i, _ in enumerate(nums):
                while lt_i < len(nums) and nums[lt_i] - nums[i] < x:
                    lt_i += 1
                while lte_i < len(nums) and nums[lte_i] - nums[i] <= x:
                    y = max(nums[lte_i] - nums[i], y)
                    lte_i += 1

                # le_i now points to the first j such that nums[i] + any nums[i+1:j] < x
                # lte_i now points to the first j such that nums[i] + any nums[i+1:j] <= x
                lt += lt_i - i - 1
                lte += lte_i - i - 1

            if lt <= k < lte:
                # If lt <= k < lte then our guess, x, produces the right
                # number of pairs sums to that x is the k-th pair sum.
                # Return the largest existing difference <= x.
                return y
            elif k < lt:
                # If k < lt, there are too many pairs sums that are less than
                # k for our given guess.  We need a smaller guess to reduce the
                # the number of pair sums less than x. Otherwise, increase the
                # guess.
                hi = x - 1
            else:
                lo = x + 1


def test_1():
    nums = [1, 5, 3, 2]
    k = 3
    expected = 2
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [1, 3, 1]
    k = 1
    expected = 2
    assert Solution().solve(nums, k) == expected


def test_3():
    nums = [1, 1, 1]
    k = 2
    expected = 0
    assert Solution().solve(nums, k) == expected


def test_4():
    nums = [1, 6, 1]
    k = 2
    expected = 5
    assert Solution().solve(nums, k) == expected


def test_5():
    "WA"
    nums = [0, 1]
    k = 0
    expected = 1
    assert Solution().solve(nums, k) == expected


def test_6():
    "WA"
    nums = [1, 1, 2]
    k = 1
    expected = 1
    assert Solution().solve(nums, k) == expected
