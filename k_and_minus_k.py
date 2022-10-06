"""
binarysearch.com :: K and -K
jramaswami
"""

class Solution:
    def solve(self, nums):
        soln = -1
        nums0 = set(nums)
        for n in nums0:
            if -n in nums0:
                soln = max(soln, abs(n))
        return soln


def test_1():
    nums = [-4, 1, 8, -5, 4, -8]
    expected = 8
    assert Solution().solve(nums) == expected


def test_2():
    nums = [5, 6, 1, -2]
    expected = -1
    assert Solution().solve(nums) == expected


def test_3():
    nums = [1, 2, 0, 3, 4]
    expected = 0
    assert Solution().solve(nums) == expected