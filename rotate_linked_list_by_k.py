"""
binarysearch.com :: Rotate a Linked List by K
jramaswami
"""


class Solution:
    def solve(self, old_head, k):
        # If k is zero, then we aren't rotating anything.
        if k == 0:
            return old_head

        # Move fast k places ahead.
        old_tail = None
        fast = old_head
        for _ in range(k):
            old_tail = fast
            fast = fast.next

        # Move until fast is at None.
        new_tail = None
        new_head = old_head
        while fast is not None:
            old_tail = fast
            fast = fast.next
            new_tail = new_head
            new_head = new_head.next

        # If new_tail is None, then we are rotating entire list, which means
        # it remains the same.
        if new_tail is None:
            return old_head

        # (1) fast should currently point to None.
        # (2) old_tail should point to the tail of the original list.
        # (3) new_head points to the new head of the list, which will be k from
        #     the end of the original list.
        # (4) new_tail points to the tail of the rotated list.

        # To rotate, move the section from new_head to old_tail to the
        # front of the list and move the section from old_head to new_tail
        # to the back of the list.
        # (1) unhook the new_tail from the new_head.
        new_tail.next = None
        # (2) hook the old_head to the the old_tail.
        old_tail.next = old_head
        # (3) return new head
        return new_head



#
# Testing
#


from bscom_linked_lists import *


def test_1():
    node = [1, 2, 3, 4]
    k = 2
    expected = [3, 4, 1, 2]
    assert ll_to_list(Solution().solve(list_to_ll(node), k)) == expected


def test_2():
    node = [1, 2, 3, 4]
    k = 4
    expected = [1, 2, 3, 4]
    assert ll_to_list(Solution().solve(list_to_ll(node), k)) == expected


def test_3():
    node = [1, 2, 3, 4]
    k = 0
    expected = [1, 2, 3, 4]
    assert ll_to_list(Solution().solve(list_to_ll(node), k)) == expected


def test_4():
    node = []
    k = 0
    expected = []
    assert ll_to_list(Solution().solve(list_to_ll(node), k)) == expected


def test_5():
    """WA"""
    node = [7, 7, 3, 5, 1]
    k = 2
    expected = [5, 1, 7, 7, 3]
    assert ll_to_list(Solution().solve(list_to_ll(node), k)) == expected
