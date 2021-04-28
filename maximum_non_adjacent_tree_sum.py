"""
binarysearch.com :: Maximum Non-Adjacent Tree Sum
jramaswami
"""

def solve0(node):
    if node is None:
        return (0, 0)

    with_left, without_left = solve0(node.left)
    with_right, without_right = solve0(node.right)

    with_me = node.val + without_left + without_right
    without_me = with_left + with_right

    return (max(with_me, without_me), without_me)


class Solution:
    def solve(self, root):
        return max(solve0(root))


# Testing
from bscom_trees import *


def test_1():
    root = [1, [4, [3, null, null], [2, null, null]], [5, null, null]]
    assert Solution().solve(make_tree(root)) == 10