"""
binarysearch.com :: Add One To List
jramaswami
"""


class Solution:
    def solve(self, nums):
        nums0 = nums[::-1]
        nums0[0] += 1
        carry = 0
        for i, n in enumerate(nums0):
            carry, nums0[i] = divmod(n + carry, 10)
        if carry:
            nums0.append(carry)
        return nums0[::-1]


def test_1():
    nums = [1, 9, 2]
    expected = [1, 9, 3]
    assert Solution().solve(nums) == expected


def test_2():
    nums = [9]
    expected = [1, 0]
    assert Solution().solve(nums) == expected


def test_3():
    nums = [1, 9, 9]
    expected = [2, 0, 0]
    assert Solution().solve(nums) == expected
