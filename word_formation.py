"""
binarysearch.com :: Word Formation
jramaswami
"""


import collections
import string


class Solution:

    def solve(self, words, letters):
        letters_freqs = collections.Counter(letters)
        def is_possible(wd):
            wd_freqs = collections.Counter(wd)
            return all(wd_freqs[c] <= letters_freqs[c] for c in string.ascii_lowercase)
        soln = 0
        for wd in words:
            if is_possible(wd):
                soln = max(soln, len(wd))
        return soln


def test_1():
    words = ["the", "word", "love", "scott", "finder", "dictionary"]
    letters = "fanierdow"
    expected = 6
    assert Solution().solve(words, letters) == expected