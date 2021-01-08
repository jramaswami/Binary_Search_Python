"""
binaryseach.com :: Leaves in Same Level
jramaswami
"""
class Solution:
    def solve(self, root):
        if root is None:
            return True

        # BFS and is should all end at the same time.
        queue = [root]
        new_queue = []

        while queue:
            leaf_found = False
            for node in queue:
                if node.right is None and node.left is None:
                    leaf_found = True

                if node.right:
                    new_queue.append(node.right)
                if node.left:
                    new_queue.append(node.left)

            if new_queue and leaf_found:
                return False

            queue, new_queue, = new_queue, []

        return True


# For testing.
from bscom_trees import *

def test_1():
    root = make_tree([3, [4, null, [2, null, null]], [1, [0, null, null], null]])
    assert Solution().solve(root) == True

def test_2():
    root = make_tree([1, [2, null, null], [3, null, [4, null, null]]])
    assert Solution().solve(root) == False

def test_3():
    assert Solution().solve(None) == True
