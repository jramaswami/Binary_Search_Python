"""
binarysearch.com :: Shortest Common Supersequence
jramaswami
"""


import functools


class Solution:

    def solve(self, a, b):
        @functools.cache
        def lcs(i, j):
            # Base case
            if (i >= len(a) or j >= len(b)):
                return 0
            if a[i] == b[j]:
                return 1 + lcs(i+1, j+1)
            return max(
                lcs(i+1, j),
                lcs(i, j+1)
            )
        return len(a) + len(b) - lcs(0, 0)


def test_1():
    a = "bell"
    b = "yellow"
    expected = 7
    assert Solution().solve(a, b) == expected
