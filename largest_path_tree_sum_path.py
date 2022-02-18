"""
binarysearch.com :: Largest Tree Sum Path
jramaswami
"""


import math


class Solution:
    def solve(self, root):

        answer = -math.inf
        def traverse(node):
            if node is None:
                return 0

            x = dfs(node.left)
            y = dfs(node.right)
            answer = max(answer, x + y + node.val)
            return max(0, node.val + max(x, y))

        traverse(root)
        return answer


# WA: [5, [-2, null, null], [-2, null, null]]
# WA: [2, [1, [0, null, null], null], [3, null, null]]
