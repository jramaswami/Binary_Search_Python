"""
binarysearch.com :: Longest Consecutive Sublist
jramaswami

REF: https://www.geeksforgeeks.org/length-largest-subarray-contiguous-elements-set-1/
"""
class Solution:
    def solve(self, nums):
        if nums:
            soln = 1
            for i in range(len(nums) - 1):
                mn = nums[i]
                mx = nums[i]
                for j in range(i + 1, len(nums)):
                    mn = min(mn, nums[j])
                    mx = max(mx, nums[j])
                    if ((mx - mn) == j - i):
                        soln = max(soln, mx - mn + 1)
        else:
            soln = 0
        return soln


def test_1():
    nums = [1, 4, 5, 3, 2, 9]
    assert Solution().solve(nums) == 5

def test_2():
    nums = [2, 4, 6, 8, 3, 5, 7]
    assert Solution().solve(nums) == 7

def test_3():
    nums = []
    assert Solution().solve(nums) == 0
