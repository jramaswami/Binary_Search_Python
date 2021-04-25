"""
binarysearch.com :: Length of a Linked List
jramaswami
"""
def solve0(node, acc):
    """Recursive solution."""
    if node is None:
        return acc
    return solve0(node.next, acc + 1)


class Solution:
    def solve(self, node):
        return solve0(node, 0)