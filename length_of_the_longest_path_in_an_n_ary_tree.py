"""
binarysearch.com :: Length of the Longest Path in an N-Ary Tree
jramaswami
"""
from collections import defaultdict, deque
from heapq import nlargest

# TODO: For any given node the longest path in the tree rooted at that node is:
#       (1) 1 if the node has no children.
#       (2) The longest path to a leaf node in the tree if the node has
#           one child.
#       (3) The sum of the longest two paths to a leaf node for all of the
#           children + 1 for the root node.
#
#       Should be able to recursively or bottom-up.
 

class Solution:
    def solve(self, edges):
        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        nodes = set()
        adj = defaultdict(list)
        for u, v in edges:
            nodes.add(u)
            nodes.add(v)
            indegree[v] += 1
            outdegree[u] += 1
            adj[u].append(v)

        # Find the root and how many leaf nodes.
        leaf_nodes = 0
        for u in nodes:
            if indegree[u] == 0:
                root = u

            if outdegree[u] == 0:
                leaf_nodes += 1

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

        print('root', root, 'leaf_nodes', leaf_nodes)
        # If there is a single leaf node, then the longest path is from
        # that leaf node to the root.
        if leaf_nodes == 1:
            return max(depth.values()) + 1

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
    """What if the tree is a straight line?"""
    edges = [
        [0, 1],
        [1, 2]
    ]
    assert Solution().solve(edges) == 3

def test_3():
    edges = [
        [0, 1],
        [1, 2],
        [1, 3]
    ]
    assert Solution().solve(edges) == 3
