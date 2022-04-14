"""
binarysearch.com :: Cutting Binary Search Tree
jramaswami
"""


class Solution:
    def solve(self, node, lo, hi):
        if node is None:
            return None

        left_subtree = self.solve(node.left, lo, hi)
        right_subtree = self.solve(node.right, lo, hi)
        if lo <= node.val <= hi:
            node.left = left_subtree
            node.righ = right_subtree
            return node
        else:
            # Node must be removed
            if left_subtree is None and right_subtree is None:
                return None
            elif left_subtree is None:
                return right_subtree
            elif right_subree is None:
                return left_subtree
            else:
                # Since left subtree is less than right subtree
                # the easiest thing to do would be to put the
                # left subtree under the right subtree
                curr = right_subtree
                while curr.left is not None:
                    curr = curr.left
                curr.left = left_subtree
                return right_subtree


#
# Testing
#


from bscom_trees import *


def test_1():
    root = [2, [1, [0, null, null], null], [4, [3, null, null], null]]
    lo = 3
    hi = 4
    expected = make_tree([4, [3, null, null], null])
    Solution().solve(make_tree(root), lo, hi) == expected


def test_2():
    root = [5, [1, null, null], [9, [7, [6, null, null], [8, null, null]], [10, null, null]]]
    lo = 7
    hi = 10
    expected = make_tree([9, [7, null, [8, null, null]], [10, null, null]])
    Solution().solve(make_tree(root), lo, hi) == expected


def test_3():
    "WA"
    root = [5, [1, null, null], [9, [7, [6, null, null], [8, null, null]], [10, null, null]]]
    lo = 7
    hi = 10
    expected = make_tree([0, null, [6, [2, null, null], null]])
    Solution().solve(make_tree(root), lo, hi) == expected
