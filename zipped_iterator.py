"""
binarysearch.com :: Zipped Iterator
jramaswami
"""


class ZippedIterator:
    def __init__(self, a, b):
        i = j = 0
        self.A = []

        while i < len(a) and j < len(b):
            self.A.append(a[i])
            self.A.append(b[j])
            i += 1
            j += 1

        while i < len(a):
            self.A.append(a[i])
            i += 1

        while j < len(b):
            self.A.append(b[i])
            j += 1

        self.i = 0

    def next(self):
        result = None
        if self.hasnext():
            result = self.A[self.i]
            self.i += 1
        return result

    def hasnext(self):
        return self.i < len(self.A)


def test_1():
    methods = ["constructor", "hasnext", "next", "next", "next", "next", "next", "hasnext"]
    arguments = [[[1, 2], [3, 4, 5]], [], [], [], [], [], [], []]
    expected = [None, True, 1, 3, 2, 4, 5, False]

    I = ZippedIterator(*arguments[0])
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        r = getattr(I, m)(*a)
        assert r == e


def test_2():
    "WA"
    methods = ["constructor", "next", "next"]
    arguments = [[[], [0,1]], [], []]
    expected = [None, 0, 1]
    I = ZippedIterator(*arguments[0])
    for m, a, e in zip(methods[1:], arguments[1:], expected[1:]):
        r = getattr(I, m)(*a)
        assert r == e
