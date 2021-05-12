"""
binarysearch.com :: Point Distances with Shared Coordinate
jramaswami
"""
import bisect
from collections import defaultdict
from math import inf


class Solution:
    def solve(self, points):
        points_by_x = defaultdict(list)
        points_by_y = defaultdict(list)
        for i, (x, y) in enumerate(points):
            bisect.insort(points_by_x[x], (y, i))
            bisect.insort(points_by_y[y], (x, i))

        soln = [inf for _ in points]
        for x in points_by_x:
            for (left, i), (right, j) in zip(points_by_x[x][:-1], points_by_x[x][1:]):
                dist = abs(left - right)
                soln[i] = min(soln[i], dist)
                soln[j] = min(soln[j], dist)

        for y in points_by_y:
            for (left, i), (right, j) in zip(points_by_y[y][:-1], points_by_y[y][1:]):
                dist = abs(left - right)
                soln[i] = min(soln[i], dist)
                soln[j] = min(soln[j], dist)

        return soln

        
            

def test_1():
    points = [
        [5, 5],
        [5, 9],
        [4, 4],
        [4, 30]
    ]
    assert Solution().solve(points) == [4, 4, 26, 26]
