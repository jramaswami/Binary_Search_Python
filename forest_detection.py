"""
binarysearch.com :: Forest Detection
jramaswami
"""


import collections


class Solution:
    def solve(self, edges):

        def dfs(u, p, adj, visited):
            """DFS to determine if graph is tree."""
            visited.add(u)
            is_tree = True
            for v in adj[u]:
                # Ignore parent
                if v == p:
                    continue

                if v in visited:
                    is_tree = False

                is_tree = is_tree and dfs(v, u, adj, visited)

            return is_tree

        # Build graph
        adj = collections.defaultdict(list)
        vertices = set()
        for u, v in edges:
            vertices.add(u)
            vertices.add(v)
            adj[u].append(v)
            adj[v].append(u)

        # DFS
        visited = set()
        for u in vertices:
            if u not in visited:
                if not dfs(u, None, adj, visited):
                    return False
        return True


def test_1():
    edges = [
        [0, 1],
        [0, 2],
        [3, 4],
        [4, 5]
    ]
    expected = True
    assert Solution().solve(edges) == expected


def test_2():
    edges = [
        [0, 1],
        [1, 2],
        [0, 2]
    ]
    expected = False
    assert Solution().solve(edges) == expected
