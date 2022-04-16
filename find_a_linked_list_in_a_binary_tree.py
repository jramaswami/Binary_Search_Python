"""
binarysearch.com :: Find a Linked List in a Binary Tree
jramaswami

REF: https://www.youtube.com/watch?v=GTJr8OvyEVQ
"""


def ll_to_list(head):
    A = []
    curr = head
    while curr:
        A.append(curr.val)
        curr = curr.next
    return A


def prefix_function(pattern):
    longest_prefix_suffix = [0 for _ in pattern]
    index = 0
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[index]:
            longest_prefix_suffix[i] = index + 1
            index += 1
            i += 1
        else:
            if index != 0:
                index = longest_prefix_suffix[index-1]
            else:
                longest_prefix_suffix[i] = 0
                i += 1
    return longest_prefix_suffix


class Solution:
    def solve(self, root, head):
        if head is None:
            return True
        if root is None:
            return False

        # Build KMP prefix/suffix table.
        pattern = ll_to_list(head)
        longest_prefix_suffix = prefix_function(pattern)

        def search(node, j):
            if j == len(pattern):
                return True

            if node is None:
                return False

            if node.val == pattern[j]:
                return search(node.left, j+1) or search(node.right, j+1)
            else:
                if j != 0:
                    j = longest_prefix_suffix[j-1]
                    return search(node, j)
                else:
                    return search(node.left, j) or search(node.right, j)

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
