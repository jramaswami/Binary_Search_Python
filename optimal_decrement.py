"""
binarysearch.com :: Optimal Decrement
jramaswami
"""


import heapq


class Solution:

    def solve(self, nums, k):
        nums0 = [-1 * n for n in nums]
        heapq.heapify(nums0)
        for _ in range(k):
            x = heapq.heappop(nums0)
            x += 1
            heapq.heappush(nums0, x)
        return -nums0[0]


def test_1():
    nums = [2, 3, 5, 4]
    k = 6
    expected = 2
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = [5, 5, 5, 5]
    k = 8
    expected = 3
    assert Solution().solve(nums, k) == expected


def test_3():
    nums = [5, 5, 5, 5]
    k = 7
    expected = 4
    assert Solution().solve(nums, k) == expected