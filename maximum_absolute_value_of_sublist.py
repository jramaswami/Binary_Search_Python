"""
binarysearch.com :: Maximum Absolute Value of Sublist
jramaswami
"""
def kadanes(arr):
    max_so_far = 0
    max_ending_here = 0
    for n in arr:
        max_ending_here = max_ending_here + n
        max_so_far = max(max_so_far, max_ending_here)
        max_ending_here = max(max_ending_here, 0)
    return max_so_far


class Solution:
    def solve(self, nums):
        return max(kadanes(nums), kadanes([-n for n in nums]))
       

def test_1():
    nums = [5, -7, -2, 4]
    assert Solution().solve(nums) == 9

