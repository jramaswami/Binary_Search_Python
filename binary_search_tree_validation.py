"""
binarysearch.com :: Binary Search Tree Validation
jramaswami
"""


from math import inf


class Solution:
    def solve(self, root):

        def solve0(node):
            if node is None:
                return True, inf, -inf

            lvalid, lmin, lmax = solve0(node.left)
            rvalid, rmin, rmax = solve0(node.right)

            return ((lvalid and rvalid and lmax < node.val and rmin > node.val),
                    min(lmin, rmin, node.val), max(lmax, rmax, node.val))

        return solve0(root)[0]
