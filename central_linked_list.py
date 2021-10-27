"""
binarysearch.com :: Central Linked List
jramaswami
"""


class Solution:
    def solve(self, node):
        # Two pointers: one slow, one fast.
        slow = node
        fast = node
        while fast:
            fast = fast.next
            if fast:
                # If fast advanced, then advance it again
                # and advance the slow pointer.
                fast = fast.next
                slow = slow.next
        return slow.val
