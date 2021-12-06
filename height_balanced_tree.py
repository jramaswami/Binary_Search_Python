"""
binarysearch.com :: Height Balanced Tree
jramaswami
"""


class Solution:

    def solve(self, root):

        def traverse(node):
            if node is None:
                return 0, True

            left_ht, left_ok = traverse(node.left)
            right_ht, right_ok = traverse(node.right)

            my_ht = 1 + max(left_ht, right_ht)
            my_ok = abs(left_ht - right_ht) <= 1 and left_ok and right_ok
            return my_ht, my_ok

        return traverse(root)[1]
