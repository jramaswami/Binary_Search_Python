"""
binarysearch.com :: Linked List Folding
jramaswami
"""


from bscom_linked_lists import *


class Solution:

    def solve(self, node):
        # Boundary cases:
        if node is None:
            return

        if node.next is None:
            return node

        if node.next.next is None:
            return LLNode(node.val + node.next.val)

        # Find the middle.
        slow = node
        fast = node
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        dummy = LLNode(0)
        curr = dummy

        # Handle odd number of elements.
        if len(stack) % 2:
            curr.next = LLNode(slow.val)
            curr = curr.next
            slow = slow.next

        while slow != None:
            curr.next = LLNode(slow.val + stack[-1])
            stack.pop()
            curr = curr.next
            slow = slow.next
        return dummy.next


#
# Testing
#


def test_1():
    node = [3, 1, 2, 4]
    expected = [3, 7]
    result = ll_to_list(Solution().solve(list_to_ll(node)))
    assert result == expected


def test_2():
    node = [2, 1, 3]
    expected = [1, 5]
    result = ll_to_list(Solution().solve(list_to_ll(node)))
    assert result == expected


def test_3():
    "WA"
    node = [3, 2]
    expected = [5]
    result = ll_to_list(Solution().solve(list_to_ll(node)))
    assert result == expected


def test_4():
    "WA"
    node = [6,10,15,11,16,3,4,7,5]
    expected = [16, 14, 19, 17, 11]
    result = ll_to_list(Solution().solve(list_to_ll(node)))
