"""
binarysearch.com :: Largest Difference Between Node and a Descendant
jramaswami
"""
from math import inf


def solve0(node, min_acc, max_acc):
    if node is None:
        return abs(min_acc - max_acc)

    return max(solve0(node.left, min(min_acc, node.val), max(max_acc, node.val)),
               solve0(node.right, min(min_acc, node.val), max(max_acc, node.val)))


class Solution:
    def solve(self, root):
        if root is None:
            return 0
        return solve0(root, inf, -inf)


# Testing

from bscom_trees import *

def test_1():
    root = make_tree([0, [4, null, null], [2, [1, [6, null, null], [3, null, null]], [7, null, null]]])
    assert Solution().solve(root) == 7

def test_2():
    assert Solution().solve(None) == 0
