"""
binarysearch.com :: Complete Binary Tree
jramaswami
"""

class Solution:

    def solve(self, root):

        queue = [root]
        new_queue = []
        while queue:

            # Check queue is valid.
            first_none = len(queue)
            last_value = -1
            for i, t in enumerate(queue):
                if t is None:
                    first_none = min(first_none, i)
                else:
                    last_value = max(last_value, i)
            if last_value > first_none:
                return False

            # BFS
            for node in queue:
                if node:
                    new_queue.append(node.left)
                    new_queue.append(node.right)

            queue, new_queue = new_queue, []

        return True


#
# TESTING
#


from bscom_trees import *


def test_1():
    root = make_tree([0, [1, [1, null, null], [0, null, null]], [0, [1, null, null], [0, null, null]]])
    expected = True
    assert Solution().solve(root) == expected


def test_2():
    root = make_tree([0, [1, [1, null, null], [0, null, null]], [0, null, null]])
    expected = True
    assert Solution().solve(root) == expected


def test_3():
    root = make_tree([0, [1, null, [0, null, null]], [0, null, null]])
    expected = False
    assert Solution().solve(root) == expected


def test_4():
    "WA"
    root = make_tree([0, [1, null, [0, null, null]], [0, null, null]])
    expected = False
    assert Solution().solve(root) == expected
