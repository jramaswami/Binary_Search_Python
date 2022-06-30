"""
binarysearch.com :: Matrix Rectangular Sums
jramaswami
"""


class Solution:
    def solve(self, matrix, k):
        prefix = [[0 for _ in row] for row in matrix]

        def get_prefix(r, c):
            if r < 0 or c < 0:
                return 0
            return prefix[r][c]

        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                prefix[r][c] = (
                    matrix[r][c] +
                    get_prefix(r-1,c) +
                    get_prefix(r, c-1) -
                    get_prefix(r-1,c-1)
                )

        def get_sum(r1, c1, r2, c2):
            return (
                get_prefix(r2, c2) -
                get_prefix(r1-1, c2) -
                get_prefix(r2, c1-1) +
                get_prefix(r1-1,c1-1)
            )

        H = len(matrix)
        W = len(matrix[0])
        soln= [[0 for _ in row] for row in matrix]
        for r, row in enumerate(soln):
            for c, _ in enumerate(row):
                r1 = max(0, r-k)
                c1 = max(0, c-k)
                r2 = min(H-1, r+k)
                c2 = min(W-1, c+k)
                matrix[r][c] = get_sum(r1, c1, r2, c2)
        return matrix



def test_1():
    matrix = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
    k = 1
    expected = [ [12, 21, 16], [27, 45, 33], [24, 39, 28] ]
    assert Solution().solve(matrix, k) == expected
