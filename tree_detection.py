"""
binarysearch.com :: Tree Detection
jramaswami
"""


import collections


class Solution:
    def solve(self, left, right):

        # Convert into a adjacency list (set).
        # Also check to make sure each node only has one parent.
        parents = dict()
        adj = [set() for _ in left]
        for u, v in enumerate(left):
            if v >= 0:
                adj[u].add(v)
                adj[v].add(u)
                if v in parents:
                    return False
                parents[v] = u
        for u, v in enumerate(right):
            if v >= 0:
                adj[u].add(v)
                adj[v].add(u)
                if v in parents:
                    return False
                parents[v] = u

        # Tree = acyclic, connected graph.
        visited = [False for _ in left]

        def dfs(node, parent):
            if visited[node]:
                return False

            visited[node] = True
            result = True
            for neighbor in adj[node]:
                if neighbor != parent:
                    result = result and dfs(neighbor, node)
            return result

        return dfs(0, -1)
