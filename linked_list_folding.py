"""
binarysearch.com :: Linked List Folding
jramaswami
"""


from bscom_linked_lists import *
import collections


class Solution:

    def solve(self, node):
        A = collections.deque()
        curr = node
        while node:
            A.append(node.val)
            node = node.next

        head = None
        while A:
            if len(A) == 1:
                head = LLNode(A[0], head)
                A.popleft()
            else:
                head = LLNode(A[0] + A[-1], head)
                A.popleft()
                A.pop()

        return head


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
