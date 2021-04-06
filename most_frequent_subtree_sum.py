"""
binarysearch.com :: Most Frequent Subtree Sum
jramaswami
"""
from collections import defaultdict


def solve0(node, acc):
    """
    Recursive solution.  
    acc is a defaultdict of the frequency of each sum.
    """
    if node is None:
        return 0

    left_subtree_sum = solve0(node.left, acc)
    right_subtree_sum = solve0(node.right, acc)
    subtree_sum = node.val + left_subtree_sum + right_subtree_sum
    acc[subtree_sum] += 1
    return subtree_sum


class Solution:
    def solve(self, root):
        freqs = defaultdict(int)
        solve0(root, freqs)
        _, soln = max((v, k) for k, v in freqs.items())
        return soln


#
# Testing
#
from bscom_trees import *


def test_1():
    root = make_tree([5, [2, null, null], [-5, null, null]])
    assert Solution().solve(root) == 2

