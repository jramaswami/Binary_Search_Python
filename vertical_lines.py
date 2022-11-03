"""
binarysearch.com :: Vertical Lines in Binary Tree
https://binarysearch.com/room/Weekly-Contest-37-u2kU8duwTB
"""

def dfs(node, num):
    l = r = num
    if node.left:
        t = dfs(node.left, num - 1)
        l = min(l, t[0])
        r = max(r, t[1])
    if node.right:
        t = dfs(node.right, num + 1)
        l = min(l, t[0])
        r = max(r, t[1])
    return l, r


class Solution:
    def solve(self, root):
        l, r = dfs(root, 0)
        return r - l

# root = [1, [2, [3, null, null], null], [4, null, [5, null, null]]]