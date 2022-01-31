"""
binarysearch.com :: Movie Theatres
jramaswami
"""

class Solution:

    def solve(self, intervals):
        events = []
        for start, stop in intervals:
            events.append((start, 1))
            events.append((stop, -1))
        events.sort()
        curr = 0
        soln = 0
        for _, etype in events:
            curr += etype
            soln = max(curr, soln)
        return soln


def test_1():
    intervals = [
        [30, 75],
        [0, 50],
        [60, 150]
    ]
    expected = 2
    assert Solution().solve(intervals) == expected


def test_2():
    intervals = [
        [10, 20],
        [20, 30]
    ]
    expected = 1
    assert Solution().solve(intervals) == expected


def test_3():
    intervals = [
        [0, 1],
        [0, 1],
        [0, 1]
    ]
    expected = 3
    assert Solution().solve(intervals) == expected


def test_4():
    intervals = []
    expected = 0
    assert Solution().solve(intervals) == expected
