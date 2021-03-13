"""
binarysearch.com :: Sum of the Deepest Nodes
jramaswami
"""
from collections import deque


class Solution:
    def solve(self, root):
        queue = deque()
        sums = [0]
        queue.append((1, root))
        while queue:
            level, node = queue.popleft()
            if node:
                while len(sums) <= level:
                    sums.append(0)
                sums[level] += node.val
                queue.append((level + 1, node.left))
                queue.append((level + 1, node.right))
        return sums[-1]

#
# Testing
#
from bscom_trees import *

def test_1():
    root = make_tree([0, [5, null, null], [9, [1, [4, null, null], [2, null, null]], [3, null, null]]])
    assert Solution().solve(root) == 6

def test_2():
    root = make_tree([0, [5, null, null], [9, null, [3, null, null]]])
    assert Solution().solve(root) == 3
