"""
binarysearch.com :: Balanced Brackets Sequel
https://binarysearch.com/problems/Balanced-Brackets-Sequel
"""

def matches(a, b):
    """Return True if the brackets are open and close of the same kind."""
    if a == '(' and b == ')':
        return True
    if a == '[' and b == ']':
        return True
    if a == '{' and b == '}':
        return True
    return False


def is_open(a):
    """Return True if this is an open bracket."""
    return a == '(' or a == '[' or a == '{'


class Solution:
    def solve(self, s):
        stack = []
        for c in s:
            if is_open(c):
                stack.append(c)
            elif stack and matches(stack[-1], c):
                stack.pop()
            else:
                return False
        return not stack


def test_1():
    s = "[(])"
    solver = Solution()
    assert solver.solve(s) == False

def test_2():
    s = "([])[]({})"
    solver = Solution()
    assert solver.solve(s) == True

def test_3():
    s = "([])[]({}))"
    solver = Solution()
    assert solver.solve(s) == False

def test_4():
    s = ""
    solver = Solution()
    assert solver.solve(s) == True