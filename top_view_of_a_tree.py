"""
binarysearch.com :: Top View of a Tree
jramaswami
"""


import collections
import math


class Solution:
    def solve(self, root):
        coordinates = collections.defaultdict(lambda: (math.inf, math.inf))

        def traverse(node, coord, level):
            if node is None:
                return

            if coordinates[coord][1] > level:
                coordinates[coord] = (node.val, level)
            traverse(node.left, coord - 1, level + 1)
            traverse(node.right, coord + 1, level + 1)

        traverse(root, 0, 0)
        return [coordinates[c][0] for c in sorted(coordinates.keys())]
