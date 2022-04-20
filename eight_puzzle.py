"""
binarysearch.com :: 8-Puzzle
jramaswami
"""


import collections


Board = collections.namedtuple('Board', ['board', 'zero_index'])


class Solver:

    OFFSETS = ((1, 0), (-1, 0), (0, 1), (0, -1))
    TARGET = (0, 1, 2, 3, 4, 5, 6, 7, 8)

    def __init__(self, board):
        self.height = len(board)
        self.width = len(board[0])

        # Make board tuple.
        t = []
        z = -1
        for row in board:
            for val in row:
                if val == 0:
                    z = len(t)
                t.append(val)

        self.init_board = Board(tuple(t), z)

    def rc2i(self, r, c):
        return (r * self.width) + c

    def i2rc(self, i):
        return (i // self.width, i % self.width)

    def inbounds(self, r, c):
        return r >= 0 and r < self.height and c >= 0 and c < self.width

    def neighbors(self, i):
        r, c = self.i2rc(i)
        for dr, dc in Solver.OFFSETS:
            r0, c0 = r + dr, c + dc
            if self.inbounds(r0, c0):
                yield(self.rc2i(r0, c0))

    def swap(self, board, j):
        i = board.zero_index
        board0 = list(board.board)
        board0[i], board0[j] = board0[j], board0[i]
        return Board(tuple(board0), (i if board0[i] == 0 else j))

    def solve(self):
        if self.init_board == Solver.TARGET:
            return 0
        visited = set()
        Q = collections.deque()
        Q.append((self.init_board, 0))
        visited.add(self.init_board)
        while Q:
            board, moves = Q.popleft()
            for y in self.neighbors(board.zero_index):
                board0 = self.swap(board, y)
                if board0.board  == Solver.TARGET:
                    return moves + 1
                if board0 not in visited:
                    visited.add(board0)
                    Q.append((board0, moves + 1))
        return -1


class Solution:

    def solve(self, board):
        solver = Solver(board)
        return solver.solve()


def test_1():
    board = [ [1, 0, 2], [3, 4, 5], [6, 7, 8] ]
    expected = 1
    assert Solution().solve(board) == expected
