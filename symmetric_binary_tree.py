"""
binarysearch.com :: Symmetric Binary Tree
jramaswami
"""


class Solution:
    def solve(self, root):

        def equal_trees(A, B):
            # Both trees are None at this node.
            if A is None and B is None:
                return True

            # One tree is None but the other is not.
            if A is None:
                return False

            # One tree is None but the other is not.
            if B is None:
                return False

            # Both trees have nodes ...
            if A.val != B.val:
                return False

            return (
                equal_trees(A.right, B.left) and
                equal_trees(A.left, B.right)
            )

        if root is None:
            return True
        return equal_trees(root.left, root.right)
