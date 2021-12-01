"""
binarysearch.com :: Largest Binary Search Subtree in Nodes
jramaswami
"""


import collections
import math


Result = collections.namedtuple('Result', ['min', 'max', 'size', 'valid_bst', 'best_bst'])
BST = collections.namedtuple('BST', ['root', 'size'])


class Solution:

    def solve(self, root):

        def traverse(node):
            # Base case: a null is a valid binary search tree.
            if node is None:
                return Result(math.inf, -math.inf, 0, True, BST(None, 0))

            left = traverse(node.left)
            right = traverse(node.right)

            new_min = min(left.min, right.min, node.val)
            new_max = max(left.max, right.max, node.val)
            new_size = 1 + left.size + right.size

            new_valid_bst = (
                left.valid_bst and
                right.valid_bst and
                left.max <= node.val and
                right.min >= node.val
            )

            new_best_bst = left.best_bst
            if new_valid_bst:
                new_best_bst = BST(node, new_size)
            elif right.best_bst.size > left.best_bst.size:
                new_best_bst = right.best_bst

            return Result(
                    new_min,
                    new_max,
                    new_size,
                    new_valid_bst,
                    new_best_bst
            )

        result = traverse(root)
        return result.best_bst.root
