"""
binarysearch.com :: Find a Linked List in a Binary Tree
jramaswami
"""


class Solution:
    def solve(self, root, head):
        if head is None:
            return True
        if root is None:
            return False

        # Build KMP pi.
        P = []
        PI = []
        curr = head
        while curr:
            P.append(curr.val)
            PI.append(0)
            curr = curr.next

        assert len(P) == len(PI)
        i = 0
        for j, _ in enumerate(P[1:], start=1):
            if P[i] == P[j]:
                PI[j] = i + 1
                i += 1
            else:
                PI[j] = 0
                i = 0

        def search(node, i):
            if i == len(P):
                return True

            if node is None:
                return False

            if node.val == P[i]:
                i = i + 1
            else:
                i = PI[i]
            return search(node.left, i) or search(node.right, i)

        return search(root, 0)




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


def test_6():
    "WA"
    root = [1, null, [1, null, [1, null, [1, null, [2, null, null]]]]]
    head = [1,1,1,2]
    expected = True
    assert Solution().solve(make_tree(root), list_to_ll(head)) == expected
