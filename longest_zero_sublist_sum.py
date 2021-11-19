"""
binarysearch.com :: Longest Zero Sublist Sum
jramaswami
"""


import collections
import math


class Solution:

    def solve(self, nums):
        visited = collections.defaultdict(lambda: math.inf)
        curr_sum = 0
        soln = 0
        # We start with a zero sum, so mark it as visited.
        visited[0] = -1
        for i, n in enumerate(nums):
            curr_sum += n
            visited[curr_sum] = min(visited[curr_sum], i)
            # curr_sum - target = 0
            # curr_sum = target
            # Have we seen this sum before?
            soln = max(soln, i - visited[curr_sum])
        return soln


def test_1():
    nums = [1, 1, 1, 1, -1, -1, 1, -1]
    expected = 6
    assert Solution().solve(nums) == expected


def test_2():
    nums = [-1, 1]
    expected = 2
    assert Solution().solve(nums) == expected


def test_3():
    nums = []
    expected = 0
    assert Solution().solve(nums) == expected