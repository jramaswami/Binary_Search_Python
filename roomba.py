"""
binarysearch.com :: Roomba
jramaswami
"""


class Solution:

    def solve(self, moves, xn, yn):
        offsets = {
            "WEST": (-1, 0), "EAST": (1, 0), "NORTH": (0, 1), "SOUTH": (0, -1)
        }
        x, y = 0, 0
        for move in moves:
            dx, dy = offsets[move]
            x, y = x + dx, y + dy
        return x == xn and y == yn


def test_1():
    moves = ["NORTH", "EAST"]
    x = 1
    y = 1
    assert Solution().solve(moves, x, y) == True


def test_2():
    moves = ["WEST", "EAST"]
    x = 1
    y = 0
    assert Solution().solve(moves, x, y) == False
