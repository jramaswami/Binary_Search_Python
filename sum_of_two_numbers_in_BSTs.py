"""
binarysearch.com :: Sum of Two Numbers in BSTs
jramaswami
"""


class Solution:
    def solve(self, left_tree, right_tree, target):

        def gather(node, acc):
            "Gather all the values from the tree."
            if node is None:
                return

            acc.add(node.val)
            gather(node.left, acc)
            gather(node.right, acc)

        def solve0(node, target, acc):
            "Given all numbers from other tree (acc), see if you can find sum to target."
            if node is None:
                return False

            delta = target - node.val
            if delta in acc:
                return True

            return solve0(node.left, target, acc) or solve0(node.right, target, acc)

        acc = set()
        gather(left_tree, acc)
        return solve0(right_tree, target, acc)
