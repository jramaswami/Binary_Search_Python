"""
binarysearch.com :: Max Character Distinct Words
jramaswami
"""

from collections import namedtuple
from string import ascii_lowercase
from itertools import combinations


Word = namedtuple('Word', ['letters', 'len'])


class Solution:
    def solve(self, words):
        soln = 0
        word_freqs = [Word(set(w), len(w)) for w in words]
        for w1, w2 in combinations(word_freqs, 2):
            if w1.letters.isdisjoint(w2.letters):
                soln = max(soln, w1.len + w2.len)
        return soln


def test_1():
    words = ["abcde", "xyz", "abdexyz", "axyz"]
    assert Solution().solve(words) == 8
