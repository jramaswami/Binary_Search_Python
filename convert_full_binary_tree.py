"""
binarysearch.com :: Convert to Full Binary Tree
jramaswami
"""


class Solution:

    def solve(self, root):
        if root is None:
            return None

        root.left = self.solve(root.left)
        root.right = self.solve(root.right)

        if root.left and not root.right:
            return root.left
        if not root.left and root.right:
            return root.right
        return root
