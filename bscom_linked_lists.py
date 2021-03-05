"""
binarysearch.com :: Utility functions for linked list problems
jramaswami
"""
class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"LLNode(val={self.val}, next={self.next})"


def list_to_ll(arr):
    if not arr:
        return None
    head = LLNode(arr[0])
    prev = head
    for v in arr[1:]:
        node = LLNode(v)
        prev.next = node
        prev = node
    return head


def ll_to_list(head):
    arr =[]
    node = head
    while node:
        arr.append(node.val)
        node = node.next
    return arr
