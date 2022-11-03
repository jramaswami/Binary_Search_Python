"""
binarysearch.com :: Weekly Contest 41 :: Consecutive Ones
jramaswami
"""
class Solution:
    def solve(self, nums):
        ones_indices = [i for i, v in enumerate(nums) if v == 1]
        return all(b - a == 1 for a, b in zip(ones_indices[:-1], ones_indices[1:]))


def test_1():
    nums = [0, 1, 1, 1, 2, 3]
    assert Solution().solve(nums) == True

def test_2():
    nums = [1, 1, 0, 1, 1]
    assert Solution().solve(nums) == False

