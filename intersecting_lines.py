"""
binarysearch.com :: Intersecting Lines
jramaswami
"""


import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        "Cross product"
        return (self.x * other.y) - (other.x * self.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


def direction(pi, pj, pk):
    return (pk - pi) * (pj - pi)


def on_segment(pi, pj, pk):
    if min(pi.x, pj.x) <= pk.x  <= max(pi.x, pj.x) and min(pi.y, pj.y) <= pk.y <= max(pi.y, pj.y):
        return True
    return False


def segments_intersect(p1, p2, p3, p4):
    d1 = direction(p3, p4, p1)
    d2 = direction(p3, p4, p2)
    d3 = direction(p1, p2, p3)
    d4 = direction(p1, p2, p4)
    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    elif d1 == 0 and on_segment(p3, p4, p1):
        return True
    elif d2 == 0 and on_segment(p3, p4, p2):
        return True
    elif d3 == 0 and on_segment(p1, p2, p3):
        return True
    elif d4 == 0 and on_segment(p1, p2, p4):
        return True
    return False


def f(slope, constant, x):
    return (slope * x) + constant


class Solution:

    def solve(self, lines, low, high):
        # Transform lines into line segments.
        segments = [(Point(low, f(m, b, low)), Point(high, f(m, b, high))) for m, b in lines]
        overlaps = [0 for _ in segments]

        for i, (p1, p2) in enumerate(segments):
            for j, (p3, p4) in enumerate(segments[i+1:], start=i+1):
                if segments_intersect(p1, p2, p3, p4):
                    overlaps[i] = 1
                    overlaps[j] = 1
        return sum(overlaps)


def test_1():
    lines = [
        [2, 3],
        [-3, 5],
        [4, 6]
    ]
    lo = 0
    hi = 1
    expected = 2
    assert Solution().solve(lines, lo, hi) == expected


def test_2():
    lines = [
        [-1, 0],
        [-1, 1],
        [-1, 2],
        [-1, 3]
    ]
    lo = 0
    hi = 1
    expected = 0
    assert Solution().solve(lines, lo, hi) == expected


def test_3():
    "RTE"
    lines = [
        [0, 2]
    ]
    lo = -1
    hi = 0
    expected = 0
    assert Solution().solve(lines, lo, hi) == expected


def test_4():
    "RTE"
    lines = [
        [-1, -2]
    ]
    lo = 0
    hi = 0
    expected = 0
    assert Solution().solve(lines, lo, hi) == expected


def test_5():
    "WA"
    lines = [
        [2, 3],
        [3, 1],
    ]
    lo = -2
    hi = 0
    expected = 0
    assert Solution().solve(lines, lo, hi) == expected


def test_6():
    "WA"
    lines = [
        [-1, 0],
        [3, 0]
    ]
    lo = 0
    hi = 0
    expected = 2
    assert Solution().solve(lines, lo, hi) == expected
