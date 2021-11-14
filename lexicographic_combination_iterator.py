"""
binarysearch.com :: Lexicographic Combination Iterator
jramaswami
"""


class LexicographicCombinationIterator:

    def __init__(self, S, k):
        self.S = S
        self.k = k
        self.limits = list(range(len(S) - k, len(S)))
        self.combo = list(range(k))

    def _exceeds_limit(self, i):
        return self.combo[i] > self.limits[i]

    def _incr(self):
        # Find the leftmost index that when incremented does not exceed
        # its limit.
        i = len(self.combo) - 1
        self.combo[i] += 1
        while i >= 0 and self._exceeds_limit(i):
            i -= 1
            self.combo[i] += 1
        # i += 1
        # i now points to the first index that is not over the limit or
        # i = 0 and 0 is over the limit.
        # Set subsequent indices.
        for j, _ in enumerate(self.combo[i+1:], start=i+1):
            self.combo[j] = self.combo[j-1] + 1

    def next(self):
        if not self._exceeds_limit(0):
            T = "".join(self.S[i] for i in self.combo)
            self._incr()
            return T

    def hasnext(self):
        return not self._exceeds_limit(0)


#
# Testing
#
import itertools
import random
import string


def test_1():
    itr = LexicographicCombinationIterator("abc", 2)
    assert itr.hasnext()
    assert itr.next() == 'ab'
    assert itr.hasnext()
    assert itr.next() == 'ac'
    assert itr.hasnext()
    assert itr.next() == 'bc'
    assert not itr.hasnext()


def test_random():
    for _ in range(20):
        S = sorted(random.sample(string.ascii_lowercase, 20))
        k = random.randint(1, len(S))
        itr = LexicographicCombinationIterator(S, k)
        for combo in itertools.combinations(S, k):
            T = "".join(combo)
            assert itr.hasnext()
            assert itr.next() == T
        assert not itr.hasnext()