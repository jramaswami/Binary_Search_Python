"""
binarysearch.com :: Points on a Line
jramaswami
"""


import collections
import fractions
import math


Point = collections.namedtuple('Point', ['x', 'y'])


class Solution:

    def solve(self, coordinates):
        points = [Point(*p) for p in coordinates]
        soln = 0
        for i, p1 in enumerate(points):
            lines = collections.defaultdict(int)
            for j, p2 in enumerate(points):
                if i == j:
                    continue
                # Compute slope.
                dy = p1.y - p2.y
                dx = p1.x - p2.x
                m = math.inf
                if dx != 0:
                    m = fractions.Fraction(dy, dx)
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




