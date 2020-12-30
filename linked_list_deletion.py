"""
binarysearch.com :: Linked List Deletion
jramaswami
"""
class Solution:
    def solve(self, node, target):
        # Recursive solution.
        if node == None:
            return node
        elif node.val == target:
            return self.solve(node.next, target)
        else:
            node.next = self.solve(node.next, target)
            return node


# TESTING
class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


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


def test_1():
    head = list_to_ll([0, 1, 1, 2])
    result = Solution().solve(head, 1)
    assert ll_to_list(result) == [0, 2]
