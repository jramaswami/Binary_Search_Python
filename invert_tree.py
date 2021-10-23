"""
binarysearch.com :: Invert Tree
jramaswami
"""


class Solution:
    def solve(self, root):

        def traverse(node):
            if node is None:
                return

            node.left, node.right = node.right, node.left
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return root
