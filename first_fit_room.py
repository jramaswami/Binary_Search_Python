"""
binarysearch.com :: First Fit Room
jramaswami
"""


class Solution:
    def solve(self, rooms, target):
        """
        Return the first integer in rooms that's target or larger. If there4
        is no solution, return -1.
        """
        for room in rooms:
            if room >= target:
                return room
        return -1


def test_1():
    rooms = [15, 10, 30, 50, 25]
    target = 20
    assert Solution().solve(rooms, target) == 30


def test_2():
    rooms = [15, 10, 30, 50, 25]
    target = 51
    assert Solution().solve(rooms, target) == -1


def test_3():
    rooms = [15, 10, 30, 50, 25]
    target = 50
    assert Solution().solve(rooms, target) == 50


def test_4():
    rooms = []
    target = 50
    assert Solution().solve(rooms, target) == -1