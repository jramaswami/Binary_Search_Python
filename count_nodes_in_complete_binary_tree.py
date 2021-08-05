"""
binarysearch.com :: Count Nodes in Complete Binary Tree

Given a complete binary tree root, return the number of nodes in the tree.

This should be done in O((log n)^2).
"""


class Solution:
    def solve(self, root):


        def get_height(node, acc):
            """Return height of tree."""
            if node is None:
                return acc
            return get_height(node.left, acc + 1)


        def get_leaf(node, bit, path):
            """Return leaf node from following bit path."""
            if bit < 0:
                return node
            if path & (1 << bit):
                return get_leaf(node.right, bit - 1, path)
            else:
                return get_leaf(node.left, bit - 1, path)


        # First get the height of the tree by going left.  O(log N)
        ht = get_height(root, 0)

        # The bottom row will have 2^(ht-1) nodes in it.
        length = pow(2, ht - 1)

        # Use the binary representation of n such that 0 <= n < length
        # to be a path to the n-th number in the bottom row, where a
        # 0 bit means go left and a 1 bit means got right.  This can be
        # used to do a binary search for the right most filled slot.
        # This requires O(lg M) searches where M is the number of possible
        # leaf nodes.  Each search requires O(lg N) to traverse tree to leaf.
        lo = 0
        hi = length - 1
        soln_index = 0
        soln_value = None
        path_bits = ht - 2
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            node = get_leaf(root, path_bits, mid)
            if node is None:
                # Move left
                hi = mid - 1
            else:
                # Move right
                if mid > soln_index:
                    soln_index = mid
                    soln_value = node.val
                lo = mid + 1
        return soln_value

#
# Testing
#


from bscom_trees import *


def test_1():
    root = [1, [2, [4, null, null], [5, null, null]], [3, null, null]]
    expected = 5
    assert Solution().solve(make_tree(root)) == expected


def test_2():
    root = [1, [2, [4, null, null], [5, null, null]], [3, [6, null, null], [7, null, null]]]
    expected = 7
    assert Solution().solve(make_tree(root)) == expected


def test_3():
    """WA"""
    root = [0, null, null]
    expected = 0
    assert Solution().solve(make_tree(root)) == expected
