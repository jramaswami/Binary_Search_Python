"""
binarysearch.com :: Collision Detection
jramaswami

REF: CLRS pp. 1017-1019
REF: Guide to Competitive Programming, p. 216
"""


import collections


Point = collections.namedtuple('Point', ['x', 'y'])


def on_segment(pi, pj, pk):
    if (min(pi.x, pj.x) <= pk.x <= max(pi.x, pj.x)) and (min(pi.y, pj.y) <= pk.y <= max(pi.y, pj.y)):
        return True
    return False


def direction(pi, pj, pk):
    # return (pk - pi) * (pj - pi)
    # (p1 - p0) * (p2 - p0) = (x1-x0)(y2-y0) - (x2 - x0)(y1 - y0)
    # (pk - pi) * (pj - pi) = (xk-xi)(yj-yi) - (xj - xi)(yk - yi)
    return (pk.x-pi.x)*(pj.y-pi.y) - (pj.x - pi.x)*(pk.y - pi.y)


def segments_intersect(p1, p2, p3, p4):
    d1 = direction(p3, p4, p1)
    d2 = direction(p3, p4, p2)
    d3 = direction(p1, p2, p3)
    d4 = direction(p1, p2, p4)
    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
        return True
    elif d1 == 0 and on_segment(p3, p4, p1):
        return True
    elif d2 == 0 and on_segment(p3, p4, p2):
        return True
    elif d3 == 0 and on_segment(p1, p2, p3):
        return True
    elif d4 == 0 and on_segment(p1, p2, p4):
        return True
    return False


class Solution:
    def solve(self, polygon, x, y):
        lines = []
        for i, _ in enumerate(polygon):
            j = (i + 1) % len(polygon)
            lines.append((Point(*polygon[i]), Point(*polygon[j])))

        p3, p4 = Point(x, y), Point(7234528, 23465236)
        intersections = 0
        for p1, p2 in lines:
            # Corner case: if p3 is a vertex, it will possibly
            # intersect (be on) two line segments only.
            if p1 == p3 or p2 == p3:
                return True
            if segments_intersect(p1, p2, p3, p4):
                intersections += 1

        return (intersections % 2 != 0)



def test_1():
    polygon = [ [-3, -3], [-3, 3], [3, 3], [3, -3] ]
    x = 0
    y = 0
    expected = True
    assert Solution().solve(polygon, x, y) == expected


def test_2():
    polygon = [ [-3, -3], [-3, 3], [3, 3], [3, -3] ]
    x = -2
    y = 3
    expected = True
    assert Solution().solve(polygon, x, y) == expected


def test_3():
    polygon = [ [-3, -3], [-3, 3], [3, 3], [3, -3] ]
    x = -3
    y = 3
    expected = True
    assert Solution().solve(polygon, x, y) == expected


def test_4():
    polygon = [ [-3, -3], [-3, 3], [3, 3], [3, -3] ]
    x = 100
    y = 3
    expected = False
    assert Solution().solve(polygon, x, y) == expected


def test_5():
    polygon = [ [-3, -3], [-3, 3], [3, 3], [3, -3] ]
    x = 20
    y = -20
    expected = False
    assert Solution().solve(polygon, x, y) == expected
