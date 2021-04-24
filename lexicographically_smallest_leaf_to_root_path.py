"""
binarysearch.com :: Lexicographically Smallest Leaf to Root Path
jramaswami
"""
from math import inf


class Solution:
    def solve(self, root):
        def solve0(node, acc):
            acc.append(node.val)
            if node.left is None and node.right is None:
                T = acc[::-1]
            else:
                L = [inf]
                R = [inf]
                if node.left:
                    L = solve0(node.left, acc)
                if node.right:
                    R = solve0(node.right, acc)
                T = min(L, R)
            acc.pop()
            return T

        acc = []
        return solve0(root, acc)

#
# Testing
#
from bscom_trees import *


def test_1():
    root = [1, [8, null, null], [7, [4, [6, null, null], [3, null, null]], [5, null, null]]]
    assert Solution().solve(make_tree(root)) == [3, 4, 7, 1]

def test_2():
    root = [1, [8, null, null], [7, [4, [6, null, null], [5, null, null]], [3, null, null]]]
    assert Solution().solve(make_tree(root)) == [3, 7, 1]

def test_3():
    """WA"""
    root = [0, null, [1, null, null]]
    assert Solution().solve(make_tree(root)) == [1,  0]

