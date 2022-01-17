"""
binarysearch.com :: Points on a Line
jramaswami
"""


import collections
import math


class Solution:

    def solve(self, coordinates):
        if not coordinates:
            return 0

        soln = 1
        for i, p1 in enumerate(coordinates):
            lines = collections.defaultdict(int)
            for j, p2 in enumerate(coordinates[i+1:], start=i+1):
                # Compute slope.
                dy = p1[1] - p2[1]
                dx = p1[0] - p2[0]
                m = math.inf
                if dx != 0:
                    m = dy / dx
                # Same slope means same line.
                lines[m] += 1
                soln = max(soln, 1 + lines[m])
        return soln


def test_1():
    coordinates = [
        [5, 1],
        [7, 2],
        [9, 3],
        [0, 0],
        [1, 1],
        [5, 5],
        [6, 6]
    ]
    assert Solution().solve(coordinates) == 4


def test_2():
    "WA"
    coordinates = [
        [3, 0]
    ]
    assert Solution().solve(coordinates) == 1
