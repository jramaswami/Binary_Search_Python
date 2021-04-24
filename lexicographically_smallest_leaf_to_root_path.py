"""
binarysearch.com :: Lexicographically Smallest Leaf to Root Path
jramaswami
"""
class Solution:
    def solve(self, root):
        if root is None:
            return None
        left = self.solve(root.left)
        right = self.solve(root.right)

        if left is None and right is None:
            return [root.val]
        elif left is None:
            return right + [root.val]
        elif right is None:
            return left + [root.val]
        return min(left, right) + [root.val]

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

