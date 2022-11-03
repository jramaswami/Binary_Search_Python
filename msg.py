"""
Binary Search :: Weekly Contest 31 :: Monotonous String Groups
"""
from math import inf

def increasing(S, start):
    i = start

    while i + 1 < len(S):
        if S[i] > S[i+1]:
            return i + 1
        i += 1
    return len(S)


def decreasing(S, start):
    i = start
    while i + 1 < len(S):
        if S[i] < S[i+1]:
            return i + 1
        i += 1
    return len(S)


class Solution:
    def solve(self, s):
        if s == "":
            return 0

        soln = 0
        start = 0
        print(s)
        print('start', 0)
        while start < len(s):
            start = max(increasing(s, start), decreasing(s, start))
            print('start', start)
            soln += 1
        return soln


def test_1():
    solver = Solution()
    s = "abcdcba"
    assert solver.solve(s) == 2


def test_2():
    solver = Solution()
    s = "zzz"
    assert solver.solve(s) == 1


def test_3():
    solver = Solution()
    s = ""
    assert solver.solve(s) == 0


def test_4():
    solver = Solution()
    s = "ba"
    assert solver.solve(s) == 1


def test_5():
    solver = Solution()
    s = "eabea"
    assert solver.solve(s) == 3

