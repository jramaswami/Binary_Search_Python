"""
binarysearch.com :: Leaf Equivalent Trees
jramaswami
"""


class Solution:
    def solve(self, root0, root1):

        def is_leaf(node):
            """Return True if node is a leaf node."""
            return node.left is None and node.right is None

        def inorder(node, acc):
            """Inorder traversal."""
            if node is None:
                return

            inorder(node.left, acc)
            if is_leaf(node):
                acc.append(node.val)
            inorder(node.right, acc)

        leaves0 = []
        inorder(root0, leaves0)
        leaves1 = []
        inorder(root1, leaves1)
        return leaves0 == leaves1

#
# Testing
#


from bscom_trees import *


def test_1():
    root0 = [0, [3, null, [2, null, null]], [1, [1, null, null], null]]
    root1 = [0, [1, null, [2, null, null]], [3, null, [1, null, null]]]
    assert Solution().solve(make_tree(root0), make_tree(root1)) == True


def test_2():
    root0 = [1, [2, null, null], [3, null, null]]
    root1 = [1, [3, null, null], [2, null, null]]
    assert Solution().solve(make_tree(root0), make_tree(root1)) == False