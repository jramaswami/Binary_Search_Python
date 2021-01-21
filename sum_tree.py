"""
binarysearch.com :: Sum Tree
jramaswami
"""
def solve0(node):
    """Recursive solution."""
    # Base Case
    if node.left is None and node.right is None:
        return True
    
    S = 0
    T = True
    if node.left:
        S += node.left.val
        T = T and solve0(node.left)
    if node.right:
        S += node.right.val
        T = T and solve0(node.right)

    return T and (node.val == S)


class Solution:
    def solve(self, root):
        if root:
            return solve0(root)
        else:
            return True


# For testing
from bscom_trees import *

def test_1():
    root = make_tree([9, [1, null, null], [8, [6, [6, null, null], null], [2, null, null]]])
    assert Solution().solve(root) == True

def test_2():
    root = make_tree([9, [1, null, null], [3, null, null]])
    assert Solution().solve(root) == False

def test_3():
    root = null
    assert Solution().solve(root) == True
