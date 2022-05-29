"""
binarysearch.com :: Special Nodes
jramaswami
"""


class Solution:

    def solve(self, tree, color):

        def traverse(node, parent):
            "Returns (number of nodes in subtree, colors, soln accumulator)"
            if node is None:
                return 0, set(), 0

            my_nodes = 1
            my_colors = set([color[node]])
            my_acc = 0
            for child in tree[node]:
                if child != parent:
                    child_nodes, child_colors, child_acc = traverse(child, node)
                    my_nodes += child_nodes
                    my_colors |= child_colors
                    my_acc += child_acc
            if len(my_colors) == my_nodes:
                my_acc += 1

            return my_nodes, my_colors, my_acc

        return traverse(0, -1)
