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


        def intersects(line1, line2):
            """
            Cramer's rule.
            ax + by + c = 0
            a = slope or line[1]
            c = line[2]
            b = -1 b/c we have y = ax + c --> 0 = ax - y + c
            """
            a1, c1 = lines[line1]
            a2, c2 = lines[line2]

            b1 = b2 = -1
            dnm = (a1 * b2) - (a2 * b1)

            # The lines do not overlap (or are the same line).
            if dnm == 0:
                return (a1, c1) == (a2, c2)

            nmr = (a1 * b2) - (c2 * b1)

            x = -(nmr / dnm)
            print(f"{line1} intersects {line2} @ {x=}")
            return low - EPS <= x <= high + EPS


        # Line sweep is used to limit comparisons.
        events = []
        for i, (m, b) in enumerate(lines):
            y_lo = (m*low) + b
            y_hi = (m*high) + b
            y_lo, y_hi = min(y_lo, y_hi), max(y_lo, y_hi)
            if m == 0 or y_lo == y_hi:
                y_hi += EPS
            events.append(Event(y_lo, i, EType.Start))
            events.append(Event(y_hi, i, EType.Stop))

        overlaps = [0 for _ in lines]
        events.sort()
        active = set()
        for event in events:
            if event.type == EType.Start:
                line1 = event.line_id
                for line2 in active:
                    if intersects(line1, line2):
                        overlaps[line1] = 1
                        overlaps[line2] = 1
                        break
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
