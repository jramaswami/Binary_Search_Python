"""
binarysearch.com :: Stacks
jramaswami
"""
from itertools import accumulate


class Solution:
    def solve(self, stacks):
        if stacks:
            intersection = set.intersection(*(set(accumulate(s)) for s in stacks))
            return max(intersection) if intersection else 0
        else:
            return 0



def test_1():
    stacks = [
        [2, 3, 4, 5],
        [4, 5, 2, 3, 3],
        [9, 1, 1, 1]
    ]
    assert Solution().solve(stacks) == 9

def test_2():
    stacks = [
        [5, 13],
        [7, 2],
        [50]
    ]
    assert Solution().solve(stacks) == 0
