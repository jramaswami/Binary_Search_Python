"""
binarysearch.com :: Univalue Tree
jramaswami
"""
def solve0(node, value):
    if node is None:
        return True

    return (node.val == value 
            and solve0(node.left, value) 
            and solve0(node.right, value)
    )

class Solution:
    def solve(self, root):
        if root is None:
            return False
        return solve0(root, root.val)

from bscom_trees import *

def test_1():
    root = make_tree([2, [2, [2, null, null], null], [2, [2, null, null], null]])
    assert Solution().solve(root) == True

def test_2():
    root = make_tree([2, [2, [9, null, null], null], [2, null, null]])
    assert Solution().solve(root) == False

def test_3():
    assert Solution().solve(None) == False
