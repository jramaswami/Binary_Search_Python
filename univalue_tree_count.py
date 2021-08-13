"""
binarysearch.com :: Univalue Tree Count
jramaswami
"""

def is_leaf(node):
    return node.left is None and node.right is None


def get_val(node, default):
    return default if node is None else node.val


def solve(node):
    if node is None:
        return True, 0

    univalue_left, left_acc = solve(node.left)
    univalue_right, right_acc = solve(node.right)

    if (univalue_left and univalue_right
    and get_val(node.left, node.val) == node.val
    and get_val(node.right, node.val) == node.val):
        return True, left_acc + right_acc + 1
    else:
        return False, left_acc + right_acc


class Solution():
    def solve(self, root):
        return solve(root)[1]
