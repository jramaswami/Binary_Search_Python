"""
binarysearch.com :: Path to Maximize Probability to Destination
jramaswami
"""


import math
import collections


class Solution:

    def solve(self, edges, success, source, sink):
        # Turn edges in adjacency list.
        adj = collections.defaultdict(list)
        for (u, v), p in zip(edges, success):
            adj[u].append((v, p))
            adj[v].append((u, p))

        queue = set()
        queue.add(source)
        new_queue = set()
        probs = collections.defaultdict(int)
        probs[source] = 1
        while queue:
            for node in queue:
                for neighbor, p in adj[node]:
                    if probs[node] * p > probs[neighbor]:
                        new_queue.add(neighbor)
                        probs[neighbor] = probs[node] * p
            queue, new_queue = new_queue, set()
        return probs[sink]



EPS = pow(10, -5)

def test_1():
    edges = [
        [0, 1],
        [1, 2],
        [2, 3]
    ]
    success = [0.2, 0.2, 0.5]
    source = 0
    sink = 3
    expected = 0.02
    result = Solution().solve(edges, success, source, sink)
    assert abs(expected - result) <= EPS

