"""
binarysearch.com :: Balanced Brackets
https://binarysearch.com/problems/Balanced-Brackets
"""

class Solution:
    def solve(self, s):
        stack = 0
        for bracket in s:
            if bracket == '(':
                stack += 1
            elif bracket == ')' and stack == 0:
                return False
            else:
                stack -= 1
        return stack == 0


def test_1():
    s = "()"
    solver = Solution()
    assert solver.solve(s) == True

def test_2():
    s = "()()"
    solver = Solution()
    assert solver.solve(s) == True

def test_3():
    s = ")("
    solver = Solution()
    assert solver.solve(s) == False

def test_4():
    s = ""
    solver = Solution()
    assert solver.solve(s) == True

def test_5():
    s = "((()))"
    solver = Solution()
    assert solver.solve(s) == True

def test_6():
    s = s = "((()"
    solver = Solution()
    assert solver.solve(s) == False