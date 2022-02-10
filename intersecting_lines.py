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
    d1 = direction(p3, p4, p1);
    d2 = direction(p3, p4, p2);
    d3 = direction(p1, p2, p3);
    d4 = direction(p1, p2, p4);
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
        START = -1
        STOP = 1

        EPS = pow(10, -9)

        # Transform lines into line segments.
        segments = []
        events = []
        for i, (m, b) in enumerate(lines):
            low_p = Point(low, f(m, b, low))
            high_p = Point(high, f(m, b, high))
            if high_p.y < low_p.y:
                low_p, high_p = high_p, low_p
            segments.append((low_p, high_p))
            low_y = low_p.y
            high_y = high_p.y
            events.append((low_y, START, i))
            events.append((high_y, STOP, i))

        events.sort()
        active = set()
        overlaps = [0 for _ in lines]
        for _, etype, i in events:
            p1, p2 = segments[i]
            if etype == START:
                for j in active:
                    p3, p4 = segments[j]
                    if segments_intersect(p1, p2, p3, p4):
                        overlaps[i] = 1
                        overlaps[j] = 1
                active.add(i)
            else:
                active.remove(i)
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
