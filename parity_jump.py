"""
binarysearch.com :: Parity Jump
jramaswami
"""


import math
import collections


class Solution:

    def solve(self, nums):

        def parity(index):
            return nums[index] % 2

        dist = [math.inf for _ in nums]

        # Find index, i, which can jump directly to an
        # index, j, with an opposite parity number.
        Q = collections.deque()
        for i, n in enumerate(nums):
            if i - n >= 0 and parity(i) != parity(i - n):
                dist[i] = 1
                Q.append(i)
            elif i + n < len(nums) and parity(i) != parity(i + n):
                dist[i] = 1
                Q.append(i)

        # BFS to find answer.
        while Q:
            i = Q.popleft()
            if i - n >= 0 and dist[i - n] > dist[i] + 1:
                Q.append(i - n)
                dist[i - n] = dist[i] + 1
            if i + n < len(nums) and dist[i + n] > dist[i] + 1:
                Q.append(i + n)
                dist[i + n] = dist[i] + 1

        return [-1 if d == math.inf else d for d in dist]


def test_1():
    nums = [5, 1, 2, 3, 4, 7, 4, 5]
    expected = [-1, 1, 1, 1, 1, -1, 2, 1]
    assert Solution().solve(nums) == expected


def test_2():
    "WA"
    nums = [6, 6, 1, 1, 2, 2, 7, 4, 9, 5]
    expected = [1, 2, 1, 1, 1, 1, -1, 1, -1, 1]
    assert Solution().solve(nums) == expected
