"""
binarysearch.com :: Longest Even Sum Path
jramaswami
"""


class PathLeg:
    def __init__(self, value, length):
        self.value = value
        self.length = length

    def is_odd(self):
        return self.value % 2 == 1

    def is_even(self):
        return self.value % 2 == 0

class Path:
    def __init__(self, leg1, leg2, nodeval):
        # Node value is double counted when combining legs.
        self.value = leg1.value + leg2.value - nodeval
        self.length = leg1.length + leg2.length - 1

    def is_even(self):
        return self.value % 2 == 0

class Solution:

    def solve(self, root):

        def get_legs(node, child):
            if child is None:
                if node.val % 2 == 1:
                    return PathLeg(0, 0), PathLeg(node.val, 1)
                return PathLeg(node.val, 1), PathLeg(0, 0)

            opl = PathLeg(node.val + child.opl.value, 1 + child.opl.length)
            epl = PathLeg(node.val + child.epl.value, 1 + child.epl.length)
            if opl.is_even:
                opl, epl = epl, opl
            return opl, epl

        def traverse(node):
            if node is None:
                return

            traverse(node.left)
            traverse(node.right)

            lopl, lepl = get_legs(node, node.left)
            ropl, repl = get_legs(node, node.right)

            # Find the longest odd leg
            if lopl.length >= ropl.length:
                node.opl = lopl
            else:
                node.opl = ropl
            # Find the longest even leg
            if lepl.length >= repl.length:
                node.epl = lepl
            else:
                node.epl = repl
            # Find the longest even path for this subtree.
            paths = [
                Path(lopl, ropl, node.val), Path(lopl, repl, node.val),
                Path(lepl, ropl, node.val), Path(lepl, repl, node.val),
                lepl, repl
            ]
            if node.left:
                paths.append(node.left.mep)
            if node.right:
                paths.append(node.right.mep)
            max_path = None
            max_path_len = -1
            for p in paths:
                if p.is_even() and p.length > max_path_len:
                    max_path_len, max_path = p.length, p
            node.mep = max_path

        traverse(root)
        return root.mep.length


#
# Testing
#

from bscom_trees import *


def test_1():
    root = [0, [3, null, null], [2, [6, [3, null, null], null], [0, null, null]]]
    expected = 5
    assert Solution().solve(make_tree(root)) == expected


def test_2():
    root = [3, [6, [0, null, null], [8, null, null]], [4, null, null]]
    expected = 3
    assert Solution().solve(make_tree(root)) == expected


def test_3():
    "WA"
    root = [3, null, null]
    expected = 0
    assert Solution().solve(make_tree(root)) == expected

def test_4():
    "WA"
    root = [133, [23, [69, [63, null, [70, [112, [131, null, [139, null, null]], [134, [43, null, null], null]], null]], [14, [1, null, null], [39, null, null]]], null], [80, [128, [74, [4, [42, null, [35, null, [71, null, [50, null, null]]]], null], [52, null, null]], [88, null, [100, [22, [26, [2, null, null], null], [64, null, null]], [84, null, [9, null, null]]]]], [38, [66, [20, [99, null, [123, null, [37, [145, [7, null, null], [104, null, null]], [73, [146, null, [126, [41, null, null], [75, null, null]]], null]]]], [34, [119, null, [25, null, null]], null]], [28, [13, [142, null, [5, [81, null, null], null]], [96, null, [95, null, [82, null, [135, null, null]]]]], [137, null, [111, null, null]]]], [40, [92, [72, null, [105, [6, [30, null, [113, null, null]], [32, null, null]], null]], [144, [33, null, null], null]], [79, [58, [36, [21, [125, null, null], null], null], null], [106, null, null]]]]]]
    expected = 19
    assert Solution().solve(make_tree(root)) == expected