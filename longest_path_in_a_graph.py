"""
binarysearch.com :: Longest Path In A Graph
jramaswami
"""


import collections


class Solution:

    def solve(self, graph):
        # Determine indegree of each node.
        indegree = [0 for _ in graph]
        for u, neighbors in enumerate(graph):
            for v in neighbors:
                indegree[v] += 1

        # Kahn's algorithm to get topological sort.
        kahnq = collections.deque(n for n, d in enumerate(indegree) if d == 0)
        topo = []
        while kahnq:
            u = kahnq.popleft()
            topo.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    kahnq.append(v)

        # Use topological sort to find longest path.
        dist = [0 for _ in graph]
        for u in topo:
            for v in graph[u]:
                dist[v] = max(dist[v], dist[u]+1)
        return max(dist)


def test_1():
    graph = [ [1, 3], [2, 5], [4], [1, 4], [5], [] ]
    expected = 5
    assert Solution().solve(graph) == expected


def test_2():
    graph = [ [], [0, 3], [0, 1], [] ]
    expected = 2
    assert Solution().solve(graph) == expected