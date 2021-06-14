"""
binarysearch.com :: Back to Front Linked List
jramaswami
"""


class Solution:
    def solve(self, node):
        """O(1) space solution."""
        # Find the midway point.
        first_right = node
        last_right = node
        last_left = None
        while last_right.next:
            last_left = first_right
            first_right = first_right.next
            last_right = last_right.next
            if last_right.next:
                last_right = last_right.next

        # Edge case: list of 1 node.
        if last_left == None:
            return node

        # Reverse the right list
        first_left = node
        last_left.next = None
        prev = None
        curr = first_right
        follow = first_right
        while curr:
            follow = curr.next
            curr.next = prev
            prev = curr
            curr = follow

        # Alternate
        head = last_right
        right = last_right.next
        left = first_left
        pick_left = True
        curr = head
        while right or left:
            if pick_left:
                if left:
                    curr.next = left
                    left = left.next
                pick_left = False
            elif not pick_left and right:
                if right:
                    curr.next = right
                    right = right.next
                pick_left = True
            curr = curr.next

        return head

#
# Testing
#
from bscom_linked_lists import *


def test_1():
    node = list_to_ll([0, 1, 2, 3])
    expected = [3, 0, 2, 1]
    assert ll_to_list(Solution().solve(node)) == expected


def test_2():
    node = list_to_ll([0, 1, 2, 3, 4])
    expected = [4, 0, 3, 1, 2]
    assert ll_to_list(Solution().solve(node)) == expected


def test_3():
    node = list_to_ll([0])
    expected = [0]
    assert ll_to_list(Solution().solve(node)) == expected
