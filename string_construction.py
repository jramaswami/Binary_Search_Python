"""
binarysearch.com :: String Construction
jramaswami
"""


import collections
import functools


class Solution:

    def solve(self, strings, a, b):

        @functools.cache
        def solve0(i, acc_a, acc_b):
            if i >= len(strings):
                return 0

            # Do not choose this string.
            result = solve0(i + 1, acc_a, acc_b)

            # Choose string, if possible.
            freqs = collections.Counter(strings[i])
            acc_a0, acc_b0 = acc_a + freqs['A'], acc_b + freqs['B']
            if acc_a0 <= a and acc_b0 <= b:
                result = max(result, 1 + solve0(i + 1, acc_a0, acc_b0))
            return result

        return solve0(0, 0, 0)


def test_1():
    strings = ["AABB", "AAAB", "A", "B"]
    a = 4
    b = 2
    expected = 3
    assert Solution().solve(strings, a, b) == expected
