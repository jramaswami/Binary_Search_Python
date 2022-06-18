"""
binarysearch.com :: Kth Pair Distance
jramaswami

https://www.youtube.com/watch?v=ym93rTBR4j8
Had to convert zero-based to one-based.
"""


class Solution:

    def solve(self, nums, k):
        # Convert zero-based to one-based.
        k += 1

        nums.sort()

        def count_pairs_lte(guess):
            "Return the number of pairs with distance <= guess."
            lte = 0
            j = 1
            for i, _ in enumerate(nums):
                while j < len(nums) and nums[j] - nums[i] <= guess:
                    j += 1
                lte += (j - i - 1)
            return lte

        # Binary search for the answer.
        lo = 0
        hi = nums[-1] - nums[0]
        while lo < hi:
            guess = lo + ((hi - lo) // 2)
            if count_pairs_lte(guess) >= k:
                hi = guess
            else:
                lo = guess + 1
        return lo



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
