"""
binarysearch.com :: Kth Smallest in a Binary Search Tree
jramaswami
"""


class Solution:
    def solve(self, root, k):

        def traverse(node, acc, soln, target):
            if node is None:
                return acc, soln

            index, soln = traverse(node.left, acc, soln, target)
            acc = index + 1
            if acc == target:
                soln = node.val
            return traverse(node.right, acc, soln, target)

        _, soln = traverse(root, -1, None, k)
        return soln
