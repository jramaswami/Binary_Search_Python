"""
binarysearch.com :: Hanging Banners
jramaswami
"""


import collections
import enum


Event = collections.namedtuple('Event', ['x', 'type', 'banner'])


class EType(enum.IntEnum):
    STOP = 1
    START = -1


class Solution:

    def solve(self, intervals):

        events = []
        for i, (left, right) in enumerate(intervals):
            events.append(Event(left, EType.START, i))
            events.append(Event(right, EType.STOP, i))
        events.sort()

        pinned = [False for _ in intervals]
        soln = 0
        curr_banners = []
        for event in events:
            if event.type == EType.START:
                curr_banners.append(event.banner)
            elif event.type == EType.STOP and pinned[event.banner]:
                pass
            elif event.type == EType.STOP and not pinned[event.banner]:
                soln += 1
                for banner in curr_banners:
                    pinned[banner] = True
                curr_banners = []
        return soln


def test_1():
    intervals = [
        [1, 4],
        [4, 5],
        [7, 9],
        [9, 12]
    ]
    expected = 2
    assert Solution().solve(intervals) == expected


def test_2():
    intervals = [
        [1, 10],
        [5, 10],
        [6, 10],
        [9, 10]
    ]
    expected = 1
    assert Solution().solve(intervals) == expected


def test_3():
    intervals = []
    expected = 0
    assert Solution().solve(intervals) == expected
