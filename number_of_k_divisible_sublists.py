"""
binarysearch.com :: Number of K-Divisible Sublists
jramaswami
"""


import collections


class Solution:

    def solve(self, nums, k):
        soln = curr_sum = 0
        freqs = collections.defaultdict(int)
        for n in nums:
            curr_sum = (curr_sum + n) % k
            if curr_sum == 0:
                soln += 1
            soln += freqs[curr_sum]
            freqs[curr_sum] += 1
        return soln


def test_1():
    nums = [5, 3, 2, 10]
    k = 5
    expected = 6
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [4,5,0,-2,-3,1]
    k = 5
    expected = 7
    assert Solution().solve(nums, k) == expected


def test_3():
    nums = [5]
    k = 9
    expected = 0
    assert Solution().solve(nums, k) == expected