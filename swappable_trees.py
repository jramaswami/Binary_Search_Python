"""
binarysearch.com :: Swappable Trees
jramaswami
"""


class Solution:

    def solve(self, root0, root1):
        # Base Case.
        if root0 is None and root1 is None:
            return True

        # If only one of the nodes is None then they cannot be equal.
        if root0 is None:
            return False

        if root1 is None:
            return False

        # If they have different values then they cannot be equal.
        if root0.val != root1.val:
            return False

        # If the values are equal, see if the subtrees are equal the
        # way they are or swapped.
        resultUnswapped = self.solve(root0.left, root1.left) and self.solve(root0.right, root1.right)
        resultSwapped = self.solve(root0.right, root1.left) and self.solve(root0.left, root1.right)
        return resultUnswapped or resultSwapped


#
# Testing
#


from bscom_trees import *


def test_1():
    root0 = [1, [3, null, null], [4, [0, null, [2, null, null]], null]]
    root1 = [1, [3, null, null], [4, [0, null, [2, null, null]], null]]
    expected = True
    assert Solution().solve(make_tree(root0), make_tree(root1)) == expected