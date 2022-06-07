"""
binarysearch.com :: Longest Equivalent Sublist After K Increments
jramaswami
"""


import collections
import heapq
import math


HItem = collections.namedtuple('HItem', ['val', 'index'])


class MaxPriorityQueue:

    def __init__(self):
        self.heap = []

    def push(self, item):
        heapq.heappush(self.heap, (-item.val, item))

    def pop(self):
        heapq.heappop(self.heap)

    def top(self):
        if not self.heap:
            return None
        return self.heap[0][1]


class Solution:

    def solve(self, nums, k):
        window = collections.deque()
        curr_sum = 0
        curr_maxs= MaxPriorityQueue()
        soln = 0
        for i, n in enumerate(nums):
            item = HItem(n, i)
            window.append(item)
            curr_sum += item.val
            curr_maxs.push(item)
            delta = ((curr_maxs.top().val * len(window)) - curr_sum)
            while delta > k:
                curr_sum -= window[0].val
                window.popleft()
                while curr_maxs.top().index < window[0].index:
                    curr_maxs.pop()
                delta = ((curr_maxs.top()[0] * len(window)) - curr_sum)
            soln = max(soln, len(window))
        return soln


def test_1():
    nums = [2, 4, 8, 5, 9, 6]
    k = 6
    expected = 3
    assert Solution().solve(nums, k) == expected


def test_2():
    nums = []
    k = 6
    expected = 0
    assert Solution().solve(nums, k) == expected


def test_3():
    "WA"
    nums = [2,3,1,1]
    k = 0
    expected = 2
    assert Solution().solve(nums, k) == expected
