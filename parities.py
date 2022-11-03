"""
binarysearch.com :: Tree with Distinct Parities
https://binarysearch.com/room/Weekly-Contest-38-CNs3hGBp9j
"""
# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def solve0(node):
    if node.right is None and node.left is None:
        # Leaf node
        return 0, node.val

    node_balanced = 1
    right_balanced = left_balanced = 0
    right_sum = left_sum = 0
    if node.right is not None:
        # Unbalanced
        right_balanced, right_sum = solve0(node.right)
    else:
        node_balanced = 0


    if node.left is not None:
        left_balanced, left_sum = solve0(node.left)
    else:
        node_balanced = 0

    if left_sum % 2 == right_sum % 2:
        node_balanced = 0

    return node_balanced + left_balanced + right_balanced, node.val + left_sum + right_sum

class Solution:
    def solve(self, root):
        if root is None:
            return 0
        soln, _ = solve0(root)
        return soln
