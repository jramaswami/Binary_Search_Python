"""
binarysearch.com :: Connected Cities
jramaswami

Kosaraju's Algorithm for Strongly Connected Components
"""

from collections import deque


class Solution:
    def solve(self, node_count, edges):
        # Convert eges into G and G' as adjacency lists.
        adj = [[] for _ in range(node_count)]
        rev_adj = [[] for _ in range(node_count)]
        for u, v in edges:
            adj[u].append(v)
            rev_adj[v].append(u)

        # Get DFS reverse postorder on G'
        visited = [False for _ in rev_adj]
        reverse_postorder = deque()

        def dfs_rp(node):
            visited[node] = True
            for neighbor in rev_adj[node]:
                if not visited[neighbor]:
                    dfs_rp(neighbor)
            reverse_postorder.appendleft(node)

        for u, _ in enumerate(rev_adj):
            if not visited[u]:
                dfs_rp(u)

        # Reset visited
        visited = [False for _ in adj]

        # DFS each node in the reverse postorder of G' on G and count
        # the number of strongly connected components.
        def dfs_scc(node):
            visited[node] = True
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs_scc(neighbor)

        count = 0
        for u in reverse_postorder:
            if not visited[u]:
                count += 1
                dfs_scc(u)

        # The count of SCCs will be 1 if the entire graph is strongly connected.
        return count == 1


def test_1():
    node_count = 2
    edges = [
        [0, 1],
        [1, 0]
    ]
    assert Solution().solve(node_count, edges) == True

def test_2():
    node_count = 2
    edges = [
        [1, 0]
    ]
    assert Solution().solve(node_count, edges) == False