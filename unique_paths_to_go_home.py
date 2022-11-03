"""
binarysearch.com :: Weekly Contest 35 :: Unique Paths to Go Home
"""

from collections import namedtuple, defaultdict, deque
from math import inf
import heapq


MOD = pow(10, 9) + 7


Edge = namedtuple('Edge', ['u', 'v', 'wt'])


def other_side(node, edge):
    if node == edge.u:
        return edge.v
    else:
        return edge.u


class Solution:
    def solve(self, edges):
        adj = defaultdict(list)
        home = 0
        for u, v, wt in edges:
            edge = Edge(u, v, wt)
            adj[u].append(edge)
            adj[v].append(edge)
            home = max(home, u, v)

        # dijkstra
        dist = [inf for _ in range(home+1)]
        dist[home] = 0
        queue = [(0, home)]
        while queue:
            d, u = queue[0]
            heapq.heappop(queue)
            if d <= dist[u]:
                for edge in adj[u]:
                    v = other_side(u, edge)
                    if dist[u] + edge.wt < dist[v]:
                        dist[v] = dist[u] + edge.wt
                        heapq.heappush(queue, (dist[v], v))

        # Filter edges
        parents = [0 for _ in range(home+1)]
        for u in range(home+1):
            neighbors = []
            for edge in adj[u]:
                v = other_side(u, edge)
                if dist[u] > dist[v]:
                    neighbors.append(v)
                    parents[v] += 1
            adj[u] = neighbors

        # Topological sort
        toposort = []
        queue = deque(u for u, p in enumerate(parents) if p == 0)
        while queue:
            u = queue.popleft()
            toposort.append(u)
            for v in adj[u]:
                parents[v] -= 1
                if parents[v] == 0:
                    queue.append(v)

        # DP to count paths
        dp = [0 for _ in range(home+1)]
        dp[home] = 1
        for u in toposort[::-1]:
            for v in adj[u]:
                dp[u] = (dp[u] + dp[v]) % MOD
        return dp[0]


def test_1():
    edges = [
        [0, 1, 1],
        [1, 2, 1],
        [2, 3, 1],
        [1, 3, 2]
    ]
    solver = Solution()
    assert solver.solve(edges) == 2


def test_2():
    edges = [
        [0, 1, 1],
        [0, 2, 1],
        [1, 2, 2]
    ]
    solver = Solution()
    assert solver.solve(edges) == 1
