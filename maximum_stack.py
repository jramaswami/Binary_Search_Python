"""
binarysearch.com :: Maximum Stack
jramaswami
"""


import heapq
import collections


SItem = collections.namedtuple('SItem', ['negval', 'index'])


class MaximumStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        self.index = 0
        self.popped = []

    def append(self, val):
        item = SItem(-val, self.index)
        self.popped.append(False)
        self.index += 1
        self.stack.append(item)
        heapq.heappush(self.heap, item)

    def peek(self):
        if self.stack:
            return -(self.stack[-1].negval)

    def max(self):
        if self.heap:
            return -(self.heap[0].negval)

    def pop(self):
        result = self.stack.pop()
        self.popped[result.index] = True
        self._cleanup()
        return -result.negval

    def popmax(self):
        result = heapq.heappop(self.heap)
        self.popped[result.index] = True
        self._cleanup()
        return -result.negval

    def _cleanup(self):
        while self.heap and self.popped[self.heap[0].index]:
            heapq.heappop(self.heap)
        while self.stack and self.popped[self.stack[-1].index]:
            self.stack.pop()


def test_1():
    methods = ["constructor", "append", "append", "append", "peek", "max", "popmax", "max", "pop", "peek"]
    arguments = [[], [1], [3], [2], [], [], [], [], [], []]
    expected = [None, None, None, None, 2, 3, 3, 2, 2, 1]
    maxstack = MaximumStack()
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(maxstack, m)(*a) == e


def test_2():
    "RTE"
    methods = ["constructor", "append", "popmax"]
    arguments = [[], [3], []]
    expected = [None, None, 3]
    maxstack = MaximumStack()
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(maxstack, m)(*a) == e


def test_3():
    "WA"
    methods = ["constructor", "append", "append", "append", "append", "popmax", "peek", "peek", "pop"]
    arguments = [[], [6], [2], [1], [6], [], [], [], []]
    expected = [None, None, None, None, None, 6, 1, 1, 1]
    maxstack = MaximumStack()
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        assert getattr(maxstack, m)(*a) == e
