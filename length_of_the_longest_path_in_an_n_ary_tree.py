"""
binarysearch.com :: Length of the Longest Path in an N-Ary Tree
jramaswami
"""
from collections import defaultdict, deque
from heapq import nlargest


class Solution:
    def solve(self, edges):
        indegree = defaultdict(int)
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            indegree[v] += 1

        # Find the root
        for u in adj:
            if indegree[u] == 0:
                root = u

        # Walk tree chart depth
        depth = dict()
        queue = deque()
        queue.append(root)
        depth[root] = 0
        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if v not in depth:
                    depth[v] = depth[u] + 1
                    queue.append(v)

        # If depth is k then there are k + 1 nodes in the path
        # So the path from leaf to leaf is depth[1] + 1 + depth[2] + 1.
        # But we are double counting the root, so subtract 1.
        # depth[1] + 1 + depth[2]
        soln = sum(nlargest(2, depth.values())) + 1
        return soln


def test_1():
    edges = [
        [1, 2],
        [1, 3],
        [1, 4],
        [4, 5]
    ]
    assert Solution().solve(edges) == 4

def test_2():
    edges = [
        [0, 1],
        [1, 2]
    ]
    assert Solution().solve(edges) == 3
