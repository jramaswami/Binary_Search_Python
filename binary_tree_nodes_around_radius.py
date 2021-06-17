"""
binarysearch.com :: Binary Tree Nodes Around Radius
jramaswami
"""


from collections import deque, defaultdict


def tree_to_undirected_graph(root):
    """
    Transform the tree into an undirected graph using BFS.  Return adjacency
    list in form a dictionary.
    """
    adj = defaultdict(list)
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node.left is not None:
            adj[node.val].append(node.left.val)
            adj[node.left.val].append(node.val)
            queue.append(node.left)
        if node.right is not None:
            adj[node.val].append(node.right.val)
            adj[node.right.val].append(node.val)
            queue.append(node.right)
    return adj


def collect_nodes(graph, target, radius):
    """Use BFS to collect nodes that are radius away from target."""
    soln = []
    queue = deque([(target, 0)])
    visited = set([target])
    while queue:
        node, dist = queue.popleft()
        if dist == radius:
            soln.append(node)
        else:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
    return soln


class Solution:
    """
    You are given a binary tree root containing unique integers and integers
    target and radius. Return a sorted list of values of all nodes that are
    distance radius away from the node with value target.
    """
    def solve(self, root, target, radius):
        """Solve problem."""
        graph = tree_to_undirected_graph(root)
        soln = collect_nodes(graph, target, radius)
        return sorted(soln)


#
# Testing
#
from bscom_trees import *


def test_1():
    root = [3, [5, null, null], [2, [1, [6, null, null], [9, null, null]], [4, null, null]]]
    target = 4
    radius = 2
    expected = [1, 3]
    assert Solution().solve(make_tree(root), target, radius) == expected


def test_2():
    root = [0]
    target = 0
    radius = 0
    expected = [0]
    assert Solution().solve(make_tree(root), target, radius) == expected


def test_3():
    """WA"""
    root = [1, [0, null, null], null]
    target = 0
    radius = 1
    expected = [1]
    assert Solution().solve(make_tree(root), target, radius) == expected
