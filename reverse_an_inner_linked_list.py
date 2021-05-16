"""
binarysearch.com :: Reverse an Inner Linked List
jramaswami
"""
class Solution:
    def solve(self, node, i, j):
        head = node
        prev = None
        preceding = None
        first = None
        last = None
        following = None
        index = 0
        while node:
            nxt = node.next
            if index < i:
                preceding = node
            if index == i:
                first = node
            if index == j:
                last = node
            if index == j + 1:
                following = node
            if index >= i and index <= j:
                node.next = prev

            prev = node
            node = nxt
            index += 1
        
        first.next = following
        if preceding:
            preceding.next = last
        if i == 0:
            return last
        return head


#
# Testing
#
from bscom_linked_lists import *


def test_1():
    node = [0, 1, 3, 4]
    i = 1
    j = 2
    assert ll_to_list(Solution().solve(list_to_ll(node), i, j)) == [0, 3, 1, 4]


def test_2():
    node = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    i = 1
    j = 6
    expected = node[:i] + list(reversed(node[i:j+1])) + node[j+1:]
    print(f"{node=} {i=} {j=} {expected=}")
    assert ll_to_list(Solution().solve(list_to_ll(node), i, j)) == expected


def test_3():
    node = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    i = 0
    j = 4
    expected = node[:i] + list(reversed(node[i:j+1])) + node[j+1:]
    print(f"{node=} {i=} {j=} {expected=}")
    assert ll_to_list(Solution().solve(list_to_ll(node), i, j)) == expected


def test_4():
    node = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    i = 3
    j = 8
    expected = node[:i] + list(reversed(node[i:j+1])) + node[j+1:]
    print(f"{node=} {i=} {j=} {expected=}")
    assert ll_to_list(Solution().solve(list_to_ll(node), i, j)) == expected


def test_5():
    node = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    i = 0
    j = 8
    expected = node[:i] + list(reversed(node[i:j+1])) + node[j+1:]
    print(f"{node=} {i=} {j=} {expected=}")
    assert ll_to_list(Solution().solve(list_to_ll(node), i, j)) == expected
