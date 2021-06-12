"""
binarysearch.com :: Binary Matrix Leftmost One
jramaswami
"""


class Solution:
    def solve(self, matrix):
        # Edge case: nothing in the matrix.
        if not matrix:
            return -1

        i = len(matrix)
        for row in matrix:
            while i - 1 >= 0 and row[i-1] == 1:
                i -= 1
        if i < len(matrix[0]):
            return i
        return -1


def test_1():
    matrix = [
        [0, 0, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 0, 1],
        [0, 1, 1, 1]
    ]
    assert Solution().solve(matrix) == 1



def test_2():
    matrix = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == -1


def test_3():
    matrix = [
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 1, 1]
    ]
    assert Solution().solve(matrix) == 0


def test_4():
    """WA"""
    matrix = [[0, 1]]
    assert Solution().solve(matrix) == 1


def test_5():
    """WA"""
    matrix = []
    assert Solution().solve(matrix) == -1


def test_6():
    """WA"""
    matrix = [[0, 0]]
    assert Solution().solve(matrix) == -1

