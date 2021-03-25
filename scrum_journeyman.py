"""
binarysearch.com :: Scrum Journeyman
jramaswami
"""
from collections import defaultdict


class Solution:
    def solve(self, intervals, types):
        # First gather events by time.
        events = defaultdict(int)
        for start, stop in intervals:
            events[start] += 1
            events[stop] -= 1

        # Process events.  Each event is a new solution inteval.
        curr_start = -1
        curr_jobs = 0
        soln = []
        for etime in sorted(events):
            # Create new inteval
            soln.append([curr_start, etime, curr_jobs])
            curr_start = etime
            curr_jobs += events[etime]

        # Remove zero job intervals.
        return [t for t in soln if t[-1]]


def test_1():
    intervals = [[0, 3], [5, 7], [0, 7]]
    types = ["hacker news", "reddit", "scrum meeting"]
    expected = [[0, 3, 2], [3, 5, 1], [5, 7, 2]]
    assert Solution().solve(intervals,types) == expected

def test_2():
    intervals = [[1, 4], [2, 3], [3, 4]]
    types = ["standup", "scrum retro", "scrum planning"]
    expected = [[1, 2, 1], [2, 3, 2], [3, 4, 2]]
    result = Solution().solve(intervals,types)
    assert result == expected

def test_3():
    """WA"""
    intervals = [[1, 4], [2, 3], [3, 4]]
    types = ["standup", "scrum retro", "scrum planning"]
    expected = [[1, 2, 1], [2, 3, 2], [3, 4, 2]]
    result = Solution().solve(intervals,types)
    assert result == expected

def test_4():
    """WA"""
    intervals = [[103, 150], [53, 65], [86, 135], [171, 231]]
    types = ["y", "y", "j", "j"]
    expected = [[53, 65, 1], [86, 103, 1], [103, 135, 2], [135, 150, 1], [171, 231, 1]]
    result = Solution().solve(intervals,types)
    assert result == expected
