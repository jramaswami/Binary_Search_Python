"""
binarysearch.com :: Matrix Search Sequel
jramaswami
"""


class Solution:
    def solve(self, matrix, target):
        # Corner case.
        if matrix == [] or matrix[0] == []:
            return False

        r, c = 0, len(matrix[0]) - 1
        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] < target:
                r += 1
            elif matrix[r][c] > target:
                c -= 1
        return False


def test_1():
    matrix = [
        [1, 3, 9],
        [2, 5, 10],
        [5, 7, 13]
    ]
    target = 7
    assert Solution().solve(matrix, target) == True


def test_2():
    matrix = [
        [1, 3, 9],
        [2, 5, 10],
        [5, 7, 13]
    ]
    target = 6
    assert Solution().solve(matrix, target) == False


def test_3():
    matrix = []
    target = 6
    assert Solution().solve(matrix, target) == False


def test_4():
    matrix = [[], [], []]
    target = 6
    assert Solution().solve(matrix, target) == False
