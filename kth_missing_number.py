"""
binarysearch.com :: Kth Missing Number
jramaswami
"""


class Solution:
    def solve(self, nums, k):
        for x, y in zip(nums[:-1], nums[1:]):
            if y - x != 1:
                # How many missing numbers.
                d = y - x - 1
                print(f"{x=} {y=} {d=} {k=}")
                if d >= k:
                    # Our missing number is here
                    return x + 1 + k
                # Our missing number is still beyond, but count what
                # the past missing numbers
                k -= d
        # If we reach here there weren't enough numbers missing.
        return nums[-1] + 1 + k


def test_1():
    nums = [5, 6, 8, 9]
    k = 0
    expected = 7
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [5, 6, 8, 9]
    k = 3
    expected = 12
    assert Solution().solve(nums, k) == expected


def test_3():
    "WA"
    nums = [2, 5]
    k = 2
    expected = 5
    assert Solution().solve(nums, k) == expected