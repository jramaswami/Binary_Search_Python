"""
binarysearch.com :: Linked List Delete Last Occurrence of Value
jramaswami
"""
def solve0(node, target):
    """Recursive solution."""
    if node is None:
        return False, None

    already_deleted, child = solve0(node.next, target)
    if not already_deleted and node.val == target:
        return True, child
    else:
        node.next = child
        return already_deleted, node


class Solution:
    def solve(self, node, target):
        return solve0(node, target)[1]



#
# TESTING
#
from bscom_linked_lists import *

def test_1():
    node = list_to_ll([1, 2, 3, 1])
    target = 1
    assert ll_to_list(Solution().solve(node, target)) == [1, 2, 3]

def test_2():
    node = list_to_ll([1, 2, 3, 1])
    target = 3
    assert ll_to_list(Solution().solve(node, target)) == [1, 2, 1]

def test_3():
    node = list_to_ll([])
    target = 3
    assert ll_to_list(Solution().solve(node, target)) == []

def test_4():
    node = list_to_ll([1, 2, 3, 7])
    target = 1
    assert ll_to_list(Solution().solve(node, target)) == [2, 3, 7]


