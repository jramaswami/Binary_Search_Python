"""
binarysearch.com :: A Strictly Increasing Linked List
jramaswami
"""
def is_strictly_increasing(node, prev):
    if node is None:
        return True

    if node.val <= prev:
        return False

    return is_strictly_increasing(node.next, node.val)


class Solution:
    def solve(self, head):
        if head is None:
            return True
        return is_strictly_increasing(head.next, head.val)


#
# Testing
#
from bscom_linked_lists import *

def test_1():
    head = [1, 5, 9, 9]
    assert Solution().solve(list_to_ll(head)) == False

def test_2():
    head = [1, 5, 8, 9]
    assert Solution().solve(list_to_ll(head)) == True


