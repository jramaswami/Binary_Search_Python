"""
binarysearch.com :: Insert Into Linked List
jramaswami
"""


class Solution:

    def solve(self, head, pos, val):
        new_node = LLNode(val)
        if pos == 0:
            new_node.next = head
            return new_node

        prev = head
        for _ in range(pos-1):
            prev = prev.next
        new_node.next = prev.next
        prev.next = new_node
        return head