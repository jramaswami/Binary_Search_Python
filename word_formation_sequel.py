"""
binarysearch.com :: Word Formation Sequel
jramaswami
"""


import string
import collections


class Solution:

    def solve(self, words, letters):
        # Boundary case:
        if not letters or not words:
            return 0

        letter_freqs = collections.Counter(letters)

        def can_form(wd):
            word_freqs = collections.Counter(wd)
            wildcards = letter_freqs['*']
            for c in string.ascii_lowercase:
                if word_freqs[c] > letter_freqs[c]:
                    delta = word_freqs[c] - letter_freqs[c]
                    wildcards -= delta
                    if wildcards < 0:
                        return False
            return True

        return max(len(w) if can_form(w) else 0 for w in words)


def test_1():
    words = ["alice", "sunstroke", "mercantilely", "lakism", "phosphine"]
    letters = "*s*ki*"
    expected = 6
    assert Solution().solve(words, letters) == expected


def test_2():
    words = ["alice", "sunstroke", "mercantilely", "lakism", "phosphine"]
    letters = ""
    expected = 0
    assert Solution().solve(words, letters) == expected


def test_3():
    words = []
    letters = "*s*ki*"
    expected = 0
    assert Solution().solve(words, letters) == expected


def test_4():
    words = ["alice", "sunstroke", "mercantilely", "lakism", "phosphine"]
    letters = "****"
    expected = 0
    assert Solution().solve(words, letters) == expected
