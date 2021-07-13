"""
binarysearch.com :: Greatest Common Divisor
jramaswami
"""


from functools import reduce


class Solution:
    def solve(self, nums):

        def gcd(a, b):
            """Recursive GCD."""
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        return reduce(gcd, nums)


def test_1():
    nums = [6, 12, 9]
    assert Solution().solve(nums) == 3


def test_2():
    nums = [6, 7, 9]
    assert Solution().solve(nums) == 1
