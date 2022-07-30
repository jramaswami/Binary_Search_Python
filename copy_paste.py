"""
binarysearch.com :: Copy Paste
jramaswami
"""


import functools


class Solution:

    def solve(self, n):

        @functools.cache
        def cp(i, buff, clip):
            if i >= n:
                return buff
            return max(
                cp(i+1, buff, buff),        # Copy buffer to clipboard.
                cp(i+1, buff+clip, clip),   # Paste clipboard to buffer.
                cp(i+1, 1+buff, clip)       # Insert one into buffer.
            )

        return cp(0, 0, 0)

def test_1():
    n = 6
    expected = 9
    assert Solution().solve(n) == expected


def test_2():
    "TLE"
    n = 40
    expected = 2125764
    assert Solution().solve(n) == expected


def test_3():
    n = 100
    expected = 7412080755407364
    assert Solution().solve(n) == expected