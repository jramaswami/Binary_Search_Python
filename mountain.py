"""
binarysearch.com :: Weekly Contest 35 :: 
"""
from collections import deque


class Solution:
    def solve(self, n, lower, upper):
        if upper == lower:
            return []

        soln = deque([upper-1, upper, upper-1])
        k = upper - 2
        while k >= lower and len(soln) < n:
            soln.append(k)
            k-=1

        k = upper - 2
        while k >= lower and len(soln) < n:
            soln.appendleft(k)
            k-=1

        if len(soln) < n:
            return []
        return list(soln)



def test_1():
    n = 5
    lower = 2
    upper = 6
    solver = Solution()
    assert solver.solve(n, lower, upper) == [5, 6, 5, 4, 3]


def test_2():
    n = 5
    lower = 90
    upper = 92
    solver = Solution()
    assert solver.solve(n, lower, upper) == [90, 91, 92, 91, 90]


def test_3():
    n = 6
    lower = 3
    upper = 5
    solver = Solution()
    assert solver.solve(n, lower, upper) == []

def test_4():
    n = 3
    lower = 8
    upper = 11
    solver = Solution()
    assert solver.solve(n, lower, upper) == [10, 11, 10]


def test_5():
    n = 9
    lower = 5
    upper = 9
    solver = Solution()
    assert solver.solve(n, lower, upper) == [5, 6, 7, 8, 9, 8, 7, 6, 5]

