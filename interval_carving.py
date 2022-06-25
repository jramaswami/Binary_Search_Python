"""
binarysearch.com :: Interval Carving
jramaswami
"""


class Solution:

    def solve(self, intervals, cut):
        cut_intervals = []
        for interval in intervals:
            if interval[1] < cut[0]:
                cut_intervals.append(interval)
            elif cut[1] < interval[0]:
                cut_intervals.append(interval)
            elif cut[0] <= interval[0] and interval[1] <= cut[1]:
                # Overlaps
                #    iiii
                # xxxxxxxxx
                pass
            else:
                # Intersects
                # iiii          iiii
                #   xxxxx     xxxx
                if interval[0] <= cut[0] <= interval[1]:
                    cut_intervals.append([interval[0], cut[0]])
                else:
                    cut_intervals.append([cut[1], interval[1]])

        return cut_intervals



def test_1():
    intervals = [[1, 10], [12, 30], [40, 60]]
    cut = [7, 45]
    expected = [[1, 7], [45, 60]]
    assert Solution().solve(intervals, cut) == expected


def test_2():
    intervals = [[3, 8]]
    cut = [5, 5]
    expected = [[3,5], [5,8]]
    assert Solution().solve(intervals, cut) == expected
