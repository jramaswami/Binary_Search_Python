"""
binarysearch.com :: Enlarge BST
jramaswami
"""


def enlarge_dfs(node, acc):
    """DFS to enlarge node."""
    if node is None:
        return 0
    
    # All nodes above and to the right of current node are larger than current
    # node:
    #       acc = sum of values above current node.
    #       delta = sum of values to the right of current node.
    delta_right = enlarge_dfs(node.right, acc)
    node.val = node.val + acc + delta_right
    delta_left = enlarge_dfs(node.left, node.val)
    # Return the value of only the nodes current node and nodes to the right
    # and below me.
    return node.val - acc + delta_left


class Solution:
    def solve(self, root):
        enlarge_dfs(root, 0)
        return root

#
# Testing
#


from bscom_trees import *


def test_1():
    root = make_tree([4, [2, [1, null, null], [3, null, null]], [5, null, null]])
    expected = make_tree([9, [14, [15, null, null], [12, null, null]], [5, null, null]])
    assert Solution().solve(root) == expected


def test_2():
    """WA"""
    root = make_tree([0, null, [2, [1, null, null], null]])
    expected = make_tree([3, null, [2, [3, null, null], null]])
    assert Solution().solve(root) == expected
