"""
binarysearch.com :: Longest Matrix Path
jramaswami
"""


class Solution:
    def solve(self, matrix):
        def inbounds(r, c):
            """Return True if r, c is inside the matrix."""
            return r >= 0 and c >= 0 and r < len(matrix) and c < len(matrix[0])

        def neighbors(r, c):
            """
            Return list of neighbors of r, c.
            Movement is down, left, or right.
            """
            offsets = [(1, 0), (0, -1), (0, 1)]
            for dr, dc in offsets:
                r0 = r + dr
                c0 = c + dc
                if inbounds(r0, c0):
                    yield (r0, c0)

        def dfs(r, c, pr, pc, steps):
            """
            DFS to traverse matrix.
            """
            soln = 0
            ns = [(r0, c0) for r0, c0 in neighbors(r, c) if matrix[r0][c0] == 0 and (r0, c0) != (pr, pc)]
            if ns:
                for r0, c0 in ns:
                    soln = max(soln, dfs(r0, c0, r, c, steps + 1))
                return soln
            else:
                if r == len(matrix) - 1:
                    return steps
                return 0

        soln = 0
        for c in range(len(matrix[0])):
            if matrix[0][c] == 0:
                soln = max(soln, dfs(0, c, -1, -1, 1))
        return soln


def test_1():
    matrix = [
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == 10


def test_2():
    matrix = [
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == 0


def test_3():
    matrix = [[0]]
    assert Solution().solve(matrix) == 1


def test_4():
    matrix = [[1]]
    assert Solution().solve(matrix) == 0


def test_5():
    matrix = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1]
    ]
    assert Solution().solve(matrix) == 0


def test_6():
    """WA"""
    matrix = [ [1, 0] ]
    assert Solution().solve(matrix) == 1
