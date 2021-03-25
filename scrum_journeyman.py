"""
binarysearch.com :: Scrum Journeyman
jramaswami
"""
from collections import defaultdict


class Solution:
    def solve(self, intervals, types):
        # First gather starts and stops by time.
        starts = defaultdict(int)
        stops = defaultdict(int)

        for start, stop in intervals:
            starts[start] += 1
            stops[stop] += 1

        # Create a list of events and sort by time, then by stop/start.
        START = 1
        STOP = -1
        events = []
        for etime, ecount in starts.items():
            events.append((etime, START, ecount))
        for etime, ecount in stops.items():
            events.append((etime, STOP, ecount))

        # Process events.  Each event is a new solution inteval.
        events.sort()
        soln = []
        curr_start = -1
        curr_jobs = 0
        for etime, etype, ecount in events:
            # Create new inteval
            soln.append([curr_start, etime, curr_jobs])
            curr_start = etime
            if etype == START:
                curr_jobs += ecount
            else:
                curr_jobs -= ecount

        # Remove entry caused by initial start.
        return soln[1:]


def test_1():
    intervals = [[0, 3], [5, 7], [0, 7]]
    types = ["hacker news", "reddit", "scrum meeting"]
    expected = [[0, 3, 2], [3, 5, 1], [5, 7, 2]]
    assert Solution().solve(intervals,types) == expected

def test_2():
    intervals = [[1, 4], [2, 3], [3, 4]]
    types = ["standup", "scrum retro", "scrum planning"]
    expected = [[1, 2, 1], [2, 3, 2], [3, 4, 2]]
    assert Solution().solve(intervals,types) == expected
