"""
binarysearch.com :: Rotate by 90 Degrees Counter-Clockwise
jramaswami
"""
class Solution:
    def solve(self, matrix):
        """Rotate matrix 90 degrees counterclockwise, in place."""
        # This is a transpose followed by a horizontal flip.
        # Transpose
        for r, row in enumerate(matrix):
            for c, _ in enumerate(row):
                if r > c:
                    matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        # Flip
        N = len(matrix)
        for c, _ in enumerate(matrix[0]):
            for r, _ in enumerate(matrix):
                if r >= (N // 2):
                    break
                matrix[r][c], matrix[N - r - 1][c] = matrix[N - r - 1][c], matrix[r][c]
        
        return matrix

def test_1():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected = [
        [3, 6, 9],
        [2, 5, 8],
        [1, 4, 7]
    ]
    assert Solution().solve(matrix) == expected

def test_2():
    matrix = [
        [0, 1],
        [2, 3]
    ]
    expected = [
        [1, 3],
        [0, 2]
    ]
    assert Solution().solve(matrix) == expected
