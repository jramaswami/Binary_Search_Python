"""
binarysearch.com :: Making Pairwise Adjacent Sums Small
jramaswami
"""


class Solution:
    def solve(self, nums, k):
        MOD = pow(10, 9) + 7
        soln = 0
        nums0 = list(nums)
        for i, _ in enumerate(nums[:-1]):
            while nums[i] + nums[i+1] > k:
                delta = nums[i] + nums[i+1] - k
                if nums[i+1] > 0:
                    delta_actual = min(nums[i+1], delta)
                    soln = (soln + delta_actual) % MOD
                    nums[i+1] -= delta_actual
                else:
                    delta_actual = min(nums[i], delta)
                    soln = (soln + delta_actual) % MOD
                    nums[i] -= delta_actual

        return soln % MOD


def test_1():
    nums = [3, 5, 1, 4]
    k = 4
    assert Solution().solve(nums, k) == 5


def test_2():
    nums = [2, 19, 5, 12, 5, 13, 11, 12, 16, 13, 8, 14, 10, 17, 3, 1, 9, 4, 13, 19]
    k = 4
    assert Solution().solve(nums, k) == 167


def test_3():
    nums = [22, 73, 22, 100, 94, 34, 28, 100, 57, 64, 33, 100, 69, 85, 77, 41, 42, 44, 78, 25, 99, 12, 83, 63, 41, 100, 30, 77, 35, 22, 81, 71, 19, 39, 74, 80, 90, 96, 51, 84, 20, 47, 80, 67, 77, 18, 3, 6, 55, 33, 35, 39, 99, 74, 73, 42, 50, 77, 93, 89, 94, 23, 100, 51, 13, 56, 33, 50, 84, 2, 92, 79, 47, 15, 42, 60, 31, 100, 76, 15, 70, 48, 85, 74, 76, 89, 80, 53, 27, 51, 21, 1, 2, 29, 55, 54, 79, 72, 54, 87]
    k = 10
    assert Solution().solve(nums, k) == 5188


def test_4():
    nums = [22, 73, 22, 100, 94, 34, 28, 100, 57, 64, 33, 100, 69, 85, 77, 41, 42, 44, 78, 25, 99, 12, 83, 63, 41, 100, 30, 77, 35, 22, 81, 71, 19, 39, 74, 80, 90, 96, 51, 84, 20, 47, 80, 67, 77, 18, 3, 6, 55, 33, 35, 39, 99, 74, 73, 42, 50, 77, 93, 89, 94, 23, 100, 51, 13, 56, 33, 50, 84, 2, 92, 79, 47, 15, 42, 60, 31, 100, 76, 15, 70, 48, 85, 74, 76, 89, 80, 53, 27, 51, 21, 1, 2, 29, 55, 54, 79, 72, 54, 87]
    k = 0
    assert Solution().solve(nums, k) == 5682


def test_5():
    """WA"""
    nums = [3, 2, 1, 0, 4]
    k = 0
    assert Solution().solve(nums, k) == 10
