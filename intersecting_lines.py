"""
binarysearch.com :: Intersecting Lines
jramaswami
"""


import collections
import operator
import math


Segment = collections.namedtuple('Segment', ['left_y', 'right_y', 'idx'])


class Solution:

    def solve(self, lines, left_x, right_x):
        has_intersection = [0 for _ in lines]
        segments = []
        for idx, (slope, constant) in enumerate(lines):
            left_y = (slope * left_x) + constant
            right_y = (slope * right_x) + constant
            segments.append(Segment(left_y, right_y, idx))

        # Sort segments by left_y.
        segments.sort(key=operator.attrgetter('left_y'))
        max_right_y = -math.inf
        for i, curr_segment in enumerate(segments):
            # Check for intersection on the same y_left.
            if i - 1 >= 0 and curr_segment.left_y == segments[i-1].left_y:
                has_intersection[curr_segment.idx] = 1
            if i + 1 < len(segments) and curr_segment.left_y == segments[i+1].left_y:
                has_intersection[curr_segment.idx] = 1

            # Do any of the lines that start below y_left end up with
            # at or above y_right?  If so, there is a line that crosses
            # this line.  We can tell by keeping track of the maximum
            # right y for all the lines below the current line.
            if curr_segment.right_y <= max_right_y:
                has_intersection[curr_segment.idx] = 1
            max_right_y = max(max_right_y, curr_segment.right_y)

        # Sort segments by right_y.
        segments.sort(key=operator.attrgetter('right_y'))
        max_left_y = -math.inf
        for i, curr_segment in enumerate(segments):
            # Check for intersection on the same y_right.
            if i - 1 >= 0 and curr_segment.right_y == segments[i-1].right_y:
                has_intersection[curr_segment.idx] = 1
            if i + 1 < len(segments) and curr_segment.right_y == segments[i+1].right_y:
                has_intersection[curr_segment.idx] = 1

            # Do any of the lines that start below y_right end up with
            # at or above y_left?  If so, there is a line that crosses
            # this line.  We can tell by keeping track of the maximum
            # left y for all the lines below the current line.
            if curr_segment.left_y <= max_left_y:
                has_intersection[curr_segment.idx] = 1
            max_left_y = max(max_left_y, curr_segment.left_y)

        return sum(has_intersection)


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
