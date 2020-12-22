"""
binarysearch.com :: Inverted Subtree
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def is_inversion(tree1, tree2):
 # A tree is defined to be an inversion of another tree if either:
    # Both trees are null
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
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
