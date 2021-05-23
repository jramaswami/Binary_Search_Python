"""
binarysearch.com :: Valid N Queens
jramaswami
"""


from collections import namedtuple
from itertools import combinations


Queen = namedtuple('Queen', ['rank', 'file'])


def get_queens(board):
    """Return list of queens on the board."""
    queens = []
    for chess_rank, row in enumerate(board):
        for chess_file, val in enumerate(row):
            if val:
                queens.append(Queen(chess_rank, chess_file))
    return queens


def peaceful(queens):
    """Return True if no queen is under threat."""
    # Base case: only 1 queen is always safe.
    if len(queens) <= 1:
        return True
    for q1, q2 in combinations(queens, 2):
        # Make sure there are no more than 1 queen rank and file.
        if q1.rank == q2.rank or q1.file == q2.file:
            return False
        # Check diagonal attacks
        if abs(q1.rank - q2.rank) == abs(q1.file - q2.file):
            return False
    return True


class Solution:
    def solve(self, matrix):
        queens = get_queens(matrix)
        return len(queens) == len(matrix) and peaceful(queens)


def test_1():
    matrix = [
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    assert Solution().solve(matrix) == False


def test_2():
    matrix = [
        [0, 0, 0, 1, 0],
        [0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1],
        [0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0]
    ]
    assert Solution().solve(matrix) == True