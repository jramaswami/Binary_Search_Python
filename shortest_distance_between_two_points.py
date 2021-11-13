"""
binarysearch.com :: Shortest Distance Between Two Points
jramaswami
"""


import collections
import math


class Solution:

    def solve(self, coordinates):

        def distance_squared(x1, y1, x2, y2):
            dx = x1 - x2
            dy = y1 - y2
            return (dx * dx) + (dy * dy)


        # Determine range of x and y coordinates.
        min_x, max_x = min_y, max_y = -math.inf, math.inf
        for x, y in coordinates:
            min_x, max_x = min(min_x, x), max(max_x, x)
            min_y, max_y = min(min_y, y), max(max_y, y)

        # Use the axis with the greatest range of numbers as the axis of
        # the line sweep.
        dx = max_x - min_x
        dy = max_y - min_y
        if dy > dx:
            X = 1
            Y = 0
        else:
            X = 0
            Y = 1

        best_distance_squared = math.inf
        # Sort coordinates left to right by x.
        coordinates.sort(key=lambda p: p[X])
        # We define our box as coordinates[left:right].
        left = 0
        for right, point in enumerate(coordinates[1:], start=1):
            x1, y1 = point[X], point[Y]
            print(f"({x1}, {y1}) box={coordinates[left:right]} {best_distance_squared=}")

            # Remove from box all items that are too far away on the x-axis.
            # Binary search for the index of the left-most coordinate within
            # the distance squared by x value.
            lo = left
            hi = right
            new_left = right
            while lo <= hi:
                mid = lo + ((hi - lo) // 2)
                x2 = coordinates[mid][X]
                dx = x1 - x2
                if (dx * dx) <= best_distance_squared:
                    new_left = min(new_left, mid)
                    hi = mid - 1
                else:
                    lo = mid + 1
            left = new_left

            print(f"({x1}, {y1}) box={coordinates[left:right]} {best_distance_squared=} {left=}")
            for j in range(left, right):
                x2, y2 = coordinates[j][X], coordinates[j][Y]
                d2 = distance_squared(x1, y1, x2, y2)
                if d2 < best_distance_squared:
                    best_distance_squared = d2

        return best_distance_squared


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