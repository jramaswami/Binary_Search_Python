"""
binarysearch.com :: Sort A Linked List
jramaswami

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def solve(self, node):
        A = []
        while node:
            A.append(node.val)
            node = node.next

        A.sort()

        dummy = LLNode(0)
        prev_node = dummy
        for n in A:
            new_node = LLNode(n)
            prev_node.next = new_node
            prev_node = new_node
        return dummy.next