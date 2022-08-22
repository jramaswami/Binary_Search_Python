"""
binarysearch.com :: Longest Sublist with Absolute Difference Condition
jramaswami
"""


import heapq
from collections import namedtuple


Element = namedtuple('Element', ['value', 'index'])


def remove(queue, new_left):
    """Remove all items in the queue up to the new left index."""
    while queue and queue[0].index < new_left:
        heapq.heappop(queue)


def queue_delta(min_queue, max_queue):
    """Return the difference between the max_queue and min_queue values."""
    return (-max_queue[0].value) - min_queue[0].value


class Solution:
    def solve(self, nums, k):
        soln = 0
        max_queue = []
        min_queue = []
        left = 0
        for right, n in enumerate(nums):
            heapq.heappush(max_queue, Element(-n, right))
            heapq.heappush(min_queue, Element(n, right))
            while queue_delta(min_queue, max_queue) > k:
                left += 1
                remove(min_queue, left)
                remove(max_queue, left)
            soln = max(soln, right - left + 1)
        return soln


def test_1():
    nums = [1, 3, 5, 9]
    k = 4
    assert Solution().solve(nums, k) == 3


def test_2():
    nums = [6, 18, 16, 16, 11, 14, 12, 7, 10, 12, 9, 1, 19, 19, 14, 4, 10, 7, 18, 12]
    k = 4
    assert Solution().solve(nums, k) == 3


def test_3():
    nums = [6, 20, 20, 10, 2, 4, 10, 5, 14, 9, 5, 13, 12, 3, 8, 4, 12, 5, 5, 11]
    k = 10
    assert Solution().solve(nums, k) == 11


def test_4():
    nums = [11, 11, 9, 6, 4, 2, 18, 20, 6, 6, 14, 18, 17, 15, 8, 17, 6, 14, 8, 4, 6, 14, 18, 16, 13, 18, 20, 10, 5, 20, 10, 15, 11, 18, 6, 10, 15, 4, 4, 12, 9, 18, 12, 6, 2, 4, 2, 6, 10, 17, 15, 14, 7, 16, 19, 18, 6, 9, 18, 9, 11, 6, 12, 8, 19, 1, 14, 2, 15, 17, 12, 19, 12, 18, 3, 20, 12, 1, 17, 4, 2, 13, 20, 10, 9, 14, 19, 8, 17, 18, 5, 3, 5, 19, 12, 9, 13, 1, 8, 11]
    k = 10
    assert Solution().solve(nums, k) == 7


def test_5():
    nums = [6]
    k = 1
    assert Solution().solve(nums, k) == 1


def test_6():
    nums = []
    k = 1
    assert Solution().solve(nums, k) == 0