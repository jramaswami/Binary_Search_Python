"""
binarysearch.com :: Binary Search Tree Iterator Sequel
jramaswami
"""


class BSTIterator:
    def __init__(self, root):
        self.values = []
        self._inorder(root)
        self.index = -1

    def _inorder(self, node):
        if node is None:
            return
        self._inorder(node.left)
        self.values.append(node.val)
        self._inorder(node.right)

    def next(self):
        self.index += 1
        return self.values[self.index]

    def hasnext(self):
        return self.index < len(self.values) - 1

    def prev(self):
        self.index -= 1
        return self.values[self.index]

    def hasprev(self):
        return self.index > 0
