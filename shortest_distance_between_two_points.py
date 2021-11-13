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
        box = collections.deque([coordinates[0]])
        for x1, y1 in coordinates[1:]:

            # Remove from box all items that are too far away on the x-axis.
            while box:
                x2 = box[0][0]
                dx = x1 - x2
                if (dx * dx) <= best_distance_squared:
                    break
                box.popleft()

            for x2, y2 in box:
                d2 = distance_squared(x1, y1, x2, y2)
                if d2 < best_distance_squared:
                    best_distance_squared = d2

            # Add current point to box.
            box.append((x1, y1))

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