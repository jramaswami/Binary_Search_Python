"""
binarysearch.com :: Number of Quadruplets That Sum Target
jramaswami
"""


import itertools
import collections


class Solution:
    def solve(self, a, b, c, d, target):
        left = collections.Counter(x + y for x, y in itertools.product(a, b))
        right = collections.Counter(x + y for x, y in itertools.product(c, d))
        return sum(left[x] * right[target - x] for x in left)


def test_1():
    a = [4, 3, 2]
    b = [7, 3]
    c = [5, 1]
    d = [3, 9]
    target = 19
    expected = 3
    assert Solution().solve(a, b, c, d, target) == expected