"""
binarysearch.com :: Special Nodes
jramaswami
"""


class Solution:

    def solve(self, tree, color):

        def traverse(node, parent):
            "Returns (number of nodes in subtree, colors, soln accumulator, flag)"
            if node is None:
                return 0, set(), 0, True

            my_nodes = 1
            my_colors = set([color[node]])
            my_acc = 0
            my_flag = True
            for child in tree[node]:
                if child != parent:
                    child_nodes, child_colors, child_acc, child_flag = traverse(child, node)
                    my_flag = my_flag and child_flag
                    my_nodes += child_nodes
                    my_acc += child_acc
                    if my_flag:
                        if len(child_colors) > len(my_colors):
                            child_colors.update(my_colors)
                            my_colors = child_colors
                        else:
                            my_colors.update(child_colors)

            if my_flag:
                if len(my_colors) == my_nodes:
                    my_acc += 1
            else:
                my_colors = set()
            return my_nodes, my_colors, my_acc, my_flag

        return traverse(0, -1)[-2]
