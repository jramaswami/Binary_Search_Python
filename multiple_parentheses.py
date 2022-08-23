"""
binarysearch.com :: Multiple Parentheses
jramaswami
"""


from collections import defaultdict


class Solution:
    def solve(self, s):
        soln = 0
        opens = closes = 0
        for c in s:
            if c == '(':
                opens += 1
            elif c == ')':
                closes += 1

            if closes > opens:
                opens = closes = 0
            elif closes == opens:
                soln = max(soln, opens + closes)

        opens = closes = 0
        for c in reversed(s):
            if c == '(':
                opens += 1
            elif c == ')':
                closes += 1

            if opens > closes:
                opens = closes = 0
            elif closes == opens:
                soln = max(soln, opens + closes)

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
    assert Solution().solve(s) == 4