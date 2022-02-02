"""
binarysearch.com :: Minimum Number of Contiguous K-Flips
jramaswami
"""


import collections


class Solution:

    def solve(self, bits, k):
        soln = 0
        flips = collections.deque()
        for i, _ in enumerate(bits):
            while flips and flips[0] <= i:
                flips.popleft()

            b = (bits[i] + len(flips)) % 2
            if b == 1:
                if i + k <= len(bits):
                    # Flip bit.
                    flips.append(i+k)
                    soln += 1
                else:
                    return -1
        return soln


def test_1():
    nums = [1, 1, 0, 1, 1]
    k = 2
    expected = 2
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [1, 1, 1]
    k = 2
    expected = -1
    assert Solution().solve(nums, k) == expected
