"""
binarysearch.com :: Tree Pruning
jramaswami
"""


class Solution:
    def solve(self, root):

        def traverse(node):
            if node is None:
                return False, None

            left_nonzero, left_node = traverse(node.left)
            right_nonzero, right_node = traverse(node.right)

            my_nonzero = left_nonzero or right_nonzero or (node.val != 0)
            if my_nonzero:
                return my_nonzero, Tree(node.val, left_node, right_node)
            return my_nonzero, None

        _, new_root = traverse(root)
        return new_root
