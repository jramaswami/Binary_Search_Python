"""
binarysearch.com :: Number of K-Length Sublists with Average at Least Target
jramaswami
"""


class Solution:
    def solve(self, nums, k, target):
        soln = 0
        i = 0
        curr_sum = sum(nums[:k])
        if curr_sum / k >= target:
            soln += 1
        for j, _ in enumerate(nums[k:], start=k):
            curr_sum -= nums[i]
            i += 1
            curr_sum += nums[j]
            if curr_sum / k >= target:
                soln += 1
        return soln



def test_1():
    nums = [0, 9, 4, 5, 6]
    k = 3
    target = 5
    expected = 2
    assert Solution().solve(nums, k, target) == expected


def test_2():
    nums = []
    k = 3
    target = 5
    expected = 0
    assert Solution().solve(nums, k, target) == expected
