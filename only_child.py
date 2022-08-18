"""
binarysearch.com :: Only Child
jramaswami
"""


class Solution:

    def solve(self, root):

        def traverse(node, children):
            if node is None:
                return 0

            children0 = (
                (0 if node.left is None else 1) +
                (0 if node.right is None else 1)
            )

            only_child = (1 if children == 1 else 0)
            return (
                only_child +
                traverse(node.left, children0) +
                traverse(node.right, children0)
            )

        return traverse(root, 0)