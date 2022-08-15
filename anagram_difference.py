"""
binarysearch.com :: Anagram Difference
jramaswami
"""


import math


class Solution:

    def solve(self, s0, s1):
        t0, t1 = list(s0), list(s1)
        def solve0(i):
            if t0 == t1:
                return 0

            if i >= len(t0):
                return math.inf

            if t0[i] != t1[i]:
                # Only make swaps if t[i] is in the wrong place.
                result = math.inf
                for j, _ in enumerate(t0[i+1:], start=i+1):
                    if t0[j] == t1[i]:
                        # Only continue if this at least fixed t[i].
                        t0[i], t0[j] = t0[j], t0[i]
                        result = min(
                            result,
                            1 + solve0(i + 1)
                        )
                        t0[i], t0[j] = t0[j], t0[i]
                return result
            else:
                return solve0(i + 1)

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


def test_3():
    "TLE"
    s0 = "fxaaieki"
    s1 = "aaeixkif"
    expected = 6
    assert Solution().solve(s0, s1) == expected


def test_4():
    "TLE"
    s0 = "kuccbrzycccswti"
    s1 = "tcuccsizrcwcybk"
    expected = 10
    assert Solution().solve(s0, s1) == expected


def test_5():
    "TLE"
    s0 = "mbkjwzboqpqzldmtiot"
    s1 = "qdttiqkozzmjowpbblm"
    expected = 12
    assert Solution().solve(s0, s1) == expected