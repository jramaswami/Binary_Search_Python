"""
binarysearch.com :: A Number and Its Triple
jramaswami
"""

class Solution:
    def solve(self, nums):
        nums0 = set(nums)
        return any((n * 3 in nums0) for n in nums)


def test_1():
    nums = [2, 3, 10, 7, 6]
    assert Solution().solve(nums) == True


def test_2():
    nums = [3, 4, 5]
    assert Solution().solve(nums) == False


def test_3():
    nums = [0, 2, 0]
    assert Solution().solve(nums) == True


def test_4():
    "WA"
    nums = [0]
    assert Solution().solve(nums) == False