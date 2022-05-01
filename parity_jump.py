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
        rgraph = [[] for _ in nums]

        # Find index, i, which can jump directly to an
        # index, j, with an opposite parity number.
        Q = collections.deque()
        for i, n in enumerate(nums):
            if i - n >= 0:
                if parity(i) != parity(i - n):
                    dist[i] = 1
                    Q.append(i)
                else:
                    # Reverse graph: i - n can be reached by i
                    rgraph[i - n].append(i)
            if i + n < len(nums):
                if parity(i) != parity(i + n):
                    dist[i] = 1
                    Q.append(i)
                else:
                    # Reverse graph: i + n can be reached by i
                    rgraph[i + n].append(i)

        # BFS to find answer.
        while Q:
            i = Q.popleft()
            for j in rgraph[i]:
                if dist[j] > dist[i] + 1:
                    dist[j] = dist[i] + 1
                    Q.append(j)

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
