"""
binarysearch.com :: Multiple Parentheses
jramaswami
"""
class Solution:
    def solve(self, s):
        soln = 0
        stack = []
        for i, c in enumerate(s):
            if c == ')' and stack:
                soln = max(soln, i - stack[-1] + 1)
            elif c == '(':
                stack.append(i)
        return soln

def test_1():
    s = ")(())(()"
    assert Solution().solve(s) == 4

def test_2():
    s = ""
    assert Solution().solve(s) == 0

def test_3():
    s = ")(()))((()()))"
    assert Solution().solve(s) == 8

def test_4():
    s = "(()()(((("
    assert Solution().solve(s) == 8
