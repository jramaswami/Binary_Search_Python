"""
binarysearch.com :: Sinking Islands
jramaswami
"""


class Solution:

    def solve(self, board):

        # Corner case: empty board
        if len(board) == 0 or len(board[0]) == 0:
            return None   # (?!?)

        def inbounds(r, c):
            """Return True if (r, c) is inside board."""
            return r >= 0 and c >= 0 and r < len(board) and c < len(board[r])


        def neighbors(r, c):
            """Generator for neighbors to (r, c) in a von Neumann neighborhood."""
            offsets = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for dr, dc in offsets:
                r0, c0 = r + dr, c + dc
                if inbounds(r0, c0):
                    yield r0, c0

        def dfs(r, c):
            board[r][c] = 2
            for r0, c0 in neighbors(r, c):
                if board[r0][c0] == 1:
                    dfs(r0, c0)

        # DFS from all board cells to find land connected to border.  Set all
        # that land to value = 2.

        # Top/bottom row
        for r in [0, len(board) - 1]:
            for c, _ in enumerate(board[0]):
                if board[r][c] == 1:
                    dfs(r, c)

        # Left/Right Column
        for c in [0, len(board[0]) - 1]:
            for r, _ in enumerate(board):
                if board[r][c] == 1:
                    dfs(r, c)

        # Since the land connected to the boarder is 2 and land not connected
        # to the border is 1, just subtract 1 from all land.
        return [[v - 1 if v else 0 for v in row] for row in board]


def test_1():
    board = [ [1, 0, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0] ]
    expected = [ [1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]
    assert Solution().solve(board) == expected


def test_2():
    board = [ [1, 1], [1, 0] ]
    expected = [ [1, 1], [1, 0] ]
    assert Solution().solve(board) == expected


def test_3():
    board = [[]]
    expected = [[]]
    assert Solution().solve(board) == expected
