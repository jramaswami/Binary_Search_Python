"""
binarysearch.com :: Complete Binary Tree
jramaswami
"""


class Solution:

    def solve(self, root):
        if root is None:
            return True

        queue = [root]
        new_queue = []
        nonfull_seen = False
        while queue:
            for node in queue:
                if nonfull_seen:
                    # If we have seen a nonfull node, the rest of the nodes
                    # must be leaf nodes.
                    if node.left or node.right:
                        return False
                elif node.left is None and node.right is not None:
                    # If the node has a right child but no left child, this
                    # is not a complete binary tree.
                    return False
                elif not (node.left is not None and node.right is not None):
                    # If this node is not full, then we have now seen a nonfull
                    # node.
                    nonfull_seen = True

                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)

            queue, new_queue = new_queue, []

        return True


#
# TESTING
#


from bscom_trees import *


def test_1():
    root = make_tree([0, [1, [1, null, null], [0, null, null]], [0, [1, null, null], [0, null, null]]])
    expected = True
    assert Solution().solve(root) == expected


def test_2():
    root = make_tree([0, [1, [1, null, null], [0, null, null]], [0, null, null]])
    expected = True
    assert Solution().solve(root) == expected


def test_3():
    root = make_tree([0, [1, null, [0, null, null]], [0, null, null]])
    expected = False
    assert Solution().solve(root) == expected


def test_4():
    "WA"
    root = make_tree([0, [1, [1, null, null], [0, null, null]], null])
    expected = False
    assert Solution().solve(root) == expected


def test_5():
    "RTE"
    root = None
    expected = True
    assert Solution().solve(root) == expected


def test_6():
    "WA"
    root = make_tree([0, null, null])
    expected = True
    assert Solution().solve(root) == expected


def test_7():
    "WA"
    root =  make_tree([14, [8, [4, null, null], [6, [12, null, null], [13, null, null]]], [1, [9, [11, null, null], [7, null, null]], [0, [3, null, null], [5, null, null]]]])
    expected = False
    assert Solution().solve(root) == expected
