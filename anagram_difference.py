"""
binarysearch.com :: Anagram Difference
jramaswami
"""


import math


class Solution:

    def solve(self, s0, s1):
        t0 = list(s0)
        t1 = list(s1)

        def solve0(i):
            if t0 == t1:
                return 0

            if i >= len(s0):
                return math.inf

            # Make no swaps
            result = solve0(i + 1)

            for j, _ in enumerate(s0):
                t0[i], t0[j] = t0[j], t0[i]
                result = min(
                    result,
                    1 + solve0(i + 1)
                )
                t0[i], t0[j] = t0[j], t0[i]

            return result

        return solve0(0)


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