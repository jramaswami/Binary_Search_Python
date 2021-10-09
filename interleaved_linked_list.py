"""
binarysearch.com :: Interleaved Linked List
jramaswami
"""


class Solution:
    def solve(self, l0, l1):
        curr0 = l0
        curr1 = l1
        dummy = LLNode(0)
        prev = dummy
        while curr0 or curr1:
            if curr0:
                prev.next = curr0
                prev = curr0
                curr0 = curr0.next
            if curr1:
                prev.next = curr1
                prev = curr1
                curr1 = curr1.next
        return dummy.next
