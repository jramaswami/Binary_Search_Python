"""
binarysearch.com :: Intersecting Lines
jramaswami
"""


import collections
import enum


EPS = pow(10, -9)


Event = collections.namedtuple('Event', ['y', 'line_id', 'type'])


class EType(enum.IntEnum):
    Start = 1
    Stop = -1


class Solution:

    def solve(self, lines, low, high):

        events = []
        for i, (m, b) in enumerate(lines):
            y_lo = (m*low) + b
            y_hi = (m*high) + b
            y_lo, y_hi = min(y_lo, y_hi), max(y_lo, y_hi)
            if m == 0:
                y_hi += EPS
            events.append(Event(y_lo, i, EType.Start))
            events.append(Event(y_hi, i, EType.Stop))

        overlaps = [0 for _ in lines]
        events.sort()
        active = set()
        for event in events:
            if event.type == EType.Start:
                if len(active) == 1:
                    # Will only be one line.
                    for line in active:
                        overlaps[line] = 1
                if len(active) > 0:
                    overlaps[event.line_id] = 1
                active.add(event.line_id)
            else:
                active.remove(event.line_id)
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
