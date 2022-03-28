"""
binarysearch.com :: Sibling Tree Value
jramaswami
"""


class Solution:
    def solve(self, root, k):

        def traverse(node, k):
            if node is None:
                return (False, None)

            if node.val == k:
                return (True, None)

            left_found, right_sibling = traverse(node.left, k)
            if left_found:
                if right_sibling is None:
                    right_sibling = node.right.val
                return (left_found, right_sibling)
            right_found, left_sibling = traverse(node.right, k)
            if right_found:
                if left_sibling is None:
                    left_sibling = node.left.val
                return (right_found, left_sibling)
            return (False, None)

        return traverse(root, k)[1]
