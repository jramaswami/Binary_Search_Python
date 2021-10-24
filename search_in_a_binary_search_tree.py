"""
binarysearch.com :: Search in a Binary Search Tree
jramaswami
"""


class Solution:
    def solve(self, root, val):

        node = root
        while node:
            if val == node.val:
                return True
            elif val < node.val:
                node = node.left
            elif val > node.val:
                node = node.right
        return False
