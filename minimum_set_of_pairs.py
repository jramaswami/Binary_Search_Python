"""
binarysearch.com :: Minimum Set of Pairs
jramaswami
"""


import itertools
import collections
import operator
import math


Pair = collections.namedtuple('Pair', ['i', 'j', 'sum'])


class Solution:

    def solve(self, nums):
        def are_disjoint(left, right):
            return (
                left.i != right.i and left.i != right.j and
                left.j != right.i and left.j != right.j
            )

        pairs = [Pair(i, j, nums[i] + nums[j]) for i, j in itertools.combinations(range(len(nums)), 2)]
        pairs.sort(key=operator.attrgetter('sum'))
        best_delta = math.inf
        for i, a in enumerate(pairs):
            for j, b in enumerate(pairs[i+1:], start=i+1):
                delta = abs(a.sum - b.sum)
                if delta >= best_delta:
                    # Sums are sorted so the difference only gets more so
                    # we can stop looking.
                    break
                if are_disjoint(a, b):
                    best_delta = delta
        return best_delta


def test_1():
    nums = [2, 3, 4, 9, 6]
    expected = 1
    assert Solution().solve(nums) == expected