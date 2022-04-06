"""
binarysearch.com :: Toeplitz Matrix
jramaswami
"""


class Solution:
    def solve(self, matrix):
        def inbounds(r, c):
            return r >= 0 and r < len(matrix) and c >= 0 and c < len(matrix[r])

        for c, _ in enumerate(matrix[0]):
            r = 0
            curr = matrix[r][c]
            while inbounds(r, c):
                if matrix[r][c] != curr:
                    return False
                r, c = r + 1, c + 1

        for r, _ in enumerate(matrix[1:], start=1):
            c = 0
            curr = matrix[r][c]
            while inbounds(r, c):
                if matrix[r][c] != curr:
                    return False
                r, c = r + 1, c + 1

        return True



def test_1():
    matrix = [ [0, 1, 2], [3, 0, 1], [4, 3, 0], [5, 4, 3] ]
    expected = True
    assert Solution().solve(matrix) == expected


def test_2():
    matrix = [ [1, 0, 0], [0, 0, 0], [0, 0, 1] ]
    expected = False
    assert Solution().solve(matrix) == expected
