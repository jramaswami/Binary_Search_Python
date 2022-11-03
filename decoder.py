"""
binarysearch.com :: Weekly Contest 32 :: Lazy Run-Length Decoding
"""
from itertools import accumulate
from bisect import bisect_right


def find_gt(a, x):
    'Find leftmost index with a value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return i
    raise ValueError

def token_generator(s):
    """Generator for the tokens of the run length encoding."""
    number = 0
    for c in s:
        if c.isdigit():
            number *= 10
            number += int(c)
        else:
            yield number
            number = 0
            yield c


class RunLengthDecoder:
    def __init__(self, s):
        self.indices = []
        self.chars = []
        for i, token in enumerate(token_generator(s)):
            if i % 2:
                self.chars.append(token)
            else:
                self.indices.append(token)

        self.partial = list(accumulate(self.indices))
        print(s)
        print(self.indices)
        print(self.partial)

    def value(self, i):
        j = find_gt(self.partial, i)
        return self.chars[j]

    def valueInRange(self, c, i, j):
        k = find_gt(self.partial, i)

        for x in range(k, len(self.chars)):
            b = self.chars[x]
            if b >= c:
                return b

            if self.partial[x] >= j:
                break

        return '?'


def test_1():
    r = RunLengthDecoder("3a3b2c1d1a") # In decoded version it's "aaabbbccda"
    assert r.value(0) == "a"
    assert r.value(4) == "b"
    assert r.valueInRange("a", 0, 9) == "a"
    assert r.valueInRange("b", 3, 9) == "b"
    assert r.valueInRange("e", 3, 9) == "?"


def test_2():
    r = RunLengthDecoder("1j")
    assert r.valueInRange("d", 0, 1) == "j"


def test_3():
    r = RunLengthDecoder("1d1y")
    assert r.valueInRange("w", 0, 1) == "?"
    assert r.value(1) == "y"

def test_4():
    r = RunLengthDecoder("1000000000a1000000000z")
    assert r.valueInRange("r", 0, 753019066) == '?'
    assert r.value(1999999997) == 'z'
