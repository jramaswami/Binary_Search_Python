"""
binarysearch.com :: Longest Tree Path
jramaswami
"""


def solve0(node):
    """
    Recursively walking tree to get:
    (1) the longest leg where the node is at the top
    (2) an accumulator of the longest path so far
    """
    if node is None:
        return (0, 0)

    longest_path = 0
    longest_leg = 0
    left_leg, left_acc = solve0(node.left)
    right_leg, right_acc = solve0(node.right)
    longest_leg = 1 + max(left_leg, right_leg)
    longest_path = 1 + left_leg + right_leg

    return longest_leg, max(longest_path, right_acc, left_acc)


class Solution:
    def solve(self, root):
        _, acc = solve0(root)
        return acc


#
# Testing
#


from bscom_trees import *


def test_1():
    root = make_tree([0, [1, null, null], [2, [3, [4, null, null], null], [0, null, null]]])
    assert Solution().solve(root) == 5


def test_2():
    root = make_tree([0, null, [2, [3, [4, null, null], null], [0, null, [6, null, [7, null, null]]]]])
    assert Solution().solve(root) == 6