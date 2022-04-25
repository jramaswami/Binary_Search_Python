"""
binarysearch.com :: Distinct Palindromes
jramaswami
"""


import collections
import math
import functools


class Solution:
    def solve(self, text):
        MOD = pow(10, 9) + 7

        def compute(freqs):
            freqs0 = [f // 2 for f in freqs.values()]
            return (
                math.factorial(sum(freqs0)) //
                math.prod(math.factorial(f) for f in freqs0)
            ) % MOD

        freqs = collections.Counter(text)
        if len(text) % 2:
            # Only one freq can be odd.
            if sum(f % 2 for f in freqs.values()) != 1:
                return 0

            odd_c = [c for c, f in freqs.items() if f % 2][0]
            freqs[odd_c] -= 1
            return compute(freqs)
        else:
            # All freqs must be even.
            if any(f % 2 for f in freqs.values()):
                return 0
            return compute(freqs)



def test_1():
    s = "abccb"
    expected = 2
    assert Solution().solve
