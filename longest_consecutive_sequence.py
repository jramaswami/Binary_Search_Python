"""
binarysearch.com :: Longest Consecutive Sequence
jramaswami
"""
class Solution:
    def solve(self, nums):
        if nums == []:
            return 0
        nums0 = sorted(nums)
        curr = 1
        soln = 1
        for a, b in zip(nums0[:-1], nums0[1:]):
            if a + 1 == b:
                curr += 1
            else:
                curr = 1
            soln = max(curr, soln)
        return soln



def test_1():
    nums = [100, 4, 200, 1, 3, 2]
    assert Solution().solve(nums) == 4


def test_2():
    nums = [100, 4, 200, 1, 3, 2, 101, 105, 103, 102, 104]
    assert Solution().solve(nums) == 6


def test_3():
    """WA"""
    nums = [1, 2, 1, 0]
    assert Solution().solve(nums) == 3
