"""
binarysearch.com :: Anagram Difference
jramaswami
"""


import math


import functools


class Solution:

    def solve(self, s0, s1):

        @functools.cache
        def solve0(i, t):
            if t == s1:
                return 0

            if i >= len(s0):
                return math.inf

            # Make no swaps
            result = solve0(i + 1, t)

            for j, _ in enumerate(s0):
                t0 = list(t)
                t0[i], t0[j] = t0[j], t0[i]
                result = min(
                    result,
                    1 + solve0(i + 1, "".join(t0))
                )

            return result

        return solve0(0, s0)


def test_1():
    s0 = "mod"
    s1 = "dom"
    expected = 1
    assert Solution().solve(s0, s1) == expected


def test_2():
    "TLE"
    s0 = "gbmqzfa"
    s1 = "qbgzamf"
    expected = 5
    assert Solution().solve(s0, s1) == expected


def test_3():
    "TLE"
    s0 = "fxaaieki"
    s1 = "aaeixkif"
    expected = 6
    assert Solution().solve(s0, s1) == expected