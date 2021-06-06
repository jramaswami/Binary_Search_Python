"""
binarysearch.com :: Twin Trees
jramaswami
"""


# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def solve(self, root0, root1):
        # If both subtrees are None, ok.
        if root0 is None and root1 is None:
            return True

        # If one subtree is None and the other is not, false.
        if root0 is None:
            return False
        if root1 is None:
            return False

        # Subtrees are equal if value of the root node is equal
        # an the left and subtrees are equal.
        return (root0.val == root1.val and 
                self.solve(root0.left, root1.left) and
                self.solve(root0.right, root1.right))
