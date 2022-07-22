"""
binarysearch.com :: Longest Even Sum Path
jramaswami
"""


import math


class Solution:

    def __init__(self):
        self.soln = 0

    def solve(self, root):

        def traverse(node):
            if node is None:
                return 0, -math.inf

            lel, lol = traverse(node.left)
            rel, rol = traverse(node.right)

            # Find my longest even leg and my longest odd leg.
            if node.val % 2 == 1:
                # I have an odd number.
                # To have an even path I must be added to an odd path.
                self.soln = max(self.soln, lel + rol + 1, lol + rel + 1)
                # To have an even leg, I must be added to an odd leg.
                # (Odd leg could be -math.inf and there should always be
                # on even length even if it is zero.)
                # To have an odd leg, I must be added to an even leg.
                return max(lol+1, rol+1, 0), max(lel+1, rel+1)
            else:
                # I have an even number.
                # To have an even path, I must be added to an even path.
                self.soln = max(self.soln, lel + rel + 1, lol + rol + 1)
                # To have an even leg, I must be added to an even leg.
                # To have an odd leg, I must be added to an odd leg.
                # (Odd leg could be -math.inf and there should always be
                # on even length even if it is zero.)
                return max(lel+1, rel+1, 0), max(lol+1, rol+1)

        self.soln = 0
        traverse(root)
        return self.soln


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