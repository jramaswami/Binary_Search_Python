"""
binarysearch.com :: Point Distances with Shared Coordinate
jramaswami
"""
from collections import defaultdict
from math import inf


class Solution:
    def solve(self, points):
        points_by_x = defaultdict(list)
        points_by_y = defaultdict(list)
        for x, y in points:
            points_by_x[x].append(y)
            points_by_y[y].append(x)

        soln = []
        for x, y in points:
            d = inf
            first_dupe = True
            for y0 in points_by_x[x]:
                if y0 == y and first_dupe:
                    first_dupe = False
                    continue
                d = min(d, abs(y - y0))
            first_dupe = True
            for x0 in points_by_y[y]:
                if x0 == x and first_dupe:
                    first_dupe = False
                    continue
                d = min(d, abs(x - x0))
            soln.append(d)
        return soln
            

def test_1():
    points = [
        [5, 5],
        [5, 9],
        [4, 4],
        [4, 30]
    ]
    assert Solution().solve(points) == [4, 4, 26, 26]
