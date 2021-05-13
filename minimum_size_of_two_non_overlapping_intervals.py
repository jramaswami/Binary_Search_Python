"""
binarysearch.com :: Minimum Size of Two Non-Overlapping Intervals
jramaswami
"""
from itertools import accumulate
from math import inf
from collections import namedtuple
from operator import attrgetter


Interval = namedtuple('Interval', ['start', 'end'])

def binsearch(intervals, interv):
    lo = 0
    hi = len(intervals) - 1
    result = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if intervals[mid].end < interv.start:
            result = max(result, mid)
            lo = mid + 1
        else:
            hi = mid - 1

    return result


class Solution:
    def solve(self, intervals):
        intervals0 = sorted((Interval(*i) for i in intervals), key=attrgetter('end'))
        deltas = [i.end - i.start + 1 for i in intervals0]
        deltas_prefix = list(accumulate(deltas, min))
        soln = inf
        for index, interv in enumerate(intervals0[::-1], start=-(len(intervals0) - 1)):
            # Find the first element that ends before this interval starts.
            d = interv.end - interv.start + 1
            left_index = binsearch(intervals0, interv)
            if left_index >= 0:
                soln = min(soln, d + deltas_prefix[left_index])
        return 0 if soln == inf else soln


def test_1():
    intervals = [
        [1, 4],
        [8, 9],
        [3, 5]
    ]
    assert Solution().solve(intervals) == 5


def test_2():
    intervals = [
        [1, 6],
        [6, 10]
    ]
    assert Solution().solve(intervals) == 0


def test_3():
    intervals = [
        [3, 4]
    ]
    assert Solution().solve(intervals) == 0
