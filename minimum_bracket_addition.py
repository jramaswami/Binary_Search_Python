"""
binarysearch.com :: Minimum Bracket Addition
jramaswami
"""


class Solution:

    def solve(self, S):
        stack = []
        soln = 0
        for c in S:
            if c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    soln += 1
            elif c == '(':
                stack.append('(')
        return soln + len(stack)


def test_1():
    s = ")))(("
    expected = 5
    assert Solution().solve(s) == expected


def test_2():
    s = ""
    expected = 0
    assert Solution().solve(s) == expected


def test_3():
    s = "((()(()))((())()))"
    expected = 0
    assert Solution().solve(s) == expected
