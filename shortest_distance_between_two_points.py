"""
binarysearch.com :: Shortest Distance Between Two Points
jramaswami

REF: https://medium.com/@andriylazorenko/closest-pair-of-points-in-python-79e2409fc0b2
"""


import itertools
import math


def brute(ax):
    """Brute force comparison of each pair of points to find closest pair."""
    best_d = math.inf
    best_pair = None
    for pt1, pt2 in itertools.combinations(ax, 2):
        d2 = math.pow(pt1[0] - pt2[0], 2) + math.pow(pt1[1] - pt2[1], 2)
        if d2 < best_d:
            best_d, best_pair = d2, (pt1, pt2)
    return best_pair, best_d


def closest_pair(ax, ay):
    """Recursive function to find closest pair."""

    # If the lenght of ax is small enough, use brute force.
    len_ax = len(ax)
    if len_ax <= 3:
        return brute(ax)

    # Split array by x coordinates in two, that is, split the plane in two
    # at ax[mid][x].
    mid = len_ax // 2
    left_x = ax[:mid]
    right_x = ax[mid:]

    # Partition array by y coordinates on their x coordinate such that
    # left_y contains points with pt[x] <= ax[mid][x] and right_y
    # contains points with pt[x] <= ax[mid][x], splitting the plane in two.
    midpoint = ax[mid][0]
    left_y = []
    right_y = []
    for pt in ay:
        if pt[0] <= midpoint:
            left_y.append(pt)
        else:
            right_y.append(pt)

    # Call recursively to find the closest pair in each side of the division.
    best_pair1, best_d1 = closest_pair(left_x, left_y)
    best_pair2, best_d2 = closest_pair(right_x, right_y)
    if best_d1 <= best_d2:
        best_d = best_d1
        best_pair = best_pair1
    else:
        best_d = best_d2
        best_pair = best_pair2

    # Now check for points that span the division.
    midpoint_x = ax[mid][0]
    # Choose coordinates from ay that are within best_d by x coordinate.
    box = [pt for pt in ay if abs(midpoint_x - pt[0]) <= best_d]
    # Brute force a comparison to see if there are any points closer then
    # our previous closest pair.
    box_best_pair, box_best_d = brute(box)
    if box_best_d < best_d:
        best_pair, best_d = box_best_pair, box_best_d

    return best_pair, best_d


class Solution:

    def solve(self, coordinates):
        # Guard against stacking the points in a single x.
        min_x, max_x = min_y, max_y = math.inf, -math.inf
        for x, y in coordinates:
            min_x, max_x = min(min_x, x), max(max_x, x)
            min_y, max_y = min(min_y, y), max(max_y, y)
        if max_y - min_y > max_x - min_x:
            coordinates = [(y, x) for x, y in coordinates]

        ax = sorted(coordinates, key=lambda pt: pt[0])
        ay = sorted(coordinates, key=lambda pt: pt[1])
        pr, d2 = closest_pair(ax, ay)
        return d2


def test_1():
    coordinates = [
        [0, 0],
        [1, 1],
        [2, 4]
    ]
    expected = 2
    assert Solution().solve(coordinates) == expected


def test_2():
    coordinates = [
        [2, 3],
        [12, 30],
        [40, 50],
        [5, 1],
        [12, 10],
        [3, 3]
    ]
    expected = 1
    assert Solution().solve(coordinates) == expected


def test_3():
    """WA"""
    coordinates = [
        [0, 0],
        [2, 2],
        [3, 0],
    ]
    expected = 5
    assert Solution().solve(coordinates) == expected


def test_4():
    N = 100000
    coordinates = [[0, y] for y in range(0, N)]
    expected = 1
    assert Solution().solve(coordinates) == expected


def test_5():
    """WA"""
    coordinates = [
        [0, 0],
        [1, 3],
        [2, 0]
    ]
    expected = 4
    assert Solution().solve(coordinates) == expected


def test_6():
    """WA"""
    coordinates = [
        [0, 2],
        [2, 0],
        [2, 3],
        [3, 0]
    ]
    expected = 1
    assert Solution().solve(coordinates) == expected