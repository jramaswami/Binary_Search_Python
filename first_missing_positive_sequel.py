"""
binarysearch.com :: First Missing Positive Sequel
https://binarysearch.com/problems/First-Missing-Positive-Sequel
"""
class Solution:
    def solve(self, arr):
        arr0 = [a for a in arr if a > 0]
        soln = len(arr0) + 1
        for i, a in enumerate(arr0):
            if i + 1 != a:
                return i + 1
        return soln


def test_1():
    arr = [2, 3, 4]
    solver = Solution()
    assert solver.solve(arr) == 1

def test_2():
    arr = [1, 2]
    solver = Solution()
    assert solver.solve(arr) == 3

def test_3():
    arr = [1, 2, 3, 4, 6, 7, 8, 9]
    solver = Solution()
    assert solver.solve(arr) == 5

def test_4():
    solver = Solution()
    assert solver.solve([]) == 1

def test_5():
    solver = Solution()
    assert solver.solve([0, 1]) == 2