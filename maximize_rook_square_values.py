"""
binarysearch.com :: Maximize Rook Square Values
jramaswami
"""


from collections import namedtuple


Tile = namedtuple('Tile', ['val', 'row', 'col'])


def flatten_board(board):
    """Return flattened board."""
    flat = []
    for r, row in enumerate(board):
        for c, val in enumerate(row):
            flat.append(Tile(val, r, c))
    return flat


class Solution:
    def solve(self, board):
        soln = 0
        flat = flatten_board(board)
        flat.sort(reverse=True)
        for i, a in enumerate(flat):
            # If twice the current value is not enough to beat the solution then:
            # (1) The current value has already been paired with with a greater
            #     value
            # (2) The current value must pair with a equal or smaller value, 4
            #     which will not produce a greater solution
            if 2 * a.val <= soln:
                break
            for j, b in enumerate(flat):
                if a.row != b.row and a.col != b.col:
                    soln = max(soln, a.val + b.val)
                    break
        return soln


#
# Testing
#


import random


def brute_force(board):
    soln = 0
    for r1, row1 in enumerate(board):
        for r2, row2 in enumerate(board):
            if r1 == r2:
                continue
            for c1, val1 in enumerate(row1):
                for c2, val2 in enumerate(row2):
                    if c1 == c2:
                        continue
                    soln = max(soln, board[r1][c1] + board[r2][c2])
    return soln


def test_brute_force():
    board = [
        [1, 9, 3, 1, 9],
        [1, 1, 1, 1, 1],
        [8, 1, 1, 1, 1]
    ]
    assert brute_force(board) == 17
    dim = 10
    board = [[1 for _ in range(dim)] for _ in range(dim)]
    assert brute_force(board) == 2


def test_1():
    board = [
        [1, 9, 3, 1, 9],
        [1, 1, 1, 1, 1],
        [8, 1, 1, 1, 1]
    ]
    assert Solution().solve(board) == 17


def test_2():
    board = [[1 for _ in range(447)] for _ in range(447)]
    assert Solution().solve(board) == 2


def test_3():
    for _ in range(10):
        dim = 50
        board = [[random.randint(1, 200) for _ in range(dim)] for _ in range(dim)]
        assert Solution().solve(board) == brute_force(board)