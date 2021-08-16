"""
binarysearch.com :: Range Query on a List
jramaswami
"""

import itertools


class RangeSum:

    def __init__(self, nums):
        self.prefix = list(itertools.accumulate(nums))
        print(self.prefix)

    def _get(self, i):
        if i < 0:
            return 0
        return self.prefix[i]

    def total(self, left, right):
        return self._get(right - 1) - self._get(left - 1)


def test_1():
    methods = ["constructor", "total", "total"]
    arguments = [[[1, 2, 5, 0, 3, 7]], [0, 3], [1, 5]]
    expected = [None, 8, 10]
    A = RangeSum(*arguments[0])
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        r = getattr(A, m)(*a)
        assert r == e
