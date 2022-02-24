"""
binarysearch.com :: Binary Tree Width
jramaswami
"""


import collections
import math


class Solution:

    def solve(self, root):
        level_mins = collections.defaultdict(lambda: math.inf)
        level_maxs = collections.defaultdict(lambda: -math.inf)

        def traverse(node, level, index):
            if node is None:
                return

            level_mins[level] = min(level_mins[level], index)
            level_maxs[level] = max(level_maxs[level], index)

            right_index = 2 * index
            left_index = right_index - 1
            traverse(node.left, level + 1, left_index)
            traverse(node.right, level + 1, right_index)

        traverse(root, 0, 1)
        return max(level_maxs[l] - level_mins[l] + 1 for l in level_mins)
