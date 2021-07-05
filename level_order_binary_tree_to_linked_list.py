"""
binarysearch.com :: Level Order Binary Tree to Linked List
jramaswami
"""


from collections import deque


class Solution:
    def solve(self, root):
        dummy_head = LLNode(-1, None)
        queue = deque()
        queue.append(root)
        prev_ll_node = dummy_head
        while queue:
            tree_node = queue.popleft()
            if tree_node:
                ll_node = LLNode(tree_node.val, None)
                prev_ll_node.next = ll_node
                prev_ll_node = ll_node
                queue.append(tree_node.left)
                queue.append(tree_node.right)
        return dummy_head.next
