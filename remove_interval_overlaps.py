"""
binarysearch.com :: Remove Interval Overlaps
jramaswami
"""


class Solution:
    def solve(self, intervals):
        # Corner case: empty intervals
        if intervals == []:
            return 0

        intervals.sort(key=lambda T: (T[1], T[0]))

        last_end = -1
        interval_count = 0
        for L, R in intervals:
            if L >= last_end:
                last_end = R
                interval_count += 1
        return len(intervals) - interval_count



def test_1():
    intervals = [
        [7, 9],
        [2, 4],
        [5, 8]
    ]
    expected = 1
    assert Solution().solve(intervals) == expected


def test_2():
    intervals = [
        [1, 5],
        [1, 5],
        [1, 5]
    ]
    expected = 2
    assert Solution().solve(intervals) == expected


def test_3():
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    expected = 1
    assert Solution().solve(intervals) == expected


def test_4():
    intervals = [[1,2],[2,3]]
    expected = 0
    assert Solution().solve(intervals) == expected


def test_5():
    """RTE"""
    intervals = []
    expected = 0
    assert Solution().solve(intervals) == expected
