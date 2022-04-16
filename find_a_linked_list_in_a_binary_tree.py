"""
binarysearch.com :: Find a Linked List in a Binary Tree
jramaswami
"""


class Solution:
    def solve(self, root, head):

        def find_head(node, head):
            if head is None:
                return True

            if node is None:
                return False

            if node.val == head.val and find_list_from(node, head):
                return True

            return find_head(node.left, head) or find_head(node.right, head)

        def find_list_from(node, curr):
            if curr is None:
                return True

            if node is None:
                return False

            if node.val == curr.val:
                return (
                    find_list_from(node.left, curr.next) or
                    find_list_from(node.right, curr.next)
                )
            return False

        return find_head(root, head)


#
#  Testing
#
from bscom_trees import *
from bscom_linked_lists import *


def test_1():
    root = [1, [2, null, null], [3, [4, null, null], [5, null, null]]]
    head = [1, 3, 4]
    expected = True
    assert Solution().solve(make_tree(root), list_to_ll(head)) == expected


def test_2():
    root = [1, [2, null, null], [3, [4, null, null], [5, null, null]]]
    head = [2, 1, 3, 5]
    expected = False
    assert Solution().solve(make_tree(root), list_to_ll(head)) == expected


def test_3():
    "WA"
    root = [2, [1, [0, null, null], null], null]
    head = [2,0]
    expected = False
    assert Solution().solve(make_tree(root), list_to_ll(head)) == expected


def test_4():
    root = null
    head = [2,0]
    expected = False
    assert Solution().solve(make_tree(root), list_to_ll(head)) == expected


def test_5():
    root = [2, [1, [0, null, null], null], null]
    head = []
    expected = True
    assert Solution().solve(make_tree(root), list_to_ll(head)) == expected
