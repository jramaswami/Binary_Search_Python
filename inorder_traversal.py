"""
binarysearch.com :: Inorder Traversal
jramaswami
"""
class Solution:
    def solve(self, root):
        traversal = []
        if root is None:
            return traversal

        WHITE = -1
        BLACK = 1
        queue = [(WHITE, root)]
        while queue:
            color, node = queue.pop()
            if color == WHITE:
                # First push node back on queue as BLACK
                queue.append((BLACK, node))
                # Go left.
                if node.left:
                    queue.append((WHITE, node.left))
            elif color == BLACK:
                # Process node
                traversal.append(node.val)
                # Go right.
                if node.right:
                    queue.append((WHITE, node.right))
        return traversal

#
# TESTING
#

from bscom_trees import *

def test_1():
    root = make_tree([1, null, [159, [80, null, null], null]])
    assert Solution().solve(root) == [1, 80, 159]
