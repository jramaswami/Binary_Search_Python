"""
binarysearch.com :: Linked List to ZigZag Tree Path
jramaswami
"""


class Solution:
    def solve(self, node):
        # Boundary case: empty linked list.
        if node is None:
            return None

        curr_list = node.next
        head_tree = curr_tree = Tree(node.val)
        while curr_list:
            if curr_list.val < curr_tree.val:
                curr_tree.left = Tree(curr_list.val)
                curr_tree = curr_tree.left
            else:
                curr_tree.right= Tree(curr_list.val)
                curr_tree = curr_tree.right
            curr_list = curr_list.next

        return head_tree
