"""
binarysearch.com :: Reverse Linked List Groups
jramswami

class LLNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def solve(self, node, k):
        curr = node
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
            nodes[-1].next = None

        for right in range(k, len(nodes)+1, k):
            nodes[right-k:right] = nodes[right-k:right][::-1]

        for i, _ in enumerate(nodes[:-1]):
            nodes[i].next = nodes[i+1]

        return nodes[0]


#
#   Testing
#


from bscom_linked_lists import *


def test_1():
    node = list_to_ll([0, 1, 2, 3])
    k = 2
    expected = [1, 0, 3, 2]
    result = ll_to_list(Solution().solve(node, k))
    assert result == expected


def test_2():
    node = list_to_ll([0, 1, 2, 3])
    k = 3
    expected = [2, 1, 0, 3]
    result = ll_to_list(Solution().solve(node, k))
    assert result == expected


def test_3():
    "WA"
    node = list_to_ll([0, 1])
    k = 14
    expected = [1, 0]
    result = ll_to_list(Solution().solve(node, k))
    assert result == expected
