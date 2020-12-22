"""
binarysearch.com :: Inverted Subtree
"""
def is_inversion(tree1, tree2):
 # A tree is defined to be an inversion of another tree if either:
    # Both trees are null
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    if tree1.val != tree2.val:
        return False
    # Its left and right children are optionally swapped and its left and right subtrees are inversions.
    if is_inversion(tree1.left, tree2.left) and is_inversion(tree1.right, tree2.right):
        return True
    if is_inversion(tree1.left, tree2.right) and is_inversion(tree1.right, tree2.left):
        return True
    return False
   
class Solution:
    def solve(self, source, target):
        if is_inversion(source, target):
            return True
        result = False
        if target.left:
            result = result or self.solve(source, target.left) 
        if target.right:
            result = result or self.solve(source, target.right)
        return result

# For testing
from bscom_trees import *

def test_1():
    source = [0, [1, null, [3, null, null]], [2, null, null]]
    target = [5, [2, null, null], [0, [2, null, null], [1, [3, null, null], null]]]
    source_t = make_tree(source)
    target_t = make_tree(target)
    assert Solution().solve(source_t, target_t) == True

def test_2():
    source = [0, null, null]
    target = [2, null, null]
    source_t = make_tree(source)
    target_t = make_tree(target)
    assert Solution().solve(source_t, target_t) == False
