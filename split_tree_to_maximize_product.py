"""
binarysearch.com :: Split Tree to Maximize Product
jramaswami
"""


import collections
import math


class Solution:

    def solve(self, root):

        def compute_subtree_sums(node, index, subtree_sums):
            if node is None:
                subtree_sums[index] = 0
                return

            left_child = index * 2
            right_child = left_child + 1
            compute_subtree_sums(node.left, left_child, subtree_sums)
            compute_subtree_sums(node.right, right_child, subtree_sums)
            subtree_sums[index] = (
                node.val + subtree_sums[left_child] + subtree_sums[right_child]
            )

        def compute_max_product(node, index, subtree_sums):
            if node is None:
                return -math.inf

            left_child = index * 2
            right_child = left_child + 1
            total = subtree_sums[1]
            return max(
                (total - subtree_sums[left_child]) * subtree_sums[left_child],
                (total - subtree_sums[right_child]) * subtree_sums[right_child],
                compute_max_product(node.left, left_child, subtree_sums),
                compute_max_product(node.right, right_child, subtree_sums)
            )

        subtree_sums = collections.defaultdict(int)
        compute_subtree_sums(root, 1, subtree_sums)
        return compute_max_product(root, 1, subtree_sums)


#
# Testing
#


from bscom_trees import *


def test_1():
    root = [1, [2, null, null], [3, [4, null, null], [5, null, null]]]
    result = Solution().solve(make_tree(root))
    expected = 50
    assert result == expected