"""
binarysearch.com :: Partition List to Pairs that Are Divisible by K
jramaswami
"""


import collections


class Solution:

    def solve(self, nums, k):
        freqs = collections.Counter(n % k for n in nums)
        for f in freqs:
            if f == 0:
                # These numbers are directly divisible by k.  They must be
                # paired together so there must be an even number of them..
                if freqs[f] % 2:
                    return False

            else:
                d = k - f
                if d == f:
                    # These numbers pair together so there must be an even
                    # number of them.
                    if freqs[f] % 2:
                        return False
                else:
                    # Pair the numbers freqs[f] with freqs[d] so there must
                    # be the same number of each.
                    if freqs[f] != freqs[d]:
                        return False
        return True


def test_1():
    nums = [4, 8, 2, 1]
    k = 3
    assert Solution().solve(nums, k) == True


def test_2():
    nums = []
    k = 5
    assert Solution().solve(nums, k) == True


def test_3():
    nums = [144, 92, 264, 156, 407, 438, 38, 409, 355, 267, 493, 145, 272, 271, 316, 475, 243, 499, 26, 77]
    k = 3
    assert Solution().solve(nums, k) == False
