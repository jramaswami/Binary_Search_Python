"""
binarysearch.com :: Max XOR of Two Integers
jramaswmai
"""


class Solution:

    def solve(self, nums):
        soln = mask = 0
        for bit in reversed(range(32)):
            mask |= (1 << bit)
            prefixes = set(n & mask for n in nums)
            candidate = soln | (1 << bit)
            if any((p ^ candidate in prefixes) for p in prefixes):
                soln = candidate
        return soln


def test_1():
    nums = [1, 2, 3, 7]
    expected = 6
    assert Solution().solve(nums) == expected


def test_2():
    nums = [3,10,5,25,2,8]
    expected = 28
    assert Solution().solve(nums) == expected


def test_3():
    nums = [14,70,53,83,49,91,36,80,92,51,66,70]
    expected = 127
    assert Solution().solve(nums) == expected


def test_4():
    nums = [8]
    expected = 0
    assert Solution().solve(nums) == expected
