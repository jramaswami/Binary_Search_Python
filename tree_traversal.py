"""
binarysearch.com :: Tree Traversal
jramaswami
"""
class Solution:
    def solve(self, root, moves):
        stack = []
        soln = None
        curr = root
        for move in moves:
            if move == 'UP':
                curr = stack.pop()
            elif move == 'LEFT':
                stack.append(curr)
                curr = curr.left
            elif move == 'RIGHT':
                stack.append(curr)
                curr = curr.right
        return curr.val
