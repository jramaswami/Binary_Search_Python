"""
binarysearch.com :: Kth Largest Numbers From Stream
jramaswami
"""


import heapq


class KthLargestStream:
    def __init__(self, nums, k):
        self.heap = list(nums)
        self.k = k + 1
        heapq.heapify(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
