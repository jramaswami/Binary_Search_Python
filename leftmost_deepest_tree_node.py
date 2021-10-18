"""
binarysearch.com :: Leftmost Deepest Tree Node
jramaswami
"""


class Solution:

    def solve(self, root):

        def traverse(node, level, acc):
            if node is None:
                return

            while level >= len(acc):
                acc.append([])

            acc[level].append(node.val)

            traverse(node.left, level + 1, acc)
            traverse(node.right, level + 1, acc)

        acc = []
        traverse(root, 0, acc)
        return acc[-1][0]
