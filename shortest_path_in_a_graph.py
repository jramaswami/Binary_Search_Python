"""
binarysearch.com :: Shortest Path in a Graph
jramaswami
"""


import heapq
from collections import defaultdict
from math import inf


class Solution:

    def solve(self, edges, source, sink):
        adj = defaultdict(list)
        for u, v, wt in edges:
            adj[u].append((v, wt))

        dist = defaultdict(lambda: inf)
        queue = []
        dist[source] = 0
        heapq.heappush(queue, (dist[source], source))
        while queue:
            d, u = heapq.heappop(queue)
            if d != dist[u]:
                continue

            for v, wt in adj[u]:
                if wt + dist[u] < dist[v]:
                    dist[v] = wt + dist[u]
                    heapq.heappush(queue, (dist[v], v))

        return dist[sink] if dist[sink] < inf else -1


def test_1():
    edges = [
        [0, 1, 3],
        [1, 2, 2],
        [0, 2, 9]
    ]
    source = 0
    sink = 2
    assert Solution().solve(edges, source, sink) == 5


def test_2():
    edges = [
        [0, 1, 3],
        [1, 2, 2],
        [0, 2, 9]
    ]
    source = 0
    sink = 7
    assert Solution().solve(edges, source, sink) == -1

