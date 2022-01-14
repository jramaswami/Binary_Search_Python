"""
binarysearch.com :: Elephant Tree
jramaswami
"""


class Solution:
    def solve(self, root):

        def get_val(node):
            if node is None:
                return 0
            return node.val

        def traverse(node):
            if node is None:
                return None

            new_node = Tree(node.val)
            new_node.left = traverse(node.left)
            new_node.right = traverse(node.right)
            new_node.val += get_val(new_node.left) + get_val(new_node.right)
            return new_node

        return traverse(root)
