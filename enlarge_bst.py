"""
binarysearch.com :: Enlarge BST
jramaswami
"""


from collections import deque


def collect_inorder(node, acc):
    """In order traversal collection of nodes into acc."""
    if node is None:
        return
    collect_inorder(node.left, acc)
    acc.append(node.val)
    collect_inorder(node.right, acc)


def enlarge_inorder(node, new_vals):
    """In order traversal enlargement of nodes."""
    if node is None:
        return None
    enlarge_inorder(node.left, new_vals)
    node.val = new_vals.popleft()
    enlarge_inorder(node.right, new_vals)


class Solution:
    def solve(self, root):
        inorder_traversal = []
        collect_inorder(root, inorder_traversal)
        suffix_sums = deque(inorder_traversal)
        prev = 0
        for i in range(len(suffix_sums) - 1, -1, -1):
            suffix_sums[i] = prev + inorder_traversal[i]
            prev += inorder_traversal[i]
        enlarge_inorder(root, suffix_sums)
        return root

#
# Testing
#


from bscom_trees import *


def test_1():
    root = make_tree([4, [2, [1, null, null], [3, null, null]], [5, null, null]])
    expected = make_tree([9, [14, [15, null, null], [12, null, null]], [5, null, null]])
    assert Solution().solve(root) == expected

