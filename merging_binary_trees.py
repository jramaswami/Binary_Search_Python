"""
binarysearch.com :: Merging Binary Trees
jramaswami
"""
def solve0(node0, node1):
    """Recursive solution."""
    if node0 is None and node1 is None:
        return None

    if node0 is None:
        return Tree(node1.val, solve0(None, node1.left), solve0(None, node1.right))

    if node1 is None:
        return Tree(node0.val, solve0(node0.left, None), solve0(node0.right, None))

    return Tree(node0.val + node1.val, solve0(node0.left, node1.left), solve0(node0.right, node1.right))


class Solution:
    def solve(self, node0, node1):
        return solve0(node0, node1)