"""
binarysearch.com :: Popularity
jramaswami

Notes:
A tree is a connected graph containing no cycles.  A tree will have a distinct
path between every pair of vertices.  The number of distinct paths between an
edge will the product of the number of edges on each side of the edge.

If we augment the tree with size of the subtree for every node, we can compute
the number of nodes on each side of an edge.  From this we can compute the
number of unique paths that use the edge in question.
"""
from collections import defaultdict


def build_graph(edges):
    """Return adjacency list (defaultdict) of graph based on the edges."""
    adj = defaultdict(list)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    return adj


def dfs(node, adj, parent, subtrees):
    """DFS to compute size of subtrees and parentage."""
    if node is None:
        return

    subtrees[node] = 1
    for neighbor in adj[node]:
        if parent[node] != neighbor:
            parent[neighbor] = node
            dfs(neighbor, adj, parent, subtrees)
            subtrees[node] += subtrees[neighbor]


class Solution:
    def solve(self, edges):
        adj = build_graph(edges)
        subtrees = defaultdict(int)
        parent = defaultdict(int)
        root = 0
        parent[root] = -1
        dfs(root, adj, parent, subtrees)
        node_count = subtrees[root]
        soln = []
        for u, v in edges:
            # Swap so u is parent of v
            if parent[u] == v:
                u, v = v, u
                
            # The count of nodes on the v side of the edge
            v_side = subtrees[v]
            # The count of nodes on the u side is the rest of the nodes.
            u_side = node_count - v_side
            # There are v_side * u_side different paths because the 
            # path between every pair of nodes is unique.
            soln.append(u_side * v_side)
        return soln


def test_1():
    edges = [
        [0, 1],
        [1, 2],
        [0, 3]
    ]
    assert Solution().solve(edges) == [4, 3, 3]
