"""
binarysearch.com :: Number of Non-Overlapping Sublists With Sum of Target
jramaswami
"""


class Solution:
    def solve(self, nums, target):
        soln = 0
        prev_sums = set([0])
        curr_sum = 0
        for n in nums:
            curr_sum += n
            if curr_sum - target in prev_sums:
                soln += 1
                curr_sum = 0
                prev_sums = set([0])
            else:
                prev_sums.add(curr_sum)
        return soln


def test_1():
    nums = [4, 3, 7, 5, -3, 10]
    target = 7
    assert Solution().solve(nums, target) == 3


def test_2():
    nums = []
    target = 7
    assert Solution().solve(nums, target) == 0

