"""
binarysearch.com :: Interval Overlaps
jramaswami
"""


class Solution:

    def solve(self, l0, l1):
        i = 0
        j = 0
        soln = []
        while i < len(l0) and j < len(l1):
            x1, x2 = l0[i]
            y1, y2 = l1[j]
            if max(x1, y1) <= min(x2, y2):
                # If intervals overlap then add the intersection to the
                # solution.
                soln.append([max(x1, y1), min(x2, y2)])

            # "Pop" the interval that ends first.
            if x2 < y2:
                i += 1
            else:
                j += 1

        return soln


def test_1():
    l0 = [
        [1, 3],
        [5, 6],
        [7, 9]
    ]

    l1 = [
        [1, 4],
        [5, 7]
    ]
    expected = [
        [1, 3],
        [5, 6],
        [7, 7]
    ]
    assert Solution().solve(l0, l1) == expected


def test_2():
    l0 = [
        [1, 3],
        [5, 6],
        [7, 9]
    ]
    l1 = [
        [100, 200]
    ]
    expected = []
    assert Solution().solve(l0, l1) == expected
