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

        best_distance_squared = math.inf
        # Sort coordinates left to right by x.
        coordinates.sort()
        # We define our box as coordinates[left:right].
        left = 0
        for right, (x1, y1) in enumerate(coordinates[1:], start=1):

            # Remove from box all items that are too far away on the x-axis.
            # Binary search for the index of the left-most coordinate within
            # the distance squared by x value.
            lo = left
            hi = right
            while lo < hi:
                mid = lo + ((hi - lo) // 2)
                x2 = coordinates[mid][0]
                dx = x1 - x2
                if (dx * dx) <= best_distance_squared:
                    left = mid
                    hi = mid - 1
                else:
                    lo = mid + 1

            for j in range(left, right):
                x2, y2 = coordinates[j]
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