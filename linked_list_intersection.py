"""
binarysearch.com :: Linked List Intersection
jramaswami

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def solve(self, l0, l1):
        left = l0
        right = l1
        soln = LLNode(None)
        curr = soln
        while left and right:
            if left.val < right.val:
                left = left.next
            elif right.val < left.val:
                right = right.next
            else:
                new_node = LLNode(left.val)
                curr.next = new_node
                curr = curr.next
                left = left.next
                right = right.next
        return soln.next
