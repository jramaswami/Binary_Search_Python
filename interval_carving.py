"""
binarysearch.com :: Interval Carving
jramaswami
"""


class Solution:

    def solve(self, intervals, cut):
        cut_intervals = []
        for interval in intervals:
            if interval[1] < cut[0]:
                # Outside
                # iiiii
                #        xxxx
                cut_intervals.append(interval)
            elif cut[1] < interval[0]:
                # Outside
                #        iiiii
                #  xxxx
                cut_intervals.append(interval)
            elif cut[1] < interval[0]:
                cut_intervals.append(interval)
            elif cut[0] <= interval[0] and interval[1] <= cut[1]:
                # Overlaps
                #    iiii
                # xxxxxxxxx
                pass
            elif interval[0] <= cut[0] and cut[1] <= interval[1]:
                # Overlaps
                # iiiiiiiii
                #    xxx
                if interval[0] < cut[0]:
                    cut_intervals.append([interval[0], cut[0]])
                if cut[1] < interval[1]:
                    cut_intervals.append([cut[1], interval[1]])
            elif interval[0] <= cut[0] <= interval[1]:
                # Intersects
                # iiii
                #   xxxxx
                cut_intervals.append([interval[0], cut[0]])
            elif cut[0] <= interval[0] <= cut[1]:
                # Intersects
                #   iiii
                # xxxx
                cut_intervals.append([cut[1], interval[1]])

        return cut_intervals



def test_1():
    intervals = [[1, 10], [12, 30], [40, 60]]
    cut = [7, 45]
    expected = [[1, 7], [45, 60]]
    assert Solution().solve(intervals, cut) == expected


def test_2():
    "WA"
    intervals = [[3, 8]]
    cut = [5, 5]
    expected = [[3,5], [5,8]]
    assert Solution().solve(intervals, cut) == expected


def test_3():
    "WA"
    intervals = [[5, 8]]
    cut = [7, 8]
    expected = [[5,7]]
    assert Solution().solve(intervals, cut) == expected
