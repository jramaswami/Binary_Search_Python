"""
binarysearch.com :: Largest Tree Sum Path
jramaswami
"""


class Solution:
    def solve(self, root):

        def traverse(node):
            if node is None:
                return 0, 0

            max_left, sum_left = traverse(node.left)
            max_right, sum_right = traverse(node.right)

            my_max = max(max_left, max_right, node.val + sum_left + sum_right)
            my_sum = max(max_left, max_right) + node.val
            return my_max, my_sum

        return traverse(root)[0]


# WA: [5, [-2, null, null], [-2, null, null]]
