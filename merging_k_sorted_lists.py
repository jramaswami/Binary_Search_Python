"""
binarysearch.com :: Merging K Sorted Lists
jramaswami
"""


import heapq


def enqueue(queue, lst, index):
    """Put the list on the queue."""
    if index < len(lst):
        heapq.heappush(queue, (lst[index], lst, index))


class Solution:
    def solve(self, lists):
        soln = []
        queue = []
        for lst in lists:
            enqueue(queue, lst, 0)

        while queue:
            next_item, lst, index = heapq.heappop(queue)
            soln.append(next_item)
            enqueue(queue, lst, index + 1)

        return soln


def test_1():
    lists = [
        [],
        [],
        [10, 12],
        [],
        [3, 3, 13],
        [3],
        [10],
        [0, 7]
    ]
    expected = [0, 3, 3, 3, 7, 10, 10, 12, 13]
    assert Solution().solve(lists) == expected
