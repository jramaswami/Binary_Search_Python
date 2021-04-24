"""
binarysearch.com :: Lexicographically Smallest Leaf to Root Path
jramaswami
"""
class Solution:
    def solve(self, root):
        if root is None:
            return []
        return min(self.solve(root.left), self.solve(root.right)) + [root.val]


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

