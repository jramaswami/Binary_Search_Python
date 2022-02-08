"""
binarysearch.com :: Distributed Systems
jramawami
"""


import heapq
import math


class Solution:

    def solve(self, node_count, edges):
        # Convert edges to adjacency list.
        adj = [[] for _ in range(node_count+1)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        # Dijkstra's algorithm
        distance = [math.inf for _ in adj]
        distance[0] = 0

        queue = [(0, 0)]
        while queue:
            du, u = heapq.heappop(queue)
            if distance[u] != du:
                continue

            for v, dv in adj[u]:
                if du + dv < distance[v]:
                    distance[v] = du + dv
                    heapq.heappush(queue, (distance[v], v))
        return max(distance)


def test_1():
    n = 3
    edges = [
        [0, 1, 2],
        [1, 2, 3],
        [2, 3, 1]
    ]
    expected = 6
    assert Solution().solve(n, edges) == expected


def test_2():
    n = 3
    edges = [
        [0, 1, 2],
        [0, 2, 3],
        [0, 3, 5]
    ]
    expected = 5
    assert Solution().solve(n, edges) == expected
