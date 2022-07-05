"""
binarysearch.com :: Largest Square Matrix with Same Value
jramaswami
"""


class Solution:
    def solve(self, matrix):
        # Boundary case:
        if matrix == [] or matrix == [[]]:
            return 0

        offsets = [(1, 0), (0, 1), (1, 1)]
        def parent_values(r, c):
            for dr, dc in offsets:
                yield matrix[r-dr][c-dc]

        def parent_freqs(r, c):
            for dr, dc in offsets:
                yield dp[r-dr][c-dc]

        soln = 1  # There is always a 1 square.
        dp = [[1 for _ in row] for row in matrix]
        for r, row in enumerate(matrix[1:], start=1):
            for c, v in enumerate(row[1:], start=1):
                if all(t == v for t in parent_values(r, c)):
                    dp[r][c] = 1 + min(parent_freqs(r, c))
                soln = max(soln, dp[r][c])
        return soln


def test_1():
    matrix = [ [1, 1, 3], [1, 1, 3], [5, 5, 5] ]
    expected = 2
    assert Solution().solve(matrix) == expected
