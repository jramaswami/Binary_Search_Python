"""
binarysearch.com :: Tree Pruning
jramaswami
"""


class Solution:
    def solve(self, root):

        def traverse(node):
            if node is None:
                return 0, None

            left_sum, left_node = traverse(node.left)
            right_sum, right_node = traverse(node.right)

            my_sum = left_sum + right_sum + node.val
            if my_sum  > 0:
                return my_sum, Tree(node.val, left_node, right_node)
            return my_sum, None

        _, new_root = traverse(root)
        return new_root
