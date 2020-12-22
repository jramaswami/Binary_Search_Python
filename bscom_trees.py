"""
For testing of binarysearch.com trees
"""

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

