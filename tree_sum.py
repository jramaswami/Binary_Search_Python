"""
binarysearch.com :: Tree Sum
jramaswami
"""


class Solution:
    def solve(self, root):

        def solve0(node):
            if node is None:
                return 0
            return solve0(node.left) + solve0(node.right) + node.val

        return solve0(root)
