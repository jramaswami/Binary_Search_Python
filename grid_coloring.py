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

        visited = [[False for _ in row] for row in matrix]

        def find_next_frontier(curr_frontier):
            next_frontier = collections.deque()
            while curr_frontier:
                r, c = curr_frontier.popleft()
                for r0, c0 in neighbors(r, c):
                    if not visited[r0][c0]:
                        visited[r0][c0] = True
                        if matrix[r0][c0] != matrix[r][c]:
                            next_frontier.append((r0, c0))
                        else:
                            curr_frontier.append((r0, c0))
            return next_frontier

        soln = 0
        frontier = collections.deque([(0, 0)])
        visited[0][0] = True
        while True:
            next_frontier = find_next_frontier(frontier)
            if not next_frontier:
                return soln
            soln += 1
            frontier = next_frontier


def test_1():
    matrix = [
        [0, 0, 0, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 0]
    ]
    expected = 2
    assert Solution().solve(matrix) == expected