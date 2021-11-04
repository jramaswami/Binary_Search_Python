"""
binarysearch.com :: Sum of Right Leaves
jramaswami

# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""


class Solution:
    def solve(self, root):

        def is_leaf(node):
            return node.left is None and node.right is None

        def traverse(node, is_right):
            if node is None:
                return 0

            if is_leaf(node) and is_right:
                return node.val

            return traverse(node.left, False) + traverse(node.right, True)

        return traverse(root, False)