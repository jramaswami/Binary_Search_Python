"""
binarysearch.com :: Palindromic Integer
https://binarysearch.com/problems/Palindromic-Integer
"""
from collections import deque
class Solution:
    def solve(self, num):
        normal = deque()
        reverse = deque()

        while num:
            num, r = divmod(num, 10)
            normal.append(r)
            reverse.appendleft(r)

        return normal == reverse


def test_1():
    solver = Solution()
    num = 121
    assert solver.solve(num) == True

def test_2():
    solver = Solution()
    num = 20200202
    assert solver.solve(num) == True

def test_3():
    solver = Solution()
    num = 44
    assert solver.solve(num) == True

def test_4():
    solver = Solution()
    num = 45
    assert solver.solve(num) == False

