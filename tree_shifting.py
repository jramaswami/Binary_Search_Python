"""
binarysearch.com :: Tree Shifting
jramaswami
"""


class Solution:
    def solve(self, root):
        # Corner case: null tree.
        if root is None:
            return None


        def dfs(node, level, level_order):
            """DFS to get the level order."""
            if node is None:
                return

            if level == len(level_order):
                level_order.append([])
            level_order[level].append(node)

            dfs(node.left, level+1, level_order)
            dfs(node.right, level+1, level_order)

        # Shift tree.
        level_order = []
        dfs(root, 0, level_order)
        level_order = list(reversed(level_order))
        for bottom, top in zip(level_order[:-1], level_order[1:]):
            j = len(bottom) - 1
            for top_node in reversed(top):
                if j >= 0:
                    top_node.right = bottom[j]
                    j -= 1
                else:
                    top_node.right = None
                if j >= 0:
                    top_node.left = bottom[j]
                    j -= 1
                else:
                    top_node.left = None

        return level_order[-1][0]
