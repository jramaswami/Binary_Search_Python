"""
binarysearch.com :: Binary Search Tree Iterator Sequel
jramaswami
"""


class BSTIterator:
    def __init__(self, root):
        self.values = []
        self._inorder(root)
        print(self.values)
        self.index = 0

    def _inorder(self, node):
        if node is None:
            return
        self._inorder(node.left)
        self.values.append(node.val)
        self._inorder(node.right)

    def next(self):
        x = self.values[self.index]
        self.index += 1
        return x

    def hasnext(self):
        return self.index < len(self.values)

    def prev(self):
        self.index -= 2
        x = self.values[self.index]
        return x

    def hasprev(self):
        return self.index > 2
