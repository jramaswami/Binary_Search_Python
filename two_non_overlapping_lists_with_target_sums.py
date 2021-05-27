"""
binarysearch.com :: Two Non-Overlapping Lists With Target Sums
jramaswami
"""


from math import inf
from collections import namedtuple


Interval = namedtuple('Interval', ['length', 'start', 'end'])


def intervals_overlap(interval1, interval2):
    """Return True if intervals overlap."""
    # |-----|
    #    |-----|
    #
    # |----------|
    #   |-----|
    if interval1.start <= interval2.start <= interval1.end:
        return True
    #   |-----|
    #|-----|
    if interval1.start <= interval2.end <= interval1.end:
        return True
    #    |-----|
    # |-----------|
    if interval2.start <= interval1.start <= interval2.end:
        return True
    return False


class Solution:
    def solve(self, nums, k):
        sums = dict()
        curr_sum = 0
        sums[0] = -1
        intervals = []
        for j, n in enumerate(nums):
            curr_sum += n
            delta = curr_sum - k
            if delta in sums:
                i = sums[delta]
                length = j - i
                intervals.append(Interval(length, i+1, j))
            sums[curr_sum] = j

        intervals.sort()
        soln = inf
        for i, a in enumerate(intervals):
            # If twice the length of the current interval is greater than
            # the current solution we can stop because (1) The current
            # interval was already paired with a smaller interval or
            # (2) the current interval must be paired with a larger interval
            # which will not beat the current solution.
            if 2 * a.length > soln:
                break
            for j, b in enumerate(intervals[i+1:], start=i+1):
                if not intervals_overlap(a, b):

                    soln = min(soln, a.length + b.length)
        return -1 if soln == inf else soln



def test_1():
    nums = [5, 9, -3, -1, 3, 2]
    k = 5
    assert Solution().solve(nums, k) == 3


def test_2():
    nums = []
    k = 5
    assert Solution().solve(nums, k) == -1


def test_3():
    nums = [1,2,3,4,5]
    k = 100
    assert Solution().solve(nums, k) == -1


def test_4():
    nums = [1,2,3,4,5]
    k = 15
    assert Solution().solve(nums, k) == -1


def test_5():
    """WA"""
    nums = [1, 0]
    k = 1
    assert Solution().solve(nums, k) == -1


def test_6():
    nums = [4, 2, -3, 1, -2, -1, 0, 2, -2, 3]
    k = 2
    assert Solution().solve(nums, k) == 2


def test_7():
    nums = [-1, -3, 5, -2, 5, 3, -1, -5, 5, 3, -1, -4, 4, -5, 5, -5, -2, -1]
    k = 0
    assert Solution().solve(nums, k) == 4
