"""
binarysearch.com :: Count BST Nodes in a Range
jramaswami
"""

class Solution:

    def solve(self, root, lo, hi):
        if root is None:
            return 0

        t = self.solve(root.left, lo, hi) + self.solve(root.right, lo, hi)
        if lo <= root.val <= hi:
            t += 1
        return t
