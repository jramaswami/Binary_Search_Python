"""
binarysearch.com :: Costly Flight of Stairs
jramaswami
"""


import heapq
import collections


QItem = collections.namedtuple('QItem', ['cost', 'index'])


class Solution:

    def solve(self, stairs, k):
        # Sliding window
        soln = 0
        if stairs:
            Q = [QItem(stairs[0], 0)]
            for i, curr_cost in enumerate(stairs[1:], start=1):
                # Clear any "stale" stairs
                while Q and Q[0].index < i - k:
                    heapq.heappop(Q)

                item = QItem(Q[0].cost + curr_cost, i)
                # The last stair will be the last cost.
                soln = item.cost
                heapq.heappush(Q, item)
        return soln


def test_1():
    stairs = [3, 10, 10, 2, 1]
    k = 3
    expected = 6
    assert Solution().solve(stairs, k) == expected


def test_2():
    stairs = []
    k = 7
    expected = 0
    assert Solution().solve(stairs, k) == expected
