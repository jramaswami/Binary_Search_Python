"""
binarysearch.com :: Binary Search Tree Typo
jramaswami

Inorder traversal of binary search tree should give items in right order.
Do an inorder traversal, sort the nodes by value.  Find the two nodes whose
value does not match the sorted order by value.  Swap the values for those
two nodes.
"""


class Solution:
    def solve(self, root):

        def traverse(node, acc):
            if node is None:
                return

            traverse(node.left, acc)
            acc.append(node)
            traverse(node.right, acc)

        inorder_traversal = []
        traverse(root, inorder_traversal)
        sorted_order = sorted(inorder_traversal, key=lambda a: a.val)
        left, right = [node_inorder for node_inorder, node_sorted
                                    in zip(inorder_traversal, sorted_order)
                                    if node_inorder.val != node_sorted.val]
        left.val, right.val = right.val, left.val
        return root
