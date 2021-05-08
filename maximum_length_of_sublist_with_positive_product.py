"""
binarysearch.com :: Maximum Length of Sublist with Positive Product
jramaswami
"""


def sign(n):
    """Return the sign of n."""
    if n < 0:
        return -1
    elif n > 0:
        return 1
    else:
        return 0


class Solution:
    def solve(self, nums):
        signs = [sign(n) for n in nums]
        curr_sign = 1
        left_neg = -1
        left_start = 0
        soln = 0
        for i, n in enumerate(nums):
            curr_sign = curr_sign * sign(n)
            if curr_sign == 0:
                left_neg = -1
                left_start = i + 1
                curr_sign = 1
            elif curr_sign < 0:
                # exclude the left most negative sign
                if left_neg >= 0:
                    soln = max(soln, i - left_neg)
                else:
                    left_neg = i
            elif curr_sign > 0:
                soln = max(soln, i - left_start + 1)
        return soln


def test_1():
    nums = [-1, 1, 2, -1, 1, 0, 1]
    assert Solution().solve(nums) == 5


def test_2():
    nums = [0, 0]
    assert Solution().solve(nums) == 0


def test_3():
    nums = [0, 1, 0, -1, 0, 1, -1, -1, 1, 0, 1, 0, 1, -1, -1, 0, 1, -1, -1, 0]
    assert Solution().solve(nums) == 4


def test_4():
    nums = [1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, 1, 1, 1, 1, 1, 1]
    assert Solution().solve(nums) == len(nums)


def test_5():
    assert Solution().solve([]) == 0