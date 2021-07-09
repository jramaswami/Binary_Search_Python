"""
binarysearch.com :: Palindromic Tree
jramaswami
"""


class Solution:
    def solve(self, root):
        def inorder(node, acc):
            if node is None:
                return
            inorder(node.left, acc)
            acc.append(node.val)
            inorder(node.right, acc)

        A = []
        inorder(root, A)
        return A == A[::-1]
