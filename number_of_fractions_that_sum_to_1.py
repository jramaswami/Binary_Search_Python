"""
binarysearch.com :: Number of Fractions that Sum to 1
jramaswami
"""

from fractions import Fraction
from bisect import bisect_left


class Solution:

    def solve(self, fractions):

        ONE = Fraction(1, 1)
        fractions0 = [Fraction(*f) for f in fractions]
        # O(n log n)
        fractions0.sort()
        soln = 0
        # O(n log n)
        while fractions0:
            fract = fractions0.pop()
            i = bisect_left(fractions0, ONE - fract)
            while i < len(fractions0) and fractions0[i] + fract == ONE:
                soln += 1
                i += 1
        return soln


def test_1():
    fractions = [
        [1, 4],
        [2, 5],
        [3, 4],
        [3, 5],
        [5, 10],
        [1, 2],
        [1, 2]
    ]
    assert Solution().solve(fractions) == 5
