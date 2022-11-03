"""
binarysearch.com :: Number of Moves to Capture the King
jramaswami
"""
class Solution:
    def solve(self, board):
        offsets = [(-2, 1), (-2, -1), (1, -2), (-1, -2),
                   (2, 1),  (2, -1),  (1, 2), (-1, 2)]
        
        visited = [[False for _ in row] for row in board]
        queue = []
        for r, row in enumerate(board):
            for c, p in enumerate(row):
                if p == 1:
                    queue.append((r, c))
                    visited[r][c] = True

        moves = 0
        new_queue = []
        while queue:
            for r, c in queue:
                if board[r][c] == 2:
                    return moves
                for r_off, c_off in offsets:
                    r0 = r + r_off
                    c0 = c + c_off
                    if r0 < 0 or r0 >= len(board):
                        continue
                    if c0 < 0 or c0 >= len(board[0]):
                        continue
                    if visited[r0][c0]:
                        continue

                    new_queue.append((r0, c0))
                    visited[r0][c0] = True
            queue, new_queue = new_queue, []
            moves += 1

        return -1


def test_1():
    board = [
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 2],
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]
    assert Solution().solve(board) == 2

def test_2():
    board = [
        [1, 2],
        [1, 1]
    ]
    assert Solution().solve(board) == -1
