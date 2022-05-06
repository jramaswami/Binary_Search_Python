"""
binarysearch.com :: Grid Coloring
jramawami
"""


import collections


class Solution:

    OFFSETS = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def solve(self, matrix):

        def inbounds(r, c):
            return r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[r])

        def neighbors(r, c):
            for dr, dc in Solution.OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        def fill_color(color):
            changed = 1
            matrix[0][0] = color
            visited = [[False for _ in row] for row in matrix]
            queue = collections.deque([(0, 0)])
            visited[0][0] = True
            while queue:
                r, c = queue.popleft()
                for r0, c0 in neighbors(r, c):
                    if not visited[r0][c0]:
                        visited[r0][c0] = True
                        if matrix[r0][c0] != color:
                            changed += 1
                            matrix[r0][c0] = color
                            queue.append((r0, c0))
            return changed

        N = len(matrix) * len(matrix[0])
        soln = 0
        while True:
            soln += 1
            color = (1 if matrix[0][0] == 0 else 0)
            changed = fill_color(color)
            if changed == N:
                return soln - 1


def test_1():
    matrix = [
        [0, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 0]
    ]
    expected = 2
    assert Solution().solve(matrix) == expected