"""
binarysearch.com :: Binary Tree to Linked List
jramaswami
"""
from bscom_trees import *
from bscom_linked_lists import *

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        if self.head is None:
            self.head = self.tail = LLNode(val, None)
        else:
            new_node = LLNode(val, None)
            self.tail.next = new_node
            self.tail = new_node

    def __repr__(self):
        return repr(self.head)


class Solution:
    def solve(self, root):
        def inorder(tree_node, linked_list):
            if tree_node == None:
                return

            inorder(tree_node.left, linked_list)
            linked_list.add(tree_node.val)
            inorder(tree_node.right, linked_list)

        linked_list = LinkedList()
        inorder(root, linked_list)
        return linked_list.head


def test_1():
    root = make_tree([2, [1, null, null], [4, [3, null, null], null]])
    assert ll_to_list(Solution().solve(root)) == [1, 2, 3, 4]
