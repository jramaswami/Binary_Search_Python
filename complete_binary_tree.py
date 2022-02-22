"""
binarysearch.com :: Complete Binary Tree
jramaswami
"""


import math


class Solution:

    def solve(self, root):

        node_count = 0
        level_count = 0
        queue = [root]
        new_queue = []
        while queue:
            level_count += 1
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
                    node_count += 1
                    new_queue.append(node.left)
                    new_queue.append(node.right)


            if all(node is None for node in new_queue):
                break

            queue, new_queue = new_queue, []

        return int(math.ceil(math.log2(node_count))) == level_count


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
    root = make_tree([0, [1, [1, null, null], [0, null, null]], null])
    expected = False
    assert Solution().solve(root) == expected


def test_5():
    "RTE"
    root = None
    expected = True
    assert Solution().solve(root) == expected
