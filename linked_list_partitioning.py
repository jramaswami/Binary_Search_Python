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
        more_tail = None
        curr_node = node
        while curr_node:
            next_node = curr_node.next
            curr_node.next = None
            if curr_node.val < k:
                # Goes into less
                if less_tail is None:
                    less_head = less_tail = curr_node
                else:
                    less_tail.next = curr_node
                    less_tail = curr_node
            elif curr_node.val > k:
                # Goes into more
                if more_tail is None:
                    more_head = more_tail = curr_node
                else:
                    more_tail.next = curr_node
                    more_tail = curr_node
            else:
                # Goes into equal
                if equal_tail is None:
                    equal_head = equal_tail = curr_node
                else:
                    equal_tail.next = curr_node
                    equal_tail = curr_node

            curr_node = next_node

        # Join parts.
        head = None
        if more_head:
            head = more_head
        if equal_head:
            equal_tail.next = head
            head = equal_head
        if less_head:
            less_tail.next = head
            head = less_head

        return head


class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"LLNode(val={self.val}, next={self.next})"


def make_list(arr):
    head = None
    if arr:
        head = LLNode(arr[0])
        prev_node = head
        for val in arr[1:]:
            curr_node = LLNode(val)
            prev_node.next = curr_node
            prev_node = curr_node
    return head

def make_array(node):
    A = []
    while node:
        A.append(node.val)
        node = node.next
    return A

def test_1():
    node = make_list([3, 2, 1, 2])
    k = 2
    head = Solution().solve(node, k)
    assert make_array(head) == [1, 2, 2, 3]

def test_2():
    node = make_list([0, 0, 2, 3, 3])
    k = 0
    head = Solution().solve(node, k)
    assert make_array(head) == [0, 0, 2, 3, 3]
