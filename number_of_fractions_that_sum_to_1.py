"""
binarysearch.com :: Number of Fractions that Sum to 1
jramaswami
"""


from collections import defaultdict
from math import gcd


class Solution:

    def solve(self, fractions):
        visited = defaultdict(lambda: defaultdict(int))
        soln = 0
        for num, den in fractions:
            g = gcd(num, den)
            num, den = num // g, den // g
            soln += visited[den][den - num]
            visited[den][num] += 1
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
