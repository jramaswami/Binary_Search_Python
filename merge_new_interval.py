"""
binarysearch.com :: Merge New Interval
jramaswami
"""


class Solution:

    def solve(self, intervals, target):

        def overlaps(a, b):
            # Case 1:
            # -----
            #  ---
            if a[0] <= b[0] and a[1] >= b[1]:
                return True

            # Case 2:
            #   ---
            # -------
            if b[0] <= a[0] and b[1] >= a[1]:
                return True

            # Case 3:
            # ---
            #   ---
            if a[1] >= b[0] and a[1] <= b[1]:
                return True

            # Case 4:
            #   ---
            # ---
            if b[1] >= a[0] and b[1] <= a[1]:
                return True

            return False

        soln = []
        for interval in intervals:
            if target and overlaps(interval, target):
                target = [min(interval[0], target[0]),
                          max(interval[1], target[1])
                ]
            elif target and target[1] < interval[0]:
                # Target does not overlap and is now before the current
                # interval.
                soln.append(target)
                target = None
                soln.append(interval)
            else:
                soln.append(interval)

        # If target has not been placed, do so.
        if target:
            soln.append(target)
        return soln


def test_1():
    intervals = [
        [1, 10],
        [20, 30],
        [70, 100]
    ]
    target = [5, 25]
    expected = [
        [1, 30],
        [70, 100]
    ]
    assert Solution().solve(intervals, target) == expected


def test_2():
    intervals = [
        [1, 2],
        [3, 5],
        [7, 10]
    ]
    target = [5, 7]
    expected = [
        [1, 2],
        [3, 10]
    ]
    assert Solution().solve(intervals, target) == expected


def test_3():
    intervals = [
        [3, 5],
        [7, 10],
        [15, 19]
    ]
    target = [1, 2]
    expected = [
        [1, 2],
        [3, 5],
        [7, 10],
        [15, 19]
    ]
    assert Solution().solve(intervals, target) == expected


def test_4():
    intervals = []
    target = [1, 3]
    expected = [[1, 3]]
    assert Solution().solve(intervals, target) == expected


def test_5():
    intervals = [[1, 2], [3, 4]]
    target = []
    expected = [[1, 2], [3, 4]]
    assert Solution().solve(intervals, target) == expected