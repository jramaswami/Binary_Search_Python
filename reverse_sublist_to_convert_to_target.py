"""
binarysearch.com :: Reverse Sublists to Convert to Target
jramaswami
"""
class Solution:
    def solve(self, nums, target):
        return sorted(nums) == sorted(target)


def test_1():
    nums = [1, 2, 3, 8, 9]
    target = [3, 2, 1, 9, 8]
    assert Solution().solve(nums, target) == True

def test_2():
    nums = [10, 2, 3, 8, 9]
    target = [3, 2, 1, 9, 8]
    assert Solution().solve(nums, target) == False

def test_3():
    nums = [3, 4, 5, 5]
    target = [3, 4, 5]
    assert Solution().solve(nums, target) == False

def test_4():
    nums = [5, 3, 2, 3, 0]
    target = [5, 0, 3, 2, 3]
    assert Solution().solve(nums, target) == True
