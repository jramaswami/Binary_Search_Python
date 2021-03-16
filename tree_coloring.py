"""
binarysearch.com :: Tree Coloring
jramaswami
"""
from collections import deque, defaultdict


class Solution:
    def solve(self, root):
        queue = deque()
        parity_freqs = defaultdict(int)
        color_freqs = defaultdict(int)
        node_count = 0
        queue.append((0, root))
        while queue:
            level, node = queue.popleft()
            if node:
                node_count += 1
                parity_freqs[level % 2] += 1
                color_freqs[node.val] += 1
                queue.append((level + 1, node.left))
                queue.append((level + 1, node.right))

        if node_count == 0:
            return True
        if node_count == 1:
            return True
        
        if node_count > 1 and len(color_freqs) < 2:
            return False

        color0, color1 = list(color_freqs)
        if parity_freqs[0] == color_freqs[color0] and parity_freqs[1] == color_freqs[color1]:
            return True
        if parity_freqs[0] == color_freqs[color1] and parity_freqs[1] == color_freqs[color0]:
            return True
        return False

#
# Testing
#
from bscom_trees import *

def test_1():
    root = make_tree([1, [1, null, null], [1, [0, null, [0, null, null]], [0, null, null]]])
    assert Solution().solve(root) == True

def test_2():
    root = make_tree([5, null, [9, [5, null, null], [9, null, null]]])
    assert Solution().solve(root) == False

def test_3():
    root = None
    assert Solution().solve(root) == True

def test_4():
    root = make_tree([0, null, null])
    assert Solution().solve(root) == True

def test_5():
    root = make_tree([6, [6, null, null], null])
    assert Solution().solve(root) == False

