"""
binarysearch.com :: Pair Matches Larger Than Target
jramaswami
"""
class Solution:
    def solve(self, nums, target):
        nums0 = sorted(nums)
        soln = 0
        right = len(nums) // 2
        for left, b in enumerate(nums0[:len(nums0) // 2]):
            while right < len(nums0) and nums0[right] - b < target:
                right += 1
            if right < len(nums0) and nums0[right] - b >= target:
                right += 1
                soln += 1
        return soln


def test_1():
    nums = [1, 3, 5, 9, 10]
    target = 3
    assert Solution().solve(nums, target) == 2


def test_2():
    """WA"""
    nums = [0, 1, 2, 3]
    target = 3
    assert Solution().solve(nums, target) == 1


def test_3():
    """WA"""
    nums = [0, 1, 2, 2]
    target = 1
    assert Solution().solve(nums, target) == 2


def test_4():
    """WA"""
    nums = [1, 1, 2, 2, 3, 3]
    target = 1
    assert Solution().solve(nums, target) == 3


def test_5():
    """WA"""
    nums = [0, 1, 1, 3]
    target = 2
    assert Solution().solve(nums, target) == 1
