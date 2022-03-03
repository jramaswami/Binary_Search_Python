"""
binarysearch.com :: Level Order Alternating
jramaswami
"""


class Solution:

    def solve(self, root):

        levels = []
        def traverse(node, level):
            if node is None:
                return
            if len(levels) <= level:
                levels.append([])
            levels[level].append(node)
            traverse(node.left, level+1)
            traverse(node.right, level+1)

        traverse(root, 0)
        soln = []
        for i, level in enumerate(levels):
            if i % 2:
                soln.extend(reversed(level))
            else:
                soln.extend(level)
        return [node.val for node in soln]

