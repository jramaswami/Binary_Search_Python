"""
binarysearch.com :: Longest Tree Sum Path From Root to Leaf
jramaswami
"""


class Solution:
    def solve(self, root):

        def traverse(node, length, acc):
            if node is None:
                return length, acc

            left_length, left_sum = traverse(node.left, length + 1, acc + node.val)
            right_length, right_sum = traverse(node.right, length + 1, acc + node.val)

            if left_length == right_length:
                return left_length, max(left_sum, right_sum)
            elif left_length > right_length:
                return left_length, left_sum
            elif right_length > left_length:
                return right_length, right_sum

        return traverse(root, 0, 0)[1]
