"""
binarysearch.com :: Longest Interval
jramaswami
"""

class Solution:
    def solve(self, intervals):
        intervals.sort()
        soln = 0
        if intervals:
            curr_start, curr_end = intervals[0]
            for int_start, int_end in intervals[1:]:
                if int_start <= curr_end:
                    curr_end = max(curr_end, int_end)
                else:
                    soln = max(soln, curr_end - curr_start + 1)
                    curr_start, curr_end = int_start, int_end
            soln = max(soln, curr_end - curr_start + 1)
        return soln


def test_1():
    intervals = [
        [1, 5],
        [3, 8],
        [4, 5],
        [10, 13],
        [15, 17]
    ]
    expected = 8
    assert Solution().solve(intervals) == expected


def test_2():
    intervals = []
    expected = 0
    assert Solution().solve(intervals) == expected


def test_3():
    intervals = [[1, 1]]
    expected = 1
    assert Solution().solve(intervals) == expected


def test_4():
    intervals = [[1, 4]]
    expected = 4
    assert Solution().solve(intervals) == expected
