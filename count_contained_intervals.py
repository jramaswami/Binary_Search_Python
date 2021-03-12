"""
binarysearch.com :: Count Contained Interval
jramaswami
"""
import heapq
from collections import namedtuple


Interval = namedtuple('Interval', ['start', 'end'])


def contains(container, containee):
    """Return True if interval called container contains the interval called containee."""
    return containee.start >= container.start and containee.end <= container.end


class Solution:
    def solve(self, intervals):
        intervals0 = [Interval(*i) for i in intervals]
        # Sort by lowest start followed by highest end.
        intervals0.sort(key=lambda t: (t[0], -t[1]))
        
        soln = 0
        active_intervals = []
        for containee in intervals0:
            # Pop any stale intervals
            while active_intervals and active_intervals[0][1].end < containee.start:
                heapq.heappop(active_intervals)

            # Is this interval contained in any of the active intervals?
            is_contained = False
            for _, container in active_intervals:
                if contains(container, containee):
                    is_contained = True
                    break
            # Add this interval to the active intervals
            if is_contained:
                soln += 1
            else:
                heapq.heappush(active_intervals, (containee.end, containee))

        return soln



def test_1():
    intervals = [
        [1, 5],
        [2, 3],
        [3, 6],
        [4, 4]
    ]
    assert Solution().solve(intervals) == 2

def test_2():
    intervals = [
        [1, 2],
        [2, 3],
        [1, 5]
    ]
    assert Solution().solve(intervals) == 2
