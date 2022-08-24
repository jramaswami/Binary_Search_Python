"""
binarysearch.com :: Profitable Job Matching
jramaswami
"""


import heapq


class MaxPQ:
    def __init__(self):
        self.heap = []

    def push(self, x):
        heapq.heappush(self.heap, -x)

    def pop(self):
        if not self.heap:
            raise Exception("MaxPQ is empty.")
        return -heapq.heappop(self.heap)

    def top(self):
        return -self.heap[0]

    def __len__(self):
        return len(self.heap)


class Solution:
    def solve(self, people, jobs, profits):
        A = list(sorted(zip(jobs, profits),reverse=True))
        people.sort()
        Q = MaxPQ()
        profit = 0
        for p in people:
            while A and A[-1][0] <= p:
                Q.push(A[-1][1])
                A.pop()
            if Q:
                profit += Q.top()
        return profit


def test_1():
    people = [5, 7, 8]
    jobs = [6, 5, 8]
    profits = [1, 2, 3]
    expected = 7
    assert Solution().solve(people, jobs, profits) == expected