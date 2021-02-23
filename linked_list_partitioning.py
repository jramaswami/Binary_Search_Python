"""
binarysearch.com :: Linked List Partitioning
jramaswami
"""
class Solution:
    def solve(self, node, k):
        # Partition into three linked lists
        less_head = None
        less_tail = None
        equal_head = None
        equal_tail = None
        more_head = None
        curr_node = node
        while curr_node:
            next_node = curr_node.next
            if curr_node.val < k:
                # Goes into less
                curr_node.next = less_head
                less_head = curr_node
                if less_tail is None:
                    less_tail = curr_node
            elif curr_node.val > k:
                # Goes into more
                curr_node.next = more_head
                more_head = curr_node
            else:
                # Goes into equal
                curr_node.next = equal_head
                equal_head = curr_node
                if equal_tail is None:
                    equal_tail = curr_node
            curr_node = next_node

        # Join parts.
        less_tail.next = equal_head
        equal_tail.next = more_head

        return less_head
