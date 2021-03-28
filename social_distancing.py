"""
binarysearch.com :: Social Distancing
jramaswami
"""
from math import inf


class Solution:
    def solve(self, s, k):
        prefix = [inf for _ in s]
        curr_dist = inf
        for i, c in enumerate(s):
            if c == 'x':
                curr_dist = 0
            else:
                curr_dist += 1
            prefix[i] = curr_dist

        N = len(s)
        suffix = [inf for _ in s]
        curr_dist = inf
        for revi, c in enumerate(reversed(s), start = 1):
            i = N - revi
            if c == 'x':
                curr_dist = 0
            else:
                curr_dist += 1
            suffix[i] = curr_dist

        for p, s in zip(prefix, suffix):
            if p >= k and s >= k:
                return True
        return False


def test_1():
    s = "x.."
    k = 2
    assert Solution().solve(s, k) == True

def test_2():
    s = "x..x"
    k = 2
    assert Solution().solve(s, k) == False

def test_3():
    s = "x...x"
    k = 2
    assert Solution().solve(s, k) == True

def test_4():
    s = "..x"
    k = 2
    assert Solution().solve(s, k) == True

def test_5():
    s = "."
    k = 1
    assert Solution().solve(s, k) == True
