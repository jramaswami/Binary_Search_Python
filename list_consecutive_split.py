"""
binarysearch.com :: List Consecutive Split
jramaswami
"""


import collections


class Solution:

    def solve(self, nums, k):
        if len(nums) % k:
            return False
        freqs = collections.Counter(nums)
        for _ in range(len(nums) // k):
            start = min(freqs)
            for x in range(start, start+k):
                if freqs[x] == 0:
                    print('failed', seq)
                    return False
                freqs[x] -= 1
                if freqs[x] == 0:
                    del freqs[x]
        return True


def test_1():
    nums = [3, 2, 3, 4, 5, 1]
    k = 3
    assert Solution().solve(nums, k) == True


def test_2():
    "WA"
    nums = [0, 0]
    k = 1
    assert Solution().solve(nums, k) == True


def test_3():
    "WA"
    nums = [0, 1, 1, 3]
    k = 2
    assert Solution().solve(nums, k) == False