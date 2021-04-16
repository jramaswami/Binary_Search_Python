"""
binarysearch.com :: Pair Matches Larger Than Target
jramaswami
"""
class Solution:
    def solve(self, nums, target):
        nums0 = sorted(nums)
        right = 1
        soln = 0
        for left, b in enumerate(nums0):
            if b is not None:
                for right, a in enumerate(nums0):
                    if left != right and a is not None and b - a <= target:
                        soln += 1
                        nums0[right] = None
                        nums0[left] = None
                        break
        return soln



def test_1():
    nums = [1, 3, 5, 9, 10]
    target = 3
    assert Solution().solve(nums, target) == 2


def test_2():
    """WA"""
    nums = [1, 3, 5, 9, 10]
    target = 3
    assert Solution().solve(nums, target) == 1
