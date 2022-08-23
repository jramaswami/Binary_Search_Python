"""
binarysearch.com :: Job Scheduling to Maximize Profit
jramaswami
"""


from collections import namedtuple, defaultdict


Job = namedtuple('Job', ['start', 'stop', 'profit'])


class Solution:
    def solve(self, intervals):
        # Turn intervals into events and store them in a dict.
        events = defaultdict(list)
        for start, stop, profit in intervals:
            events[start].append(Job(start, stop, profit))
            events[stop].append(Job(start, stop, profit))

        curr_max = 0
        max_profit = defaultdict(int)
        max_profit[0] = 0
        for t in sorted(events):
            # Compute the current maximum profit that could be had at this time.
            curr_max = max(curr_max, max_profit[t])
            for job in events[t]:
                # If an job starts here and we take it then the profit when the job is over is
                # the current max profit + the job profit.  We record that profit at events.stop_time
                if t == job.start:
                    max_profit[job.stop] = job.profit + curr_max

        return curr_max


def test_1():
    intervals = [
        [1, 2, 50],
        [3, 5, 20],
        [6, 19, 100],
        [2, 100, 200]
    ]
    expected = 250
    assert Solution().solve(intervals) == expected


def test_2():
    intervals = [
        [10, 12, 250],
        [3, 5, 20],
        [6, 19, 100],
        [2, 100, 200]
    ]
    expected = 270
    assert Solution().solve(intervals) == expected