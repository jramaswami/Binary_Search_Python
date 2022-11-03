"""
binarysearch.com :: Weekly Contest 42 :: Search in a Virtually Complete Binary Tree
jramaswami
"""

def search(node, target):
    if node is None:
        return False

    if node.val == target:
        return True

    return search(node.left, target) or search(node.right, target)


class Solution:
    def solve(self, root, target):
        return search(root, target)


# binarysearch.com uses "null" in their test cases.
null = None

class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Tree(val={self.val}, left={self.left}, right={self.right}"


def make_tree(array):
    if array == None:
        return None
    val, left, right = array[0], array[1], array[2]
    return Tree(val, make_tree(left), make_tree(right))

def test_1():
    root = [1, [2, [4, null, null], null], [3, [6, null, null], [7, null, null]]]
    target = 6
    assert Solution().solve(make_tree(root), target) == True

def test_2():
    root = [1, [2, [4, null, null], null], [3, [6, null, null], null]]
    target = 7
    assert Solution().solve(make_tree(root), target) == False
