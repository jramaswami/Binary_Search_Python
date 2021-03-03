"""
binarysearch.com :: Hit Counter
jramaswami
"""
from collections import deque


class HitCounter:
    def __init__(self):
        self.curr_hits = deque()

    def add(self, timestamp):
        self.curr_hits.append(timestamp)

    def count(self, timestamp):
        while self.curr_hits and self.curr_hits[0] < timestamp - 60:
            self.curr_hits.popleft()
        return len(self.curr_hits)


def test_1():
    methods = ["constructor", "add", "add", "count", "add", "count"]
    arguments = [[], [10], [40], [40], [70], [100]]
    expected = [None, None, None, 2, None, 2]
    hc = HitCounter()
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(hc, m)(*a) == e

def test_2():
    methods = ["constructor", "count", "count"]
    arguments = [[], [0], [0]]
    expected = [None, 0, 0]
    hc = HitCounter()
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(hc, m)(*a) == e
