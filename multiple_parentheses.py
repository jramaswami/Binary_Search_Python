"""
binarysearch.com :: Multiple Parentheses
jramaswami
"""
class Solution:
    def solve(self, s):
        delta = 0
        length = 0
        soln = 0
        for i, c in enumerate(s):
            if c == ')':
                delta -= 1
            elif c == '(':
                delta += 1
            length += 1

            if delta < 0:
                length = 0
                delta = 0
            elif delta == 0:
                soln = max(soln, length)

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
