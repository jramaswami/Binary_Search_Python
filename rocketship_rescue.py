"""
binarysearch.com :: Rocketship Rescue
jramaswami
"""


import collections


class Solution:
    def solve(self, weights, limit):
        weights0 = collections.deque(sorted(weights))
        soln = 0
        while weights0:
            soln += 1
            if len(weights0) == 1 or weights0[0] + weights0[-1] > limit:
                weights0.pop()
            else:
                weights0.popleft()
                weights0.pop()
        return soln


def test_1():
    weights = [200, 300, 200]
    limit = 400
    expected = 2
    assert Solution().solve(weights, limit) == expected


def test_2():
    """WA"""
    weights = [1, 1, 1, 3]
    limit = 3
    expected = 3
    assert Solution().solve(weights, limit) == expected


def test_3():
    weights = [1, 1, 2, 2]
    limit = 3
    expected = 2
    assert Solution().solve(weights, limit) == expected