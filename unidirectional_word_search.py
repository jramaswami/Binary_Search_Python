"""
binarysearch.com :: Unidirectional Word Search
https://binarysearch.com/problems/Unidirectional-Word-Search
"""

def get_col_word(col, board):
    """Return the word formed by given column top down."""
    return "".join(board[r][col] for r, _ in enumerate(board))


def get_row_word(row, board):
    """Return the word formed by the given grow left to right."""
    return "".join(board[row])


class Solution:
    def solve(self, board, word):
        for r, _ in enumerate(board):
            if get_row_word(r, board).find(word) >= 0:
                return True
        for c, _ in enumerate(board[0]):
            if get_col_word(c, board).find(word) >= 0:
                return True
        return False


def test_1():
    board = [
        ["H", "E", "L", "L", "O"],
        ["A", "B", "C", "D", "E"]
    ]
    word = "HELLO"
    solver = Solution()
    assert solver.solve(board, word) == True

def test_2():
    board = [
        ["x", "z", "d", "x"],
        ["p", "g", "u", "x"],
        ["k", "j", "z", "d"]
    ]
    word = "xgz"
    solver = Solution()
    assert solver.solve(board, word) == False

def test_3():
    board = [
        ["x", "z", "d", "x"],
        ["p", "g", "u", "x"],
        ["k", "j", "z", "d"]
    ]
    word = "u"
    solver = Solution()
    assert solver.solve(board, word) == True