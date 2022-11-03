"""
binarysearch.com :: Collecting Coins Sequel
jramaswami
"""


from math import inf


class MatrixGraph:
    """Matrix as graph."""

    def __init__(self, matrix):
        self.matrix = matrix
        self.offsets = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def inbounds(self, r, c):
        """Return True if (r, c) is inside the matrix."""
        return (r >= 0 and c >= 0 and
                r < len(self.matrix) and c < len(self.matrix[r])
        )

    def neighbors(self, r, c):
        """Return the four neighbors of (r, c)."""
        for dr, dc in self.offsets:
            r0 = r + dr
            c0 = c + dc
            if self.inbounds(r0, c0):
                yield (r0, c0)

    def get(self, r, c):
        """Return value at matrix[r][c]."""
        return self.matrix[r][c]


class MaxPath:
    def __init__(self, src_r, src_c, matrix):
        self.matrix = matrix
        self.visited = set()
        self.curr_score = 0
        self.max_score = 0
        self.max_path = set()
        self._dfs(src_r, src_c)

    def _dfs(self, r, c):
        """DFS to traverse matrix."""
        # Add to visited
        self.visited.add((r, c))
        self.curr_score += self.matrix.get(r, c)
        deadend = True
        for r0, c0 in self.matrix.neighbors(r, c):
            if (r0, c0) not in self.visited and self.matrix.get(r0, c0) != 0:
                deadend = False
                self._dfs(r0, c0)

        # If this is a deadend and we have a new high score, record
        # cells used and the new max score.
        if deadend and self.curr_score > self.max_score:
            self.max_path = set(self.visited)
            self.max_score = self.curr_score

        self.curr_score -= self.matrix.get(r, c)
        self.visited.remove((r, c))


class Solution:
    def solve(self, matrix):
        matrix_g = MatrixGraph(matrix)
        soln = -inf
        visited = set()
        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                if (r, c) not in visited:
                    print(f"{r=} {c=} {visited=}")
                    path = MaxPath(r, c, matrix_g)
                    visited.update(path.max_path)
                    soln = max(soln, path.max_score)
        return soln-1



def test_1():
    matrix = [
        [1, 3, 2],
        [2, 5, 0],
        [1, 0, 10]
    ]
    expected = 13
    assert Solution().solve(matrix) == 13


def test_2():
    matrix = [
        [1,2,3,4,5],
        [6,7,8,9,1],
        [2,3,4,5,6],
        [7,8,9,1,2],
        [3,4,5,6,7]
    ]
    expected = 13
    assert Solution().solve(matrix) == 118


def test_3():
    matrix = [
        [4, 1, 0, 4, 0, 0, 2, 1, 3, 0, 3, 4, 2, 0, 1, 5, 2, 1, 0, 3],
        [2, 4, 0, 5, 2, 4, 0, 2, 4, 2, 4, 3, 5, 3, 2, 1, 2, 3, 4, 2],
        [2, 0, 4, 5, 2, 0, 2, 1, 0, 5, 4, 2, 0, 4, 1, 3, 3, 3, 4, 5],
        [3, 5, 1, 0, 0, 5, 4, 3, 1, 3, 3, 2, 2, 3, 2, 3, 0, 5, 1, 1],
        [0, 3, 3, 1, 4, 3, 4, 2, 5, 0, 3, 2, 2, 1, 3, 2, 3, 1, 2, 5],
        [0, 5, 5, 5, 5, 1, 3, 4, 2, 0, 1, 2, 0, 5, 4, 4, 0, 5, 5, 1],
        [3, 4, 4, 3, 1, 5, 3, 0, 0, 0, 3, 3, 4, 5, 1, 0, 4, 3, 2, 1],
        [2, 4, 0, 1, 1, 4, 1, 5, 3, 1, 0, 2, 3, 3, 5, 5, 2, 0, 1, 2],
        [4, 0, 5, 3, 1, 0, 3, 3, 2, 5, 4, 0, 3, 1, 4, 4, 2, 5, 2, 5],
        [0, 4, 4, 1, 0, 5, 2, 2, 4, 2, 0, 3, 3, 1, 5, 0, 5, 4, 4, 5],
        [2, 5, 2, 0, 5, 2, 2, 4, 2, 4, 0, 1, 4, 5, 5, 5, 0, 1, 5, 0],
        [4, 4, 5, 4, 0, 2, 0, 4, 0, 4, 4, 0, 2, 5, 4, 0, 3, 5, 0, 3],
        [2, 4, 0, 5, 2, 0, 0, 5, 5, 5, 4, 0, 3, 2, 2, 5, 2, 5, 5, 0],
        [0, 2, 0, 4, 5, 0, 4, 2, 5, 1, 3, 0, 1, 5, 0, 3, 2, 0, 4, 3],
        [5, 4, 4, 1, 3, 5, 2, 3, 2, 4, 5, 2, 1, 1, 2, 2, 2, 4, 4, 1],
        [0, 3, 5, 1, 1, 3, 3, 1, 3, 3, 0, 4, 5, 3, 3, 0, 0, 0, 2, 5],
        [5, 0, 0, 5, 4, 2, 3, 3, 4, 5, 0, 3, 0, 3, 3, 2, 1, 4, 3, 4],
        [5, 0, 4, 2, 3, 2, 1, 1, 1, 5, 1, 5, 5, 2, 2, 4, 3, 1, 5, 4],
        [0, 4, 3, 5, 5, 5, 4, 3, 3, 5, 3, 1, 0, 3, 5, 0, 0, 0, 0, 0],
        [0, 1, 5, 1, 4, 2, 5, 5, 1, 0, 1, 3, 5, 5, 2, 2, 2, 2, 1, 4]
    ]
    expected = 13
    assert Solution().solve(matrix) == 118
