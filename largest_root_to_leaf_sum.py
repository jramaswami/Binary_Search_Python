"""
binarysearch.com :: Largest Root to Leaf Sum
jramaswami
"""


class Solution:
    def solve(self, root):

        def traverse(node, acc):
            if node is None:
                return acc

            return max(
                traverse(node.left, acc + node.val),
                traverse(node.right, acc + node.val)
            )

        return traverse(root, 0)
