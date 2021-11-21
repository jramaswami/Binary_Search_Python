"""
binarysearch.com :: Tree From Pre/Inorder Traversals
jramaswami
"""


class Solution:

    def solve(self, preorder, inorder):

        def traverse(P, I):
            # Base case:
            if not P:
                return None

            # In the preorder traversal, P, P[0] is the root.
            root = Tree(P[0])

            # Find the index of P[0] in the inorder traversal, I.
            i = I.index(P[0])

            # Recurse
            root.left = traverse(P[1:i+1], I[:i])
            root.right = traverse(P[i+1:], I[i+1:])
            return root

        return traverse(preorder, inorder)