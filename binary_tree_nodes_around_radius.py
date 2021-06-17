"""
binarysearch.com :: Binary Tree Nodes Around Radius
jramaswami
"""


from collections import deque
from math import inf


def path_to_target(node, target, radius, acc):
    """
    Use dfs to find the path from root to target as well as the distance
    from each one to the target.  Only include nodes that are within the
    radius from target.
    """
    if node is None:
        return inf

    if node.val == target:
        acc.append((node, 0))
        return 0

    left_dist = 1 + path_to_target(node.left, target, radius, acc)
    right_dist = 1 + path_to_target(node.right, target, radius, acc)
    if left_dist <= radius:
        acc.append((node, left_dist))
        return left_dist

    if right_dist <= radius:
        acc.append((node, right_dist))
        return right_dist

    return inf


class Solution:
    """
    You are given a binary tree root containing unique integers and integers
    target and radius. Return a sorted list of values of all nodes that are
    distance radius away from the node with value target.
    """
    def solve(self, root, target, radius):
        """Solve problem."""
        queue = deque()
        path_to_target(root, target, radius, queue)
        visited = set()
        for node, _ in queue:
            visited.add(node.val)

        # BFS to find elements within radius
        soln = []
        while queue:
            node, dist = queue.popleft()
            if dist == radius:
                soln.append(node.val)
            else:
                if node.left and node.left.val not in visited:
                    queue.append((node.left, dist + 1))
                    visited.add(node.left.val)
                if node.right and node.right.val not in visited:
                    queue.append((node.right, dist + 1))
                    visited.add(node.right.val)
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
