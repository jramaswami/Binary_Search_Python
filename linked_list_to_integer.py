"""
binarysearch.com :: Linked List to Integer
jramaswami
"""


class Solution:
    def solve(self, node):
        n = 0
        curr = node
        while curr:
            n *= 2
            if curr.val:
                n += 1
            curr = curr.next
        return n
