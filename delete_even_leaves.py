"""
binarysearch.com :: Delete Even Leaves
jramaswami
"""


class Solution:

    def solve(self, root):

        def is_even_leaf(node):
            return node.val % 2 == 0 and node.left is None and node.right is None

        def traverse(node):
            if node is None:
                return None

            if is_even_leaf(node):
                return None

            node.left = traverse(node.left)
            node.right = traverse(node.right)

            if is_even_leaf(node):
                return None

            return node

        return traverse(root)
