"""
binarysearch.com :: Interval Duration
jramaswami
"""
class Solution:
    def solve(self, intervals):
        if intervals == []:
            return 0

        intervals0 = sorted(intervals)
        interval_start, interval_end = intervals0[0]
        merged_intervals = []
        for s, e in intervals0[1:]:
            if s > interval_end:
                merged_intervals.append((interval_start, interval_end))
                interval_start, interval_end = s, e
            else:
                interval_end = max(interval_end, e)
        merged_intervals.append((interval_start, interval_end))
        return sum(1 + e - s for s, e in merged_intervals)


def test_1():
    intervals = [
        [45, 60],
        [1, 5],
        [5, 15],
        [2, 3]
    ]
    assert Solution().solve(intervals) == 31

def test_2():
    intervals = []
    assert Solution().solve(intervals) == 0


def test_3():
    intervals = [[1, 100]]
    assert Solution().solve(intervals) == 100


def test_4():
    intervals = [[1, 1]]
    assert Solution().solve(intervals) == 1