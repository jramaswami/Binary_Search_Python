"""
binarysearch.com :: Subtree with Maximum Value
jramaswami
"""


class Solution:
    def solve(self, root):

        def traverse(node):
            if node is None:
                return 0, 0

            left_subtree_sum, left_subtree_max = traverse(node.left)
            right_subtree_sum, right_subtree_max = traverse(node.right)
            my_subtree_sum = left_subtree_sum + right_subtree_sum + node.val
            my_subtree_max = max(left_subtree_max, right_subtree_max, my_subtree_sum)
            return my_subtree_sum, my_subtree_max

        _, soln = traverse(root)
        return soln
