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
        return f"Tree(val={self.val}, left={self.left}, right={self.right})"

    def __eq__(self, other):
        if other is None:
            return self is None
        return self.val == other.val and self.left == other.left and self.right == other.right


def make_tree(array):
    if array == None:
        return None
    if len(array) == 1:
        return Tree(array[0], None, None)
    val, left, right = array[0], array[1], array[2]
    return Tree(val, make_tree(left), make_tree(right))
