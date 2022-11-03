"""
binarysearch.com :: Mutual Followers
jramaswami
"""
from collections import defaultdict


class Solution:
    def solve(self, relations):
        following = defaultdict(set)
        soln = set()
        for a, b in relations:
            following[a].add(b)
            if a in following[b]:
                soln.add(a)
                soln.add(b)
        return list(sorted(soln))


def test_1():
    relations = [
        [0, 1],
        [2, 3],
        [3, 4],
        [1, 0]
    ]
    assert Solution().solve(relations) == [0, 1]

def test_2():
    relations = [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 0]
    ]
    assert Solution().solve(relations) == []
