"""
binarysearch.com :: Tic Tac Toe
jramaswami
"""


import collections


class TicTacToe:
    def __init__(self, n):
        self.n = n
        self.row_sums = collections.defaultdict(int)
        self.col_sums = collections.defaultdict(int)
        self.neg_diag_sum = 0
        self.pos_diag_sum = 0

    def move(self, r, c, me):
        sign = 1 if me else -1
        self.row_sums[r] += sign
        if self.row_sums[r] == (sign * self.n):
            return sign
        self.col_sums[c] += sign
        if self.col_sums[c] == (sign * self.n):
            return sign
        if r == c:
            self.neg_diag_sum += sign
            if self.neg_diag_sum == (sign * self.n):
                return sign
        if r + c == self.n - 1:
            self.pos_diag_sum += sign
            if self.pos_diag_sum == (sign * self.n):
                return sign
        return 0


def test_1():
    methods = ["constructor", "move", "move", "move", "move", "move"]
    arguments = [[3], [0, 0, True], [2, 0, False], [0, 1, True], [2, 1, False], [0, 2, True]]
    expected = [None, 0, 0, 0, 0, 1]
    tt = TicTacToe(*arguments[0])
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(tt, m)(*a) == e


def test_2():
    methods = ["constructor", "move", "move", "move", "move", "move"]
    arguments = [[3], [0, 0, True], [2, 0, False], [1, 1, True], [2, 1, False], [2, 2, True]]
    expected = [None, 0, 0, 0, 0, 1]
    tt = TicTacToe(*arguments[0])
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(tt, m)(*a) == e
