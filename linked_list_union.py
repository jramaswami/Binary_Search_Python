"""
binarysearch.com :: Linked List Union
jramaswami
"""


import math
from bscom_linked_lists import *


class Solution:

    def solve(self, head1, head2):
        curr1 = head1
        curr2 = head2

        dummy = LLNode(-math.inf)
        tail = dummy

        while curr1 and curr2:
            if curr1.val <= curr2.val:
                if curr1.val != tail.val:
                    tail.next = LLNode(curr1.val)
                    tail = tail.next
                curr1 = curr1.next
            else:
                if curr2.val != tail.val:
                    tail.next = LLNode(curr2.val)
                    tail = tail.next
                curr2 = curr2.next

        while curr1:
            if curr1.val != tail.val:
                tail.next = LLNode(curr1.val)
                tail = tail.next
            curr1 = curr1.next

        while curr2:
            if curr2.val != tail.val:
                tail.next = LLNode(curr2.val)
                tail = tail.next
            curr2 = curr2.next

        return dummy.next



def test_1():
    ll0 = [1, 3, 4]
    ll1 = [2, 3, 4]
    expected = [1, 2, 3, 4]
    result = Solution().solve(list_to_ll(ll0), list_to_ll(ll1))
    assert ll_to_list(result) == expected


def test_2():
    ll0 = [1, 3, 4]
    ll1 = []
    expected = [1, 3, 4]
    result = Solution().solve(list_to_ll(ll0), list_to_ll(ll1))
    assert ll_to_list(result) == expected


def test_3():
    ll0 = []
    ll1 = [1, 3, 4]
    expected = [1, 3, 4]
    result = Solution().solve(list_to_ll(ll0), list_to_ll(ll1))
    assert ll_to_list(result) == expected


def test_4():
    ll0 = []
    ll1 = []
    expected = []
    result = Solution().solve(list_to_ll(ll0), list_to_ll(ll1))
    assert ll_to_list(result) == expected
