"""
binarysearch.com :: Kth Last Node of a Linked List
jramaswami
"""
class Solution:
    def solve(self, node, k):
        fast = node
        for _ in range(k):
            fast = fast.next

        slow = node
        while fast:
            fast = fast.next
            if fast:
                slow = slow.next

        return slow.val

#
# Testing
#
from bscom_linked_lists import *


def test_1():
    node = list_to_ll([1, 2])
    k = 1
    assert Solution().solve(node, k) == 1

def test_2():
    node = list_to_ll([0, 1, 2, 3])
    k = 2
    assert Solution().solve(node, k) == 1