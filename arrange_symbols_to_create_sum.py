"""
binarysearch.com :: Arrange Symbols to Create Sum
jramaswami
"""


import collections


class Solution:
    def solve(self, nums, target):
        Q = collections.deque()
        Q.append((0, 0))
        soln = 0
        while Q:
            t, i = Q.popleft()
            if i >= len(nums):
                S = []
                if t == target:
                    soln += 1
            else:
                # Add
                Q.append((t + nums[i], i + 1))
                # Subtract
                Q.append((t - nums[i], i + 1))
        return soln


def test_1():
    nums = [1, 2, 2, 2, 1]
    target = 6
    expected = 2
    assert Solution().solve(nums, target) == expected


def test_2():
    """TLE"""
    nums = [2, 4, 3, 0, 3, 5, 1, 2, 2, 5, 6, 4, 9, 8, 2, 0, 4, 7, 0, 2]
    target = 69
    expected = 8
    assert Solution().solve(nums, target) == expected
