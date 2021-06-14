"""
binarysearch.com :: Back to Front Linked List
jramaswami
"""

from collections import deque


class Solution:
    def solve(self, node):
        """O(n) space solution."""
        if node is None:
            return node
        nodes = deque()
        # Place nodes in deque
        curr = node
        while curr:
            nodes.append(curr)
            curr = curr.next
            nodes[-1].next = None

        # Alternate left and right
        head = nodes[-1]
        head.next = None
        curr = head
        nodes.pop()
        side = 0
        while nodes:
            curr.next = nodes[side]
            if side == 0:
                nodes.popleft()
                side = -1
            else:
                nodes.pop()
                side = 0
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
