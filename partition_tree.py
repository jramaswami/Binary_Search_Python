"""
binarysearch.com :: Partition Tree
jramaswami
"""


class Solution:
    def solve(self, root):

        def traverse(node):
            if node is None:
                return (0, 0)

            if node.left is None and node.right is None:
                return (1, 1)

            left_nodes, left_leaves = traverse(node.left)
            right_nodes, right_leaves = traverse(node.right)
            return (left_nodes + right_nodes + 1, left_leaves + right_leaves)


        total_nodes, leaf_nodes = traverse(root)
        return leaf_nodes, total_nodes - leaf_nodes
