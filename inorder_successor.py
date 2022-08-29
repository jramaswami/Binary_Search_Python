"""
binarysearch.com :: Inorder Successor
jramaswami
"""


import math


class Solution:

    def solve(self, root, t):
        def inorder(node, t, found_already, successor):
            # Base case.
            if node is None:
                return found_already, successor

            found_left, successor = inorder(node.left, t, found_already, successor)
            found_already = (found_already or node.val == t)
            found_right, successor = inorder(node.right, t, found_already, successor)
            found_already = (found_already or found_left or found_right)
            if found_already and (t < node.val < successor):
                successor = node.val
            return found_already, successor

        return inorder(root, t, False, math.inf)[1]
