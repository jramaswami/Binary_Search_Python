"""
binarysearch.com :: Rotate a Linked List by K
jramaswami
"""


class Solution:
    def solve(self, node, k):
        # Find the tail of the list
        tail = None
        curr = node
        while curr is not None:
            tail = curr
            curr = curr.next

        # Find the point of rotation
        new_tail = None
        new_head = node
        for _ in range(k):
            new_tail = new_head
            new_head = new_head.next

        # Zero rotation or rotation of entire list returns the same list.
        if k == 0 or new_head is None:
            return node

        # Rotate list
        new_tail.next = None
        tail.next = node
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
    node = [1, 2, 3, 4]
    k = 2
    expected = [5, 1, 7, 7, 3]
    assert ll_to_list(Solution().solve(list_to_ll(node), k)) == expected
