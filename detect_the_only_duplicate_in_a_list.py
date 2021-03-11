"""
binarysearch.com :: Detect the Only Duplicate in a List
jramaswami
"""
class Solution:
    def solve(self, nums):
        N = len(nums) - 1
        S = (N * (N+1)) // 2
        return sum(nums) - S


def test_1():
    nums = [1, 2, 3, 1]
    assert Solution().solve(nums) == 1

def test_2():
    nums = [4, 2, 1, 3, 2]
    assert Solution().solve(nums) == 2
