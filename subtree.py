"""
binarysearch.com :: Subtree
jramaswami
"""


class Solution:
    def solve(self, root, target):

        def traverse(node):
            if node is None:
                return False

            return (
                check(node, target) or
                traverse(node.left) or
                traverse(node.right)
            )

        def check(node, target):
            if node is None and target is None:
                return True
            if node is None or target is None:
                return False
            if node.val != target.val:
                return False
            return (check(node.left, target.left) and check(node.right, target.right))

        return traverse(root)