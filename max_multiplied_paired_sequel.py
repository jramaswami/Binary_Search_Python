"""
binarysearch.com :: Max Multiplied Pairings Sequel
jramaswami
"""


from functools import lru_cache


class Solution:

    def solve(self, nums, multipliers):

        @lru_cache(maxsize=None)
        def solve0(left, right, mindex):
            if mindex >= len(multipliers):
                return 0

            # You can take from the left.
            left_soln = (solve0(left + 1, right, mindex + 1) +
                         (nums[left] * multipliers[mindex])
            )
            # You can take from the right.
            right_soln = (solve0(left, right - 1, mindex + 1) +
                          (nums[right] * multipliers[mindex])
            )
            return max(right_soln, left_soln)

        return solve0(0, len(nums) - 1, 0)


def test_1():
    nums = [5, 2, -7]
    multipliers = [2, 4, -1]
    expected = 25
    assert Solution().solve(nums, multipliers) == expected


def test_2():
    nums = [-34, -53, -70, -91, 87, -56, 98, -89, 6, 80, -85, 88, 40, -57, -86, -89, -20, -59, -44, -19, -26, 76, -69, -45, 29, 16, -21, -76, 11, 0, -51, -6, -16, -69, 32, 8, -43, -35, -89, 19, 39, 99, 44, 12, -8, -58, 24, -85, -92, -33, -35, 30, 69, -21, 67, -46, 79, -55, 22, -52, -30, -65, 95, 51, 2, -52, 48, -92, 57, -54, 31, -18, 5, -18, -13, -38, -86, -38, 68, -60, -67, 68, -51, 73, -42, 55, 74, 71, 52, -64, 98, 76, -57, -95, -16, 42, -44, -68, -86, -78]
    multipliers = [-26, -3, 62, 62, -30, 18, 20, -70, 52, -24, 38, 7, -20, 1, -58, -16, 46, 51, 55, -40, 84, -34, 55, 69, 97, -14, -14, 98, 97, -45, -72, 35, -85, 46, 61, -16, -80, -54, 7, 88, 91, 33, -30, 26, 72, -48, -19, -86, 16, 29, 59, 0, 86, -26, 0, -24, -23, 13, 55, -62, 53, -20, 68, -69, 63, 0, -80, 32, 71, -76, 75, 59, 92, -16, 62, 83, 56, 36, 49, -22, -11, -97, -11, 53, -86, -67, 79, 17, -95, 67, -56, -21, -19, -2, -66, 24, -85, -11, 40, 80]
    expected = 228487
    assert Solution().solve(nums, multipliers) == expected


def test_3():
    nums = []
    multipliers = []
    expected = 0
    assert Solution().solve(nums, multipliers) == expected
