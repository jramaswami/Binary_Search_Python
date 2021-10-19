"""
binarysearch.com :: Level Order Traversal
jramaswami
"""


import collections


class Solution:
    def solve(self, root):
        level_order = []
        queue = collections.deque()
        if root:
            queue.append(root)
        while queue:
            node = queue.popleft()
            level_order.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return level_order
