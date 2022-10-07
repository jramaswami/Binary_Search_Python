"""
binarysearch.com :: One Interval
jramaswami
"""


class Solution:

    def solve(self, intervals):
        intervals.sort()
        combined = []
        curr_start = intervals[0][0]
        curr_stop = intervals[0][1]
        for start, stop in intervals[1:]:
            if start <= curr_stop:
                curr_stop = max(stop, curr_stop)
            else:
                combined.append((curr_start, curr_stop))
                curr_start, curr_stop = start, stop
        combined.append((curr_start, curr_stop))
        if len(combined) <= 1:
            return 0
        return combined[-1][0] - combined[0][1]


def test_1():
    intervals = [
        [10, 20],
        [25, 100]
    ]
    expected = 5
    assert Solution().solve(intervals) == expected


def test_2():
    "WA"
    intervals = [[3,15],[37,92],[49,92]]
    expected = 22
    assert Solution().solve(intervals) == expected