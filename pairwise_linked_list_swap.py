"""
binarysearch.com :: Pairwise Linked List Swap
jramaswami
"""


class Solution:
    def solve(self, node):

        head = node

        if head is None:
            return head

        left = node
        right = node.next

        while left and right:
            left.val, right.val = right.val, left.val
            left = right.next
            if left:
                right = left.next
            else:
                right = None

        return head
