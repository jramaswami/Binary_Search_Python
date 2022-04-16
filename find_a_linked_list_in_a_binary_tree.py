"""
binarysearch.com :: Find a Linked List in a Binary Tree
jramaswami
"""


import collections


class Solution:
    def solve(self, root, head):
        if head is None:
            return True
        if root is None:
            return False

        def find_list_from(node):
            P = collections.deque()
            P.append((node, head))
            while P:
                tree_node, list_node = P.popleft()
                if list_node.next is None:
                    return True
                if tree_node.left and tree_node.left.val == list_node.next.val:
                    P.append((tree_node.left, list_node.next))
                if tree_node.right and tree_node.right.val == list_node.next.val:
                    P.append((tree_node.right, list_node.next))
            return False

        Q = collections.deque()
        Q.append(root)
        while Q:
            tree_node = Q.popleft()
            if tree_node.val == head.val and find_list_from(tree_node):
                return True
            if tree_node.left:
                Q.append(tree_node.left)
            if tree_node.right:
                Q.append(tree_node.right)
        return False


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
