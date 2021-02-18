"""
binarysearch.com :: Lowest Common Ancestor
jramaswami
"""
def dfs(u, p, h, parent, level):
    """DFS to establish parentage and level."""
    if p:
        parent[u.val] = p.val
    else:
        parent[u.val] = None
    level[u.val] = h

    if u.left:
        dfs(u.left, u, h+1, parent, level)
    if u.right:
        dfs(u.right, u, h+1, parent, level)


def lca(a, b, parent, level):
    """Get LCA by moving up the tree until pointer meet."""
    if level[a] < level[b]:
        a, b = b, a

    while level[a] > level[b]:
        a = parent[a]

    while a != b:
        a = parent[a]
        b = parent[b]

    return a


class Solution:
    def solve(self, root, a, b):
        level = dict()
        parent = dict()
        dfs(root, None, 0, parent, level)
        print(parent)
        print(level)
        return lca(a, b, parent, level)


from bscom_trees import *

def test_1():
    root = make_tree([0, [1, null, null], [2, [6, [3, null, null], [4, null, null]], [5, null, null]]])
    a = 3
    b = 5
    assert Solution().solve(root, a, b) == 2

def test_2():
    root = make_tree([0, [1, null, null], [2, [6, [3, null, null], [4, null, null]], [5, null, null]]])
    a = 6
    b = 4
    assert Solution().solve(root, a, b) == 6

def test_3():
    root = make_tree([0, [1, null, null], [2, [6, [3, null, null], [4, null, null]], [5, null, null]]])
    a = 2
    b = 3
    assert Solution().solve(root, a, b) == 2

def test_4():
    root = make_tree([0, [1, null, null], [2, [6, [3, null, null], [4, null, null]], [5, null, null]]])
    a = 1
    b = 5
    assert Solution().solve(root, a, b) == 0

def test_5():
    root = make_tree([0, [1, null, null], [2, [6, [3, null, null], [4, null, null]], [5, null, null]]])
    a = 6
    b = 6
    assert Solution().solve(root, a, b) == 6

def test_6():
    root = make_tree([0, [1, null, null], [2, [6, [3, null, null], [4, null, null]], [5, null, null]]])
    a = 0
    b = 0
    assert Solution().solve(root, a, b) == 0
