"""
binarysearch.com :: Largest Tree Sum Path
jramaswami
"""


class Solution:
    def solve(self, root):

        def traverse(node):
            if node is None:
                return 0, 0

            left_max_path, left_max_sum = traverse(node.left)
            right_max_path, right_max_sum = traverse(node.right)

            # Max path is the best "leg" to use.  It can be the best from the
            # right, the best from the left, or just the current node.
            my_max_path = node.val + max(left_max_path, right_max_path, 0)
            # Max sum is the best path sum that is below or including the
            # current node.  It will be either the best sum from the right,
            # the best sum from the left, the node + left leg, the node +
            # right leg, the node + both legs, or even just the node.
            my_max_sum = max(
                left_max_sum,
                right_max_sum,
                node.val,
                node.val + left_max_path,
                node.val + right_max_path,
                node.val + left_max_path + right_max_path
            )

            return my_max_path, my_max_sum

        return traverse(root)[0]


# WA: [5, [-2, null, null], [-2, null, null]]
# WA: [2, [1, [0, null, null], null], [3, null, null]]
