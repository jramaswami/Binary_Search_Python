"""
binarysearch.com :: Pair Matches Larger Than Target
jramaswami
"""
class Solution:
    def solve(self, nums, target):
        nums0 = sorted(nums)
        soln = 0
        partition = len(nums) // 2
        for left, b in enumerate(nums[:len(nums) // 2]):
            for right, a in enumerate(nums[partition:], start=partition):
                if a - b >= target:
                    soln += 1
                    partition = right + 1
                    break
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
