"""
binarysearch.com :: Left Side View of a Tree
jramaswami
"""
def solve0(node, level, acc):
    """Recursive solution."""
    if node is None:
        return
    if len(acc) == level:
        acc.append(node.val)
    solve0(node.left, level + 1, acc)
    solve0(node.right, level + 1, acc)


class Solution:
    def solve(self, root):
        soln = []
        solve0(root, 0, soln)
        return soln
