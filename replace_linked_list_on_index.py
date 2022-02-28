"""
binarysearch.com :: Replace Linked List on Index
jramaswami
"""


class Solution:

    def solve(self, root_a, root_b, low, high):
        dummy_a = LLNode(0, root_a)
        dummy_b = LLNode(0, root_b)

        prev_node = dummy_a
        succ_node = None
        curr_node = root_a
        index = 0
        while curr_node:
            if index < low:
                prev_node = curr_node
            if index > high:
                succ_node = curr_node
                break
            curr_node = curr_node.next
            index += 1
        prev_node.next = root_b


        if root_b is None:
            prev_node.next = succ_node
        else:
            curr_node = root_b
            while curr_node and curr_node.next:
                curr_node = curr_node.next
            if curr_node:
                curr_node.next = succ_node
        return dummy_a.next


#
# Testing
#


from bscom_linked_lists import *


def test_1():
    a = [1, 2, 3, 4, 5, 6]
    b = [10, 20, 30]
    lo = 1
    hi = 2
    expected = [1, 10, 20, 30, 4, 5, 6]
    root_a = list_to_ll(a)
    root_b = list_to_ll(b)
    result = ll_to_list(Solution().solve(root_a, root_b, lo, hi))
    assert result == expected


def test_2():
    a = [1, 2, 3]
    b = [10, 20, 30]
    lo = 0
    hi = 2
    expected = [10, 20, 30]
    root_a = list_to_ll(a)
    root_b = list_to_ll(b)
    result = ll_to_list(Solution().solve(root_a, root_b, lo, hi))
    assert result == expected


def test_3():
    a = [1, 2, 3]
    b = [10, 20, 30]
    lo = 4
    hi = 20
    expected = [1, 2, 3, 10, 20, 30]
    root_a = list_to_ll(a)
    root_b = list_to_ll(b)
    result = ll_to_list(Solution().solve(root_a, root_b, lo, hi))
    assert result == expected


def test_4():
    b = [10, 20, 30]
    lo = 0
    hi = 0
    expected = list(b)
    root_a = None
    root_b = list_to_ll(b)
    result = ll_to_list(Solution().solve(root_a, root_b, lo, hi))
    assert result == expected


def test_5():
    a = [0, 1, 2, 3, 4]
    b = []
    lo = 1
    hi = 3
    expected = [0, 4]
    root_a = list_to_ll(a)
    root_b = list_to_ll(b)
    result = ll_to_list(Solution().solve(root_a, root_b, lo, hi))
    assert result == expected
