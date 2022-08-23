"""
binarysearch.com :: Complete an Arithmetic Sequence
jramaswami
"""

def sum_arithmetic_sequence(ai, an, N):
    """Return the sum of the arithmetic sequence given a[i], a[N], and N."""
    return (N * (ai + an)) // 2


class Solution:
    def solve(self, nums):
        # Sum of arithmetic sequence is S[n] = (n(a[i] + a[n])) // 2
        return sum_arithmetic_sequence(nums[0], nums[-1], len(nums) + 1) - sum(nums)


def test_1():
    nums = [1, 3, 5, 9]
    assert Solution().solve(nums) == 7


def test_2():
    nums = [10, 7, 1, -2]
    assert Solution().solve(nums) == 4


def test_3():
    nums = [-10, -6, -2, 6, 10]
    assert Solution().solve(nums) == 2


def test_4():
    nums= [0, 0]
    assert Solution().solve(nums) == 0


def test_5():
    nums = [4, 12]
    assert Solution().solve(nums) == 8


def test_6():
    nums = [6, 2, 0]
    assert Solution().solve(nums) == 4


def test_7():
    nums = [0, 0, 0, 0]
    assert Solution().solve(nums) == 0