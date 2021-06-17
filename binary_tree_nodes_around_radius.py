"""
binarysearch.com :: Binary Tree Nodes Around Radius
jramaswami
"""


from collections import defaultdict
from math import inf


def dfs_second_pass(node, parent, radius, distance, acc):
    """
    Traverse tree again, gathering nodes with matching radius.  The distance
    for nodes not in path from root to target is also computed.
    """
    if node is None:
        return
    distance[node.val] = min(distance[node.val], 1 + distance[parent])
    dfs_second_pass(node.left, node.val, radius, distance, acc)
    dfs_second_pass(node.right, node.val, radius, distance, acc)
    if distance[node.val] == radius:
        acc.append(node.val)


def dfs_first_pass(node, target, distance):
    """
    Find the target and while recursing up set the distance to the target node.
    """
    if node is None:
        return inf

    if node.val == target:
        distance[node.val] = 0
    else:
        distance[node.val] = 1 + min(dfs_first_pass(
                                        node.left, target, distance),
                                     dfs_first_pass(
                                        node.right, target, distance))
    return distance[node.val]


class Solution:
    """
    You are given a binary tree root containing unique integers and integers
    target and radius. Return a sorted list of values of all nodes that are
    distance radius away from the node with value target.
    """
    def solve(self, root, target, radius):
        """Solve problem."""
        distance = defaultdict(lambda: inf)
        distance[-1] = inf
        dfs_first_pass(root, target, distance)
        soln = []
        dfs_second_pass(root, -1, radius, distance, soln)
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
