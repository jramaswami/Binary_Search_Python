"""
binarysearch.com :: Line Segment
jramaswami
"""


class Solution:

    def solve(self, coordinates):
        # Corner case: at least two points are required to form a line.
        if len(coordinates) < 2:
            return False

        # First determine the slope of the line (if there is one).
        # where m = (y1 - y2) / (x1 - x2)
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]

        if x1 == x2:
            # This will yield an infinite slope or vertical line.
            # A vertical line requires all x values to be the same.
            return all(x == x1 for x, _ in coordinates)
        else:
            m = (y1 - y2) / (x1 - x2)

            # Use point slope form to determine the linear equation.
            # y - y1 = m(x - x1)
            # y = m(x - x1) + y1
            # Then iterate over all coordinates to see if they satisfy
            # the equation.
            for x, y in coordinates:
                if y != (m * (x - x1)) + y1:
                    return False
            return True


def test_1():
    coordinates = [
        [1, 1],
        [3, 3],
        [7, 7]
    ]
    expected = True
    assert Solution().solve(coordinates) == expected


def test_2():
    coordinates = [
        [1, 1],
        [3, 3],
        [4, 6]
    ]
    expected = False
    assert Solution().solve(coordinates) == expected


def test_3():
    """RTE"""
    coordinates = [
        [1, 1],
        [1, 2],
        [3, 4],
        [3, 5]
    ]
    expected = False
    assert Solution().solve(coordinates) == expected