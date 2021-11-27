"""
binarysearch.com :: Longest Increasing Path
jramaswami
"""


class Solution:
    def solve(self, matrix):
        OFFSETS = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def inbounds(r, c):
            return r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[r])

        def neighbors(r, c):
            for dr, dc in OFFSETS:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        order = sorted(((matrix[r][c], r, c) for r, row in enumerate(matrix)
                                             for c, _ in enumerate(row)))
        dist = [[1 for _ in row] for row in matrix]
        soln = 1
        for _, r, c in order:
            for r0, c0 in neighbors(r, c):
                if matrix[r][c] < matrix[r0][c0]:
                    dist[r0][c0] = max(dist[r0][c0], dist[r][c] + 1)
                    soln = max(soln, dist[r0][c0])
        return soln


def test_1():
    matrix = [
        [1, 3, 5],
        [0, 4, 6],
        [2, 2, 9]
    ]
    expected = 6
    assert Solution().solve(matrix) == expected


def test_2():
    "WA"
    matrix = [[0]]
    expected = 1
    assert Solution().solve(matrix) == expected
